# -*- coding: utf-8 -*-
# AUTEUR : Gwénaël Richomme
# Date : 16 septembre 2011
###########################################
# Exemple de manipulations de fichier csv

import csv

def exemple( nom_fichier_csv ):
   fichier = open(nom_fichier_csv,"r")
   cr = csv.reader( fichier,delimiter="|")
   for row in cr:
      print(row)
      print(len(row))
      texte = str(len(row)) + " : "
      for i in range(len(row)):
         texte = texte + " | "+ row[i]
         print (row[i])
      print("Texte est : " + texte )
   fichier.close()
'''
   fichier = open("quelques_entiers.csv", 'w')
   cw = csv.writer(fichier, delimiter=';')
   for i in range(0, 3):
      cw.writerow( [i, i+1, i+2] )
   fichier.close()
'''
exemple("essai.csv")