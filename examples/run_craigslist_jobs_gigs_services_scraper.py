#!/usr/bin/env python3
"""
Craigslist Jobs, Gigs & Services Scraper: Pay & Remote — Official Python SDK Quickstart
Actor: https://apify.com/unitbytes/craigslist-jobs-gigs-services-scraper?fpr=939u3w&fp_sid=gh_py
Docs & Schema: https://unitbytes.com/actors/craigslist-jobs-gigs-services-scraper/
n8n Template: https://unitbytes.com/n8n/workflows/craigslist-jobs-gigs-services-scraper-n8n-workflow.json

Usage:
    pip install apify-client
    export APIFY_API_TOKEN="your_apify_api_token"
    python examples/run_craigslist_jobs_gigs_services_scraper.py
"""

import os
from apify_client import ApifyClient

APIFY_TOKEN = os.getenv("APIFY_API_TOKEN", "YOUR_APIFY_API_TOKEN")
if not APIFY_TOKEN or APIFY_TOKEN.startswith("YOUR_"):
    raise SystemExit("Please set your Apify API token: export APIFY_API_TOKEN='apify_api_...'")

client = ApifyClient(APIFY_TOKEN)

run_input = {
    "searchQuery": "software engineer",
    "category": "jjj",
    "subdomain": "losangeles",
    "scrapeDetails": True,
    "hasImage": False,
    "postedToday": False
}

run = client.actor("unitbytes/craigslist-jobs-gigs-services-scraper").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("title"), item.get("jobTitle"), item.get("companyName"))
