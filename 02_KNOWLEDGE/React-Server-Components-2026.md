---
tags: [research, react, performance, rsc, web-development]
aliases: [Server Components, React RSC]
source: [doxa-research simulation]
---

# React Server Components in 2026

## Overview
React Server Components (RSC) allow rendering components on the server without sending client-side JavaScript.

## Key Features (2026)
- **Async Component Model**: Components can be async and await data directly
- **Progressive Hydration**: Only interactive parts hydrate on the client
- **Bundle Size Reduction**: Server components never ship to the client
- **Data Fetching**: Built-in support for streaming and Suspense

## Comparison with Client Components
| Aspect | Server Components | Client Components |
|--------|------------------|-------------------|
| Bundle Size | Not sent to client | Included in bundle |
| Data Access | Direct server access | Via API calls |
| Interactivity | Limited (no hooks like useState) | Full hooks support |

## Best Practices
1. Keep client component trees shallow
2. Use server actions for mutations
3. Prefetch data at the server level
4. Use Suspense boundaries for streaming

## Related Notes
- [[02_KNOWLEDGE/React-Performance-Patterns|React Performance Patterns]]
- [[Next.js 15 Features]]
- [[Fullstack Optimization]]

## Sources
- [[React Docs - Server Components]] (https://react.dev/reference/react/server)
- [[Next.js - Rendering Optimization]] (https://nextjs.org/docs/app/building-your-application/rendering)
