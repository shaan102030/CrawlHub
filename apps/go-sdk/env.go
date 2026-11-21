package firecrawl

import (
	"os"
	"strings"
)

func envFirst(keys ...string) string {
	for _, key := range keys {
		if v := strings.TrimSpace(os.Getenv(key)); v != "" {
			return v
		}
	}
	return ""
}

func envAPIKey() string {
	return envFirst("CRAWLHUB_API_KEY", "FIRECRAWL_API_KEY")
}

func envAPIURL() string {
	return envFirst("CRAWLHUB_API_URL", "FIRECRAWL_API_URL")
}