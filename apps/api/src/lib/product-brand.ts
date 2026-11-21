/** Display name for this fork (CrawlHub). */
export const PRODUCT_NAME = "CrawlHub";

/** Preferred API key env var for this fork; legacy Firecrawl name still accepted. */
export const API_KEY_ENV_VARS = ["CRAWLHUB_API_KEY", "FIRECRAWL_API_KEY"] as const;

/** Preferred API URL env var for this fork; legacy Firecrawl name still accepted. */
export const API_URL_ENV_VARS = ["CRAWLHUB_API_URL", "FIRECRAWL_API_URL"] as const;

export function readEnvApiKey(): string | undefined {
  for (const name of API_KEY_ENV_VARS) {
    const value = process.env[name]?.trim();
    if (value) return value;
  }
  return undefined;
}

export function readEnvApiUrl(): string | undefined {
  for (const name of API_URL_ENV_VARS) {
    const value = process.env[name]?.trim();
    if (value) return value;
  }
  return undefined;
}