"""
Apify Client Runner for Clutch B2B Agencies & IT Services Scraper
Actor URL: https://apify.com/moneygain/clutch-agencies-scraper
"""

import os
from apify_client import ApifyClient

# 1. Initialize the client with your Apify API token
# Get your free token at: https://console.apify.com/account/integrations
api_token = os.getenv("APIFY_TOKEN", "YOUR_APIFY_TOKEN")
client = ApifyClient(api_token)

# 2. Define Actor input parameters
run_input = {
    "startUrls": [
        {
            "url": "https://clutch.co/agencies"
        },
        {
            "url": "https://clutch.co/developers"
        }
    ],
    "category": "agencies",
    "minRating": 0,
    "maxItems": 10,
    "proxyConfiguration": {
        "useApifyProxy": true,
        "apifyProxyGroups": [
            "RESIDENTIAL"
        ]
    }
}

def main():
    print("🚀 Starting Clutch B2B Agencies & IT Services Scraper on Apify Cloud...")
    run = client.actor("moneygain/clutch-agencies-scraper").call(run_input=run_input)
    print(f"✅ Scraping completed! Run ID: {run.get('id')}")
    
    # 3. Fetch results from default dataset
    dataset_client = client.dataset(run["defaultDatasetId"])
    items = list(dataset_client.iterate_items())
    print(f"📊 Retrieved {len(items)} records.")
    for item in items[:5]:
        print(item)

if __name__ == "__main__":
    main()
