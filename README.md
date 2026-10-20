# 🏷️ Craigslist & OfferUp Scraper API (Local Classifieds, Cars & Real Estate Leads)

<div align="center">

[![Available on Apify](https://img.shields.io/badge/Available_on-Apify-28B52A?style=for-the-badge&logo=apify&logoColor=white)](https://apify.com/unitbytes/craigslist-scraper?fpr=939u3w&fp_sid=gh_classifieds)
[![n8n Creator Hub](https://img.shields.io/badge/n8n_Creator_Hub-@unitbytes-EA4B71?style=for-the-badge&logo=n8n&logoColor=white)](https://n8n.io/creators/unitbytes/)
[![Zero Login](https://img.shields.io/badge/Account_Required-None-blue?style=for-the-badge)](https://apify.com/unitbytes/craigslist-scraper?fpr=939u3w&fp_sid=gh_classifieds)
[![Pricing](https://img.shields.io/badge/Pricing-Pay_Per_Result-orange?style=for-the-badge)](https://apify.com/unitbytes/craigslist-scraper?fpr=939u3w&fp_sid=gh_classifieds)

**High-speed Craigslist Worldwide ($0.50/1k) and OfferUp Marketplace Scraper API on Apify. Extract used cars, real estate housing leads, local resale bargains, and verified seller data.**

[**🚀 Try Live on Apify**](https://apify.com/unitbytes/craigslist-scraper?fpr=939u3w&fp_sid=gh_classifieds) • [**⚡ Official n8n Creator Hub**](https://n8n.io/creators/unitbytes/) • [**🔧 23 Free n8n Templates**](https://unitbytes.com/n8n/) • [**📖 Documentation & Schemas**](https://unitbytes.com/actors/) • [**📚 Engineering Playbooks**](https://unitbytes.com/blog/)

</div>

---

<p align="center">
  <a href="https://apify.com/unitbytes/craigslist-scraper?fpr=939u3w&fp_sid=gh_classifieds" target="_blank">
    <img src="https://raw.githubusercontent.com/unitbytes/.github/main/assets/banners/unitbytes-craigslist-leads-housing-cars-scraper-banner.jpg" alt="🏷️ Craigslist & OfferUp Scraper API (Local Classifieds, Cars & Real Estate Leads)" width="100%" />
  </a>
</p>

<p align="center">
  <a href="https://apify.com/unitbytes/craigslist-scraper?fpr=939u3w&fp_sid=gh_classifieds" target="_blank">
    <img src="https://raw.githubusercontent.com/unitbytes/.github/main/assets/try-it-for-free.svg" width="240" height="48" alt="Try it for Free">
  </a>
  <br>
  <sub>⚡ <b>1-Click Free Trial:</b> Test live queries using Apify's $5 free monthly credit • Zero login or cookies required</sub>
</p>

---

<!-- UNITBYTES_REPO_KIT_START -->
## 📦 Included in This Repository (Python Quickstarts, n8n Workflows, MCP & Sample Data)

This repository contains ready-to-run **Python SDK scripts**, **1-click n8n automation workflow `.json` templates**, **AI Agent MCP configuration (`.cursor/mcp.json`)**, and **sample output datasets (JSON & CSV)**:

| Extraction Engine | 🐍 Python SDK Quickstart | ⚡ n8n Workflow Template | 📊 Sample Output | 🚀 Cloud Console |
| :--- | :--- | :--- | :---: | :---: |
| **Craigslist Scraper Worldwide: All Cities Subareas & Leads $0.50**<br><sub>[`unitbytes/craigslist-scraper`](https://apify.com/unitbytes/craigslist-scraper?fpr=939u3w&fp_sid=gh_classifieds) • [Full Schema](https://unitbytes.com/actors/craigslist-scraper/) • [Engineering Playbook](https://unitbytes.com/blog/local-classifieds-arbitrage-facebook-marketplace-craigslist-offerup-guide/)</sub> | [`examples/run_craigslist_scraper.py`](examples/run_craigslist_scraper.py) | [`n8n/craigslist-scraper-n8n-workflow.json`](n8n/craigslist-scraper-n8n-workflow.json) | [`JSON`](samples/craigslist-scraper-sample.json) · [`CSV`](samples/craigslist-scraper-sample.csv) | [⚡ **Run on Apify**](https://apify.com/unitbytes/craigslist-scraper?fpr=939u3w&fp_sid=gh_classifieds) |
| **OfferUp Scraper: Marketplace Listings, Cars & Deals**<br><sub>[`unitbytes/offerup-scraper`](https://apify.com/unitbytes/offerup-scraper?fpr=939u3w&fp_sid=gh_classifieds) • [Full Schema](https://unitbytes.com/actors/offerup-scraper/) • [Engineering Playbook](https://unitbytes.com/blog/local-classifieds-arbitrage-facebook-marketplace-craigslist-offerup-guide/)</sub> | [`examples/run_offerup_scraper.py`](examples/run_offerup_scraper.py) | [`n8n/offerup-scraper-n8n-workflow.json`](n8n/offerup-scraper-n8n-workflow.json) | [`JSON`](samples/offerup-scraper-sample.json) · [`CSV`](samples/offerup-scraper-sample.csv) | [⚡ **Run on Apify**](https://apify.com/unitbytes/offerup-scraper?fpr=939u3w&fp_sid=gh_classifieds) |

- 🤖 **Cursor, Windsurf & Claude Code MCP Ready:** Includes [`.cursor/mcp.json`](.cursor/mcp.json) pre-configured with `https://mcp.apify.com` so AI coding agents can invoke these UnitBytes scrapers natively.
- 💡 **Using n8n?** Explore our official creator profile at **[n8n.io/creators/unitbytes](https://n8n.io/creators/unitbytes/)** or copy all 23 pre-built scraping workflows (`Ctrl+V`) at **[unitbytes.com/n8n](https://unitbytes.com/n8n/)**.
- 📚 **Engineering Playbook:** Read **[Automating Local Classifieds Arbitrage: Scraping Facebook Marketplace, Craigslist & OfferUp](https://unitbytes.com/blog/local-classifieds-arbitrage-facebook-marketplace-craigslist-offerup-guide/)** or browse all scraping & automation guides at **[unitbytes.com/blog](https://unitbytes.com/blog/)**.
<!-- UNITBYTES_REPO_KIT_END -->

---

## ⚡ Pre-Configured 1-Click Task Presets

Launch pre-configured extraction templates directly in the Apify Cloud Console with zero parameter setup:

| Task Preset | Target Extraction Use Case | Direct Launch |
| :--- | :--- | :---: |
| **Find Used Cars Under $5,000 by Owner on Craigslist** | Extract used cars, trucks, and SUVs priced under $5,000 sold directly by private owners across top US metros. Get VIN, mileage, title status, and seller phone numbers. | [⚡ Run Task Preset](https://apify.com/unitbytes/craigslist-scraper/examples/used-cars-under-5000-by-owner?fpr=939u3w&fp_sid=web_tasks) |
| **Track Toyota Tacoma & 4x4 Trucks on Craigslist** | Monitor Toyota Tacoma, Tundra, and 4x4 pickup trucks across any metro. Extract model year, trim, mileage, 17-character VIN, and high-resolution photo galleries. | [⚡ Run Task Preset](https://apify.com/unitbytes/craigslist-scraper/examples/craigslist-toyota-tacoma-trucks?fpr=939u3w&fp_sid=web_tasks) |
| **Find Honda Civic & Accord Deals on Craigslist** | Discover Honda Civic and Accord listings for car flipping or daily commuting. Extract asking price, clean/salvage title status, transmission, and seller phone numbers. | [⚡ Run Task Preset](https://apify.com/unitbytes/craigslist-scraper/examples/craigslist-honda-civic-deals?fpr=939u3w&fp_sid=web_tasks) |
| **Scrape Apartments & Rental Housing on Craigslist** | Extract rental housing listings across major US cities. Collect rent prices, bedroom counts, bathrooms, square footage, neighborhood locations, and full descriptions. | [⚡ Run Task Preset](https://apify.com/unitbytes/craigslist-scraper/examples/craigslist-apartments-rental-housing?fpr=939u3w&fp_sid=web_tasks) |
| **Find FSBO Real Estate & Homes for Sale on Craigslist** | Capture For Sale by Owner (FSBO) real estate, land, houses, and commercial property listings with asking prices, seller contact info, and coordinates. | [⚡ Run Task Preset](https://apify.com/unitbytes/craigslist-scraper/examples/craigslist-fsbo-real-estate-homes?fpr=939u3w&fp_sid=web_tasks) |
| **Find Apple iPhones & MacBooks on Craigslist for Resale** | Discover discounted Apple MacBooks, iPhones, iPads, and AirPods for e-commerce flipping and resale arbitrage on eBay, Amazon, or Mercari. | [⚡ Run Task Preset](https://apify.com/unitbytes/craigslist-scraper/examples/craigslist-apple-macbook-iphone?fpr=939u3w&fp_sid=web_tasks) |
| **Scrape Used Cars Under $5,000 on OfferUp** | Extract budget cars, trucks, and SUVs under $5,000 including mileage, title status, and seller rating. | [⚡ Run Task Preset](https://apify.com/unitbytes/offerup-scraper/examples/cheap-used-cars-under-5000?fpr=939u3w&fp_sid=web_tasks) |
| **Find Honda Civic Deals on OfferUp** | Find all Honda Civics listed for sale with VIN, mileage, transmission, and photo gallery. | [⚡ Run Task Preset](https://apify.com/unitbytes/offerup-scraper/examples/honda-civic-deals-finder?fpr=939u3w&fp_sid=web_tasks) |
| **Track Toyota Tacoma Trucks on OfferUp** | Extract Toyota Tacoma and 4Runner listings with year, trim, mileage, and seller contact stats. | [⚡ Run Task Preset](https://apify.com/unitbytes/offerup-scraper/examples/toyota-tacoma-trucks-tracker?fpr=939u3w&fp_sid=web_tasks) |
| **Extract iPhone & Apple Device Deals** | Extract unlocked iPhones, iPads, and MacBooks with condition notes and seller ratings. | [⚡ Run Task Preset](https://apify.com/unitbytes/offerup-scraper/examples/iphone-apple-deals-extractor?fpr=939u3w&fp_sid=web_tasks) |
| **Find MacBook Pro & Laptop Deals on OfferUp** | Monitor MacBook Pro and laptop bargains with price, seller response time, and specs. | [⚡ Run Task Preset](https://apify.com/unitbytes/offerup-scraper/examples/macbook-pro-laptop-deals?fpr=939u3w&fp_sid=web_tasks) |
| **Find PS5 & Gaming Console Deals** | Extract PlayStation 5, Xbox Series X, and Nintendo Switch console listings with seller history. | [⚡ Run Task Preset](https://apify.com/unitbytes/offerup-scraper/examples/playstation-ps5-and-gaming-deals?fpr=939u3w&fp_sid=web_tasks) |

---

## 🛠️ Extraction Engines in This Suite

### 🚀 Craigslist Scraper Worldwide: All Cities Subareas & Leads $0.50 (`unitbytes/craigslist-scraper`)

Ultra Fast & Cheapest Craigslist Scraper worldwide across 700+ cities and boroughs in the US, Canada, UK, Australia, Europe, and Asia. Extract direct seller phones, emails, cars, housing, and multi-currency pricing from $0.50/1k.

- **Pricing:** `$0.0005 / item` (Pay-Per-Event — $0.0005 search result, $0.0015 detailed listing (volume tiers from $0.00035))
- **Cloud Console:** [https://apify.com/unitbytes/craigslist-scraper?fpr=939u3w&fp_sid=gh_classifieds](https://apify.com/unitbytes/craigslist-scraper?fpr=939u3w&fp_sid=gh_classifieds)
- **Full Documentation & Schema:** [https://unitbytes.com/actors/craigslist-scraper/](https://unitbytes.com/actors/craigslist-scraper/)
- **n8n Workflow File:** [`n8n/craigslist-scraper-n8n-workflow.json`](n8n/craigslist-scraper-n8n-workflow.json)
- **Engineering Playbook:** [Automating Local Classifieds Arbitrage: Scraping Facebook Marketplace, Craigslist & OfferUp](https://unitbytes.com/blog/local-classifieds-arbitrage-facebook-marketplace-craigslist-offerup-guide/)

#### Key Capabilities
- **Cross-City Geographic Aggregation:** Scrape single metro areas or aggregate queries across entire states and nationwide regions simultaneously.
- **Automotive Specification Parsing:** Extracts vehicle title status, odometer mileage, VIN, transmission, fuel type, and seller type (dealer vs owner).
- **Rental & Real Estate Breakdown:** Captures rent prices, bedroom count, bathrooms, square footage, housing type, and pet accommodation flags.
- **Clean Uncluttered JSON:** Filters out HTML markup, extracting normalized text, posted timestamps, updated timestamps, and image arrays.

#### Python SDK Quickstart (`examples/run_craigslist_scraper.py`)
```python
from apify_client import ApifyClient

client = ApifyClient("YOUR_APIFY_TOKEN")

run_input = {
    "startUrls": [],
    "searchUrl": "",
    "searchQuery": "",
    "subarea": "",
    "subdomains": [],
    "postal": "",
    "customStoreName": ""
}

run = client.actor("unitbytes/craigslist-scraper").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("title"), item.get("vehicleTitleStatus"), item.get("price"))
```

#### Sample Output Schema (`samples/craigslist-scraper-sample.json`)
```json
{
  "listingId": "7782194820",
  "url": "https://www.craigslist.org/view/d/santa-monica-2015-nissan-nv2500-high/7782194820",
  "title": "2015 Nissan NV2500 High Roof Cargo Van",
  "price": 18500,
  "currency": "USD",
  "subarea": "wst",
  "condition": "excellent",
  "description": "Clean 2015 Nissan NV2500 High Roof van. V8 5.6L engine, automatic transmission, cold A/C. Call or text me at (310) 555-1234 or email seller@gmail.com for questions. Clean title in hand.",
  "postDate": "2026-09-13T18:42:15-0700",
  "city": "Santa Monica",
  "state": "CA",
  "zipCode": "90401",
  "latitude": 34.0195,
  "longitude": -118.4912,
  "isDealer": false,
  "contactObfuscated": false,
  "phoneNumbers": [
    "(310) 555-1234"
  ],
  "emails": [
    "seller@gmail.com"
  ],
  "isVehicle": true,
  "vehicleYear": 2015,
  "vehicleMake": "Nissan",
  "vehicleModel": "NV2500",
  "vehicleMiles": 112400,
  "vehicleVin": "1N6BF0KY5FN812345",
  "vehicleTransmission": "automatic",
  "vehicleFuelType": "gas",
  "vehicleTitleStatus": "clean",
  "thumbnailUrl": "https://images.craigslist.org/00B0B_1ZBm7qXYZ_600x450.jpg",
  "imageUrls": [
    "https://images.craigslist.org/00B0B_1ZBm7qXYZ_1200x900.jpg",
    "https://images.craigslist.org/00H0H_2CDe8rUVW_1200x900.jpg"
  ]
}
```

#### Frequently Asked Questions
**Q: Can I search multiple cities at the same time?**
Yes. Pass a list of Craigslist subdomains (e.g. ["austin", "dallas", "houston"]) to execute multi-city sweeps in one run.

**Q: How does the scraper handle Craigslist IP rate limits?**
Craigslist strictly blocks cloud datacenter IPs. The UnitBytes engine automatically routes requests through rotating residential proxies with zero IP bans.

**Q: Can I extract email addresses or phone numbers?**
Any contact information published directly in the listing body is extracted. Craigslist two-way relay email addresses are preserved.

**Q: How frequently can I run this scraper?**
Run on demand or schedule hourly cron runs to detect new bargain listings minutes after publication.

---

### 🚀 OfferUp Scraper: Marketplace Listings, Cars & Deals (`unitbytes/offerup-scraper`)

Fast OfferUp Scraper with no login required. Extract local marketplace listings, used cars & VINs, seller ratings, HD photos, and prices with Smart Scrape deduplication. From $0.80/1k.

- **Pricing:** `$0.003 / item` (Pay-Per-Event — $0.003 listing discovery, $0.008 deep detail enrichment (volume tiers from $0.0006))
- **Cloud Console:** [https://apify.com/unitbytes/offerup-scraper?fpr=939u3w&fp_sid=gh_classifieds](https://apify.com/unitbytes/offerup-scraper?fpr=939u3w&fp_sid=gh_classifieds)
- **Full Documentation & Schema:** [https://unitbytes.com/actors/offerup-scraper/](https://unitbytes.com/actors/offerup-scraper/)
- **n8n Workflow File:** [`n8n/offerup-scraper-n8n-workflow.json`](n8n/offerup-scraper-n8n-workflow.json)
- **Engineering Playbook:** [Automating Local Classifieds Arbitrage: Scraping Facebook Marketplace, Craigslist & OfferUp](https://unitbytes.com/blog/local-classifieds-arbitrage-facebook-marketplace-craigslist-offerup-guide/)

#### Key Capabilities
- **Precise Postal Zip Code Targeting:** Target any US zip code with radius filtering (5, 10, 20, 50 miles) to extract hyper-local classifieds.
- **Seller Reputation & TruYou Badges:** Extract seller star ratings, total sales count, account join date, and OfferUp TruYou ID verification status.
- **Shipping & Local Pickup Segmentation:** Distinguish between nationwide shipped items and local cash-and-carry listings for precise deal finding.
- **Condition & Negotiable Flags:** Captures item condition (New, Open Box, Used, For Parts) and whether the seller is open to price offers.

#### Python SDK Quickstart (`examples/run_offerup_scraper.py`)
```python
from apify_client import ApifyClient

client = ApifyClient("YOUR_APIFY_TOKEN")

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
```

#### Sample Output Schema (`samples/offerup-scraper-sample.json`)
```json
{
  "listingId": "98ac7bc0-3fb6-3841-a8c6-e09242e60239",
  "url": "https://offerup.com/item/detail/98ac7bc0-3fb6-3841-a8c6-e09242e60239",
  "title": "2000 Honda Civic",
  "price": 16999,
  "originalPrice": 16999,
  "isFirmPrice": false,
  "condition": "Open Box / Like New",
  "description": "Selling my 2000 Honda Civic Si (EM1) with 168,635 miles. Clean title, runs great, AC cold.",
  "locationName": "Snohomish, WA",
  "distanceMiles": 12.4,
  "latitude": 48.035,
  "longitude": -122.039,
  "sellerName": "Kyle",
  "sellerRating": 5,
  "sellerReviewCount": 69,
  "sellerDateJoined": "2016-03-10T04:17:26Z",
  "sellerItemsSold": 115,
  "sellerResponseTime": "Responds in a few minutes",
  "sellerVerified": true,
  "isDealer": false,
  "isVehicle": true,
  "vehicleYear": 2000,
  "vehicleMake": "Honda",
  "vehicleModel": "Civic",
  "vehicleTrim": "SI",
  "vehicleMiles": 168635,
  "vehicleTransmission": "Manual",
  "vehicleFuelType": "Regular",
  "vehicleTitleStatus": "clean",
  "thumbnailUrl": "https://images.offerup.com/lpERZEJKw582yoN6AQA9YowYf8U=/333x250/4f74/4f7412e94d3542ecbb49a6012adeae69.jpg",
  "imageUrls": [
    "https://images.offerup.com/3wcWUHuAUp24fM0rkI4UffFmn_k=/1280x960/4f74/4f7412e94d3542ecbb49a6012adeae69.jpg",
    "https://images.offerup.com/XmgJCqtcdbPol0IbjbPHZFIVmJE=/960x1280/5f2a/5f2a8b7b78ce4f31a32f5f7d810f3c2f.jpg"
  ],
  "localPickup": true,
  "shippingAvailable": false
}
```

#### Frequently Asked Questions
**Q: Can I filter listings by shipping availability?**
Yes. You can isolate local pickup items, nationwide shipping listings, or collect both.

**Q: How does the scraper handle OfferUp rate limits?**
The UnitBytes engine utilizes managed cloud request routing and residential proxy pools, handling anti-bot checks automatically.

**Q: Are high-resolution photos included?**
Yes, every listing includes direct links to full-resolution photos hosted on OfferUp CDN.

**Q: What data export formats are provided?**
Download directly in JSON, CSV, Excel, or stream records via REST API and Webhooks.


---

## ⚡ Quick Installation & Local Usage

### 1. Run with Python (`apify-client`)
```bash
git clone https://github.com/unitbytes/Craigslist-OfferUp-Scraper-API.git
cd Craigslist-OfferUp-Scraper-API
pip install -r requirements.txt
export APIFY_API_TOKEN="your_apify_api_token"
python examples/run_craigslist_scraper.py
```

### 2. Import into n8n (Self-Hosted or Cloud)
1. Open any `.json` file inside the [`n8n/`](n8n/) folder (or copy in 1 click from **[unitbytes.com/n8n](https://unitbytes.com/n8n/)** / **[n8n.io/creators/unitbytes](https://n8n.io/creators/unitbytes/)**).
2. Press **`Ctrl+V` / `Cmd+V`** directly onto your n8n workflow canvas.
3. Paste your Apify API Token into Node `1. Set Apify Token & Input` and click **Test Workflow**.

### 3. Use with AI Coding Agents (Cursor, Windsurf & Claude Code MCP)
This repository includes a ready-to-use Model Context Protocol configuration at [`.cursor/mcp.json`](.cursor/mcp.json) pointing to `https://mcp.apify.com` with this suite's UnitBytes actors pre-registered. Open this folder in **Cursor** or **Windsurf** to let your AI agent run live extractions and inspect schemas automatically.

---

## 💼 Need Done-For-You Datasets or Custom Pipelines?

Don't want to manage API tokens or scripts? **UnitBytes Data Delivery** provides ready-to-use **CSV, Excel (.xlsx), Google Sheets, or Webhook feeds** tailored to your exact target keywords, cities, or categories.

- 🌐 **Request a Sample Dataset:** [https://unitbytes.com/#enterprise-intake](https://unitbytes.com/#enterprise-intake)
- 📧 **Direct Engineering Contact:** [contact@unitbytes.com](mailto:contact@unitbytes.com)
- ⚡ **Explore All 23 Scrapers:** [https://unitbytes.com/actors/](https://unitbytes.com/actors/)
- 📚 **Engineering Playbooks & Guides:** [https://unitbytes.com/blog/](https://unitbytes.com/blog/)
- 🔗 **Official n8n Creator Profile:** [https://n8n.io/creators/unitbytes/](https://n8n.io/creators/unitbytes/)
