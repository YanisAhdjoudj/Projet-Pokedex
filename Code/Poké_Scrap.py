# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 19:26:10 2020

@author: Yanis
"""
#J'importe les modules nécessaires
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

#J'indique l'endroit ou est situé le web-driver dans mon PC et je l'éxecute
#j'initialise aussi la fonction ait
chrome_path=r"C:\Users\Yanis\Documents\Cours\Master\Master 1 Econometrie statistique\M1-S1\Python\Scrapping selenium\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
wait = WebDriverWait(driver, 10)
#J'indique ici toutes les listes de variables qui me serviront

Noms_list=[]
Noms_anglais_List=[]
Types_list=[]
Catégories_list=[]
Taille_list=[]
Poids_list=[]
Talents_list=[]
Groupe_oeuf_list=[]
Taux_de_capture_list=[]
PV_list=[]
Attaque_list=[]
Défense_list=[]
Attaque_spé_list=[]
Défense_spé_list=[]
Vitesse_list=[]
Spécial_list=[]
Somme_des_statistiques_de_base_list=[]
Moyenne_des_statistiques_de_base_list=[]

i=0

#je demande ensuite  au driver d'acceder a la page du pokédex de poképédia
driver.get("https://www.pokepedia.fr/Bulbizarre")

while i<890:
    
       Nom=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#firstHeading"))).text
       Noms_list.append(Nom)
       
       Nom_anglais=driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[2]/tbody//th[contains(text(), "Nom anglais" )]/following-sibling::td').text
       Noms_anglais_List.append(Nom_anglais)
       
       Type1=driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[2]/tbody//a[contains(@title, "Type")]/following::td/a').get_attribute("title")[:-7]
       try:
           Type2=driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[2]/tbody//a[contains(@title, "Type")]/following::td/a[2][contains(@title, "type")]').get_attribute("title")[:-7]
           Types_list.append([Type1,Type2])
       except:
           Types_list.append(Type1)
       
       
       Catégorie=driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[2]/tbody//a[contains(@href, "Famille")]/following::td').text
       Catégories_list.append(Catégorie)
        
       Taille=driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[2]/tbody//a[contains(@title, "Liste des Pokémon par taille")]/following::td').text
       if Taille[4]== "m" :
           Taille_list.append(Taille[:4])
       else:
          Taille_list.append(Taille[:5])
       
       Poids=driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[2]/tbody//a[contains(@title, "Liste des Pokémon par poids")]/following::td').text
       if Poids[4]=="k":
           Poids_list.append(Poids[:4])
       elif Poids[5]=="k":
           Poids_list.append(Poids[:5])
       elif Poids[6]=="k":
           Poids_list.append(Poids[:6])
       
       Talent1=driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[2]/tbody//a[contains(@href, "Talent")]/following::td/a[1]').text
       try:
           Talent2=driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[2]/tbody//a[contains(@href, "Talent")]/following::td[contains(text(), "1.")]/a[2]').text
           try:
               Talent3=driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[2]/tbody//a[contains(@href, "Talent")]/following::td[contains(text(), "1.")]/a[3]').text
               Talents_list.append([Talent1,Talent2,Talent3])
           except:
               Talents_list.append([Talent1,Talent2])
       except:
           Talents_list.append(Talent1)
           
       
       Groupe_Oeuf1=driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[2]/tbody//a[contains(@title, "Liste des Pokémon par groupe")]/following::td/a').text
       try:
           Groupe_Oeuf2=driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[2]/tbody//a[contains(@title, "Liste des Pokémon par groupe")]/following::td/a[contains(@title, "Catégorie")][2]').text
           Groupe_oeuf_list.append([Groupe_Oeuf1,Groupe_Oeuf2])  
       except:
           Groupe_oeuf_list.append(Groupe_Oeuf1)

       try:
           Taux_de_capture=driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[2]/tbody//a[contains(@title, "Capture des Pokémon")]/following::td').text
           Taux_de_capture_list.append(Taux_de_capture)
       except:
           Taux_de_capture_list.append("nan")
       
      
       PV=driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[contains(@class, "tableaustandard")]/tbody/tr/th[contains(text(), "Statistiques indicatives")]/following::td/a[contains(text(), "PV")]/following::td').text
       PV_list.append(PV)
       
       Attaque=driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[contains(@class, "tableaustandard")]/tbody/tr/th[contains(text(), "Statistiques indicatives")]/following::td/a[contains(text(), "Attaque")]/following::td').text
       Attaque_list.append(Attaque)
       
       Défense=driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[contains(@class, "tableaustandard")]/tbody/tr/th[contains(text(), "Statistiques indicatives")]/following::td/a[contains(text(), "Défense")]/following::td').text
       Défense_list.append(Défense)
       
       Attaque_spé=driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[contains(@class, "tableaustandard")]/tbody/tr/th[contains(text(), "Statistiques indicatives")]/following::td/a[contains(text(), "Attaque Spéciale")]/following::td').text
       Attaque_spé_list.append(Attaque_spé)
       
       Défense_spé=driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[contains(@class, "tableaustandard")]/tbody/tr/th[contains(text(), "Statistiques indicatives")]/following::td/a[contains(text(), "Défense Spéciale")]/following::td').text
       Défense_spé_list.append(Défense_spé)
       
       Vitesse=driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[contains(@class, "tableaustandard")]/tbody/tr/th[contains(text(), "Statistiques indicatives")]/following::td/a[contains(text(), "Vitesse")]/following::td').text
       Vitesse_list.append(Vitesse)
       
       Spécial=driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[contains(@class, "tableaustandard")]/tbody/tr/th[contains(text(), "Statistiques indicatives")]/following::td/a[contains(text(), "Spécial")]/following::td').text
       Spécial_list.append(Spécial)
       
       Somme_des_statistiques_de_base=driver.find_element_by_xpath('//*[@id="mw-content-text"]//a[contains(text(), "Somme des statistiques de base")]/following::td').text
       Somme_des_statistiques_de_base_list.append(Somme_des_statistiques_de_base)        
       
       Moyenne_des_statistiques_de_base=driver.find_element_by_xpath('//*[@id="mw-content-text"]//a[contains(text(), "Moyenne des statistiques de base")]/following::td').text
       Moyenne_des_statistiques_de_base_list.append(Moyenne_des_statistiques_de_base)            

        
       nextpage=wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="mw-content-text"]/div/table[1]/tbody/tr[1]/td[7]')))
       nextpage.click()
       
       i+=1
        
       
       
Pokédex=pd.DataFrame({"Nom": Noms_list,"Nom anglais": Noms_anglais_List,"Types":Types_list,"Catégorie":Catégories_list,"Taille": Taille_list ,"Poids":Poids_list,"Talents": Talents_list, "Groupe Oeuf":Groupe_oeuf_list, "Taux de capture":Taux_de_capture_list, "PV_base":PV_list, "Attaque_base":Attaque_list,"Défense_base":Défense_list, "Attaque_spé_base":Attaque_spé_list, "Défense_spé_base":Défense_spé_list, "Vitesse_base":Vitesse_list, "Spécial_base":Spécial_list, "Moyenne des statistiques de base":Moyenne_des_statistiques_de_base_list, "Somme des statistiques de base":Somme_des_statistiques_de_base_list,})    
Pokédex.index += 1 

print (Pokédex.memory_usage())
Pokédex.info()

Pokédex.to_excel(r'C:\Users\Yanis\Scrapédex.xlsx')
Pokédex.to_csv(r'C:\Users\Yanis\Scrapédex.csv')
Pokédex.to_pickle(r'C:\Users\Yanis\Scrapédex.pkl')

