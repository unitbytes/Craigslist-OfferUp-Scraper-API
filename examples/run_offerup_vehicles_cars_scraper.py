#!/usr/bin/env python3
"""
OfferUp Used Cars, Vehicles & VIN Scraper: Dealer Specs — Official Python SDK Quickstart
Actor: https://apify.com/unitbytes/offerup-vehicles-cars-scraper?fpr=939u3w&fp_sid=gh_py
Docs & Schema: https://unitbytes.com/actors/offerup-vehicles-cars-scraper/
n8n Template: https://unitbytes.com/n8n/workflows/offerup-vehicles-cars-scraper-n8n-workflow.json

Usage:
    pip install apify-client
    export APIFY_API_TOKEN="your_apify_api_token"
    python examples/run_offerup_vehicles_cars_scraper.py
"""

import os
from apify_client import ApifyClient

APIFY_TOKEN = os.getenv("APIFY_API_TOKEN", "YOUR_APIFY_API_TOKEN")
if not APIFY_TOKEN or APIFY_TOKEN.startswith("YOUR_"):
    raise SystemExit("Please set your Apify API token: export APIFY_API_TOKEN='apify_api_...'")

client = ApifyClient(APIFY_TOKEN)

run_input = {
    "make": "Honda",
    "model": "Civic",
    "zipCode": "90001",
    "categoryId": "5.1",
    "radius": 50,
    "sortBy": "-posted"
}

run = client.actor("unitbytes/offerup-vehicles-cars-scraper").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("title"), item.get("price"), item.get("vehicleMiles"), item.get("vehicleVin"))
