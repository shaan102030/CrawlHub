//! CrawlHub fork branding for user-facing text and env var aliases.

pub const PRODUCT_NAME: &str = "CrawlHub";

pub const SIGN_IN_HINT: &str =
  "Run `crawlhub-local login` (or `firecrawl-local login`), or set CRAWLHUB_API_KEY or FIRECRAWL_API_KEY.";

pub fn env_api_key() -> Option<String> {
  for key in ["CRAWLHUB_API_KEY", "FIRECRAWL_API_KEY"] {
    if let Ok(value) = std::env::var(key) {
      let trimmed = value.trim();
      if !trimmed.is_empty() {
        return Some(trimmed.to_string());
      }
    }
  }
  None
}

pub fn env_api_url() -> Option<String> {
  for key in ["CRAWLHUB_API_URL", "FIRECRAWL_API_URL"] {
    if let Ok(value) = std::env::var(key) {
      let trimmed = value.trim();
      if !trimmed.is_empty() {
        return Some(trimmed.to_string());
      }
    }
  }
  None
}