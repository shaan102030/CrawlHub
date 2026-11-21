import os


def _env_first(*names: str) -> str | None:
    for name in names:
        value = os.getenv(name)
        if value and value.strip():
            return value.strip()
    return None


def env_api_key() -> str | None:
    return _env_first("CRAWLHUB_API_KEY", "FIRECRAWL_API_KEY")


def env_api_url() -> str | None:
    return _env_first("CRAWLHUB_API_URL", "FIRECRAWL_API_URL")