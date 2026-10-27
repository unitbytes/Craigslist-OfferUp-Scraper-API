#!/usr/bin/env python3
"""
Craigslist Cars & Vehicles Scraper: By Owner, VIN & Miles — Official Python SDK Quickstart
Actor: https://apify.com/unitbytes/craigslist-cars-vehicles-scraper?fpr=939u3w&fp_sid=gh_py
Docs & Schema: https://unitbytes.com/actors/craigslist-cars-vehicles-scraper/
n8n Template: https://unitbytes.com/n8n/workflows/craigslist-cars-vehicles-scraper-n8n-workflow.json

Usage:
    pip install apify-client
    export APIFY_API_TOKEN="your_apify_api_token"
    python examples/run_craigslist_cars_vehicles_scraper.py
"""

import os
from apify_client import ApifyClient

APIFY_TOKEN = os.getenv("APIFY_API_TOKEN", "YOUR_APIFY_API_TOKEN")
if not APIFY_TOKEN or APIFY_TOKEN.startswith("YOUR_"):
    raise SystemExit("Please set your Apify API token: export APIFY_API_TOKEN='apify_api_...'")

client = ApifyClient(APIFY_TOKEN)

run_input = {
    "searchQuery": "toyota tacoma",
    "autoMakeModel": "toyota tacoma",
    "category": "cto",
    "subdomain": "losangeles",
    "scrapeDetails": True,
    "hasImage": False
}

run = client.actor("unitbytes/craigslist-cars-vehicles-scraper").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("title"), item.get("vehicleTitleStatus"), item.get("price"))
