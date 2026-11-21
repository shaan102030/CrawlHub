# CrawlHub branding

CrawlHub is a fork of [Firecrawl](https://github.com/firecrawl/firecrawl), licensed under the same GNU Affero General Public License v3. Source modifications in this repository are offered as CrawlHub.

## What is branded as CrawlHub

- Product name and logos in the README, test site, and API root response
- Logo assets under `img/` and `apps/test-site/`

## What stays as Firecrawl (compatibility)

To remain compatible with the upstream Firecrawl ecosystem, these identifiers are unchanged:

- NPM/cargo package names (`firecrawl-local`, `@mendable/firecrawl-js`, etc.)
- Environment variables (`FIRECRAWL_API_KEY`, `FIRECRAWL_API_URL`, …)
- HTTP headers and Slack command names used by existing integrations
- Links and copy that refer to [firecrawl.dev](https://firecrawl.dev) cloud services when you choose to use hosted Firecrawl

You may point a self-hosted deployment at your own domain and customize further in your fork.