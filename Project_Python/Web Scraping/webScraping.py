
'''
xpath = '/html/body/div[2]'  --> #look for specific generations
xpath = '//table'   --> #look forward allfuture generations
xpath = '/html/body/div[2]//table' --> #direct to all table elements which are descendants of the 2nd div child of the body
'''

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

sel = Selector( text = html )
sel.xpath("//p").extract()
