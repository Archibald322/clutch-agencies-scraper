# Clutch B2B Agencies & IT Services Scraper

[![Apify Actor](https://img.shields.io/badge/Apify-Actor%20Store-orange?logo=apify)](https://apify.com/moneygain/clutch-agencies-scraper)
[![Python Version](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-blue?logo=python)](https://github.com/Archibald322/clutch-agencies-scraper)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Live Apify Store Actor:** [https://apify.com/moneygain/clutch-agencies-scraper](https://apify.com/moneygain/clutch-agencies-scraper)

This repository provides an open-source Python runner and documentation for **[Clutch B2B Agencies & IT Services Scraper](https://apify.com/moneygain/clutch-agencies-scraper)**.

---

## ⚡ Quickstart

### Option 1: Run in Cloud (No Code)
Launch directly from your browser via the Apify Store console:
👉 **[Open Clutch B2B Agencies & IT Services Scraper on Apify Store](https://apify.com/moneygain/clutch-agencies-scraper)**

### Option 2: Run via Python SDK
```bash
git clone https://github.com/Archibald322/clutch-agencies-scraper.git
cd clutch-agencies-scraper
pip install -r requirements.txt
export APIFY_TOKEN="your_apify_token_here"
python run.py
```

---

# 🏢 Clutch B2B Agencies & IT Services Scraper

**Scrape Clutch.co agency directory data to JSON, CSV, or Excel in seconds without browser overhead.** Extract verified B2B software development companies, web development firms, IT service providers, digital marketing agencies, SEO consultants, and mobile app studios from **Clutch.co** — the world's premier B2B agency rating and review directory.

Designed for outbound sales teams, marketing agencies, B2B lead generation specialists, partnership directors, and autonomous AI agents. Built with high-speed HTTP requests, **zero browser overhead**, and **100% Pay-Per-Event (PPE) pricing** — you only pay for verified agency records returned, never for empty results or blocked attempts.

---

## ⚡ Speed & Value Comparison

| Feature | Our Lightweight Clutch Scraper | Heavy Browser Scrapers (Playwright / Puppeteer) |
|---|---|---|
| **Memory Usage** | **128 MB – 256 MB** | 2 GB – 4 GB |
| **Startup Fee** | **$0.00 (Zero Start Fee)** | $0.05 – $0.10 per run |
| **Extraction Speed** | **0.5s – 1s per page** | 10s – 20s per directory page |
| **Pricing Model** | **Pay-Per-Event ($0.008 / agency)** | Heavy Compute / $50+ Monthly Rental |
| **Direct Website Extraction** | **Automatically decodes direct destination URLs** | Raw redirect links (`/redirect?u=...`) |
| **Service Focus Breakdown** | **Clean percentages (e.g. 30% AI, 40% Web)** | Raw unstructured HTML tooltips |

---

## 📦 Sample JSON Output

```json
{
  "id": "178522",
  "name": "Power Digital",
  "profileUrl": "https://clutch.co/profile/power-digital",
  "directWebsite": "https://powerdigitalmarketing.com/growthplan/",
  "websiteDomain": "powerdigitalmarketing.com",
  "rating": 4.87,
  "reviewsCount": 66,
  "minProjectSize": "$5,000+",
  "hourlyRate": "$100 - $149 / hr",
  "employees": "250 - 999",
  "location": "San Diego, CA",
  "serviceFocus": [
    "15% Advertising",
    "20% SEO",
    "25% Content Marketing"
  ],
  "isSponsor": true,
  "scrapedAt": "2026-11-17T12:00:00.000000+00:00"
}
```

---

## 🎯 Use Cases & Business Value

- **B2B Outbound Lead Generation**: Extract direct decoded company websites and root domains (`directWebsite`, `websiteDomain`) for high-converting cold email and LinkedIn outreach campaigns.
- **Competitor & Market Research**: Benchmark hourly billing rates (`$100 - $149 / hr`), minimum project requirements (`$10,000+`), and client satisfaction ratings across global agency hubs.
- **Vendor & Partner Sourcing**: Identify top-rated software engineering, cloud, AI, and design partners verified by real client reviews and ratings.
- **Autonomous AI Agents & MCP Workflows**: Feed fresh, verified agency intelligence directly into autonomous prospecting and vendor assessment workflows via **Apify MCP Server**.

---

## ⚙️ Input Parameters

> [!IMPORTANT]
> **Residential Proxy Recommended**: Clutch.co strictly filters datacenter IP addresses. In the actor's input settings, **Apify Residential Proxy** is enabled and prefilled by default (`RESIDENTIAL` group). Ensure your Apify account has access to Residential Proxies for 100% reliable execution. Under Pay-Per-Event (PPE) pricing, you are only charged for verified items successfully delivered ($0 charged if a block occurs).

| Parameter | Type | Default | Description |
|---|---|---|---|
| `startUrls` | Array | `["https://clutch.co/agencies"]` | Direct Clutch directory or category URLs to scrape. |
| `category` | String | `"agencies"` | Category shortcut (`agencies`, `developers`, `web-developers`, `seo-firms`, `it-services`, `mobile-app-developers`). |
| `minRating` | Number | `0` | Filter agencies with client rating at or above threshold (e.g. `4.5`). |
| `maxItems` | Integer | `10` | Maximum number of verified agency records to scrape and return (Prefilled for instant 5-second test runs). |
| `proxyConfiguration` | Object | `{"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}` | Apify Proxy settings. Residential proxy group is strongly recommended. |

---

## 🤖 Integrate with AI Agents & No-Code Platforms

### 1. Claude Desktop & Cursor via Apify MCP Server
Connect this actor directly to Cursor, Claude Desktop, Windsurf, or LangChain agents using the official Apify MCP Server:

```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": ["-y", "@apify/mcp-server"],
      "env": {
        "APIFY_TOKEN": "YOUR_APIFY_API_TOKEN"
      }
    }
  }
}
```
*Prompt example:*
> *"Find 10 top-rated custom software development agencies in the US with at least 4.8 stars and minimum project size under $25k using clutch-agencies-scraper."*

### 2. n8n Automation Workflows
1. Add an **Apify Node** or **HTTP Request Node** in your n8n workflow.
2. Select `Run an Actor` with Actor ID: `moneygain/clutch-agencies-scraper`.
3. Pipe the resulting decoded domains directly into Hunter.io or Apollo to enrich decision-maker emails.

### 3. Make.com (Integromat)
1. Add the **Apify Module** ➔ `Run Actor and get dataset items`.
2. Push qualified agency leads directly into HubSpot or Notion CRM.

### 4. Clay.com Enrichment
1. Use the **Apify Integration** inside Clay.
2. Automatically enrich B2B vendor tables with Clutch review counts and hourly rate brackets.

### 5. Python SDK Integration
```python
from apify_client import ApifyClient

client = ApifyClient("YOUR_APIFY_API_TOKEN")
run_input = {
    "category": "developers",
    "minRating": 4.8,
    "maxItems": 25,
    "proxyConfiguration": {"useApifyProxy": True, "apifyProxyGroups": ["RESIDENTIAL"]}
}
run = client.actor("moneygain/clutch-agencies-scraper").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(f"{item['name']} ({item['rating']}★) | {item['hourlyRate']} -> {item['directWebsite']}")
```

---

## ❓ Frequently Asked Questions (SEO FAQ)

### Q1: Is it legal to scrape data from Clutch.co?
**Yes.** All information extracted by this scraper is publicly displayed company profile data, verified review aggregates, and service capability overviews intended for public discovery. The actor does not access private reviewer communications or confidential account credentials.

### Q2: How much does it cost to scrape 1,000 agencies?
Under our **Pay-Per-Event (PPE)** pricing model, you only pay **$0.008 per verified agency record**, meaning 1,000 agencies cost **$8.00**. There are zero startup costs and zero charges for empty pages or blocked attempts. Apify subscribers receive tiered discounts up to 20% ($6.40 per 1,000).

### Q3: Can I export Clutch data to Excel, CSV, or Google Sheets?
**Yes.** Apify provides 1-click export options in JSON, CSV, XML, Excel (.xlsx), and HTML table formats. You can also sync datasets automatically to Google Sheets or Airtable via webhooks.

### Q4: Do I need residential proxies to scrape Clutch?
**Yes, recommended.** Clutch.co employs strict anti-bot detection against cloud datacenter IPs. Selecting Apify Residential Proxies (`RESIDENTIAL` group) ensures 100% reliable execution. If a block occurs, the actor stops gracefully and you are charged $0.00.

### Q5: Does this scraper extract the real agency homepage URL?
**Yes.** Clutch wraps external links in redirect tracking parameters (`/redirect?u=...`). Our actor automatically decodes the underlying query to return the clean, direct agency website URL (`directWebsite`) and root domain (`websiteDomain`).

---

## 🔗 Explore More High-Speed B2B Scrapers & Enrichers by Our Team

Supercharge your data pipelines, sales outreach, and AI agents with our suite of lightweight, Pay-Per-Event scrapers:

| Scraper | Segment / Target | Key Value | Store Link |
|---|---|---|---|
| **TrustMRR SaaS Startups Scraper** | SaaS Revenue & M&A Data | Stripe-verified MRR, 30d revenue, active subscriptions & founder contacts | [Open on Apify Store](https://apify.com/moneygain/trustmrr-startups-scraper) |
| **Ashby ATS Tech Jobs Scraper** | Next-Gen ATS Career Feeds | Direct ATS API extraction, salaries, departments & remote flags | [Open on Apify Store](https://apify.com/moneygain/ashby-jobs-scraper) |
| **Clutch B2B Agencies Scraper** | B2B Agencies & IT Services | Decoded direct websites, review ratings, hourly rates & service focus | [Open on Apify Store](https://apify.com/moneygain/clutch-agencies-scraper) |
| **Wellfound Startup Talent Scraper** | AI & Tech Startup Jobs | Startup jobs, compensation ranges, equity & tech stack tags | [Open on Apify Store](https://apify.com/moneygain/wellfound-jobs-scraper) |
| **TheProtocol.it IT Careers Scraper** | IT Salaries & Vacancies | Verified salary brackets, tech requirements & seniority levels | [Open on Apify Store](https://apify.com/moneygain/theprotocol-scraper) |
| **Bulldogjob Tech Recruitment Scraper** | Tech Recruitment Feeds | B2B/Employment rates, tech tags & recruiter contacts | [Open on Apify Store](https://apify.com/moneygain/bulldogjob-scraper) |
