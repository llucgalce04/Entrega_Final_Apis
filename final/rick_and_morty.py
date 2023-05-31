#!/usr/bin/python3

from fabulous import utils, image
import requests
import random
import webbrowser
from colorama import Fore, Style

########################### Random Character ###########################################
def PersonajeRandom():
	numero_aleatorio = random.randint(1, 826)

	api_url = "https://rickandmortyapi.com/api/character/"+str(numero_aleatorio)

	response = requests.get(api_url)

	info = (response.json())

	name = (info["name"])
	url = (info["image"])
	id = (info["id"])
	specie = info["species"]
	gender = info["gender"]
	origen_list = info["origin"]
	origen_name = origen_list["name"]
	episode_large = len(info["episode"])
	
	
	print("Imagen de "+str(name))
	nombre_local_imagen = (name + ".jpeg")
	imagen = requests.get(url).content

	with open(nombre_local_imagen, 'wb') as handler:
		handler.write(imagen)

	img = image.Image(name + ".jpeg")
	webbrowser.open(name + ".jpeg")
	print("El id de este personaje es: "+Fore.GREEN +str(id))
	print(Style.RESET_ALL)
	print("La especie del personaje es: "+Fore.RED +str(specie))
	print(Style.RESET_ALL)
	print("El genero del personaje es: "+Fore.BLUE +str(gender))
	print(Style.RESET_ALL)
	print("Este personaje es del planeta: "+Fore.YELLOW +str(origen_name))
	print(Style.RESET_ALL)

######################## Filter Characters #############################################

def BuscarPersonaje():
	nombre = input("Escribe el nombre del pibe: \n")
	nombre_mas_encode = str("?name=")+ nombre

	api_url = "https://rickandmortyapi.com/api/character/" + str(nombre_mas_encode)
	response = requests.get(api_url)
	info = response.json()

	pages = info["info"]["pages"]
	page_prin = int(input("Hay " + str(pages) + " paginas, elige el número de la que quieras ir: \n"))
	page_prin_mas_encode = "?page="+str(page_prin)
	nombre_mas_encode = "&name=" + nombre

	api_url_mas_page = "https://rickandmortyapi.com/api/character/" + str(page_prin_mas_encode) + str(nombre_mas_encode)
	response_2 = requests.get(api_url_mas_page)
	info_2 = response_2.json()
	count = len(info_2["results"])
	possible = int(input("Hay " + str(count) + " respuestas, elige el número del que quieres seleccionar: \n"))

	id = info_2['results'][possible]['id']
	specie = info_2['results'][possible]['species']
	gender = info_2['results'][possible]['gender']
	name = info_2['results'][possible]['name']
	foto = info_2['results'][possible]['image']
	origen_list = info_2['results'][possible]["origin"]
	origen_name = origen_list["name"]

	print("Fotito del personaje: \n")
	nombre_local_imagen = (name + ".jpeg")
	imagen = requests.get(foto).content

	with open(nombre_local_imagen, 'wb') as handler:
		handler.write(imagen)

	img = image.Image(name + ".jpeg")
	webbrowser.open(name + ".jpeg")
	print("El id del personaje es: "+Fore.GREEN +str(id)+"\n")
	print(Style.RESET_ALL)
	print("El nombre del personaje es: "+Fore.RED +str(name)+"\n")
	print(Style.RESET_ALL)
	print("La especie del personaje es: "+Fore.BLUE +str(specie)+"\n")
	print(Style.RESET_ALL)
	print("El genero del personaje es: "+Fore.YELLOW +str(gender)+"\n")
	print(Style.RESET_ALL)
	print("Este personaje es del planeta: "+Fore.LIGHTWHITE_EX +str(origen_name)+"\n")
	print(Style.RESET_ALL)

######################## Episode random #############################################

