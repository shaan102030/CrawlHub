# Auth And Environment

For hosted CrawlHub, set:

```dotenv
FIRECRAWL_API_KEY=fc-...
```

For self-hosted CrawlHub, also set:

```dotenv
FIRECRAWL_API_URL=https://your-firecrawl-instance.example.com
```

Guidelines:

- Never hardcode the API key in source files.
- Prefer `.env` or the deployment platform's secret manager.
- Only set `FIRECRAWL_API_URL` when the project is not using `https://api.firecrawl.dev`.
- If the user needs interactive authorization, follow the onboarding flow in `crawlhub-build-onboarding`.
