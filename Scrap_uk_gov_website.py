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


#Extraction des titres et les stocker dans une liste
# la variable pour stocker les titres
titres_texte = [] 		
titres = soup.find_all('a', class_='gem-c-document-list__item-title')
for titre in titres:
	if(titre.string != ''):
		titres_texte.append(titre.string)
		#print(titre.string + '__________')

#Extraction des descriptions et les stocker dans une liste
# la variable pour stocker les descriptions
descriptions_texte = [] 		
descriptions = soup.find_all('p', class_='gem-c-document-list__item-description')
for description in descriptions:
	if description.string != '':
		descriptions_texte.append(description.string)
		#print(description.string + '_________')


#Creation du fichier data.csv
entete = ['Titres', 'Descriptions']
with open('data_uk.csv', 'w') as csv_file:
	writer = csv.writer(csv_file, dialect = 'unix', delimiter='|')
	writer.writerow(entete)
	for titre, description in zip(titres_texte, descriptions_texte):
		writer.writerow([titre, description])