def EpisodioRandom():
	numero_aleatorio = random.randint(1, 51)

	api_url = "https://rickandmortyapi.com/api/episode/"+str(numero_aleatorio)
	response = requests.get(api_url)

	info = (response.json())
	id = (info["id"])
	name = (info["name"])
	create = (info["created"])
	characters= info["characters"]

	print("El id del episodio es: "+Fore.GREEN+str(id)+"\n")
	print(Style.RESET_ALL)
	print("El nombre del episodio es: "+Fore.RED+str(name)+"\n")
	print(Style.RESET_ALL)
	print("El episodio fue creado el: "+Fore.BLUE +str(create)+"\n")
	print(Style.RESET_ALL)

	print(Fore.RED +"Los personajes que salen en este episodio son: ")
	print(Style.RESET_ALL)
	for character_url in characters:
		response = requests.get(character_url)
		character_info = response.json()
		character_id = character_info["name"]
		print(character_id)

######################## Filtrar Episodio #############################################

def BuscarEpisodio():
	print("Escribe aqui el episodio un ejemplo:\n")
	print("Quieres buscar el episodio 1 de la temporada 1 se escribiria así: S01E01\n")
	episode_in = input("Ahora te toca a tí escribe que episodio quieres buscar: \n")

	episode_mas_encode = "?episode="+str(episode_in)
	

	api_url = "https://rickandmortyapi.com/api/episode/"+str(episode_mas_encode)

	response = requests.get(api_url)
	info = (response.json())
	

	id = info["results"][0]["id"]
	name = info["results"][0]["name"]
	create = info["results"][0]["created"]
	characters= info["results"][0]["characters"]

	print("El id del episodio es: "+Fore.GREEN+str(id)+"\n")
	print(Style.RESET_ALL)
	print("El nombre del episodio es: "+Fore.RED+str(name)+"\n")
	print(Style.RESET_ALL)
	print("El episodio fue creado el: "+Fore.BLUE +str(create)+"\n")
	print(Style.RESET_ALL)

	print(Fore.RED +"Los personajes que salen en este episodio son: ")
	print(Style.RESET_ALL)
	for character_url in characters:
		response = requests.get(character_url)
		character_info = response.json()
		character_id = character_info["name"]
		print(character_id)

	

######################## Random Location #############################################

def RandomLocation():
	numero_aleatorio = random.randint(1, 126)
	api_url = "https://rickandmortyapi.com/api/location/"+str(numero_aleatorio)

	response = requests.get(api_url)
	info = (response.json())
	id = (info["id"])
	name = (info["name"])
	type = (info["type"])
	dimension = info["dimension"]
	residents = info["residents"]
	create = info["created"]

	print("El id de la localizaion es: "+Fore.GREEN+str(id)+"\n")
	print(Style.RESET_ALL)
	print("El nombre de la localizacion es: "+Fore.RED+str(name)+"\n")
	print(Style.RESET_ALL)
	print("La localizacion fue creada el: "+Fore.BLUE +str(create)+"\n")
	print(Style.RESET_ALL)
	print("La localizacion es de tipo: "+Fore.YELLOW+str(type)+"\n")
	print(Style.RESET_ALL)
	print("La localizacion esta en la dimension: "+Fore.LIGHTWHITE_EX+str(dimension)+"\n")
	print(Style.RESET_ALL)

	print(Fore.RED +"Los personajes que salen en este episodio son: ")
	print(Style.RESET_ALL)
	for residents_url in residents:
		response = requests.get(residents_url)
		resident_info = response.json()
		resident_id = resident_info["name"]
		print(resident_id)

	######################## Filtrar Localizacion #############################################

