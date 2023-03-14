# code pour scraper le site du gouvernement UK pour extraire les titres et descriptions des news

#importation des packages/methodes à utiliser
import requests
from bs4 import BeautifulSoup
import csv

#site web à scraper
url='https://www.gov.uk/search/news-and-communications'

#extraction du code source de la page dont l'url est mentionné
page=requests.get(url)

#print(page.content)

#parsing du contenu de la page (variable page) avec BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

'''
Extraction des titres et descriptions utilisent le meme codage et processus,
alors nous allons le mettre comme une fonction extraire_donnees
'''
def extraire_donnees (contenus_extrait):
	resutlat = []
	for contenu in contenus_extrait:
		resutlat.append(contenu.string)
		#print(contenu.string)

	return resutlat

# la variable pour stocker les titres
titres_texte = [] 		

#extraction des titres entre la balise a avec comme class celle specifiee
titres = soup.find_all('a', class_='gem-c-document-list__item-title')
titres_texte = extraire_donnees(titres)

# la variable pour stocker les descriptions
descriptions_texte = [] 

#extraction des descriptions entre la balise p avec comme class celle specifiee
descriptions = soup.find_all('p', class_='gem-c-document-list__item-description')
descriptions_texte = extraire_donnees(descriptions)

#Creation du fichier data.csv
entete = ['Titres', 'Descriptions']
with open('data_uk.csv', 'w') as csv_file:
	#le dialect='unix' permet d'éviter des lignes vides dans le fichier excel
	writer = csv.writer(csv_file, dialect = 'unix', delimiter='|')
	writer.writerow(entete)
	for titre, description in zip(titres_texte, descriptions_texte):
		writer.writerow([titre, description])


