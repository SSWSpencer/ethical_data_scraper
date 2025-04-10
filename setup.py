import asyncio
from playwright.async_api import async_playwright

async def save_chrome_state():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, channel="chrome")
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto("https://www.newegg.com/")
        print("Hey. Pay attention to me here. Log into Newegg and then press enter to save your browser state.")
        input()
        await context.storage_state(path="chrome_state.json")
        await browser.close()
        print("Session saved.")

asyncio.run(save_chrome_state())
