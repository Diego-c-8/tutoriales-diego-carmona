
# Tutorial #9: WEBscrpaing con python

El web scraping es una técnica que sirve para extraer información de páginas web de forma automatizada. Si traducimos del inglés su significado vendría a significar algo así como “escarbar una web”.

esta funcion es muy importante para ser analista de data debidoa que todo el internet se vuelve tu entorno de trabajo 

lo primero que haremos es instalar el paquete 

```
pip install bs4
```


en lo personal a mi me gusta la musica asique buscare en una pagina los mejores reproductores de musica baratos

con esto tenemos toda la pagina agregada en mi caso querria buscar los productos junto con descripcciones pero esto requererira mas codigo en principio solo mostrare un poco de la pagina

con el siguiente codigo
```
	from urllib.request import urlopen as uReq
	from bs4 import BeautifulSoup as soup
	##aqui importamos las librerias necesarias##
	my_url = 'https://tienda.mediaplayer.cl/amplificadores-de-audifonos-dac/fiio.html'
	##aqui agregue esta pagina, puede que algunas paginas no se puedan debido a sus parametros de seguridad, pero si se investiga mas se puede hacer algo##

	uClient = uReq(my_url)
	page_html = uClient.read()
	uClient.close()
	##leemos y cerramos la pagina con este comando##

	page_soup = soup(page_html,"html.parser")
	##aqui tenemos toda la data##

	containers = page_soup.findAll("div",{"class":"product-item"})
	##buscamos data en especificosi inspeccionamos la pagina podemos encontrar en en httml
	cosas que dicen class, entonces como es una pagina de venta yo quiero el nomnre y el precio ##


	print(len(containers))
	##aqui revisas si containers agrego lo que querias esto lo pone en una lista##

	print(containers[0])
	containe = containers[0]
	print(containe.a)
	##dentro de container si encontramos a, que nos muestra el nombre del producto y la pagina del producto 0 ##
```







