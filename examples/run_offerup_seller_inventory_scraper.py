#!/usr/bin/env python3
"""
OfferUp Seller Inventory & Auto Dealer Leads Scraper — Official Python SDK Quickstart
Actor: https://apify.com/unitbytes/offerup-seller-inventory-scraper?fpr=939u3w&fp_sid=gh_py
Docs & Schema: https://unitbytes.com/actors/offerup-seller-inventory-scraper/
n8n Template: https://unitbytes.com/n8n/workflows/offerup-seller-inventory-scraper-n8n-workflow.json

Usage:
    pip install apify-client
    export APIFY_API_TOKEN="your_apify_api_token"
    python examples/run_offerup_seller_inventory_scraper.py
"""

import os
from apify_client import ApifyClient

APIFY_TOKEN = os.getenv("APIFY_API_TOKEN", "YOUR_APIFY_API_TOKEN")
if not APIFY_TOKEN or APIFY_TOKEN.startswith("YOUR_"):
    raise SystemExit("Please set your Apify API token: export APIFY_API_TOKEN='apify_api_...'")

client = ApifyClient(APIFY_TOKEN)

run_input = {
    "sellerIds": ["100098765"],
    "zipCode": "77082",
    "categoryId": "5.1",
    "radius": 50,
    "maxItems": 20,
    "scrapeDetails": False
}

run = client.actor("unitbytes/offerup-seller-inventory-scraper").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("title"), item.get("price"), item.get("sellerName"), item.get("url"))
