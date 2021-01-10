
#tutorial #6: git y github avanzado

git es un servicio de control de versiones.
git es un programa que sirve para versionar codigo
si tu tienes un archivo y quieres hacerle modificaciones
no puedes mantener estas versiones,o si hay mucha gente trabajando en el mismo codigo

entonces git puedes ver si alguien le hace un cambio al codigo ver si lo aceptas o no,si no funciona, vuelves a la version anterior

para instalar git 

vas a la pagina
 

 **https://git-scm.com**

 muchas distribuciones de linux ya lo tienen instalado pero si no lo tienes aqui esta la pagina

 para ver si tienes git instalado 

```
git version
```
esto te muestra la version por lo menos a mi me muestra **git version 2.7.4**

lo primero que hacemos es poner nuestro nombre y mail
es una buena practica que diga tu nombre cuando vayas a
configurar codigo, para que cuando alguien vea el codigo vea quien hizo
ese cambio 

```
git config --global user.name "nombre apellido"
```

```
git config --global user.email "mail@correo"
```

para ver si estas bien 
```
git config --list
```
 para empezar a usar git les entrego este ejemplo en la carpeta

 crean una carpeta ejemplo 

 dentro de ella hay un **Dockerfile**:
```
 	FROM php:7.4-apache
```



 y tambien contiene un archivo php llamado **index.php**:
```
 
 	<?php

 	echo "Hola con git"

 	?>
```
ahora para convertir la carpeta en un repositorio hacemos 
```
git init
```
si usamos 

```
ls -alh
```
 puedes ver que se creo el repositorio git, **este repositorio contiene tdoo no lo borres**

si quieres hacer un archivo que solo lo veas tu usamos gitignore

creamos un archivo

por ejemplo **secreto.txt**

no importa lo que tenga luego creamos un archivo

**.gitignore** que contiene solo esto:


```
	secreto.txt	
```

ahora tenemos que tener en cuenta que git tiene 3 diferentes etapas 
podemos estar en 
**working dir**: que seria donde estas haciedno cambios en ut codigo
**staging**: lugar donde puedes traer el codigo del repositorio para llevarlo a working dir
**repositorio**:aqui estaria todo el historial y todo el codigo completo 

si hacemos 

```
git status 
```
podemos ver el estado de los archivos de la carpeta 

si lo hacemos nos dice que estamos en branch master

no commits yet (no se ha hecho ningun commit que es un comando que haremos mas adelante)

y tenemos los 3 archivos que esta untrack osea no estan en el staging

para esto usamos

```
git add -A 
```

si hacemos
```
git status 
```


si queremos borrar un archivo de esta carpeta git que no queriamos cuando hicimos add usamos
```
git rm --cached nombrearchivo
``` 

podemos ver los cambios pero todavia sale que no ha habido commits
como ya les hicimos add podemos hacerle commit

que es commit ? es poner un comentario(es buena practica poner comentarios para saber que hiciste y porque estas subiendo este archivo) y subir estos archivos al repositorio
```
git commit -m "agregando mis primeros archivos"
 
```
en la consola deberia salir algo asi

 create mode 100644 .gitignore
 create mode 100644 Dockerfile
 create mode 100644 index.php
si hacemos 
```
git status 
```
podemos ver que estos archivos ya no estan ni en working dir ni en staging
sino que esta en el repositorio, no esque se hayan borrado solo que git ya sabe que estan en el repositorio los archivos siguen ahi en la carpeta

si hacemos 
```
git log
```
podemos ver el historial de todos los commit 

lo mejor que podemos hacer con git es usar el repositorio de alguien para uno trabajar en ello usaremos el del tutorial 1

para esto usaremos la pagina 

**https://github.com**

ya que es gratis

para hacer git clone buscamos en git hub un repositorio en este caso

**https://github.com/matthieuvernier/INFO229_2020**
buscaoms donde dice code or download y buscamos https


```
git clone https://github.com/matthieuvernier/INFO229_2020.git
```
podemos usar todos los comandos anteriores para revisar el log y el status 

si queremos cambiar algo y no recordamos que cambiamos podemos usar

```
git diff 
```
loque nos mostrara la diferencia de lo nuestro con el repositorio

una buena practica para empezar a hacer el codigo es hacer
```
git pull origin master
```
ya que nos mostrara la version final de el codigo

finalmente si queremos subir esta carpeta que es un git usamos

```
git push origin master
```
si varias personas estan trabajando en un archivo lo mejor es usar branch para evitar chocarse


```
git branch minueva
```
nos vamos a la nueva branch

```
git checkout minueva
```
y podemos usar los comandos anteriores en esta branch

si queremos ver las branch
```
git branch
``` 

si hicieramos cambios en esta branch tendriamos que hacer

```
git push -u origin minueva
```

ahora si quisieramos poner todo lo que pusimos en la branch en el repositrio master

```
git checkout master
```
```
git pull origin master
```
y finalmente 
```
git branch --merged
```
```
git merge minueva
```

y esta branch quedara con master

```
git push origin master
```

y con esto se sube

recuerda borrar las branch que ya usaste
```
git push origin --delete minueva
```
```
git branch -d minueva
```

resumen

hacemos esto para prueba
```
git checkout master
```

```
git pull origin master
```

```
git branch otranueva
```
```
git checkout otranueva
```
modificamos codigo

```
git add -A
```

```
git commit -m "agregando cosas"
```

```
git push origin otranueva
```

```
git checkout master
```

```
git branch --merged
```

```
git merge otranueva
```

```
git origin origin master
```












