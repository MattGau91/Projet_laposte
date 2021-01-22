# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np

##################################### Question 1 #####################################################
url="https://simplonco.github.io/nanterre-p10-devdata/s1/python/projet/connexion.log"
df = pd.read_csv(url, sep = ";",encoding='ANSI',names=["Ip","Noms","Date"])

print(df)

utilisateur_f=open("utilisateurs.txt","a")
f=open("connexion.txt","r")
line=f.readlines()
for i in line:
    print(i.split(";")[1])
    utilisateur_f.write(i.split(";")[1]+"\n")

f.close()
utilisateur_f.close()
   
##################################### Question 2 #####################################################

for i in line:
    if int(i.split(";")[2][-6:-4])<8 or int(i.split(";")[2][-6:-4])>19:
        print(i.split(";")[0:2])
       
##################################### Question 3 #####################################################

ip_dangereuses=open('warning.txt',"r")
line2=ip_dangereuses.readlines()

liste_suspects = []
f=open("connexion.txt","r")
line=f.readlines()
for i in line:
    for c in line2:
        if i.split(";")[0]==c[:-1]:
            #print(i.split(";")[0])
            liste_suspects.append(i.split(";")[1])
print(liste_suspects)

fileoutput=open("suspects.txt","w")

last_list=set(liste_suspects)
for i in last_list:
    fileoutput.write(i+" "+str(liste_suspects.count(i))+"\n")
    print(i+";"+str(liste_suspects.count(i)))
    
ip_dangereuses.close()
