import asyncio
import aiohttp

async def textpage(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as page:
            return await page.text()

async def main():
    urls = ['https://info.cern.ch/hypertext/WWW/TheProject.html', 'https://www.columbia.edu/~fdc/sample.html', 
            'http://help.websiteos.com/websiteos/example_of_a_simple_html_page.htm']

    tasks = [textpage(url) for url in urls]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)
        print("\n ===========================\n\n")
asyncio.run(main())