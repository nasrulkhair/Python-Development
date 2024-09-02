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

'''
sel = Selector(text=html)
paragraphs = sel.xpath("//p/text()").getall()  # Recommended method
print(paragraphs)
'''



'''
#other method
sel.xpath("//p").extract_first()
'''

#other method
sel = Selector(text=html)
sel.xpath("//p").extract_first()