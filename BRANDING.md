# CrawlHub branding

CrawlHub is a fork of [Firecrawl](https://github.com/firecrawl/firecrawl), licensed under the same GNU Affero General Public License v3.

## Rebranded in this fork

| Item | CrawlHub value | Legacy (still works) |
|------|----------------|----------------------|
| Product name | **CrawlHub** | — |
| Local CLI | `crawlhub-local` | `firecrawl-local` (alias) |
| API key env | `CRAWLHUB_API_KEY` | `FIRECRAWL_API_KEY` |
| API URL env | `CRAWLHUB_API_URL` | `FIRECRAWL_API_URL` |
| Docker Compose project | `crawlhub` | — |
| K8s ConfigMap/Secret names | `crawlhub-config`, `crawlhub-secret` | — |
| Helm chart path | `examples/kubernetes/crawlhub-helm` | — |
| PHP package (Composer) | `crawlhub/crawlhub-sdk` | — |
| Logos | `img/crawlhub_*` | — |

SDKs (JavaScript, Python, Go, PHP) resolve **CRAWLHUB_*** env vars first, then **FIRECRAWL_***.

## Intentionally unchanged (compatibility)

These keep upstream names so existing scripts, hosted Firecrawl Cloud, and published NPM/PyPI crates keep working:

- Crates.io / npm package names (`firecrawl-local` crate name, `@mendable/firecrawl-js`, `firecrawl` PyPI module)
- Class and type names (`FirecrawlClient`, `FirecrawlApp`, …)
- Slack slash command `/firecrawl` and HTTP headers `X-Firecrawl-*`
- Default cloud API host `https://api.firecrawl.dev` when no custom URL is set
- Internal Rust crate `firecrawl_local` and config keys prefixed with `FIRECRAWL_` in `apps/api`

You can point `CRAWLHUB_API_URL` at your own deployment and customize further in your fork.