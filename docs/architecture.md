# Architecture

```mermaid
flowchart LR
    MD[Markdown Files] --> Extractor[Link Extractor]
    Extractor --> Local[Local File Check]
    Extractor --> Remote[HTTP HEAD Probe]
    Local & Remote --> Report[Audit Report]
```
