# 🏷️ Craigslist & OfferUp Scraper API Suite (Cars, Real Estate, Jobs & Dealer Leads)

<div align="center">

[![Available on Apify](https://img.shields.io/badge/Available_on-Apify-28B52A?style=for-the-badge&logo=apify&logoColor=white)](https://apify.com/unitbytes/craigslist-scraper?fpr=939u3w&fp_sid=gh_classifieds)
[![Open in Colab](https://img.shields.io/badge/Open_in-Google_Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white)](https://colab.research.google.com/github/unitbytes/Craigslist-OfferUp-Scraper-API/blob/main/notebooks/quickstart.ipynb)
[![n8n Creator Hub](https://img.shields.io/badge/n8n_Creator_Hub-@unitbytes-EA4B71?style=for-the-badge&logo=n8n&logoColor=white)](https://n8n.io/creators/unitbytes/)
[![Release](https://img.shields.io/github/v/release/unitbytes/Craigslist-OfferUp-Scraper-API?style=for-the-badge&logo=github&color=10b981)](https://github.com/unitbytes/Craigslist-OfferUp-Scraper-API/releases)
[![Pricing](https://img.shields.io/badge/Pricing-Pay_Per_Result-orange?style=for-the-badge)](https://apify.com/unitbytes/craigslist-scraper?fpr=939u3w&fp_sid=gh_classifieds)

**High-speed Craigslist Worldwide (`$0.50/1k`) and OfferUp Marketplace (`$0.80/1k`) Scraper API suite on Apify. Extract used cars & VINs, real estate housing leads, jobs & gigs, seller inventories, auto dealer phones, and local resale bargains.**

[**🚀 Try Live on Apify**](https://apify.com/unitbytes/craigslist-scraper?fpr=939u3w&fp_sid=gh_classifieds) • [**📓 Open in Google Colab**](https://colab.research.google.com/github/unitbytes/Craigslist-OfferUp-Scraper-API/blob/main/notebooks/quickstart.ipynb) • [**⚡ Official n8n Creator Hub**](https://n8n.io/creators/unitbytes/) • [**🔧 39 Free n8n Templates**](https://unitbytes.com/n8n/) • [**📖 Documentation & Schemas**](https://unitbytes.com/actors/) • [**📚 Engineering Playbooks**](https://unitbytes.com/blog/)

</div>

---

<p align="center">
  <a href="https://apify.com/unitbytes/craigslist-scraper?fpr=939u3w&fp_sid=gh_classifieds" target="_blank">
    <img src="https://raw.githubusercontent.com/unitbytes/.github/main/assets/banners/unitbytes-craigslist-leads-housing-cars-scraper-banner.jpg" alt="🏷️ Craigslist & OfferUp Scraper API Suite (Cars, Real Estate, Jobs & Dealer Leads)" width="100%" />
  </a>
</p>

<p align="center">
  <a href="https://apify.com/unitbytes/craigslist-scraper?fpr=939u3w&fp_sid=gh_classifieds" target="_blank">
    <img src="https://raw.githubusercontent.com/unitbytes/.github/main/assets/try-it-for-free.svg" width="240" height="48" alt="Try it for Free">
  </a>
  <br>
  <sub>⚡ <b>1-Click Free Trial:</b> Test live queries using Apify's `$5` free monthly credit • Zero login or cookies required</sub>
</p>

---

<!-- UNITBYTES_REPO_KIT_START -->
## 📦 Included in This Repository (Python Quickstarts, Google Colab, n8n Workflows, MCP & Sample Data)

This repository contains ready-to-run **Python SDK scripts**, an **interactive 1-Click Google Colab notebook (`notebooks/quickstart.ipynb`)**, **9-node n8n automation workflow `.json` templates**, **AI Agent MCP configuration (`.cursor/mcp.json`)**, and **sample output datasets (JSON & CSV)**:

| Extraction Engine | 🐍 Python SDK Quickstart | ⚡ n8n Workflow Template | 📊 Sample Output | 🚀 Cloud Console |
| :--- | :--- | :--- | :---: | :---: |
| **Craigslist Search Scraper: Cars, Housing, Jobs & For Sale**<br><sub>[`unitbytes/craigslist-scraper`](https://apify.com/unitbytes/craigslist-scraper?fpr=939u3w&fp_sid=gh_classifieds) • [Full Schema](https://unitbytes.com/actors/craigslist-scraper/) • [Engineering Playbook](https://unitbytes.com/blog/local-classifieds-arbitrage-facebook-marketplace-craigslist-offerup-guide/)</sub> | [`examples/run_craigslist_scraper.py`](examples/run_craigslist_scraper.py) | [`n8n/craigslist-scraper-n8n-workflow.json`](n8n/craigslist-scraper-n8n-workflow.json) | [`JSON`](samples/craigslist-scraper-sample.json) · [`CSV`](samples/craigslist-scraper-sample.csv) | [⚡ **Run on Apify**](https://apify.com/unitbytes/craigslist-scraper?fpr=939u3w&fp_sid=gh_classifieds) |
| **Craigslist Cars & Vehicles Scraper: By Owner, VIN & Miles**<br><sub>[`unitbytes/craigslist-cars-vehicles-scraper`](https://apify.com/unitbytes/craigslist-cars-vehicles-scraper?fpr=939u3w&fp_sid=gh_classifieds) • [Full Schema](https://unitbytes.com/actors/craigslist-cars-vehicles-scraper/) • [Engineering Playbook](https://unitbytes.com/blog/used-car-vin-real-estate-fsbo-scraping-facebook-marketplace-craigslist-offerup-guide/)</sub> | [`examples/run_craigslist_cars_vehicles_scraper.py`](examples/run_craigslist_cars_vehicles_scraper.py) | [`n8n/craigslist-cars-vehicles-scraper-n8n-workflow.json`](n8n/craigslist-cars-vehicles-scraper-n8n-workflow.json) | [`JSON`](samples/craigslist-cars-vehicles-scraper-sample.json) · [`CSV`](samples/craigslist-cars-vehicles-scraper-sample.csv) | [⚡ **Run on Apify**](https://apify.com/unitbytes/craigslist-cars-vehicles-scraper?fpr=939u3w&fp_sid=gh_classifieds) |
| **Craigslist Real Estate, Property & Housing Scraper (FSBO)**<br><sub>[`unitbytes/craigslist-real-estate-property-scraper`](https://apify.com/unitbytes/craigslist-real-estate-property-scraper?fpr=939u3w&fp_sid=gh_classifieds) • [Full Schema](https://unitbytes.com/actors/craigslist-real-estate-property-scraper/) • [Engineering Playbook](https://unitbytes.com/blog/used-car-vin-real-estate-fsbo-scraping-facebook-marketplace-craigslist-offerup-guide/)</sub> | [`examples/run_craigslist_real_estate_property_scraper.py`](examples/run_craigslist_real_estate_property_scraper.py) | [`n8n/craigslist-real-estate-property-scraper-n8n-workflow.json`](n8n/craigslist-real-estate-property-scraper-n8n-workflow.json) | [`JSON`](samples/craigslist-real-estate-property-scraper-sample.json) · [`CSV`](samples/craigslist-real-estate-property-scraper-sample.csv) | [⚡ **Run on Apify**](https://apify.com/unitbytes/craigslist-real-estate-property-scraper?fpr=939u3w&fp_sid=gh_classifieds) |
| **Craigslist Jobs, Gigs & Services Scraper: Pay & Remote**<br><sub>[`unitbytes/craigslist-jobs-gigs-services-scraper`](https://apify.com/unitbytes/craigslist-jobs-gigs-services-scraper?fpr=939u3w&fp_sid=gh_classifieds) • [Full Schema](https://unitbytes.com/actors/craigslist-jobs-gigs-services-scraper/) • [Engineering Playbook](https://unitbytes.com/blog/local-classifieds-arbitrage-facebook-marketplace-craigslist-offerup-guide/)</sub> | [`examples/run_craigslist_jobs_gigs_services_scraper.py`](examples/run_craigslist_jobs_gigs_services_scraper.py) | [`n8n/craigslist-jobs-gigs-services-scraper-n8n-workflow.json`](n8n/craigslist-jobs-gigs-services-scraper-n8n-workflow.json) | [`JSON`](samples/craigslist-jobs-gigs-services-scraper-sample.json) · [`CSV`](samples/craigslist-jobs-gigs-services-scraper-sample.csv) | [⚡ **Run on Apify**](https://apify.com/unitbytes/craigslist-jobs-gigs-services-scraper?fpr=939u3w&fp_sid=gh_classifieds) |
| **OfferUp Scraper: Marketplace Listings, Cars & Deals**<br><sub>[`unitbytes/offerup-scraper`](https://apify.com/unitbytes/offerup-scraper?fpr=939u3w&fp_sid=gh_classifieds) • [Full Schema](https://unitbytes.com/actors/offerup-scraper/) • [Engineering Playbook](https://unitbytes.com/blog/local-classifieds-arbitrage-facebook-marketplace-craigslist-offerup-guide/)</sub> | [`examples/run_offerup_scraper.py`](examples/run_offerup_scraper.py) | [`n8n/offerup-scraper-n8n-workflow.json`](n8n/offerup-scraper-n8n-workflow.json) | [`JSON`](samples/offerup-scraper-sample.json) · [`CSV`](samples/offerup-scraper-sample.csv) | [⚡ **Run on Apify**](https://apify.com/unitbytes/offerup-scraper?fpr=939u3w&fp_sid=gh_classifieds) |
| **OfferUp Used Cars, Vehicles & VIN Scraper: Dealer Specs**<br><sub>[`unitbytes/offerup-vehicles-cars-scraper`](https://apify.com/unitbytes/offerup-vehicles-cars-scraper?fpr=939u3w&fp_sid=gh_classifieds) • [Full Schema](https://unitbytes.com/actors/offerup-vehicles-cars-scraper/) • [Engineering Playbook](https://unitbytes.com/blog/used-car-vin-real-estate-fsbo-scraping-facebook-marketplace-craigslist-offerup-guide/)</sub> | [`examples/run_offerup_vehicles_cars_scraper.py`](examples/run_offerup_vehicles_cars_scraper.py) | [`n8n/offerup-vehicles-cars-scraper-n8n-workflow.json`](n8n/offerup-vehicles-cars-scraper-n8n-workflow.json) | [`JSON`](samples/offerup-vehicles-cars-scraper-sample.json) · [`CSV`](samples/offerup-vehicles-cars-scraper-sample.csv) | [⚡ **Run on Apify**](https://apify.com/unitbytes/offerup-vehicles-cars-scraper?fpr=939u3w&fp_sid=gh_classifieds) |
| **OfferUp Seller Inventory & Auto Dealer Leads Scraper**<br><sub>[`unitbytes/offerup-seller-inventory-scraper`](https://apify.com/unitbytes/offerup-seller-inventory-scraper?fpr=939u3w&fp_sid=gh_classifieds) • [Full Schema](https://unitbytes.com/actors/offerup-seller-inventory-scraper/) • [Engineering Playbook](https://unitbytes.com/blog/used-car-vin-real-estate-fsbo-scraping-facebook-marketplace-craigslist-offerup-guide/)</sub> | [`examples/run_offerup_seller_inventory_scraper.py`](examples/run_offerup_seller_inventory_scraper.py) | [`n8n/offerup-seller-inventory-scraper-n8n-workflow.json`](n8n/offerup-seller-inventory-scraper-n8n-workflow.json) | [`JSON`](samples/offerup-seller-inventory-scraper-sample.json) · [`CSV`](samples/offerup-seller-inventory-scraper-sample.csv) | [⚡ **Run on Apify**](https://apify.com/unitbytes/offerup-seller-inventory-scraper?fpr=939u3w&fp_sid=gh_classifieds) |
| **OfferUp Deal Monitor, Price Drop & Status Tracker**<br><sub>[`unitbytes/offerup-deal-monitor-scraper`](https://apify.com/unitbytes/offerup-deal-monitor-scraper?fpr=939u3w&fp_sid=gh_classifieds) • [Full Schema](https://unitbytes.com/actors/offerup-deal-monitor-scraper/) • [Engineering Playbook](https://unitbytes.com/blog/local-classifieds-arbitrage-facebook-marketplace-craigslist-offerup-guide/)</sub> | [`examples/run_offerup_deal_monitor_scraper.py`](examples/run_offerup_deal_monitor_scraper.py) | [`n8n/offerup-deal-monitor-scraper-n8n-workflow.json`](n8n/offerup-deal-monitor-scraper-n8n-workflow.json) | [`JSON`](samples/offerup-deal-monitor-scraper-sample.json) · [`CSV`](samples/offerup-deal-monitor-scraper-sample.csv) | [⚡ **Run on Apify**](https://apify.com/unitbytes/offerup-deal-monitor-scraper?fpr=939u3w&fp_sid=gh_classifieds) |

- 📓 **1-Click Interactive Google Colab Notebook:** Open [`notebooks/quickstart.ipynb`](notebooks/quickstart.ipynb) directly in your browser via [**Google Colab ↗**](https://colab.research.google.com/github/unitbytes/Craigslist-OfferUp-Scraper-API/blob/main/notebooks/quickstart.ipynb) to inspect sample DataFrames and test live API queries with zero local setup.
- 🤖 **Cursor, Windsurf & Claude Code MCP Ready:** Includes [`.cursor/mcp.json`](.cursor/mcp.json) pre-configured with `https://mcp.apify.com` so AI coding agents can invoke these UnitBytes scrapers natively.
- 💡 **Using n8n?** Explore our official creator profile at **[n8n.io/creators/unitbytes](https://n8n.io/creators/unitbytes/)** or copy all 39 pre-built 9-node scraping workflows (`Ctrl+V`) at **[unitbytes.com/n8n](https://unitbytes.com/n8n/)**.
- 📚 **Engineering Playbooks:** [**Classifieds Arbitrage Playbook**](https://unitbytes.com/blog/local-classifieds-arbitrage-facebook-marketplace-craigslist-offerup-guide/) • [**Used Car VIN & Auto Leads Playbook**](https://unitbytes.com/blog/used-car-vin-real-estate-fsbo-scraping-facebook-marketplace-craigslist-offerup-guide/) — or browse all guides at **[unitbytes.com/blog](https://unitbytes.com/blog/)**.
<!-- UNITBYTES_REPO_KIT_END -->

---

## ⚡ Pre-Configured 1-Click Task Presets

Launch pre-configured extraction templates directly in the Apify Cloud Console with zero parameter setup:

| Task Preset | Target Extraction Use Case | Direct Launch |
| :--- | :--- | :---: |
| **Find Used Cars Under `$5`,000 by Owner on Craigslist** | Extract used cars, trucks, and SUVs priced under `$5`,000 sold directly by private owners across top US metros. Get VIN, mileage, title status, and seller phone numbers. | [⚡ Run Task Preset](https://apify.com/unitbytes/craigslist-scraper/examples/used-cars-under-5000-by-owner?fpr=939u3w&fp_sid=gh_classifieds) |
| **Track Toyota Tacoma & 4x4 Trucks on Craigslist** | Monitor Toyota Tacoma, Tundra, and 4x4 pickup trucks across any metro. Extract model year, trim, mileage, 17-character VIN, and high-resolution photo galleries. | [⚡ Run Task Preset](https://apify.com/unitbytes/craigslist-scraper/examples/craigslist-toyota-tacoma-trucks?fpr=939u3w&fp_sid=gh_classifieds) |
| **Find Honda Civic & Accord Deals on Craigslist** | Discover Honda Civic and Accord listings for car flipping or daily commuting. Extract asking price, clean/salvage title status, transmission, and seller phone numbers. | [⚡ Run Task Preset](https://apify.com/unitbytes/craigslist-scraper/examples/craigslist-honda-civic-deals?fpr=939u3w&fp_sid=gh_classifieds) |
| **Scrape Apartments & Rental Housing on Craigslist** | Extract rental housing listings across major US cities. Collect rent prices, bedroom counts, bathrooms, square footage, neighborhood locations, and full descriptions. | [⚡ Run Task Preset](https://apify.com/unitbytes/craigslist-scraper/examples/craigslist-apartments-rental-housing?fpr=939u3w&fp_sid=gh_classifieds) |
| **Find FSBO Real Estate & Homes for Sale on Craigslist** | Capture For Sale by Owner (FSBO) real estate, land, houses, and commercial property listings with asking prices, seller contact info, and coordinates. | [⚡ Run Task Preset](https://apify.com/unitbytes/craigslist-scraper/examples/craigslist-fsbo-real-estate-homes?fpr=939u3w&fp_sid=gh_classifieds) |
| **Find Apple iPhones & MacBooks on Craigslist for Resale** | Discover discounted Apple MacBooks, iPhones, iPads, and AirPods for e-commerce flipping and resale arbitrage on eBay, Amazon, or Mercari. | [⚡ Run Task Preset](https://apify.com/unitbytes/craigslist-scraper/examples/craigslist-apple-macbook-iphone?fpr=939u3w&fp_sid=gh_classifieds) |
| **Scrape Craigslist Private-Party Cars & Trucks with VIN & Title Status** | Extract owner-direct vehicle listings across US Craigslist metros with 17-digit VIN, odometer reading, clean/salvage title status, and seller contact. | [⚡ Run Task Preset](https://apify.com/unitbytes/craigslist-cars-vehicles-scraper?fpr=939u3w&fp_sid=gh_classifieds) |
| **Extract Craigslist FSBO Real Estate, Apartments & Landlord Rentals** | Scrape Craigslist housing and real estate listings with rent/sale price, bedrooms, square footage, laundry/parking amenities, and map coordinates. | [⚡ Run Task Preset](https://apify.com/unitbytes/craigslist-real-estate-property-scraper?fpr=939u3w&fp_sid=gh_classifieds) |
| **Scrape Craigslist Local Gigs, Skilled Trade Jobs & B2B Service Leads** | Extract local job postings, paid gigs, and small-business service providers on Craigslist for B2B outreach and staffing pipelines. | [⚡ Run Task Preset](https://apify.com/unitbytes/craigslist-jobs-gigs-services-scraper?fpr=939u3w&fp_sid=gh_classifieds) |
| **Scrape Used Cars Under `$5`,000 on OfferUp** | Extract budget cars, trucks, and SUVs under `$5`,000 including mileage, title status, and seller rating. | [⚡ Run Task Preset](https://apify.com/unitbytes/offerup-scraper/examples/cheap-used-cars-under-5000?fpr=939u3w&fp_sid=gh_classifieds) |
| **Find Honda Civic Deals on OfferUp** | Find all Honda Civics listed for sale with VIN, mileage, transmission, and photo gallery. | [⚡ Run Task Preset](https://apify.com/unitbytes/offerup-scraper/examples/honda-civic-deals-finder?fpr=939u3w&fp_sid=gh_classifieds) |
| **Track Toyota Tacoma Trucks on OfferUp** | Extract Toyota Tacoma and 4Runner listings with year, trim, mileage, and seller contact stats. | [⚡ Run Task Preset](https://apify.com/unitbytes/offerup-scraper/examples/toyota-tacoma-trucks-tracker?fpr=939u3w&fp_sid=gh_classifieds) |
| **Extract iPhone & Apple Device Deals** | Extract unlocked iPhones, iPads, and MacBooks with condition notes and seller ratings. | [⚡ Run Task Preset](https://apify.com/unitbytes/offerup-scraper/examples/iphone-apple-deals-extractor?fpr=939u3w&fp_sid=gh_classifieds) |
| **Find MacBook Pro & Laptop Deals on OfferUp** | Monitor MacBook Pro and laptop bargains with price, seller response time, and specs. | [⚡ Run Task Preset](https://apify.com/unitbytes/offerup-scraper/examples/macbook-pro-laptop-deals?fpr=939u3w&fp_sid=gh_classifieds) |
| **Find PS5 & Gaming Console Deals** | Extract PlayStation 5, Xbox Series X, and Nintendo Switch console listings with seller history. | [⚡ Run Task Preset](https://apify.com/unitbytes/offerup-scraper/examples/playstation-ps5-and-gaming-deals?fpr=939u3w&fp_sid=gh_classifieds) |
| **Scrape OfferUp Local Used Cars & Trucks by Zip Code** | Find underpriced local vehicles on OfferUp with make, model, mileage, title status, and TruYou seller verification badges. | [⚡ Run Task Preset](https://apify.com/unitbytes/offerup-vehicles-cars-scraper?fpr=939u3w&fp_sid=gh_classifieds) |
| **Audit OfferUp Seller Profiles, TruYou Status & Active/Sold Inventory** | Extract every active and sold listing from any OfferUp seller profile along with TruYou verification, response rate, and seller rating. | [⚡ Run Task Preset](https://apify.com/unitbytes/offerup-seller-inventory-scraper?fpr=939u3w&fp_sid=gh_classifieds) |
| **Monitor OfferUp for Instant Flipping Deals & Price Drops** | Poll OfferUp search feeds and listing URLs to catch newly listed bargains, price cuts, and sold velocity before local competitors. | [⚡ Run Task Preset](https://apify.com/unitbytes/offerup-deal-monitor-scraper?fpr=939u3w&fp_sid=gh_classifieds) |

---

## 🛠️ Extraction Engines in This Suite

### 🚀 Craigslist Search Scraper: Cars, Housing, Jobs & For Sale (`unitbytes/craigslist-scraper`)

Scrape Craigslist search results across 700+ cities: cars, housing, jobs, electronics, furniture & free stuff. Multi-city clusters, real-time new listing alerts, HD photos & optional contacts. MCP & AI Agent ready.

- **Pricing:** `$0.0005 / item` (Pay-Per-Event — `$0.0005` search result, `$0.0015` detailed listing (volume tiers from `$0.00035`))
- **Cloud Console:** [https://apify.com/unitbytes/craigslist-scraper?fpr=939u3w&fp_sid=gh_classifieds](https://apify.com/unitbytes/craigslist-scraper?fpr=939u3w&fp_sid=gh_classifieds)
- **Full Documentation & Schema:** [https://unitbytes.com/actors/craigslist-scraper/](https://unitbytes.com/actors/craigslist-scraper/)
- **n8n Workflow File:** [`n8n/craigslist-scraper-n8n-workflow.json`](n8n/craigslist-scraper-n8n-workflow.json)
- **Engineering Playbook:** [Automating Local Classifieds Arbitrage: Scraping Facebook Marketplace, Craigslist & OfferUp](https://unitbytes.com/blog/local-classifieds-arbitrage-facebook-marketplace-craigslist-offerup-guide/)

#### Key Capabilities
- **Cross-City Geographic Aggregation:** Scrape single metro areas or aggregate queries across entire states and nationwide regions simultaneously.
- **Automotive Specification Parsing:** Extracts vehicle title status, odometer mileage, VIN, transmission, fuel type, and seller type (dealer vs owner).
- **Rental & Real Estate Breakdown:** Captures rent prices, bedroom count, bathrooms, square footage, housing type, and pet accommodation flags.
- **Clean Uncluttered JSON:** Filters out HTML markup, extracting normalized text, posted timestamps, updated timestamps, and image arrays.

#### ⚙️ Input Parameters (Schema)

| Parameter | Type | Default / Prefill | Description |
| :--- | :---: | :--- | :--- |
| `startUrls` | `array` | — | List of Craigslist search, category, borough/subarea, or direct listing URLs (e.g. https://sfbay.craigslist.org/eby/cta, https://newyork.craigslist.org/mnh/apa, https://toronto.craigslist.org/search/cta). |
| `searchUrl` | `string` | — | Easiest method: Browse to any search, neighborhood, or borough on Craigslist, copy the URL from your browser address bar (e.g. https://sfbay.craigslist.org/eby/cta or https://newyork.craigslist.org/mnh/apa), and paste it here. |
| `searchQuery` | `string` | `macbook pro` | Keyword to search for (e.g. 'toyota', 'macbook', 'apartment'). Leave blank to scrape ALL listings in the selected category or city. |
| `category` | `string` | `sss` | Craigslist category code. |
| `subdomain` | `string` | `losangeles` | Select from top global metropolitan areas across US, Canada, UK, Australia, Europe, and Asia, OR simply paste any Craigslist URL above to target ANY city, town, or neighborhood worldwide. |
| `subarea` | `string` | — | Optional sub-region or borough code (e.g., 'mnh' for Manhattan, 'eby' for East Bay, 'wst' for Westside, 'tor' for City of Toronto). Leave empty to search the entire metropolitan area, or paste a URL above. |
| `regionPreset` | `string` | `none` | Target an entire regional market across multiple cities in a single run. Overrides the single Metro Area dropdown above. |
| `subdomains` | `array` | — | List of specific Craigslist metropolitan subdomains to scrape in a single run (e.g. ['miami', 'orlando', 'tampa'] or ['austin', 'dallas']). |
| `scrapeDetails` | `boolean` | `True` | Enabled by default (`$1.50/1k`). Extracts complete listing details including full description, direct contact info (phones/emails), complete vehicle specs (VIN, mileage, year, title status, transmission), real estate attributes (beds, baths, sqft, laundry, parking, pets), job. |
| `minPrice` | `integer` | — | Minimum listing price in USD. |
| `maxPrice` | `integer` | — | Maximum listing price in USD. |
| `purveyor` | `string` | `all` | Filter by owner or dealer. |
| `hasImage` | `boolean` | `False` | Only return listings that include photos. |
| `postedToday` | `boolean` | `False` | Only return listings published within the last 24 hours. |
| `sort` | `string` | `date` | Sort order for returned listings (Newest first, lowest price, highest price, or relevance). |
| `postal` | `string` | — | Target a specific postal or ZIP code (e.g. '90210', '10001', 'M5V 2T6'). Combine with Search Radius below. |
| `radius` | `integer` | — | Distance radius in miles around the specified Postal / ZIP Code. |
| `condition` | `string` | `all` | Filter listings by item condition (for vehicles, electronics, furniture, for sale). |

#### 📊 Live Dataset Output Previews

**🚗 Craigslist Cars, Trucks & Vehicles Scraper (`unitbytes/craigslist-cars-vehicles-scraper`)**
<p align="center">
  <a href="https://apify.com/unitbytes/craigslist-cars-vehicles-scraper?fpr=939u3w&fp_sid=gh_classifieds" target="_blank">
    <img src="https://raw.githubusercontent.com/unitbytes/Craigslist-OfferUp-Scraper-API/main/assets/craigslist-cars-vehicles-scraper-output-sample.png" alt="Craigslist Cars & Vehicles Scraper Dataset Output" width="100%" />
  </a>
</p>

**🏠 Craigslist Real Estate, Property & Housing Scraper (`unitbytes/craigslist-real-estate-property-scraper`)**
<p align="center">
  <a href="https://apify.com/unitbytes/craigslist-real-estate-property-scraper?fpr=939u3w&fp_sid=gh_classifieds" target="_blank">
    <img src="https://raw.githubusercontent.com/unitbytes/Craigslist-OfferUp-Scraper-API/main/assets/craigslist-real-estate-property-scraper-output-sample.png" alt="Craigslist Real Estate & Housing Scraper Dataset Output" width="100%" />
  </a>
</p>

**💼 Craigslist Jobs, Gigs & Services Scraper (`unitbytes/craigslist-jobs-gigs-services-scraper`)**
<p align="center">
  <a href="https://apify.com/unitbytes/craigslist-jobs-gigs-services-scraper?fpr=939u3w&fp_sid=gh_classifieds" target="_blank">
    <img src="https://raw.githubusercontent.com/unitbytes/Craigslist-OfferUp-Scraper-API/main/assets/craigslist-jobs-gigs-services-scraper-output-sample.png" alt="Craigslist Jobs, Gigs & Services Scraper Dataset Output" width="100%" />
  </a>
</p>

#### Python SDK Quickstart (`examples/run_craigslist_scraper.py`)
```python
from apify_client import ApifyClient

APIFY_TOKEN = os.getenv("APIFY_API_TOKEN", "YOUR_APIFY_API_TOKEN")
if not APIFY_TOKEN or APIFY_TOKEN.startswith("YOUR_"):
    raise SystemExit("Please set your Apify API token: export APIFY_API_TOKEN='apify_api_...'")

client = ApifyClient(APIFY_TOKEN)

run_input = {
    "searchQuery": "macbook pro",
    "category": "sss",
    "subdomain": "losangeles",
    "scrapeDetails": True,
    "hasImage": False,
    "postedToday": False
}

run = client.actor("unitbytes/craigslist-scraper").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("title"), item.get("vehicleTitleStatus"), item.get("price"))
```

#### Sample Output Schema (`samples/craigslist-scraper-sample.json`)
```json
{
  "listingId": "7900000001",
  "url": "https://www.craigslist.org/view/d/norwalk-2013-toyota-tacoma-trd-off-road/7900000001",
  "listingStatus": "active",
  "title": "2013 Toyota Tacoma TRD Off Road 4x4",
  "price": 14500.0,
  "currency": "USD",
  "subarea": "sfv",
  "condition": "excellent",
  "description": "Clean 2013 Toyota Tacoma TRD Off-Road. 104,500 miles, automatic transmission, clean title in hand.",
  "postDate": "2026-10-22T07:07:19-0700",
  "city": "Norwalk",
  "state": "CA",
  "zipCode": "90652",
  "latitude": 33.9022,
  "longitude": -118.0817,
  "isDealer": false,
  "isVehicle": true,
  "vehicleYear": 2013,
  "vehicleMake": "toyota tacoma trd off-road",
  "vehicleMiles": 104500,
  "vehicleVin": "5TFUX4EN4DX012345",
  "vehicleTransmission": "automatic",
  "vehicleFuelType": "gas",
  "vehicleTitleStatus": "clean",
  "thumbnailUrl": "https://images.craigslist.org/00B0B_1ZBm7qXYZ_600x450.jpg",
  "imageUrls": [
    "https://images.craigslist.org/00B0B_1ZBm7qXYZ_1200x900.jpg"
  ]
}
```

#### Frequently Asked Questions
**Q: Can I scrape Craigslist across multiple cities in a single run?**
Yes. Use built-in regional corridor presets (socal, norcal_bayarea, texas, florida, tri_state_ny, pacific_northwest, midwest_chicago) or pass any list of Craigslist city subdomains.

**Q: Does it extract phone numbers and email addresses from descriptions?**
Yes. When scrapeDetails is enabled, the Actor parses un-obfuscated phone numbers and email addresses directly from listing descriptions for outbound lead generation.

**Q: What Craigslist categories are supported?**
Supports all major verticals including Cars & Trucks (cta), Apartments/Housing (apa), Real Estate for Sale (rea), All For Sale (sss), Jobs (jjj), Gigs (ggg), and Services (bbb).

**Q: Can I paste a filtered search URL directly from my browser?**
Yes. Copy any Craigslist search URL from your browser and paste it into searchUrl or startUrls; the Actor automatically parses the metro subdomain, category, and filters.

---

### 🚀 Craigslist Cars & Vehicles Scraper: By Owner, VIN & Miles (`unitbytes/craigslist-cars-vehicles-scraper`)

Scrape Craigslist cars, trucks, motorcycles, RVs, boats, heavy equipment & auto parts by owner or dealer across 700+ cities. Filter by make/model, year, odometer mileage, clean title & VIN. MCP & AI Agent ready.

- **Pricing:** `$0.0005 / item` (Pay-Per-Event — `$0.0005` search result, `$0.0015` detailed listing (volume tiers from `$0.00035`))
- **Cloud Console:** [https://apify.com/unitbytes/craigslist-cars-vehicles-scraper?fpr=939u3w&fp_sid=gh_classifieds](https://apify.com/unitbytes/craigslist-cars-vehicles-scraper?fpr=939u3w&fp_sid=gh_classifieds)
- **Full Documentation & Schema:** [https://unitbytes.com/actors/craigslist-cars-vehicles-scraper/](https://unitbytes.com/actors/craigslist-cars-vehicles-scraper/)
- **n8n Workflow File:** [`n8n/craigslist-cars-vehicles-scraper-n8n-workflow.json`](n8n/craigslist-cars-vehicles-scraper-n8n-workflow.json)
- **Engineering Playbook:** [Used Car VIN, Auto Dealer & FSBO Real Estate Scraping Guide in 2026 (FB Marketplace, Craigslist & OfferUp)](https://unitbytes.com/blog/used-car-vin-real-estate-fsbo-scraping-facebook-marketplace-craigslist-offerup-guide/)

#### Key Capabilities
- **17-Character VIN & Structured Automotive Specs:** Extracts vehicle VINs, model year, odometer mileage, title status (clean, salvage, rebuilt), transmission, fuel type, drive train, cylinders, paint color, and body type.
- **Private Owner vs. Dealership Filtering:** Filter upstream by private-party FSBO owners (purveyor=owner) for wholesale vehicle acquisition or dealerships (purveyor=dealer) for competitive lot inventory analysis.
- **Direct Seller Contact & Multi-Metro Coverage:** Parses un-obfuscated phone numbers and email addresses from listing bodies across single Craigslist subdomains or entire regional corridors (socal, texas, florida, tri_state_ny).
- **Exact GPS Coordinates & High-Res Photo Galleries:** Captures latitude/longitude coordinates, neighborhood tags, listing timestamps, and full-resolution image arrays at `$0.50` per 1,000 vehicles.

#### ⚙️ Input Parameters (Schema)

| Parameter | Type | Default / Prefill | Description |
| :--- | :---: | :--- | :--- |
| `startUrls` | `array` | — | List of Craigslist vehicle search, borough/subarea, or direct listing URLs (e.g. https://losangeles.craigslist.org/search/cto, https://sfbay.craigslist.org/eby/cta, https://dallas.craigslist.org/search/rva). |
| `searchUrl` | `string` | — | Easiest method: Browse to any cars, trucks, motorcycles, RVs, or boats search on Craigslist, copy the URL from your browser address bar (e.g. https://losangeles.craigslist.org/search/cto?auto_make_model=tacoma or https://sfbay.craigslist.org/eby/cta), and paste it here. |
| `searchQuery` | `string` | `toyota tacoma` | Keyword to search for in listing titles and descriptions (e.g. 'toyota tacoma', 'honda civic', '4x4', 'cummins', 'sprinter'). Leave blank to scrape ALL vehicles in the selected category or city. |
| `category` | `string` | `cto` | Craigslist category code. |
| `subdomain` | `string` | `losangeles` | Select from top global metropolitan areas across US, Canada, UK, Australia, Europe, and Asia, OR simply paste any Craigslist URL above to target ANY city, town, or neighborhood worldwide. |
| `subarea` | `string` | — | Optional sub-region or borough code (e.g., 'mnh' for Manhattan, 'eby' for East Bay, 'wst' for Westside, 'tor' for City of Toronto). Leave empty to search the entire metropolitan area, or paste a URL above. |
| `regionPreset` | `string` | `none` | Target an entire regional market across multiple cities in a single run. Overrides the single Metro Area dropdown above. |
| `subdomains` | `array` | — | List of specific Craigslist metropolitan subdomains to scrape in a single run (e.g. ['miami', 'orlando', 'tampa'] or ['austin', 'dallas']). |
| `scrapeDetails` | `boolean` | `True` | Enabled by default (`$1.50/1k`). Extracts complete vehicle details including 17-character VIN, clean/salvage title status, transmission, fuel type, body type, drivetrain, cylinders, paint color, condition, full description, seller phones/emails, and up to 24 HD photos (1200x900). |
| `minPrice` | `integer` | — | Minimum listing price in USD. |
| `maxPrice` | `integer` | — | Maximum listing price in USD. |
| `purveyor` | `string` | `all` | Filter by owner or dealer. |
| `hasImage` | `boolean` | `False` | Only return listings that include photos. |
| `postedToday` | `boolean` | `False` | Only return listings published within the last 24 hours. |
| `sort` | `string` | `date` | Sort order for returned listings (Newest first, lowest price, highest price, or relevance). |
| `postal` | `string` | — | Target a specific postal or ZIP code (e.g. '90210', '10001', 'M5V 2T6'). Combine with Search Radius below. |
| `radius` | `integer` | — | Distance radius in miles around the specified Postal / ZIP Code. |
| `condition` | `string` | `all` | Filter listings by item condition (for vehicles, electronics, furniture, for sale). |

#### Python SDK Quickstart (`examples/run_craigslist_cars_vehicles_scraper.py`)
```python
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
```

#### Sample Output Schema (`samples/craigslist-cars-vehicles-scraper-sample.json`)
```json
{
  "listingId": "7900000001",
  "url": "https://www.craigslist.org/view/d/norwalk-2013-toyota-tacoma-trd-off-road/7900000001",
  "listingStatus": "active",
  "title": "2013 Toyota Tacoma TRD Off Road 4x4",
  "price": 14500.0,
  "currency": "USD",
  "subarea": "sfv",
  "condition": "excellent",
  "description": "Clean 2013 Toyota Tacoma TRD Off-Road. 104,500 miles, automatic transmission, clean title in hand.",
  "postDate": "2026-10-22T07:07:19-0700",
  "city": "Norwalk",
  "state": "CA",
  "zipCode": "90652",
  "latitude": 33.9022,
  "longitude": -118.0817,
  "isDealer": false,
  "isVehicle": true,
  "vehicleYear": 2013,
  "vehicleMake": "toyota tacoma trd off-road",
  "vehicleMiles": 104500,
  "vehicleVin": "5TFUX4EN4DX012345",
  "vehicleTransmission": "automatic",
  "vehicleFuelType": "gas",
  "vehicleTitleStatus": "clean",
  "thumbnailUrl": "https://images.craigslist.org/00B0B_1ZBm7qXYZ_600x450.jpg",
  "imageUrls": [
    "https://images.craigslist.org/00B0B_1ZBm7qXYZ_1200x900.jpg"
  ]
}
```

#### Frequently Asked Questions
**Q: Does this scraper extract 17-character VINs and odometer mileage?**
Yes. Every vehicle record includes parsed VIN, model year, make/model, odometer miles, title status (clean, salvage, rebuilt), transmission, fuel type, drive train, and cylinders.

**Q: Can I filter for private-party owners only (FSBO cars)?**
Yes. Set purveyor to 'owner' to exclude commercial dealerships and source private-party vehicles directly from owners.

**Q: Can I filter by minimum/maximum price, model year, and mileage?**
Yes. Configure minPrice, maxPrice, minYear, maxYear, minMiles, maxMiles, autoTransmission, and cleanTitleOnly across one or multiple Craigslist cities.

**Q: Can I paste a browser search URL directly?**
Yes. Paste any Craigslist cars/trucks search URL into searchUrl or startUrls and the Actor automatically extracts the city subdomain, query, and automotive filters.

---

### 🚀 Craigslist Real Estate, Property & Housing Scraper (FSBO) (`unitbytes/craigslist-real-estate-property-scraper`)

Scrape Craigslist real estate for sale (FSBO), rental properties, apartments, houses, rooms, sublets & commercial property across 700+ cities. Filter by beds, baths, sqft, pets & parking. MCP & AI Agent ready.

- **Pricing:** `$0.0005 / item` (Pay-Per-Event — `$0.0005` search result, `$0.0015` detailed listing (volume tiers from `$0.00035`))
- **Cloud Console:** [https://apify.com/unitbytes/craigslist-real-estate-property-scraper?fpr=939u3w&fp_sid=gh_classifieds](https://apify.com/unitbytes/craigslist-real-estate-property-scraper?fpr=939u3w&fp_sid=gh_classifieds)
- **Full Documentation & Schema:** [https://unitbytes.com/actors/craigslist-real-estate-property-scraper/](https://unitbytes.com/actors/craigslist-real-estate-property-scraper/)
- **n8n Workflow File:** [`n8n/craigslist-real-estate-property-scraper-n8n-workflow.json`](n8n/craigslist-real-estate-property-scraper-n8n-workflow.json)
- **Engineering Playbook:** [Used Car VIN, Auto Dealer & FSBO Real Estate Scraping Guide in 2026 (FB Marketplace, Craigslist & OfferUp)](https://unitbytes.com/blog/used-car-vin-real-estate-fsbo-scraping-facebook-marketplace-craigslist-offerup-guide/)

#### Key Capabilities
- **FSBO Real Estate & Apartment Rental Extraction:** Scrapes apartments/housing for rent (apa), real estate for sale by owner or broker (rea/reo), sublets (sub), rooms/shares (roo), and commercial office space (off).
- **Bedrooms, Bathrooms, SqFt & Amenity Attributes:** Extracts structured bedrooms, bathrooms, square footage, housing type (apartment, house, condo, townhouse), laundry options, parking type, and pet policies (cats_ok, dogs_ok).
- **Direct Landlord & Seller Contact Parsing:** Extracts phone numbers and email addresses directly from property descriptions alongside exact GPS coordinates and neighborhood boundaries.
- **Multi-City Regional Presets & Custom Search URLs:** Scan dozens of Craigslist metro markets in a single run using regional presets or paste any filtered browser search URL directly into startUrls.

#### ⚙️ Input Parameters (Schema)

| Parameter | Type | Default / Prefill | Description |
| :--- | :---: | :--- | :--- |
| `startUrls` | `array` | — | List of Craigslist housing, apartment, or real estate search, borough/subarea, or direct listing URLs (e.g. https://newyork.craigslist.org/mnh/apa, https://sfbay.craigslist.org/sfc/apa, https://miami.craigslist.org/search/reo). |
| `searchUrl` | `string` | — | Easiest method: Browse to any apartments, rentals, or real estate search on Craigslist, copy the URL from your browser address bar (e.g. https://newyork.craigslist.org/mnh/apa or https://losangeles.craigslist.org/wst/rea), and paste it here. |
| `searchQuery` | `string` | `2br apartment` | Keyword to search for in property listings (e.g. 'no broker fee', 'loft', 'pool', 'backyard', 'duplex', 'penthouse'). Leave blank to scrape ALL properties in the selected category or city. |
| `category` | `string` | `apa` | Craigslist category code. |
| `subdomain` | `string` | `losangeles` | Select from top global metropolitan areas across US, Canada, UK, Australia, Europe, and Asia, OR simply paste any Craigslist URL above to target ANY city, town, or neighborhood worldwide. |
| `subarea` | `string` | — | Optional sub-region or borough code (e.g., 'mnh' for Manhattan, 'eby' for East Bay, 'wst' for Westside, 'tor' for City of Toronto). Leave empty to search the entire metropolitan area, or paste a URL above. |
| `regionPreset` | `string` | `none` | Target an entire regional market across multiple cities in a single run. Overrides the single Metro Area dropdown above. |
| `subdomains` | `array` | — | List of specific Craigslist metropolitan subdomains to scrape in a single run (e.g. ['miami', 'orlando', 'tampa'] or ['austin', 'dallas']). |
| `scrapeDetails` | `boolean` | `True` | Enabled by default (`$1.50/1k`). Extracts complete property details including bedrooms, bathrooms, square footage (sqft), property type, laundry, parking, pet policy (Cats/Dogs OK), move-in availability date, street address, ZIP code, landlord/broker status, full description. |
| `minPrice` | `integer` | — | Minimum monthly rent or property sale price. |
| `maxPrice` | `integer` | — | Maximum monthly rent or property sale price. |
| `purveyor` | `string` | `all` | Filter by private owner/landlord (FSBO / no fee) or real estate broker/property manager. |
| `hasImage` | `boolean` | `False` | Only return listings that include photos. |
| `postedToday` | `boolean` | `False` | Only return listings published within the last 24 hours. |
| `sort` | `string` | `date` | Sort order for returned listings (Newest first, lowest price, highest price, or relevance). |
| `postal` | `string` | — | Target a specific postal or ZIP code (e.g. '90210', '10001', 'M5V 2T6'). Combine with Search Radius below. |
| `radius` | `integer` | — | Distance radius in miles around the specified Postal / ZIP Code. |
| `minBedrooms` | `integer` | — | Minimum number of bedrooms (0 for Studio, 1, 2, 3+). |

#### Python SDK Quickstart (`examples/run_craigslist_real_estate_property_scraper.py`)
```python
from apify_client import ApifyClient

APIFY_TOKEN = os.getenv("APIFY_API_TOKEN", "YOUR_APIFY_API_TOKEN")
if not APIFY_TOKEN or APIFY_TOKEN.startswith("YOUR_"):
    raise SystemExit("Please set your Apify API token: export APIFY_API_TOKEN='apify_api_...'")

client = ApifyClient(APIFY_TOKEN)

run_input = {
    "searchQuery": "2br apartment",
    "category": "apa",
    "subdomain": "losangeles",
    "scrapeDetails": True,
    "hasImage": False,
    "postedToday": False
}

run = client.actor("unitbytes/craigslist-real-estate-property-scraper").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("title"), item.get("price"), item.get("postDate"))
```

#### Sample Output Schema (`samples/craigslist-real-estate-property-scraper-sample.json`)
```json
{
  "listingId": "7900000003",
  "url": "https://www.craigslist.org/view/d/white-plains-spacious-3br-apartment/7900000003",
  "listingStatus": "active",
  "title": "Spacious Top-Floor 3BR Apartment — Garage, Laundry, Pet Friendly",
  "price": 3650.0,
  "currency": "USD",
  "subarea": "wch",
  "description": "Bright 3-bedroom, 1.5-bath apartment with attached garage parking and laundry in building. Dogs and cats OK.",
  "postDate": "2026-10-22T10:01:59-0400",
  "city": "White Plains",
  "state": "NY",
  "zipCode": "10601",
  "latitude": 41.034,
  "longitude": -73.7629,
  "isDealer": false,
  "bedrooms": 3,
  "bathrooms": 1.5,
  "sqft": 1300,
  "housingType": "apartment",
  "laundry": "laundry in bldg",
  "parking": "attached garage",
  "thumbnailUrl": "https://images.craigslist.org/00B0B_1ZBm7qXYZ_600x450.jpg",
  "imageUrls": [
    "https://images.craigslist.org/00B0B_1ZBm7qXYZ_1200x900.jpg"
  ]
}
```

#### Frequently Asked Questions
**Q: Which Craigslist housing and real estate categories are supported?**
Supports Apartments & Housing for Rent (apa), Real Estate for Sale (rea), By-Owner FSBO Real Estate (reo), Rooms & Shares (roo), Sublets (sub), Vacation Rentals (vac), and Commercial Office (off).

**Q: What structured property attributes are extracted?**
Extracts price, bedrooms, bathrooms, square_feet, housing_type, laundry, parking, cats_ok, dogs_ok, wheelchair_accessible, no_smoking, furnished, GPS coordinates, and parsed phone/email contacts.

**Q: Can I filter by bedrooms, bathrooms, square footage, and pet policy?**
Yes. Set minPrice, maxPrice, minBedrooms, minBathrooms, minSqft, maxSqft, catsOk, and dogsOk across any city or regional preset.

**Q: Can I paste a custom Craigslist housing search URL?**
Yes. Copy any filtered Craigslist housing or real estate URL from your browser into searchUrl or startUrls for instant extraction at `$0.50` per 1,000 properties.

---

### 🚀 Craigslist Jobs, Gigs & Services Scraper: Pay & Remote (`unitbytes/craigslist-jobs-gigs-services-scraper`)

Scrape Craigslist jobs, local gigs, resumes & services across 700+ cities and 35+ categories. Filter by full-time, part-time, contract, remote/telecommute & paid gigs with compensation details. MCP & AI Agent ready.

- **Pricing:** `$0.0005 / item` (Pay-Per-Event — `$0.0005` search result, `$0.0015` detailed listing (volume tiers from `$0.00035`))
- **Cloud Console:** [https://apify.com/unitbytes/craigslist-jobs-gigs-services-scraper?fpr=939u3w&fp_sid=gh_classifieds](https://apify.com/unitbytes/craigslist-jobs-gigs-services-scraper?fpr=939u3w&fp_sid=gh_classifieds)
- **Full Documentation & Schema:** [https://unitbytes.com/actors/craigslist-jobs-gigs-services-scraper/](https://unitbytes.com/actors/craigslist-jobs-gigs-services-scraper/)
- **n8n Workflow File:** [`n8n/craigslist-jobs-gigs-services-scraper-n8n-workflow.json`](n8n/craigslist-jobs-gigs-services-scraper-n8n-workflow.json)
- **Engineering Playbook:** [Automating Local Classifieds Arbitrage: Scraping Facebook Marketplace, Craigslist & OfferUp](https://unitbytes.com/blog/local-classifieds-arbitrage-facebook-marketplace-craigslist-offerup-guide/)

#### Key Capabilities
- **Direct Contact Extraction for B2B Lead Generation:** Automatically parses phone numbers and email addresses from job postings, gig listings, and local contractor advertisements for outbound recruiting and sales.
- **Jobs, Gigs & Local Contractor Categories:** Supports all Craigslist employment and service verticals including All Jobs (jjj), Tech/Software, Healthcare, Skilled Trades, Computer/Creative Gigs (ggg), and Local Services (bbb).
- **Multi-Metro Regional Corridor Scanning:** Run a single job across entire economic corridors using built-in presets (socal, norcal_bayarea, florida, texas, tri_state_ny, pacific_northwest, midwest_chicago) or custom city lists.
- **Compensation, Employment Type & Telecommute Flags:** Extracts compensation text, employment type (full-time, part-time, contract), remote/telecommute badges, and company names in flat CSV/JSON.

#### ⚙️ Input Parameters (Schema)

| Parameter | Type | Default / Prefill | Description |
| :--- | :---: | :--- | :--- |
| `startUrls` | `array` | — | List of Craigslist jobs, gigs, resumes, or local services search, borough/subarea, or direct listing URLs (e.g. https://sfbay.craigslist.org/search/sof, https://losangeles.craigslist.org/search/jjj, https://newyork.craigslist.org/mnh/ggg). |
| `searchUrl` | `string` | — | Easiest method: Browse to any jobs, gigs, resumes, or services search on Craigslist, copy the URL from your browser address bar (e.g. https://sfbay.craigslist.org/search/sof?is_telecommuting=1 or https://newyork.craigslist.org/mnh/jjj), and paste it here. |
| `searchQuery` | `string` | `software engineer` | Keyword to search for in job, gig, or service postings (e.g. 'software engineer', 'CDL driver', 'bartender', 'bookkeeper', 'HVAC'). Leave blank to scrape ALL postings in the selected category or city. |
| `category` | `string` | `jjj` | Craigslist category code. |
| `subdomain` | `string` | `losangeles` | Select from top global metropolitan areas across US, Canada, UK, Australia, Europe, and Asia, OR simply paste any Craigslist URL above to target ANY city, town, or neighborhood worldwide. |
| `subarea` | `string` | — | Optional sub-region or borough code (e.g., 'mnh' for Manhattan, 'eby' for East Bay, 'wst' for Westside, 'tor' for City of Toronto). Leave empty to search the entire metropolitan area, or paste a URL above. |
| `regionPreset` | `string` | `none` | Target an entire regional market across multiple cities in a single run. Overrides the single Metro Area dropdown above. |
| `subdomains` | `array` | — | List of specific Craigslist metropolitan subdomains to scrape in a single run (e.g. ['miami', 'orlando', 'tampa'] or ['austin', 'dallas']). |
| `scrapeDetails` | `boolean` | `True` | Enabled by default (`$1.50/1k`). Extracts complete posting details including pay/compensation text, employment type (full-time, part-time, contract), role/job title, hiring company name, remote/telecommute status, full job description, direct contact phone numbers & emails, ZIP. |
| `hasImage` | `boolean` | `False` | Only return postings that include photos or company flyers. |
| `postedToday` | `boolean` | `False` | Only return postings published within the last 24 hours. |
| `sort` | `string` | `date` | Sort order for returned postings (Newest first or Relevance). |
| `postal` | `string` | — | Target a specific postal or ZIP code (e.g. '90210', '10001', 'M5V 2T6'). Combine with Search Radius below. |
| `radius` | `integer` | — | Distance radius in miles around the specified Postal / ZIP Code. |
| `employmentType` | `string` | `all` | Filter job postings by full-time, part-time, or contract status. |
| `isTelecommuting` | `boolean` | `False` | Only return remote or telecommute-friendly job listings. |
| `isInternship` | `boolean` | `False` | Only return internship positions. |
| `isNonProfit` | `boolean` | `False` | Only return jobs at non-profit organizations. |

#### Python SDK Quickstart (`examples/run_craigslist_jobs_gigs_services_scraper.py`)
```python
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
```

#### Sample Output Schema (`samples/craigslist-jobs-gigs-services-scraper-sample.json`)
```json
{
  "listingId": "7900000002",
  "url": "https://www.craigslist.org/view/d/san-mateo-senior-site-reliability/c5edHqKDrLu5zQsnY8fPbo",
  "listingStatus": "active",
  "title": "Senior Site Reliability Engineer",
  "currency": "USD",
  "subarea": "pen",
  "description": "We are seeking a Senior Site Reliability Engineer to scale our cloud infrastructure. Full-time role with competitive salary, equity, and comprehensive benefits.",
  "postDate": "2026-10-21T13:54:31-0700",
  "city": "San Mateo",
  "state": "CA",
  "latitude": 37.5538,
  "longitude": -122.27,
  "isDealer": false,
  "compensation": "$130,000 to $200,000 + equity + benefits",
  "employmentType": "full-time",
  "jobTitle": "Software Engineering Manager",
  "companyName": "Acme Tech Corp",
  "isTelecommuting": true
}
```

#### Frequently Asked Questions
**Q: How do agencies and recruiters use this Actor for lead generation?**
By scraping Craigslist Jobs (jjj), Gigs (ggg), and Local Services (bbb) with contact extraction enabled, teams capture direct phone numbers, emails, compensation details, and hiring managers.

**Q: Can I scan an entire state or multi-city corridor in one run?**
Yes. Select a regional preset like texas, florida, socal, norcal_bayarea, or tri_state_ny to aggregate job and service leads across every metro in that region.

**Q: Does it extract compensation, employment type, and remote work flags?**
Yes. Every record includes parsed compensation strings, employment type (full-time, part-time, contract, internship), telecommute/remote flags, and GPS coordinates.

**Q: Can I paste a browser search URL directly?**
Yes. Paste any Craigslist jobs, gigs, or services URL into searchUrl or startUrls and the Actor handles pagination and detail extraction automatically.

---

### 🚀 OfferUp Scraper: Marketplace Listings, Cars & Deals (`unitbytes/offerup-scraper`)

<p align="center">
  <a href="https://apify.com/unitbytes/offerup-scraper?fpr=939u3w&fp_sid=gh_classifieds" target="_blank">
    <img src="https://raw.githubusercontent.com/unitbytes/.github/main/assets/banners/unitbytes-offerup-marketplace-local-deals-scraper-banner.jpg" alt="OfferUp Scraper: Marketplace Listings, Cars & Deals" width="100%" />
  </a>
</p>

Fast OfferUp Scraper with no login required. Extract local marketplace listings, used cars & VINs, seller inventories, HD photos, and price drops across any US ZIP code. From `$0.80/1k`.

- **Pricing:** `$0.0008 / item` (Pay-Per-Event — `$0.0008` listing discovery, `$0.0025` deep detail enrichment (volume tiers from `$0.0006`))
- **Cloud Console:** [https://apify.com/unitbytes/offerup-scraper?fpr=939u3w&fp_sid=gh_classifieds](https://apify.com/unitbytes/offerup-scraper?fpr=939u3w&fp_sid=gh_classifieds)
- **Full Documentation & Schema:** [https://unitbytes.com/actors/offerup-scraper/](https://unitbytes.com/actors/offerup-scraper/)
- **n8n Workflow File:** [`n8n/offerup-scraper-n8n-workflow.json`](n8n/offerup-scraper-n8n-workflow.json)
- **Engineering Playbook:** [Automating Local Classifieds Arbitrage: Scraping Facebook Marketplace, Craigslist & OfferUp](https://unitbytes.com/blog/local-classifieds-arbitrage-facebook-marketplace-craigslist-offerup-guide/)

#### Key Capabilities
- **Precise Postal Zip Code Targeting:** Target any US zip code with radius filtering (5, 10, 20, 50 miles) to extract hyper-local classifieds.
- **Seller Reputation & TruYou Badges:** Extract seller star ratings, total sales count, account join date, and OfferUp TruYou ID verification status.
- **Shipping & Local Pickup Segmentation:** Distinguish between nationwide shipped items and local cash-and-carry listings for precise deal finding.
- **Condition & Negotiable Flags:** Captures item condition (New, Open Box, Used, For Parts) and whether the seller is open to price offers.

#### ⚙️ Input Parameters (Schema)

| Parameter | Type | Default / Prefill | Description |
| :--- | :---: | :--- | :--- |
| `searchQuery` | `string` | `iphone 15` | Keyword to search for (e.g., 'honda civic', 'iphone 15', 'couch'). Leave blank to browse ALL items in the category or location. |
| `zipCode` *(Required)* | `string` | `90001` | 5-digit US ZIP code to center the search (e.g. 90001 for Los Angeles, 10001 for New York, 33101 for Miami). Note: City names are not supported by OfferUp's API. |
| `radius` | `integer` | `50` | Search distance radius around the ZIP code (5 to 500 miles). |
| `categoryId` | `string` | `all` | Filter by OfferUp category. |
| `conditionFilter` | `string` | `all` | Server-side filter by OfferUp item condition. |
| `deliveryMethod` | `string` | `all` | Filter by Local Pickup ('local'), Nationwide Shipping ('shipping'), or All ('all'). |
| `sortBy` | `string` | `-posted` | Sorting order for search results. |
| `minPrice` | `integer` | — | Minimum item price in USD. |
| `maxPrice` | `integer` | — | Maximum item price in USD. |
| `make` | `string` | — | Vehicle manufacturer (e.g., 'Honda', 'Toyota', 'Ford', 'BMW'). |
| `model` | `string` | — | Vehicle model (e.g., 'Civic', 'Camry', 'F-150', 'Tacoma'). |
| `minYear` | `integer` | — | Server-side filter for minimum model year (e.g. 2018). |
| `maxYear` | `integer` | — | Server-side filter for maximum model year (e.g. 2026). |
| `maxMiles` | `integer` | — | Server-side filter for maximum odometer mileage (OfferUp uses 25,000-mile increments: 25000, 50000, 75000, 100000, 125000, 150000, 175000, 200000). |
| `sellerIds` | `array` | — | OfferUp Seller IDs (e.g. '100098765') or profile URLs ('https://offerup.com/p/100098765') to extract complete dealer/seller profile + active inventory. |
| `maxItems` | `integer` | `20` | Maximum number of listings to scrape. Set to 10-20 for instant trial results. |
| `scrapeDetails` | `boolean` | `True` | When enabled, enriches listings with high-res photos, vehicle VIN/specs, Carfax/history issues, seller phone/website/address, and descriptions (`$2.50/1k`). When disabled, extracts fast search summaries at only `$0.80/1k`. |
| `maxConcurrency` | `integer` | `5` | Number of concurrent item detail requests. |

#### Python SDK Quickstart (`examples/run_offerup_scraper.py`)
```python
from apify_client import ApifyClient

APIFY_TOKEN = os.getenv("APIFY_API_TOKEN", "YOUR_APIFY_API_TOKEN")
if not APIFY_TOKEN or APIFY_TOKEN.startswith("YOUR_"):
    raise SystemExit("Please set your Apify API token: export APIFY_API_TOKEN='apify_api_...'")

client = ApifyClient(APIFY_TOKEN)

run_input = {
    "searchQuery": "iphone 15",
    "zipCode": "90001",
    "radius": 50,
    "categoryId": "all",
    "conditionFilter": "all",
    "deliveryMethod": "all"
}

run = client.actor("unitbytes/offerup-scraper").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("title"), item.get("price"), item.get("locationName"), item.get("url"))
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
  "sellerName": "Seller_A",
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
**Q: Do I need an OfferUp account or mobile app login?**
No. The OfferUp Scraper runs 100% cookieless in the cloud with built-in US residential proxy routing.

**Q: Can I search OfferUp by ZIP code, GPS coordinates, or category?**
Yes. Search any US ZIP code or latitude/longitude radius by keyword or category, with server-side filters for condition, price range, and delivery method (local pickup vs. shipping).

**Q: What is the difference between Fast Mode and Full Details Mode?**
Fast Mode (`$0.80/1K` items) extracts search feed cards, prices, cover photos, and locations in seconds. Full Details Mode (scrapeDetails: true) adds full descriptions, multi-photo galleries, VINs, and seller TruYou badges.

**Q: Can I also scrape seller profiles and check SOLD status?**
Yes. Paste any OfferUp /p/<userId> profile link to extract a seller's catalog, or pass /item/detail/<id> URLs to verify live vs. SOLD status.

---

### 🚀 OfferUp Used Cars, Vehicles & VIN Scraper: Dealer Specs (`unitbytes/offerup-vehicles-cars-scraper`)

Extract OfferUp used cars, trucks, VIN numbers, mileage, title status, MPG, history report issues, and auto dealer phone numbers by make, model, year & ZIP code. From `$0.80/1k`.

- **Pricing:** `$0.0008 / item` (Pay-Per-Event — `$0.0008` listing discovery, `$0.0025` deep detail enrichment (volume tiers from `$0.0006`))
- **Cloud Console:** [https://apify.com/unitbytes/offerup-vehicles-cars-scraper?fpr=939u3w&fp_sid=gh_classifieds](https://apify.com/unitbytes/offerup-vehicles-cars-scraper?fpr=939u3w&fp_sid=gh_classifieds)
- **Full Documentation & Schema:** [https://unitbytes.com/actors/offerup-vehicles-cars-scraper/](https://unitbytes.com/actors/offerup-vehicles-cars-scraper/)
- **n8n Workflow File:** [`n8n/offerup-vehicles-cars-scraper-n8n-workflow.json`](n8n/offerup-vehicles-cars-scraper-n8n-workflow.json)
- **Engineering Playbook:** [Used Car VIN, Auto Dealer & FSBO Real Estate Scraping Guide in 2026 (FB Marketplace, Craigslist & OfferUp)](https://unitbytes.com/blog/used-car-vin-real-estate-fsbo-scraping-facebook-marketplace-craigslist-offerup-guide/)

#### Key Capabilities
- **19 Structured Vehicle & VIN Attributes:** Extracts vehicleVin, vehicleYear, vehicleMake, vehicleModel, vehicleTrim, vehicleMiles, vehicleTitleStatus, vehicleDriveTrain, vehicleTransmission, and vehicleEngineCylinders.
- **Make, Model, Mileage & Price Range Filters:** Filter server-side by vehicle make, model, minimum/maximum model year, maximum odometer mileage, clean title status, and local radius around any US ZIP code.
- **Private Owner vs. Auto Dealership Lead Split:** Distinguishes commercial auto dealers (isAutosDealer) from private-party sellers and extracts verified dealership phone numbers, website URLs, and lot addresses.
- **Price-Drop Detection & Historical Comps:** Calculates originalPrice vs. current price drops (USD and %) and tracks active vs. SOLD vehicle velocity starting at `$0.80` per 1,000 listings.

#### ⚙️ Input Parameters (Schema)

| Parameter | Type | Default / Prefill | Description |
| :--- | :---: | :--- | :--- |
| `make` | `string` | `Honda` | Vehicle manufacturer (e.g., 'Honda', 'Toyota', 'Ford', 'BMW', 'Chevrolet'). |
| `model` | `string` | `Civic` | Vehicle model (e.g., 'Civic', 'Camry', 'F-150', 'Tacoma'). |
| `searchQuery` | `string` | — | Optional extra search keywords (e.g., 'Si', 'hybrid', 'clean title', 'AWD'). |
| `categoryId` | `string` | `5.1` | OfferUp automotive category. |
| `minYear` | `integer` | — | Server-side filter for minimum model year (e.g. 2018). |
| `maxYear` | `integer` | — | Server-side filter for maximum model year (e.g. 2026). |
| `maxMiles` | `integer` | — | Server-side filter for maximum odometer mileage (OfferUp uses 25,000-mile increments: 25000, 50000, 75000, 100000, 125000, 150000, 175000, 200000). |
| `minPrice` | `integer` | — | Minimum vehicle price in USD. |
| `maxPrice` | `integer` | — | Maximum vehicle price in USD. |
| `zipCode` *(Required)* | `string` | `90001` | 5-digit US ZIP code (e.g. 90001 for Los Angeles, 77082 for Houston, 33101 for Miami). |
| `radius` | `integer` | `50` | Search distance radius around the ZIP code (5 to 500 miles). |
| `sortBy` | `string` | `-posted` | Sorting order for vehicle listings. |
| `maxItems` | `integer` | `20` | Maximum number of vehicle listings to extract. |
| `scrapeDetails` | `boolean` | `True` | When enabled (default), extracts full 17-character VIN, title status, drivetrain, cylinders, MPG, vehicle options, history report issues, and dealer phone/address (`$2.50/1k`). Disable for fast summary discovery (`$0.80/1k`). |
| `startUrls` | `array` | — | OfferUp vehicle search, dealer profile (/p/<userId>), or direct car listing URLs. |
| `proxyConfiguration` | `object` | `{"useApifyProxy": true, "apifyProxyGroups": ["RE` | Apify Residential US proxy configuration. |

#### Python SDK Quickstart (`examples/run_offerup_vehicles_cars_scraper.py`)
```python
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
```

#### Sample Output Schema (`samples/offerup-vehicles-cars-scraper-sample.json`)
```json
{
  "listingId": "31e89a78-c823-3e02-89b3-8b15e2380f28",
  "url": "https://offerup.com/item/detail/31e89a78-c823-3e02-89b3-8b15e2380f28",
  "title": "2022 Honda Civic Si",
  "price": 18995.0,
  "status": "LISTED",
  "categoryName": "Vehicles",
  "subcategoryName": "Cars & Trucks",
  "locationName": "Houston, TX",
  "latitude": 29.7301,
  "longitude": -95.6432,
  "isVehicle": true,
  "vehicleYear": 2022,
  "vehicleMake": "Honda",
  "vehicleModel": "Civic Si",
  "vehicleTrim": "Si",
  "vehicleMiles": 70408,
  "vehicleVin": "1HGCM82633A004352",
  "vehicleColor": "red",
  "vehicleBody": "Sedan",
  "vehicleDoors": 4,
  "vehicleTransmission": "Manual",
  "vehicleDriveTrain": "FWD",
  "vehicleFuelType": "Premium gasoline",
  "vehicleEngineCylinders": "4",
  "vehicleEngineDescription": "1.5L I-4 direct injection, DOHC, VTEC variable valve control, intercooled turbo, 200HP",
  "vehicleCityMpg": 27,
  "vehicleHighwayMpg": 37,
  "vehicleStockNumber": "CN1015",
  "vehicleSellerType": "dealer",
  "vehicleOptions": [
    "Backup Camera",
    "LED Headlights",
    "Lane Keeping Assist"
  ],
  "sellerId": "100098765",
  "sellerProfileUrl": "https://offerup.com/p/100098765",
  "sellerName": "Metro Auto Group",
  "sellerPhone": "5550192834",
  "sellerWebsite": "https://example-motors.com",
  "sellerAddress": "100 Market St, Houston, TX 77002, USA",
  "isDealer": true,
  "isAutosDealer": true,
  "sellerBadges": [
    "Confirmed phone",
    "Confirmed email"
  ],
  "sellerGoogleReviewRating": 4.0
}
```

#### Frequently Asked Questions
**Q: Does the OfferUp Vehicles Scraper extract 17-character VINs and mileage?**
Yes. Enable scrapeDetails: true to extract vehicleVin, vehicleYear, vehicleMake, vehicleModel, vehicleTrim, vehicleMiles, vehicleTitleStatus, drivetrain, transmission, and cylinder count.

**Q: Can I filter private-party car sellers from commercial dealerships?**
Yes. Every record includes isAutosDealer and vehicleSellerType ('private' vs. 'dealer') alongside verified dealership phone numbers and lot addresses.

**Q: Can I search by specific make, model, and ZIP code radius?**
Yes. Filter by vehicle make (e.g. Toyota, Honda, Ford), model, year range, maximum odometer miles, and price bounds around any US ZIP code.

**Q: How much does OfferUp vehicle extraction cost?**
Fast search mode costs `$0.80` per 1,000 vehicles (`$0.0008/item`), making it ideal for high-frequency multi-city automotive arbitrage monitoring.

---

### 🚀 OfferUp Seller Inventory & Auto Dealer Leads Scraper (`unitbytes/offerup-seller-inventory-scraper`)

Scrape OfferUp seller storefronts (/p/<userId>), complete dealer inventories, verified business phone numbers, websites, physical addresses, opening hours, and Google reviews. From `$0.80/1k`.

- **Pricing:** `$0.0008 / item` (Pay-Per-Event — `$0.0008` listing discovery, `$0.0025` deep detail enrichment (volume tiers from `$0.0006`))
- **Cloud Console:** [https://apify.com/unitbytes/offerup-seller-inventory-scraper?fpr=939u3w&fp_sid=gh_classifieds](https://apify.com/unitbytes/offerup-seller-inventory-scraper?fpr=939u3w&fp_sid=gh_classifieds)
- **Full Documentation & Schema:** [https://unitbytes.com/actors/offerup-seller-inventory-scraper/](https://unitbytes.com/actors/offerup-seller-inventory-scraper/)
- **n8n Workflow File:** [`n8n/offerup-seller-inventory-scraper-n8n-workflow.json`](n8n/offerup-seller-inventory-scraper-n8n-workflow.json)
- **Engineering Playbook:** [Used Car VIN, Auto Dealer & FSBO Real Estate Scraping Guide in 2026 (FB Marketplace, Craigslist & OfferUp)](https://unitbytes.com/blog/used-car-vin-real-estate-fsbo-scraping-facebook-marketplace-craigslist-offerup-guide/)

#### Key Capabilities
- **Complete Paginated Seller Storefronts:** Paste any OfferUp seller profile URL (/p/<userId>) or numeric seller ID to extract their entire active and sold storefront catalog in a single run.
- **Verified TruYou & Auto Dealership Metadata:** Captures TruYou identity verification status, review averages, response metrics, join dates, and full commercial dealership contact profiles (phone, website, physical address).
- **Fast Catalog Mode at `$0.80 / 1,000 Items`:** Extracts seller profile metrics plus storefront listing titles, prices, SOLD status flags, vehicle mileage, and cover images in Fast Mode without paying per-item detail fees.
- **Optional Deep Item Enrichment (scrapeDetails):** Enable scrapeDetails: true whenever you need full multi-photo galleries, long-form item descriptions, 17-character vehicle VINs, and exact GPS coordinates.

#### ⚙️ Input Parameters (Schema)

| Parameter | Type | Default / Prefill | Description |
| :--- | :---: | :--- | :--- |
| `sellerIds` | `array` | `["100098765"]` | OfferUp Seller IDs (e.g. '100098765') or profile URLs ('https://offerup.com/p/100098765'). Leave empty to discover local sellers/dealers by ZIP code below. |
| `startUrls` | `array` | — | Paste OfferUp seller storefront URLs (https://offerup.com/p/<userId>) or local search URLs. |
| `searchQuery` | `string` | — | Keyword to discover local sellers/dealers (e.g., 'toyota', 'furniture', 'iphone'). |
| `categoryId` | `string` | `5.1` | Category for local seller/dealer discovery. |
| `zipCode` *(Required)* | `string` | `77082` | 5-digit US ZIP code (e.g. 77082 for Houston, 90001 for Los Angeles). |
| `radius` | `integer` | `50` | Search distance radius around the ZIP code (5 to 500 miles). |
| `maxItems` | `integer` | `20` | Maximum number of storefront listings to extract. |
| `scrapeDetails` | `boolean` | `False` | Note: When scraping Seller IDs (/p/<userId>), full seller contact info (phone, website, address, hours, reviews) is ALREADY extracted in Fast Mode (`$0.80/1k`)! Enable this only if you also need per-item VIN/descriptions or when discovering sellers via keyword search. |
| `proxyConfiguration` | `object` | `{"useApifyProxy": true, "apifyProxyGroups": ["RE` | Apify Residential US proxy configuration. |

#### Python SDK Quickstart (`examples/run_offerup_seller_inventory_scraper.py`)
```python
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
```

#### Sample Output Schema (`samples/offerup-seller-inventory-scraper-sample.json`)
```json
{
  "listingId": "d9f7c56b-a931-35e1-a286-12f83fa44589",
  "url": "https://offerup.com/item/detail/d9f7c56b-a931-35e1-a286-12f83fa44589",
  "title": "2019 BMW X4",
  "price": 23995.0,
  "status": "LISTED",
  "locationName": "Houston, TX",
  "latitude": 29.7301361,
  "longitude": -95.643225,
  "isVehicle": true,
  "vehicleMiles": 103937,
  "sellerId": "100098765",
  "sellerProfileUrl": "https://offerup.com/p/100098765",
  "sellerName": "Metro Auto Group",
  "sellerPhone": "5550192834",
  "sellerWebsite": "https://example-motors.com",
  "sellerAddress": "100 Market St, Houston, TX 77002, USA",
  "sellerBio": "Welcome to Metro Auto Group! Our virtual showroom is stocked with a wide selection of inspected pre-owned vehicles.",
  "sellerLastActive": "Active in the last day",
  "isDealer": true,
  "isAutosDealer": true,
  "isSubPrimeDealer": false,
  "sellerBadges": [
    "Confirmed phone",
    "Confirmed email"
  ],
  "sellerOpeningHours": "Monday: 9:00 AM–7:00 PM | Tuesday: 9:00 AM–7:00 PM | Wednesday: 9:00 AM–7:00 PM | Thursday: 9:00 AM–7:00 PM | Friday: 9:00 AM–7:00 PM | Saturday: 9:00 AM–7:00 PM | Sunday: Closed",
  "sellerGoogleReviewRating": 4.0
}
```

#### Frequently Asked Questions
**Q: How do I scrape all active and sold items from an OfferUp seller?**
Paste any OfferUp seller profile URL (https://offerup.com/p/12345678) or numeric user ID into startUrls or sellerIds to extract their complete paginated storefront inventory.

**Q: Does it extract commercial auto dealership contact details?**
Yes. For verified auto dealers and power sellers, the Actor extracts business name, phone number (sellerPhone), website URL, physical lot address, and TruYou verification status.

**Q: How much does scraping a seller's inventory cost?**
In Fast Mode (scrapeDetails: false), full seller contact details and all storefront listings are extracted at just `$0.80` per 1,000 items.

**Q: Can I filter a seller's catalog to only active or sold listings?**
Yes. Every item includes explicit isSold and status flags so you can analyze either available stock or historical sold velocity.

---

### 🚀 OfferUp Deal Monitor, Price Drop & Status Tracker (`unitbytes/offerup-deal-monitor-scraper`)

Monitor OfferUp for fresh bargains, price drops, used electronics & phones, and batch-check listing status (LISTED vs SOLD) across any US ZIP code. From `$0.80/1k`.

- **Pricing:** `$0.0008 / item` (Pay-Per-Event — `$0.0008` listing discovery, `$0.0025` deep detail enrichment (volume tiers from `$0.0006`))
- **Cloud Console:** [https://apify.com/unitbytes/offerup-deal-monitor-scraper?fpr=939u3w&fp_sid=gh_classifieds](https://apify.com/unitbytes/offerup-deal-monitor-scraper?fpr=939u3w&fp_sid=gh_classifieds)
- **Full Documentation & Schema:** [https://unitbytes.com/actors/offerup-deal-monitor-scraper/](https://unitbytes.com/actors/offerup-deal-monitor-scraper/)
- **n8n Workflow File:** [`n8n/offerup-deal-monitor-scraper-n8n-workflow.json`](n8n/offerup-deal-monitor-scraper-n8n-workflow.json)
- **Engineering Playbook:** [Automating Local Classifieds Arbitrage: Scraping Facebook Marketplace, Craigslist & OfferUp](https://unitbytes.com/blog/local-classifieds-arbitrage-facebook-marketplace-craigslist-offerup-guide/)

#### Key Capabilities
- **Automatic Price-Drop Calculation (USD and %):** Compares originalPrice against current listing price and outputs exact priceDropAmount ($) and priceDropPercent (%) alongside firm vs. negotiable price flags.
- **Electronics, Phones & Local Flipping Filters:** Target for_parts (repair arbitrage), like_new (open-box flips), or new items across Cell Phones, Computers, Video Games, and Collectibles with local pickup or shipping filters.
- **Batch Listing SOLD / LIVE Status Verification:** Pass a list of OfferUp item URLs in startUrls to verify in seconds whether tracked deals are still LISTED, marked SOLD, or removed.
- **Multi-ZIP Geo-Targeting & Seller Trust Scores:** Scan any US ZIP code or coordinate radius while filtering for TruYou-verified sellers, high rating counts, and freshly posted under-market listings.

#### ⚙️ Input Parameters (Schema)

| Parameter | Type | Default / Prefill | Description |
| :--- | :---: | :--- | :--- |
| `searchQuery` | `string` | `iphone 15 pro` | Keyword to monitor (e.g., 'iphone 15 pro', 'macbook m3', 'ps5', 'rtx 4090'). Leave blank if checking specific listing URLs in Start URLs below. |
| `categoryId` | `string` | `all` | OfferUp category to monitor. |
| `conditionFilter` | `string` | `all` | Server-side condition filter — e.g. 'for_parts' for repair/refurbish arbitrage or 'new'/'like_new' for retail flips. |
| `deliveryMethod` | `string` | `all` | Filter by Local Pickup ('local'), Nationwide Shipping ('shipping'), or All ('all'). |
| `minPrice` | `integer` | — | Minimum price in USD (helps filter out `$0`/`$1` spam listings). |
| `maxPrice` | `integer` | — | Under-$X bargain cap in USD. |
| `zipCode` *(Required)* | `string` | `90001` | 5-digit US ZIP code to center the deal radar. |
| `radius` | `integer` | `50` | Search distance radius around the ZIP code (5 to 500 miles). |
| `sortBy` | `string` | `-posted` | Default '-posted' ensures newest listings appear first. |
| `startUrls` | `array` | — | Direct OfferUp item URLs (for LISTED/SOLD status & price drop tracking) or search URLs. |
| `maxItems` | `integer` | `20` | Maximum number of listings to check or extract. |
| `scrapeDetails` | `boolean` | `True` | Enriches listings with originalPrice, priceDropAmount, priceDropPercent, postDate, live status (LISTED/SOLD), and seller reputation. |
| `proxyConfiguration` | `object` | `{"useApifyProxy": true, "apifyProxyGroups": ["RE` | Apify Residential US proxy configuration. |

#### Python SDK Quickstart (`examples/run_offerup_deal_monitor_scraper.py`)
```python
from apify_client import ApifyClient

APIFY_TOKEN = os.getenv("APIFY_API_TOKEN", "YOUR_APIFY_API_TOKEN")
if not APIFY_TOKEN or APIFY_TOKEN.startswith("YOUR_"):
    raise SystemExit("Please set your Apify API token: export APIFY_API_TOKEN='apify_api_...'")

client = ApifyClient(APIFY_TOKEN)

run_input = {
    "searchQuery": "iphone 15 pro",
    "zipCode": "90001",
    "categoryId": "all",
    "conditionFilter": "all",
    "deliveryMethod": "all",
    "radius": 50
}

run = client.actor("unitbytes/offerup-deal-monitor-scraper").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("title"), item.get("price"), item.get("conditionText"), item.get("url"))
```

#### Sample Output Schema (`samples/offerup-deal-monitor-scraper-sample.json`)
```json
{
  "listingId": "9a781d60-e703-3486-9a62-2d713775362c",
  "url": "https://offerup.com/item/detail/9a781d60-e703-3486-9a62-2d713775362c",
  "title": "iPhone 15 Pro 256GB Unlocked",
  "price": 450.0,
  "originalPrice": 550.0,
  "priceDropAmount": 100.0,
  "priceDropPercent": 18.2,
  "isFirmPrice": false,
  "condition": "Open Box / Like New",
  "status": "LISTED",
  "categoryName": "Electronics & Media",
  "subcategoryName": "Cell phones & Accessories",
  "locationName": "Los Angeles, CA",
  "localPickup": true,
  "shippingAvailable": true,
  "sellerName": "Seller_B",
  "sellerItemsSold": 10
}
```

#### Frequently Asked Questions
**Q: How does automatic price-drop detection work on OfferUp?**
The Actor compares each item's originalPrice against its current price and computes priceDropAmount ($) and priceDropPercent (%) alongside isFirmPrice flags.

**Q: Can I filter for cracked/for-parts phones or open-box electronics?**
Yes. Use conditionFilter ('for_parts', 'like_new', 'new', 'good', 'fair') across Cell Phones, Computers, and Video Games to source high-margin repair and resale inventory.

**Q: How do I batch-check if tracked OfferUp deals have sold?**
Pass your saved https://offerup.com/item/detail/<id> URLs in startUrls and the Actor returns whether each listing is still LISTED, SOLD, or NOT_FOUND.

**Q: Can I trigger instant Telegram or Slack alerts for under-market deals?**
Yes. Pair this Actor with our pre-built n8n OfferUp Deal Monitor workflow to score new listings and alert your buying team in real time.


---

## ⚡ Quick Installation & Local Usage

### 1. Run Interactively in Google Colab (Zero Local Setup)
Click **[Open in Google Colab ↗](https://colab.research.google.com/github/unitbytes/Craigslist-OfferUp-Scraper-API/blob/main/notebooks/quickstart.ipynb)** ([`notebooks/quickstart.ipynb`](notebooks/quickstart.ipynb)) to inspect the sample output DataFrame immediately and run live extractions in your browser without installing Python locally.

### 2. Run Locally with Python (`apify-client`)
```bash
git clone https://github.com/unitbytes/Craigslist-OfferUp-Scraper-API.git
cd Craigslist-OfferUp-Scraper-API
pip install -r requirements.txt
export APIFY_API_TOKEN="your_apify_api_token"
python examples/run_craigslist_scraper.py
```

### 3. Import into n8n (Self-Hosted or Cloud)
1. Open any `.json` file inside the [`n8n/`](n8n/) folder (or copy in 1 click from **[unitbytes.com/n8n](https://unitbytes.com/n8n/)** / **[n8n.io/creators/unitbytes](https://n8n.io/creators/unitbytes/)**).
2. Press **`Ctrl+V` / `Cmd+V`** directly onto your n8n workflow canvas.
3. Configure your Apify API Token in the `HTTP Header Auth` credential on Node `2. Run UnitBytes (...)` (and customize your search inputs in Node `1. Configure Search & Rules`), then click **Test Workflow**.

### 4. Use with AI Coding Agents (Cursor, Windsurf & Claude Code MCP)
This repository includes a ready-to-use Model Context Protocol configuration at [`.cursor/mcp.json`](.cursor/mcp.json) pointing to `https://mcp.apify.com` with this suite's UnitBytes actors pre-registered. Open this folder in **Cursor** or **Windsurf** to let your AI agent run live extractions and inspect schemas automatically.

---

## 💼 Need Done-For-You Datasets or Custom Pipelines?

Don't want to manage API tokens or scripts? **UnitBytes Data Delivery** provides ready-to-use **CSV, Excel (.xlsx), Google Sheets, or Webhook feeds** tailored to your exact target keywords, cities, or categories.

- 🌐 **Request a Sample Dataset:** [https://unitbytes.com/#enterprise-intake](https://unitbytes.com/#enterprise-intake)
- 📧 **Direct Engineering Contact:** [contact@unitbytes.com](mailto:contact@unitbytes.com)
- ⚡ **Explore All 39 Scrapers:** [https://unitbytes.com/actors/](https://unitbytes.com/actors/)
- 📚 **Engineering Playbooks & Guides:** [https://unitbytes.com/blog/](https://unitbytes.com/blog/)
- 🔗 **Official n8n Creator Profile:** [https://n8n.io/creators/unitbytes/](https://n8n.io/creators/unitbytes/)
