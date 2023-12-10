from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import json
from .models import Resource

# Create your views here.

def status(request):
    return HttpResponse("Map app running")

def index(request, category=None, order='name'):
    template = loader.get_template('checklist.html')
    context = {
        'resources' : Resource.objects.filter(category__in=category).order_by(order),
        'progress' : Resource.getProgress(category)
    }
    return HttpResponse(template.render(context,request))

def menu(request):
    from .urls import urlpatterns
    template = loader.get_template('menu.html')
    context = {
        'urlpatterns' : urlpatterns
    }
    return HttpResponse(template.render(context,request))

def update_state(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        id = data.get('id')
        state = data.get('state')

        resource = Resource.objects.get(id=id)

        resource.found = state
        resource.save()
        
        return HttpResponse(json.dumps({'success': True}), content_type='application/json')
    return HttpResponse(json.dumps({'success': False}), content_type='application/json')

import requests
from bs4 import BeautifulSoup

def obtener_datos_tabla(url, id_tabla, ):
    # Encabezados simulando el comportamiento de un navegador
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Realiza la solicitud GET a la URL con los encabezados
    response = requests.get(url, headers=headers)

    # Verifica si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Parsea el contenido HTML de la página con BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Encuentra la tabla por su id
        tabla = soup.find('table', {'id': id_tabla})

        # Verifica si se encontró la tabla
        if tabla:
            # Extrae los datos de la tabla
            datos = []
            filas = tabla.find_all('tr')
            for fila in filas[1:]:
                celdas = fila.find_all(['th', 'td'])
                fila_datos = []

                for index, celda in enumerate(celdas):
                    if index == 0:
                        fila_datos.append(False)
                    elif index == 3:
                        # Si la celda contiene una etiqueta <a>, extrae el enlace
                        enlace = celda.find('a')
                        if enlace:
                            fila_datos.append(enlace.get('href'))
                        else:
                            fila_datos.append(None)  # Puedes ajustar esto según tus necesidades si no hay enlace
                    elif index == 2:
                        fila_datos.append(str(celda).replace('<td class="info">', '').replace('</td>', ''))
                    else:
                        # Copia el contenido de la celda tal cual
                        fila_datos.append(celda.text.strip())

                datos.append(fila_datos)

            return datos
        else:
            print(f"No se encontró una tabla con id '{id_tabla}' en la página.")
    else:
        print(f"Error al obtener la página. Código de estado: {response.status_code}")
def load_data_func(request):
    url_ejemplo = 'https://mapgenie.io/elden-ring/guides/ashes-of-war'
    id_tabla_ejemplo = 'items-table'

    datos_tabla = obtener_datos_tabla(url_ejemplo, id_tabla_ejemplo)

    if datos_tabla:
        for item in datos_tabla:
            Resource(found=item[0], location='', name=item[1], 
                    category='Ash of war', region=item[3], info=item[2]).save()
    return HttpResponse("OK")

def getTableData(url,table_id):
    import requests
    from bs4 import BeautifulSoup
    # Encabezados simulando el comportamiento de un navegador
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Realiza la solicitud GET a la URL con los encabezados
    response = requests.get(url, headers=headers)

    # Verifica si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Parsea el contenido HTML de la página con BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Encuentra la tabla por su id
        tabla = soup.find('table', {'id': table_id})

        # Verifica si se encontró la tabla
        if tabla:
            # Extrae los datos de la tabla
            filas = tabla.find_all('tr')
            datos = []
            for fila in filas[1:len(filas)-1]:
                celdas = fila.find_all(['th', 'td'])
                fila_datos = []

                for index, celda in enumerate(celdas):
                    if index == 0:
                        fila_datos.append(False)
                    elif index == 2:
                        fila_datos.append(str(celda).replace('<td class="mapify-links">', '').replace('</td>', ''))
                    elif index == 3:
                        # Si la celda contiene una etiqueta <a>, extrae el enlace
                        enlace = celda.find('a')
                        if enlace:
                            fila_datos.append(enlace.get('href'))
                        else:
                            fila_datos.append(celda.text.strip())
                    else:
                        fila_datos.append(celda.text.strip())

                datos.append(fila_datos)
            return datos
        else:
            print(f"No se encontró una tabla con id '{table_id}' en la página.")
    else:
        print(f"Error al obtener la página. Código de estado: {response.status_code}")


def load_data(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        id_table = request.POST.get('id_table')
        data = getTableData(url, id_table)
        for item in data:
            #print(item)
            Resource(found=item[0], location=item[3], name=item[1], 
                    category='Crystal Tears', region='', info=item[2]).save()
        return HttpResponse("OK")
    else:
        template = loader.get_template('load_data.html')
        context = {
        }
        return HttpResponse(template.render(context,request))
