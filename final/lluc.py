#!/usr/bin/python3

from fabulous import utils, image
import requests
import random
import webbrowser
from textual.app import App, ComposeResult
from textual.widgets import Button, Label

class Ricky(App):
	CSS_PATH = "estilo.css"

	def compose(self) -> ComposeResult:
		self.close_button = Button("Salir", id ="close")
		self.option_button1 = Button("Personaje Random", id = "RandomImage")
		self.option_button2 = Button("Buscar Personaje", id = "SearchImage")
		self.option_button3 = Button("Episodio Random", id = "RandomEpisodio")
		self.option_button4 = Button("Buscar Episodio", id = "SearchEpisodio")
		self.option_button5 = Button("Localizacion Random", id = "RandomLocate")
		self.option_button6 = Button("Buscar Localizacion", id = "SearchLocation")
		yield Label("Bienvendio a la Api Rick and Morty", id="title")
		yield self.option_button1
		yield self.option_button2
		yield self.option_button3
		yield self.option_button4
		yield self.option_button5
		yield self.option_button6
		yield self.close_button


	########################### Random Character ###########################################
	def PersonajeRandom(self):
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
		print("El id de este personaje es: " +str(id))
		print("La especie del personaje es: " +str(specie))
		print("El genero del personaje es: " +str(gender))
		print("Este personaje es del planeta: " +str(origen_name))

	######################## Filter Characters #############################################

	def BuscarPersonaje(self):
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
		print("El id del personaje es: " +str(id)+"\n")
		print("El nombre del personaje es: " +str(name)+"\n")
		print("La especie del personaje es: " +str(specie)+"\n")
		print("El genero del personaje es: " +str(gender)+"\n")
		print("Este personaje es del planeta: " +str(origen_name)+"\n")

	######################## Episode random #############################################

	def EpisodioRandom(self):
		numero_aleatorio = random.randint(1, 51)

		api_url = "https://rickandmortyapi.com/api/episode/"+str(numero_aleatorio)
		response = requests.get(api_url)

		info = (response.json())
		id = (info["id"])
		name = (info["name"])
		create = (info["created"])
		characters= info["characters"]

		print("El id del episodio es: "+str(id)+"\n")
		print("El nombre del episodio es: "+str(name)+"\n")
		print("El episodio fue creado el: " +str(create)+"\n")

		print("Los personajes que salen en este episodio son: ")
		for character_url in characters:
			response = requests.get(character_url)
			character_info = response.json()
			character_id = character_info["name"]
			print(character_id)

	######################## Filtrar Episodio #############################################

	def BuscarEpisodio(self):
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

		print("El id del episodio es: "+str(id)+"\n")
		print("El nombre del episodio es: "+str(name)+"\n")
		print("El episodio fue creado el: " +str(create)+"\n")

		print("Los personajes que salen en este episodio son: ")
		for character_url in characters:
			response = requests.get(character_url)
			character_info = response.json()
			character_id = character_info["name"]
			print(character_id)

		

	######################## Random Location #############################################

	def RandomLocation(self):
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

		print("El id de la localizaion es: "+str(id)+"\n")
		print("El nombre de la localizacion es: "+str(name)+"\n")
		print("La localizacion fue creada el: " +str(create)+"\n")
		print("La localizacion es de tipo: "+str(type)+"\n")
		print("La localizacion esta en la dimension: "+str(dimension)+"\n")

		print("Los personajes que salen en este episodio son: ")
		for residents_url in residents:
			response = requests.get(residents_url)
			resident_info = response.json()
			resident_id = resident_info["name"]
			print(resident_id)

		######################## Filtrar Localizacion #############################################

	def BuscarLocalizacion(self):
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

		print("El id de la localizaion es: "+str(id)+"\n")
		print("El nombre de la localizacion es: "+str(name)+"\n")
		print("La localizacion fue creada el: " +str(create)+"\n")
		print("La localizacion es de tipo: "+str(type)+"\n")
		print("La localizacion esta en la dimension: "+str(dimension)+"\n")

		print("Los residentes de esta localizacion son: ")
		for residents_url in residents:
			response = requests.get(residents_url)
			resident_info = response.json()
			resident_id = resident_info["name"]
			print(resident_id)
        
	def on_mount(self) -> None:
		self.screen.styles.background = "darkblue"
		self.close_button.styles.background = "red"
 
	def on_button_pressed(self, event: Button.Pressed) -> None:
		button_id = event.button_id

		if button_id == "RandomImage":
			self.PersonajeRandom()

		if button_id == "SearchImage":
			self.BuscarPersonaje

		if button_id == "RandomEpisodio":
			self.EpisodioRandom()

		if button_id == "SearchEpisodio":
			self.BuscarEpisodio()

		if button_id == "RandomLocate":
			self.RandomLocation()

		if button_id == "SearchLocation":
			self.BuscarLocalizacion()

		if button_id == "close":
			self.exit(event.button_id)


if __name__ == "__main__":
	app = Ricky()
	app.run()
	


	#while True:

		#print("\n Si escribes 1 puedes hacer un personaje random, 2 Filtrar un personaje por su nombre")
		#print("3 Per bucar un episodio al azar, 4 para filtrar por un episodio en concreto")
		#print("5 para generar una localizacion random, 6 para buscar una localizacion y 7 para salir\n")
		#opcio = int(input("¿Que quieres hacer?\n"))
		#if opcio == 1:
		#	PersonajeRandom()
		#elif opcio == 2:
		#	BuscarPersonaje()
		#elif opcio == 3:
		#	EpisodioRandom()
		#elif opcio == 4:
		#	BuscarEpisodio()
		#elif opcio == 5:
		#	RandomLocation()
		#elif opcio == 6:
		#	BuscarLocalizacion()
		#elif opcio == 7:
		#	break

