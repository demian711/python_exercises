#!/usr/bin/env python

##################################################
### Simple wikipedia search... just practicing ###
##################################################

import urllib2
from IPython.display import clear_output
from bs4 import BeautifulSoup
array = []

busqueda = str(raw_input('Que queres buscar?: ')).lower()
while True:
    busqueda
    busqueda.replace (" ", "_")
    clear_output()
    try:
        f = urllib2.urlopen('https://es.wikipedia.org/wiki/'+ busqueda)
    except urllib2.HTTPError, err:
        if err.code == 404:
            f = urllib2.urlopen('https://es.wikipedia.org/w/index.php?search='+ busqueda +'&title=Especial%3ABuscar&go=Ir')
            soup = BeautifulSoup(f, 'html.parser')
            print('Nada che, por ahi quisiste decir:')
            print(' ')
            for each_div in soup.findAll('div',{'class':"mw-search-result-heading"}):
                for link in each_div.find_all('a'):
                    print(link.get('title'))
            busqueda = raw_input("Que quisiste decir?(copia y pega tal cual figura en la lista): ").lower()
            clear_output()
    else:
        soup = BeautifulSoup(f, 'html.parser')
        for link in soup.find_all('p'):
            print(link.get_text())
        busqueda = str(raw_input('Que queres buscar?: ')).lower()
        clear_output()

