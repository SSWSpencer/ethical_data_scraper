# 🧠 Ethical Data Scraper
## (for Newegg, Playwright-Based)

This project is a stealthy, human-like web scraper for Newegg products, built using [Playwright](https://playwright.dev/) and Python. It allows you to programmatically gather product names, prices, and links — useful for filtering out the noise when you're looking for the best bang for your buck.

> ⚠️ This scraper is a proof-of-concept and is intended for **personal, educational, or internal use only**. Use it responsibly and respect Newegg’s terms of service.

---

## 🚀 Features

- Uses your **real Chrome installation** instead of bundled Chromium
- Loads your actual Newegg login session (cookies, cart, etc.)
- Randomized mouse movement and wait times to mimic real users
- Saves scraped results to `results.txt`
- Scrapes a customizable number of pages

---

## 📦 Setup

1. **Install Playwright**:

```bash
pip install playwright
playwright install
```
2. **Save your Newegg Login session**
```
python setup.py
```
> when the browser window opens, log into your Newegg account. Then press Enter in the terminal

3. **Configure scraper.py**
```
BASE_URL = "[Your_URL_Here]"
NUMBER_OF_PAGES = [Number_of_Pages_to_Scrape]
```
> Note: the URL must be formatted appropriately, ending with '&page=' or '/Page-'. The way the script navigates pages is by appending a number to the end of the url. There is an example in the script

4. **Run the Script**
```
python scraper.py
```
> This will start at page 1 and continue through however many pages you set it to scrape, saving the file after every page so you don't lose progress

## 📁 Output
Scraped data is written to `results.txt` in this format:
```
[product_name] - [product_price] - [product_link]
```
Note: It does not filter out-of-stock or backordered items.

## ❌ Do Not
- Use this product for scrape the entire Newegg catalog
- Use this for resale, bulk listing, or data mining
- Redistribute your `chrome_state.json` file (it contains your session cookies)

## 📜 License
MIT License (modify as needed). You are responsible for your own usage. Use this ethically and legally.

## 🙏 A Note on Ethics
This script does not abuse or exploit Newegg. It mimics what any human shopper could do manually — just faster. Please don't use it for unethical or commercial scraping.
