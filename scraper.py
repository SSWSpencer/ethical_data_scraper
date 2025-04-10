import asyncio
from playwright.async_api import async_playwright
import random


# ===========================================================================================================================
# ===================================Stuff to edit for your own (ethical) purposes===========================================
# ===========================================================================================================================

# url of the page(s) it will get the data from
# important note: the url needs to have a way to determine the page number. This is not automatically applied to the URL from the 'first' page.
# sometimes the page identifier is an attribute ("&page=") and sometimes it's a route ('/Page-).
# manually navigate to the SECOND page of whatever you're looking to get the data from, and copy that url. It should be like newegg.com/p/..&page=2 or newegg.com/something/../Page-2. You want THIS url. Then just remove the 2, and put that URL on the next line. 
BASE_URL = "https://www.newegg.com/p/pl?N=100897449%20601416058%20601413441%20601432216%20601411321%20601432181%20601409839%20601432215%20601409838%20601468988%20601387049%20601357786%20601321513%20600530838%20601189465%20601202226%20601397000%20601399480%20601409042%20601427355&Order=1&page="

# number of pages to get data from. this one is self-explanatory, but newegg seems to be like 'oh there's only 20 pages of results' meanwhile there's a lot more.
# there was definitely a smarter way to incorporate this so it dynamically knows when to stop searching. Maybe when it starts seeing 'out of stock'? Idk, im rambling, this script served it's purpose. if I/anyone else ever uses this, hardcoding 'oh, there's 24 pages before shit starts showing up as out-of-stock' would be a hell of a lot more reliable than trusting my code to do it effectively
NUMBER_OF_PAGES = 24

# ===========================================================================================================================
# ===========================================================================================================================
# ===========================================================================================================================


async def grab_data():

    results = []


    async with async_playwright() as p:
        #launch chrome with "yes, I am definitely human"-flags
        browser = await p.chromium.launch(
            headless=False,
            channel="chrome", 
            args=[
                "--disable-blink-features=AutomationControlled",
                "--disable-infobars", 
                "--no-sandbox" 
            ]
        )
        
        # create browser context that loads saved session
        context = await browser.new_context(
            storage_state="chrome_state.json",
            viewport={"width": 1920, "height": 1080} # common 1080p w.
        )


        page = await context.new_page()
        page_num = 1 
        
        # start loop to go through declared number of pages
        while page_num <= NUMBER_OF_PAGES:

            url = BASE_URL + str(page_num) 
            print(f"Grabbing data from page {page_num}") 
            await page.goto(url, timeout=60000) # 

            # Fake a little mouse movement to look human
            await page.mouse.move(random.randint(100, 800), random.randint(100, 600))
            await asyncio.sleep(random.uniform(1, 2))


            # wait for product titles to load
            try:
                await page.wait_for_selector(".item-title", timeout=20000)
            except:
                print(f"Page {page_num}: No products found. Ending. (or bot detection kicked in)")
                break

            items = await page.query_selector_all(".item-cell")
            if not items:
                print("Finished")
                break

            for item in items:
                try:
                    title_el = await item.query_selector(".item-title")
                    price_el = await item.query_selector(".price-current")

                    title = await title_el.inner_text()
                    link = await title_el.get_attribute("href")
                    price = await price_el.inner_text()

                    results.append(f"{title} - {price} - {link}")
                except:
                    continue

            # Save after each page
            with open("results.txt", "w", encoding="utf-8") as f:
                for line in results:
                    f.write(line + "\n")

            page_num += 1
            delay = random.uniform(3, 7)
            print(f"Page finished. Wait {delay:.2f} seconds")
            await asyncio.sleep(delay)

        await browser.close()
        print(f"Finished. {len(results)} items recorded.")

asyncio.run(grab_data())