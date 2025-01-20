from playwright.async_api import async_playwright

async def automated_login():
    async with async_playwright() as p:
        print("Launching browser...")
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        print("Navigating to the login page...")
        await page.goto("https://ai.invideo.io/login")

        print("Filling in the email address...")
        await page.fill("input[name='email_id']", "your_email@example.com")  # Replace with your email

        print("Clicking the 'Continue with Email' button...")
        await page.click("button[type='submit']")

        print("Waiting for the code input field to appear...")
        await page.wait_for_selector("input[name='code']")

        print("Filling in the login code...")
        login_code = "123456"  # Replace with the actual code you receive or handle it dynamically
        await page.fill("input[name='code']", login_code)

        print("Clicking the 'Login' button...")
        await page.click("button[type='submit']")

        print("Waiting for the final page to load...")
        await page.wait_for_load_state("networkidle")

        # Check the current URL to verify login success
        current_url = page.url
        print("Current URL:", current_url)

        if "dashboard" in current_url:  # Replace "dashboard" with the actual path of the logged-in page
            print("Login successful!")
        else:
            print("Login failed: Check the login code or site issue.")

        await browser.close()

import asyncio
asyncio.run(automated_login())