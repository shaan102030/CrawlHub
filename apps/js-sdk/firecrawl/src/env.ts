const API_KEY_ENV_VARS = ["CRAWLHUB_API_KEY", "FIRECRAWL_API_KEY"] as const;
const API_URL_ENV_VARS = ["CRAWLHUB_API_URL", "FIRECRAWL_API_URL"] as const;

export function resolveApiKeyFromEnv(
  env: Record<string, string | undefined> = process.env,
): string | undefined {
  for (const name of API_KEY_ENV_VARS) {
    const value = env[name]?.trim();
    if (value) return value;
  }
  return undefined;
}

export function resolveApiUrlFromEnv(
  env: Record<string, string | undefined> = process.env,
): string | undefined {
  for (const name of API_URL_ENV_VARS) {
    const value = env[name]?.trim();
    if (value) return value;
  }
  return undefined;
}