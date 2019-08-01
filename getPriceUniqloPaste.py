import bs4,requests,pyperclip

def getUniqloPrice(productURL):
    res=requests.get(productURL)
    res.raise_for_status()
    
    soup=bs4.BeautifulSoup(res.text,'html.parser')
    elems=soup.select('#product-content > div > div.product-price > span.price-sales.pdp-space-price.sale-price-only')
    return elems[0].text.strip()


price=getUniqloPrice(pyperclip.paste())
print('The price is '+ price)
