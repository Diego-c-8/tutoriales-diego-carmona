from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
##aqui importamos las
my_url = 'https://tienda.mediaplayer.cl/amplificadores-de-audifonos-dac/fiio.html'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html,"html.parser")

containers = page_soup.findAll("div",{"class":"product-item"})
print(len(containers))
##print(containers[0])
containe = containers[0]
print(containe.a)
##