def BuscarLocalizacion():
	nombre_locate = input("Escribe aqui el nombre de la localizacion: \n")
	location_mas_encode = "?location="+str(nombre_locate)

	api_url = "https://rickandmortyapi.com/api/location/"+str(location_mas_encode)

	response = requests.get(api_url)
	info = (response.json())
		

	id = info["results"][0]["id"]
	name = info["results"][0]["name"]
	create = info["results"][0]["created"]
	type = info["results"][0]["type"]
	dimension = info["results"][0]["dimension"]
	residents = info["results"][0]["residents"]

	print("El id de la localizaion es: "+Fore.GREEN+str(id)+"\n")
	print(Style.RESET_ALL)
	print("El nombre de la localizacion es: "+Fore.RED+str(name)+"\n")
	print(Style.RESET_ALL)
	print("La localizacion fue creada el: "+Fore.BLUE +str(create)+"\n")
	print(Style.RESET_ALL)
	print("La localizacion es de tipo: "+Fore.YELLOW+str(type)+"\n")
	print(Style.RESET_ALL)
	print("La localizacion esta en la dimension: "+Fore.LIGHTWHITE_EX+str(dimension)+"\n")
	print(Style.RESET_ALL)

	print(Fore.RED +"Los residentes de esta localizacion son: ")
	print(Style.RESET_ALL)
	for residents_url in residents:
		response = requests.get(residents_url)
		resident_info = response.json()
		resident_id = resident_info["name"]
		print(resident_id)

print(Fore.CYAN +'''

 $$$$$$\  $$$$$$$\ $$$$$$\       $$$$$$$\  $$$$$$\  $$$$$$\  $$\   $$\        $$$$$$\  $$\   $$\ $$$$$$$\        $$\      $$\  $$$$$$\  $$$$$$$\ $$$$$$$$\ $$\     $$\ 
$$  __$$\ $$  __$$\\_$$  _|      $$  __$$\ \_$$  _|$$  __$$\ $$ | $$  |      $$  __$$\ $$$\  $$ |$$  __$$\       $$$\    $$$ |$$  __$$\ $$  __$$\\__$$  __|\$$\   $$  |
$$ /  $$ |$$ |  $$ | $$ |        $$ |  $$ |  $$ |  $$ /  \__|$$ |$$  /       $$ /  $$ |$$$$\ $$ |$$ |  $$ |      $$$$\  $$$$ |$$ /  $$ |$$ |  $$ |  $$ |    \$$\ $$  / 
$$$$$$$$ |$$$$$$$  | $$ |        $$$$$$$  |  $$ |  $$ |      $$$$$  /        $$$$$$$$ |$$ $$\$$ |$$ |  $$ |      $$\$$\$$ $$ |$$ |  $$ |$$$$$$$  |  $$ |     \$$$$  /  
$$  __$$ |$$  ____/  $$ |        $$  __$$<   $$ |  $$ |      $$  $$<         $$  __$$ |$$ \$$$$ |$$ |  $$ |      $$ \$$$  $$ |$$ |  $$ |$$  __$$<   $$ |      \$$  /   
$$ |  $$ |$$ |       $$ |        $$ |  $$ |  $$ |  $$ |  $$\ $$ |\$$\        $$ |  $$ |$$ |\$$$ |$$ |  $$ |      $$ |\$  /$$ |$$ |  $$ |$$ |  $$ |  $$ |       $$ |    
$$ |  $$ |$$ |     $$$$$$\       $$ |  $$ |$$$$$$\ \$$$$$$  |$$ | \$$\       $$ |  $$ |$$ | \$$ |$$$$$$$  |      $$ | \_/ $$ | $$$$$$  |$$ |  $$ |  $$ |       $$ |    
\__|  \__|\__|     \______|      \__|  \__|\______| \______/ \__|  \__|      \__|  \__|\__|  \__|\_______/       \__|     \__| \______/ \__|  \__|  \__|       \__| ''')
print(Style.RESET_ALL)


while True:

	print(Fore.MAGENTA+"\n Si escribes 1 puedes hacer un personaje random, 2 Filtrar un personaje por su nombre")
	print("3 Per bucar un episodio al azar, 4 para filtrar por un episodio en concreto")
	print("5 para generar una localizacion random, 6 para buscar una localizacion y 7 para salir\n")
	print(Style.RESET_ALL)

	opcio = int(input("¿Que quieres hacer?\n"))
	if opcio == 1:
		PersonajeRandom()
	elif opcio == 2:
		BuscarPersonaje()
	elif opcio == 3:
		EpisodioRandom()
	elif opcio == 4:
		BuscarEpisodio()
	elif opcio == 5:
		RandomLocation()
	elif opcio == 6:
		BuscarLocalizacion()
	elif opcio == 7:
		break

