#tutorial #7: go

Go es un lenguaje de programación concurrente y compilado inspirado en la sintaxis de C, que intenta ser dinámico como Python y con el rendimiento de C o C++

como es la conbinacion de los 2 se de describe como un lenguaje de programación compilado, concurrente, imperativo, estructurado, orientado a objetos y con recolector de basura(trabaja mejor el cache en otro tipo de cosas) que de momento es soportado en diferentes tipos de sistemas UNIX, incluidos Linux, FreeBSD, Mac OS X y Plan 9

Ventajas : 
	-multiplataforma
	-sintaxis muy simplificada
	-gestion automatica de memoria
	-formato de codigo unitario
	-importacion mas sencilla
	-admite diferente valores de devolucion para funciones y metodos
	-correcion de codigo automatizada 
	-concurrencia
	-extensa biblioteca estandar, sobre todo para http y tareas de red
	
	
	
	
	
	
	
	
desventajas:
	-no soporta tipos genéricos
	-orientado a objetos
	-soporte ampliable de IDE
	-oferta limitada de bibliotecas y paquetes externos
	-cambiar de lenguajes clasicos orientados como java o C++ requiere esfuerzo
	-hasta ahora pocos manuales y expertos

para descargarlo lo haremos en esta pagina

https://golang.org/dl/

elijimos la version en la seccion de "featured download"

y luego vamos a la carpeta contenedora y usamos 

la version depende de la que hayas descargado
```
sudo tar -C /usr/local -xzf go1.15.6.linux-amd64.tar.gz
```
luego vamos 

/usr/local

ejecutamos 

```
sudo chown -R $USER:$USER go
```
luego vamos a home

```
cd $HOME
```

modificamos .profile

se puede usar vim o nano

pero en la ultima linea insertar
```
export PATH=$PATH:/usr/local/go/bin
```

luego hacemos

```
source .profile
```
 
y veremos si go esta instalado

```
go version
```

luego vamos a /home 
para crear el espacio de trabajo

```
mkdir bin
mkdir pkg
mkdir scr
```
en /scr
```
mkdir github.com
```

```
mkdir TuNombreEnGithub
```

volvemos a /home

modificamos .profile denuevo con nano o vim
```
export GOPATH=$HOME/go
export PATH=$PATH:$GOPATH
```

```
source .profile
```

por ultimo hacemos 
```
sudo apt install goland
```
```
sudo apt
```

ahora vamos a programar holamundo

**hello.go**:
```
	package main

	import "fmt"

	func main(){
		fmt.Println("hola mundo!")
	}	
```




