import asyncio
from pyppeteer import launch

async def preparePageForTests(page):
    userAgent = 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'
    await page.setUserAgent(userAgent)
    await page.evaluateOnNewDocument("""() => { Object.defineProperty(navigator, 'webdriver', { get: () => false, }); }""")
    await page.evaluateOnNewDocument("""() => { window.chrome = { runtime: {}, }; }""")
    await page.evaluateOnNewDocument("""() => { const originalQuery = window.navigator.permissions.query; return window.navigator.permissions.query = (parameters) => ( parameters.name === 'notifications' ? Promise.resolve({ state: Notification.permission }) : originalQuery(parameters) ); }""")
    await page.evaluateOnNewDocument("""() => { Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5], }); }""")
    await page.evaluateOnNewDocument("""() => { Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'], }); }""")


async def main():
    browser = await launch({
        'args': ['--no-sandbox'],
        'headless': True,
    })
    page = await browser.newPage()
    await preparePageForTests(page);
    await page.goto('https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')
    await page.screenshot({'path': 'example.png'})
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
