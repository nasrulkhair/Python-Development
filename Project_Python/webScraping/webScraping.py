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





