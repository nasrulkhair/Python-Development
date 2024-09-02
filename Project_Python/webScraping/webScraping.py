"""
from scrapy import Selector

html = '''
<!DOCTYPE html>
<html>
<head>
    <title>DataCamp Example</title>
</head>
<body>
    <div class="hello datacamp">
        <p>Hello World!</p>
    </div>
    <p>Enjoy DataCamp!</p>
</body>
</html>
'''


sel = Selector(text=html)
paragraphs = sel.xpath("//p").extract()  # Recommended method / also can use extract_first
print(paragraphs)

"""

from scrapy import Selector
import requests

# URL to scrape
url = 'https://en.wikipedia.org/wiki/Web_scraping'

# Fetch the HTML content
response = requests.get(url)
html = response.text  # Use .text to get the HTML as a string
#print(html)

# Create a Scrapy Selector instance
sel = Selector(text=html)

# Example: Extract all the headings (h1, h2, h3, etc.)
headings = sel.xpath('//h1/text() | //h2/text() | //h3/text()').getall()

print("Headings found on the page:")
print(headings)
