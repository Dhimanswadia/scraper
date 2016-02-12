from lxml import html
import requests

page = requests.get('https://www.doctor-oogle.com')
tree = html.fromstring(page.content)


#buyers = tree.xpath('//div[@title="buyer-name"]/text()')
prices = tree.xpath('//span[@class="rating"]/text()')

#print 'Buyers: ', buyers
print 'Prices: ', prices[0]


