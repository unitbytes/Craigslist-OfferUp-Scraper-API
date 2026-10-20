#!/usr/bin/env python3
"""
OfferUp Scraper: Marketplace Listings, Cars & Deals — Official Python SDK Quickstart
Actor: https://apify.com/unitbytes/offerup-scraper?fpr=939u3w&fp_sid=gh_py
Docs & Schema: https://unitbytes.com/actors/offerup-scraper/
n8n Template: https://unitbytes.com/n8n/workflows/offerup-scraper-n8n-workflow.json

Usage:
    pip install apify-client
    export APIFY_API_TOKEN="your_apify_api_token"
    python examples/run_offerup_scraper.py
"""

import os
from apify_client import ApifyClient

client = ApifyClient(os.getenv("APIFY_API_TOKEN", "YOUR_APIFY_API_TOKEN"))

run_input = {
    "searchQuery": "iphone 15",
    "zipCode": "90001",
    "startUrls": [],
    "proxyConfiguration": {
        "useApifyProxy": True,
        "apifyProxyGroups": ["RESIDENTIAL"],
        "apifyProxyCountry": "US"
    }
}

run = client.actor("unitbytes/offerup-scraper").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("title"), item.get("vehicleTitleStatus"), item.get("locationName"))
