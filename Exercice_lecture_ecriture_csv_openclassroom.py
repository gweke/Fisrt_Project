import csv

noms = []
salaires = []
multipicateur = 15
entete = ['Nom', 'Salaire']
i = 0

with open('input.csv', 'r') as csv_file:
	reader = csv.reader(csv_file, delimiter=',')
	for row in reader: 
		#permet de sauter la première ligne, qui est l'entete
		if i != 0:
			#print(row[0])
			#print(int(row[1]) * multipicateur)
			noms.append (row[0])
			salaires.append(int(int(row[1]) * multipicateur))
		else:
			i = i + 1


with open('output.csv', 'w') as csv_output_file:
	writer = csv.writer(csv_output_file, dialect='unix', delimiter=',')
	writer.writerow(entete)
	for nom, salaire in zip(noms, salaires):
		writer.writerow([nom, salaire])



