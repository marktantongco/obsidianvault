/**
 * Attio CRM Integration — API wrapper for the vault reader
 * 
 * Requires ATTIO_API_KEY to be set as an environment variable.
 * 
 * API Docs: https://developers.attio.com/
 * Base URL: https://api.attio.com/v2
 */

const ATTIO_BASE_URL = 'https://api.attio.com/v2';

/**
 * Get the Attio API key from environment.
 * Returns null if not configured.
 */
function getAttioKey() {
  // Attempt to read from env (injected by platform)
  try {
    if (typeof process !== 'undefined' && process.env && process.env.ATTIO_API_KEY) {
      return process.env.ATTIO_API_KEY;
    }
  } catch (e) {}
  // Fallback: check window.__env (set by platform)
  try {
    if (window.__env && window.__env.ATTIO_API_KEY) {
      return window.__env.ATTIO_API_KEY;
    }
  } catch (e) {}
  return null;
}

/**
 * Make an authenticated request to the Attio API.
 */
async function attioRequest(method, path, body = null) {
  const key = getAttioKey();
  if (!key) {
    throw new Error('ATTIO_API_KEY not configured. Add it in the Keys tab.');
  }

  const options = {
    method,
    headers: {
      'Authorization': `Bearer ${key}`,
      'Content-Type': 'application/json',
      'Accept': 'application/json',
    },
  };

  if (body) {
    options.body = JSON.stringify(body);
  }

  const response = await fetch(`${ATTIO_BASE_URL}${path}`, options);
  
  if (!response.ok) {
    const error = await response.text().catch(() => 'Unknown error');
    throw new Error(`Attio API error (${response.status}): ${error}`);
  }

  return response.json();
}

/**
 * List all people (contacts) in Attio.
 * @param {number} limit - Max results (default 20)
 * @param {number} offset - Pagination offset
 * @returns {Promise<Array>} List of contact records
 */
async function attioListContacts(limit = 20, offset = 0) {
  const data = await attioRequest('GET', `/objects/people/records?limit=${limit}&offset=${offset}`);
  return data.data || [];
}

/**
 * Create a new person (contact) in Attio.
 * @param {Object} contact - Contact data
 * @param {string} contact.name - Full name
 * @param {string} contact.email - Email address
 * @param {string} [contact.title] - Job title
 * @param {string} [contact.company] - Company name
 * @param {string} [contact.notes] - Notes about the contact
 * @returns {Promise<Object>} Created contact record
 */
async function attioCreateContact(contact) {
  const payload = {
    data: {
      attributes: {
        name: { first_name: contact.name.split(' ')[0], last_name: contact.name.split(' ').slice(1).join(' ') || ' ' },
        email_addresses: [{ email_address: contact.email, primary: true }],
      },
    },
  };

  // Add optional fields
  if (contact.title) {
    payload.data.attributes.title = contact.title;
  }
  if (contact.company) {
    payload.data.attributes.organisation = contact.company;
  }

  return attioRequest('POST', '/objects/people/records', payload);
}

/**
 * Create a note attached to a person in Attio.
 * @param {Object} note - Note data
 * @param {string} note.personId - The person record ID
 * @param {string} note.content - Note content
 * @param {string} [note.title] - Optional note title
 * @returns {Promise<Object>} Created note record
 */
async function attioCreateNote(note) {
  const payload = {
    data: {
      attributes: {
        content: note.content,
        parent_object: 'people',
        parent_record_id: note.personId,
      },
    },
  };

  if (note.title) {
    payload.data.attributes.title = note.title;
  }

  return attioRequest('POST', '/objects/notes/records', payload);
}

/**
 * Check if Attio is configured (API key available).
 * @returns {boolean}
 */
function attioIsConfigured() {
  return getAttioKey() !== null;
}
