# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 18:53:17 2020

@author: Yanis
"""

import pandas as pd
import numpy as np

#Nettoyage des donnée et ajout d'information

#J'importe la base de donnée scrappé (en pickle car en csv et en excel cela transformait 
#mes listes (par exemple "types") de str, en simplement une var str 
#par exemple loc[1,"types][1] me renvoyait "p" au lieu de "plante" )
#Je réindex pour partir de 1 car ca correspond au numero du pokemon dans le pokédex
Scrapédex=pd.read_pickle(r'C:\Users\Yanis\Documents\Cours\Master\Master 1 Econometrie statistique\M1-S2\Python\Data\Scrapédex.pkl')
Scrapédex.info()
sp=Scrapédex.copy()

#Pour certaines valeurs le site poképédia ne renseignait pas le groupe oeuf, par chance 
#seul 9 pokémon on ce probleme sur 890, je remplace donc à la main les valeurs
sp["Groupe Oeuf"][882]="Inconnu"
sp["Groupe Oeuf"][880]="Inconnu"
sp["Groupe Oeuf"][866]="Humanoïd"
sp["Groupe Oeuf"][862]="Terrestre"
sp["Groupe Oeuf"][831]="Terrestre"
sp["Groupe Oeuf"][832]="Terrestre"
sp["Groupe Oeuf"][837]="Minéral"
sp.loc[838,"Groupe Oeuf"]="Minéral"
sp.iloc[838,7]="Minéral"
#loc prend en compte le fait que j'ai changer l'index, mais pas iloc


#Ensuite je converti les valeurs numériques en float pour pouvoir faire des calculs
#Pour convertir "Poids", "Taille" et "Moyenne des statistiques de base" en float
# il faut remplacer les virgules par des points
sp["Poids"]=[x.replace(",", ".") for x in sp["Poids"]]
sp["Poids"]=sp["Poids"].astype(np.float64)
sp["Taille"]=[x.replace(",", ".") for x in sp["Taille"]]
sp["Taille"]=sp["Taille"].astype(float)
sp["Moyenne des statistiques de base"]=[x.replace(",", ".") for x in sp["Moyenne des statistiques de base"]]
sp["Moyenne des statistiques de base"]=sp["Moyenne des statistiques de base"].astype(float)

#Pour le reste on peut directement convertir (on convertit tout en float)
sp["PV_base"]=sp["PV_base"].astype(float)
sp["Attaque_base"]=sp["Attaque_base"].astype(float)
sp["Défense_base"]=sp["Défense_base"].astype(float)
sp["Attaque_spé_base"]=sp["Attaque_spé_base"].astype(float)
sp["Défense_spé_base"]=sp["Défense_spé_base"].astype(float)
sp["Vitesse_base"]=sp["Vitesse_base"].astype(float)
sp["Spécial_base"]=sp["Spécial_base"].astype(float)
sp["Somme des statistiques de base"]=sp["Somme des statistiques de base"].astype(float)


#les taux de captures on beaucoup de valeurs manquantes
sp["Taux de capture"].value_counts()
#23 exactement, plus 1 qui a deux valeurs différentes (il faudrat trancher)
#Dans le but d'avoir un data-set complet je vais remplacer les 23 valeurs a la main
#meme si cela est trés fastidieux... j'applique un filtre à ma data-frame pour repérer
#les valeurs manquantes, et je vais chercher sur internet les tx de captures manquants
Masktxdecapt=sp["Taux de capture"]=="—"
sppbcapt=sp[Masktxdecapt]

sp.loc[811,"Taux de capture"]="45"
sp.loc[812,"Taux de capture"]="45"
sp.loc[814,"Taux de capture"]="45"
sp.loc[815,"Taux de capture"]="45"
sp.loc[816,"Taux de capture"]="45"
sp.loc[817,"Taux de capture"]="45"
sp.loc[818,"Taux de capture"]="45"
sp.loc[831,"Taux de capture"]="255"
sp.loc[832,"Taux de capture"]="127"
sp.loc[837,"Taux de capture"]="255"
sp.loc[838,"Taux de capture"]="120"
sp.loc[839,"Taux de capture"]="45"
sp.loc[843,"Taux de capture"]="255"
sp.loc[845,"Taux de capture"]="45"
sp.loc[856,"Taux de capture"]="235"
sp.loc[857,"Taux de capture"]="120"
sp.loc[858,"Taux de capture"]="45"
sp.loc[862,"Taux de capture"]="45"
sp.loc[863,"Taux de capture"]="90"
sp.loc[865,"Taux de capture"]="45"
sp.loc[866,"Taux de capture"]="45"
sp.loc[867,"Taux de capture"]="90"
sp.loc[868,"Taux de capture"]="200"

sp.loc[774,"Taux de capture"]="30"

sp["Taux de capture"]=sp["Taux de capture"].astype(float)




#ensuite on vas controler si on a pas de doublons dans les listes,
#on vas decomposer les listes en plusiseurs colonnes, ainsi type vas engranger type1 
# et type 2, pareil pour Groupe Oeuf et Talents

#Pour les types:

sp["Type1"]=""
sp["Type2"]=""

for t in sp.index:
    if type(sp.loc[t,'Types'])==list:
        sp["Type1"][t]=sp.loc[t,"Types"][0]
        sp["Type2"][t]=sp.loc[t,"Types"][1]
    else:
        sp["Type1"][t]=sp.loc[t,"Types"]
        sp["Type2"][t]=np.nan
        
        

#Pour les groupes oeufs:

sp["GroupeOeuf1"]=""
sp["GroupeOeuf2"]=""

for t in sp.index:
    if type(sp.loc[t,'Groupe Oeuf'])==list:
        sp["GroupeOeuf1"][t]=sp.loc[t,"Groupe Oeuf"][0]
        sp["GroupeOeuf2"][t]=sp.loc[t,"Groupe Oeuf"][1]
    else:
        sp["GroupeOeuf1"][t]=sp.loc[t,"Groupe Oeuf"]
        sp["GroupeOeuf2"][t]=np.nan

#Pour les talents:
        
    
sp["Talent1"]=""
sp["Talent2"]=""
sp["Talent3"]=""

for t in sp.index:
    if type(sp.loc[t,'Talents'])==list:
        if len(sp.loc[t,'Talents'])==2:
            sp["Talent1"][t]=sp.loc[t,"Talents"][0]
            sp["Talent2"][t]=sp.loc[t,"Talents"][1]
            sp["Talent3"][t]=np.nan
        else:
            sp["Talent1"][t]=sp.loc[t,"Talents"][0]
            sp["Talent2"][t]=sp.loc[t,"Talents"][1]
            sp["Talent3"][t]=sp.loc[t,"Talents"][2]
            
    else:
        sp["Talent1"][t]=sp.loc[t,"Talents"]
        sp["Talent2"][t]=np.nan
        sp["Talent3"][t]=np.nan
        
    
    
#On controle ensuite si il ya des doublons a a partir de la fonction df.eq
  
#Pour le type:
        
val=sp["Type1"].eq(sp["Type2"])
val.value_counts()
#On a un pokemon qui a deux fois le meme type, il faut corriger,on le localise
np.where(val==True)
#En considérant 672 comme le pokémon 673 a cause du changement d'index 
#(que np.where ne considere pas) on trouve donc que ce pokémon est Chevroum
#on corrige ensuite la valeur
sp.loc[673,"Types"]="Plante"
#je relance le code pour prendre en compte ce changement
for t in sp.index:
    if type(sp.loc[t,'Types'])==list:
        sp["Type1"][t]=sp.loc[t,"Types"][0]
        sp["Type2"][t]=sp.loc[t,"Types"][1]
    else:
        sp["Type1"][t]=sp.loc[t,"Types"]
        sp["Type2"][t]=np.nan
        
        

#Pour les oeufs:

valoeuf=sp["GroupeOeuf1"].eq(sp["GroupeOeuf2"])
valoeuf.value_counts()
#Tout semble en ordre

#Pour les talents:

valtalent1=sp["Talent1"].eq(sp["Talent2"])
valtalent2=sp["Talent2"].eq(sp["Talent3"])
valtalent3=sp["Talent1"].eq(sp["Talent3"])
valtalent=sp["Talent1"].eq(sp["Talent2"]).eq(sp["Talent3"])

valtalent1.value_counts()
valtalent2.value_counts()
valtalent3.value_counts()

#Pas de doublon à déclarer


##########################################################################################
#####Je cherche ensuite a compléter la base dans le but de d'ajouter de l'information#####
# A partir des variables de la base et des infos qu'on a (quand on est connait pokémon)
# 1) On recrée les sensibilité des pokémons aux types, la base de kaggle les avait
#    directement scrappé, ici on peux directement les recrées en connaissant
#    le systeme des sensibilités face aux types
# 2) On indique la génération des pokémons de 1 à 8 , les paliers sont connus explicitement


#1)On crée les colonnes indicant les sensibilité par rapport à l'attaque subi
sp["Normal_sensi"]=1
sp["Plante_sensi"]=1
sp["Feu_sensi"]=1
sp["Eau_sensi"]=1
sp["Electrik_sensi"]=1
sp["Glace_sensi"]=1
sp["Combat_sensi"]=1
sp["Poison_sensi"]=1
sp["Sol_sensi"]=1
sp["Vol_sensi"]=1
sp["Psy_sensi"]=1
sp["Insecte_sensi"]=1
sp["Roche_sensi"]=1
sp["Spectre_sensi"]=1
sp["Dragon_sensi"]=1
sp["Ténèbres_sensi"]=1
sp["Acier_sensi"]=1
sp["Fée_sensi"]=1


#Pour chaque type on a des regles qui decrivent les dégats reçus, on commence par le premier type 
#en indiquant pour chaque type la sensibilité
#par exemple un pokemon de type feu subi le double de degat quand l'attaque est de type eau, Eau_sensi=2
for a in sp.index:
    if sp.loc[a,"Type1"]=="Normal":
        sp.loc[a,"Combat_sensi"]=sp.loc[a,"Combat_sensi"]*2
        sp.loc[a,"Spectre_sensi"]=sp.loc[a,"Spectre_sensi"]*0
    elif sp.loc[a,"Type1"]=="Plante":
        sp.loc[a,"Eau_sensi"]=sp.loc[a,"Eau_sensi"]/2
        sp.loc[a,"Electrik_sensi"]=sp.loc[a,"Electrik_sensi"]/2
        sp.loc[a,"Plante_sensi"]=sp.loc[a,"Plante_sensi"]/2
        sp.loc[a,"Sol_sensi"]=sp.loc[a,"Sol_sensi"]/2
        sp.loc[a,"Feu_sensi"]=sp.loc[a,"Feu_sensi"]*2
        sp.loc[a,"Glace_sensi"]=sp.loc[a,"Glace_sensi"]*2
        sp.loc[a,"Insecte_sensi"]=sp.loc[a,"Insecte_sensi"]*2
        sp.loc[a,"Poison_sensi"]=sp.loc[a,"Poison_sensi"]*2
        sp.loc[a,"Vol_sensi"]=sp.loc[a,"Vol_sensi"]*2
    elif sp.loc[a,"Type1"]=="Feu":
        sp.loc[a,"Acier_sensi"]=sp.loc[a,"Acier_sensi"]/2
        sp.loc[a,"Fée_sensi"]=sp.loc[a,"Fée_sensi"]/2
        sp.loc[a,"Feu_sensi"]=sp.loc[a,"Feu_sensi"]/2
        sp.loc[a,"Glace_sensi"]=sp.loc[a,"Glace_sensi"]/2
        sp.loc[a,"Insecte_sensi"]=sp.loc[a,"Insecte_sensi"]/2
        sp.loc[a,"Plante_sensi"]=sp.loc[a,"Plante_sensi"]/2 
        sp.loc[a,"Eau_sensi"]=sp.loc[a,"Eau_sensi"]*2
        sp.loc[a,"Roche_sensi"]=sp.loc[a,"Roche_sensi"]*2
        sp.loc[a,"Sol_sensi"]=sp.loc[a,"Sol_sensi"]*2
    elif sp.loc[a,"Type1"]=="Eau":
        sp.loc[a,"Acier_sensi"]=sp.loc[a,"Acier_sensi"]/2
        sp.loc[a,"Eau_sensi"]=sp.loc[a,"Eau_sensi"]/2
        sp.loc[a,"Feu_sensi"]=sp.loc[a,"Feu_sensi"]/2
        sp.loc[a,"Glace_sensi"]=sp.loc[a,"Glace_sensi"]/2
        sp.loc[a,"Electrik_sensi"]=sp.loc[a,"Electrik_sensi"]*2
        sp.loc[a,"Plante_sensi"]=sp.loc[a,"Plante_sensi"]*2
    elif sp.loc[a,"Type1"]=="Électrik":
        sp.loc[a,"Acier_sensi"]=sp.loc[a,"Acier_sensi"]/2
        sp.loc[a,"Electrik_sensi"]=sp.loc[a,"Electrik_sensi"]/2
        sp.loc[a,"Vol_sensi"]=sp.loc[a,"Vol_sensi"]/2
        sp.loc[a,"Sol_sensi"]=sp.loc[a,"Sol_sensi"]*2
    elif sp.loc[a,"Type1"]=="Glace":
        sp.loc[a,"Glace_sensi"]=sp.loc[a,"Glace_sensi"]/2
        sp.loc[a,"Acier_sensi"]=sp.loc[a,"Acier_sensi"]*2
        sp.loc[a,"Combat_sensi"]=sp.loc[a,"Combat_sensi"]*2
        sp.loc[a,"Feu_sensi"]=sp.loc[a,"Feu_sensi"]*2
        sp.loc[a,"Roche_sensi"]=sp.loc[a,"Roche_sensi"]*2
    elif sp.loc[a,"Type1"]=="Combat":
         sp.loc[a,"Insecte_sensi"]=sp.loc[a,"Insecte_sensi"]/2
         sp.loc[a,"Roche_sensi"]=sp.loc[a,"Roche_sensi"]/2
         sp.loc[a,"Ténèbres_sensi"]=sp.loc[a,"Ténèbres_sensi"]/2
         sp.loc[a,"Fée_sensi"]=sp.loc[a,"Fée_sensi"]*2
         sp.loc[a,"Psy_sensi"]=sp.loc[a,"Psy_sensi"]*2
         sp.loc[a,"Vol_sensi"]=sp.loc[a,"Vol_sensi"]*2
    elif sp.loc[a,"Type1"]=="Poison":
        sp.loc[a,"Combat_sensi"]=sp.loc[a,"Combat_sensi"]/2
        sp.loc[a,"Fée_sensi"]=sp.loc[a,"Fée_sensi"]/2
        sp.loc[a,"Insecte_sensi"]=sp.loc[a,"Insecte_sensi"]/2
        sp.loc[a,"Plante_sensi"]=sp.loc[a,"Plante_sensi"]/2
        sp.loc[a,"Poison_sensi"]=sp.loc[a,"Poison_sensi"]/2
        sp.loc[a,"Psy_sensi"]=sp.loc[a,"Psy_sensi"]*2
        sp.loc[a,"Sol_sensi"]=sp.loc[a,"Sol_sensi"]*2
    elif sp.loc[a,"Type1"]=="Sol":
        sp.loc[a,"Electrik_sensi"]=sp.loc[a,"Electrik_sensi"]*0
        sp.loc[a,"Poison_sensi"]=sp.loc[a,"Poison_sensi"]/2
        sp.loc[a,"Roche_sensi"]=sp.loc[a,"Roche_sensi"]/2
        sp.loc[a,"Eau_sensi"]=sp.loc[a,"Eau_sensi"]*2
        sp.loc[a,"Glace_sensi"]=sp.loc[a,"Glace_sensi"]*2
        sp.loc[a,"Plante_sensi"]=sp.loc[a,"Plante_sensi"]*2
    elif sp.loc[a,"Type1"]=="Vol":
        sp.loc[a,"Combat_sensi"]=sp.loc[a,"Combat_sensi"]/2
        sp.loc[a,"Insecte_sensi"]=sp.loc[a,"Insecte_sensi"]/2
        sp.loc[a,"Plante_sensi"]=sp.loc[a,"Plante_sensi"]/2
        sp.loc[a,"Sol_sensi"]=sp.loc[a,"Sol_sensi"]*0
        sp.loc[a,"Electrik_sensi"]=sp.loc[a,"Electrik_sensi"]*2
        sp.loc[a,"Glace_sensi"]=sp.loc[a,"Glace_sensi"]*2
        sp.loc[a,"Roche_sensi"]=sp.loc[a,"Roche_sensi"]*2
    elif sp.loc[a,"Type1"]=="Psy":
        sp.loc[a,"Combat_sensi"]=sp.loc[a,"Combat_sensi"]/2
        sp.loc[a,"Psy_sensi"]=sp.loc[a,"Psy_sensi"]/2
        sp.loc[a,"Insecte_sensi"]=sp.loc[a,"Insecte_sensi"]*2
        sp.loc[a,"Spectre_sensi"]=sp.loc[a,"Spectre_sensi"]*2
        sp.loc[a,"Ténèbres_sensi"]=sp.loc[a,"Ténèbres_sensi"]*2
    elif sp.loc[a,"Type1"]=="Insecte":
        sp.loc[a,"Combat_sensi"]=sp.loc[a,"Combat_sensi"]/2
        sp.loc[a,"Plante_sensi"]=sp.loc[a,"Plante_sensi"]/2
        sp.loc[a,"Sol_sensi"]=sp.loc[a,"Sol_sensi"]/2
        sp.loc[a,"Feu_sensi"]=sp.loc[a,"Feu_sensi"]*2
        sp.loc[a,"Roche_sensi"]=sp.loc[a,"Roche_sensi"]*2
        sp.loc[a,"Vol_sensi"]=sp.loc[a,"Vol_sensi"]*2
    elif sp.loc[a,"Type1"]=="Roche":
         sp.loc[a,"Feu_sensi"]=sp.loc[a,"Feu_sensi"]/2
         sp.loc[a,"Normal_sensi"]=sp.loc[a,"Normal_sensi"]/2
         sp.loc[a,"Poison_sensi"]=sp.loc[a,"Poison_sensi"]/2
         sp.loc[a,"Vol_sensi"]=sp.loc[a,"Vol_sensi"]/2
         sp.loc[a,"Acier_sensi"]=sp.loc[a,"Acier_sensi"]*2
         sp.loc[a,"Combat_sensi"]=sp.loc[a,"Combat_sensi"]*2
         sp.loc[a,"Eau_sensi"]=sp.loc[a,"Eau_sensi"]*2
         sp.loc[a,"Plante_sensi"]=sp.loc[a,"Plante_sensi"]*2
         sp.loc[a,"Sol_sensi"]=sp.loc[a,"Sol_sensi"]*2
    elif sp.loc[a,"Type1"]=="Spectre":
        sp.loc[a,"Combat_sensi"]=sp.loc[a,"Combat_sensi"]*0
        sp.loc[a,"Normal_sensi"]=sp.loc[a,"Normal_sensi"]*0
        sp.loc[a,"Insecte_sensi"]=sp.loc[a,"Insecte_sensi"]/2
        sp.loc[a,"Poison_sensi"]=sp.loc[a,"Poison_sensi"]/2
        sp.loc[a,"Spectre_sensi"]=sp.loc[a,"Spectre_sensi"]*2
        sp.loc[a,"Ténèbres_sensi"]=sp.loc[a,"Ténèbres_sensi"]*2
    elif sp.loc[a,"Type1"]=="Dragon":
        sp.loc[a,"Eau_sensi"]=sp.loc[a,"Eau_sensi"]/2
        sp.loc[a,"Electrik_sensi"]=sp.loc[a,"Electrik_sensi"]/2
        sp.loc[a,"Feu_sensi"]=sp.loc[a,"Feu_sensi"]/2
        sp.loc[a,"Plante_sensi"]=sp.loc[a,"Plante_sensi"]/2
        sp.loc[a,"Dragon_sensi"]=sp.loc[a,"Dragon_sensi"]*2
        sp.loc[a,"Fée_sensi"]=sp.loc[a,"Fée_sensi"]*2
        sp.loc[a,"Glace_sensi"]=sp.loc[a,"Glace_sensi"]*2
    elif sp.loc[a,"Type1"]=="Ténèbres":
        sp.loc[a,"Psy_sensi"]=sp.loc[a,"Psy_sensi"]*0
        sp.loc[a,"Spectre_sensi"]=sp.loc[a,"Spectre_sensi"]/2
        sp.loc[a,"Ténèbres_sensi"]=sp.loc[a,"Ténèbres_sensi"]/2
        sp.loc[a,"Fée_sensi"]=sp.loc[a,"Fée_sensi"]*2 
        sp.loc[a,"Insecte_sensi"]=sp.loc[a,"Insecte_sensi"]*2
        sp.loc[a,"Combat_sensi"]=sp.loc[a,"Combat_sensi"]*2
    elif sp.loc[a,"Type1"]=="Acier":
        sp.loc[a,"Poison_sensi"]=sp.loc[a,"Poison_sensi"]*0
        sp.loc[a,"Acier_sensi"]=sp.loc[a,"Acier_sensi"]/2
        sp.loc[a,"Dragon_sensi"]=sp.loc[a,"Dragon_sensi"]/2
        sp.loc[a,"Fée_sensi"]=sp.loc[a,"Fée_sensi"]/2
        sp.loc[a,"Insecte_sensi"]=sp.loc[a,"Insecte_sensi"]/2
        sp.loc[a,"Glace_sensi"]=sp.loc[a,"Glace_sensi"]/2
        sp.loc[a,"Normal_sensi"]=sp.loc[a,"Normal_sensi"]/2
        sp.loc[a,"Plante_sensi"]=sp.loc[a,"Plante_sensi"]/2
        sp.loc[a,"Psy_sensi"]=sp.loc[a,"Psy_sensi"]/2
        sp.loc[a,"Roche_sensi"]=sp.loc[a,"Roche_sensi"]/2
        sp.loc[a,"Vol_sensi"]=sp.loc[a,"Vol_sensi"]/2
        sp.loc[a,"Combat_sensi"]=sp.loc[a,"Combat_sensi"]*2
        sp.loc[a,"Feu_sensi"]=sp.loc[a,"Feu_sensi"]*2
        sp.loc[a,"Sol_sensi"]=sp.loc[a,"Sol_sensi"]*2
    elif sp.loc[a,"Type1"]=="Fée":
        sp.loc[a,"Combat_sensi"]=sp.loc[a,"Combat_sensi"]/2
        sp.loc[a,"Dragon_sensi"]=sp.loc[a,"Dragon_sensi"]*0
        sp.loc[a,"Insecte_sensi"]=sp.loc[a,"Insecte_sensi"]/2
        sp.loc[a,"Ténèbres_sensi"]=sp.loc[a,"Ténèbres_sensi"]/2
        sp.loc[a,"Acier_sensi"]=sp.loc[a,"Acier_sensi"]*2
        sp.loc[a,"Poison_sensi"]=sp.loc[a,"Poison_sensi"]*2
        

#On procede de la même maniere pour les pokémons qui ont un deuxieme type
        
for a in sp.index:
    if type(sp.loc[a,"Type2"])!=type(np.nan):
            if sp.loc[a,"Type2"]=="Normal":
                sp.loc[a,"Combat_sensi"]=sp.loc[a,"Combat_sensi"]*2
                sp.loc[a,"Spectre_sensi"]=sp.loc[a,"Spectre_sensi"]*0
            elif sp.loc[a,"Type2"]=="Plante":
                sp.loc[a,"Eau_sensi"]=sp.loc[a,"Eau_sensi"]/2
                sp.loc[a,"Electrik_sensi"]=sp.loc[a,"Electrik_sensi"]/2
                sp.loc[a,"Plante_sensi"]=sp.loc[a,"Plante_sensi"]/2
                sp.loc[a,"Sol_sensi"]=sp.loc[a,"Sol_sensi"]/2
                sp.loc[a,"Feu_sensi"]=sp.loc[a,"Feu_sensi"]*2
                sp.loc[a,"Glace_sensi"]=sp.loc[a,"Glace_sensi"]*2
                sp.loc[a,"Insecte_sensi"]=sp.loc[a,"Insecte_sensi"]*2
                sp.loc[a,"Poison_sensi"]=sp.loc[a,"Poison_sensi"]*2
                sp.loc[a,"Vol_sensi"]=sp.loc[a,"Vol_sensi"]*2
            elif sp.loc[a,"Type2"]=="Feu":
                sp.loc[a,"Acier_sensi"]=sp.loc[a,"Acier_sensi"]/2
                sp.loc[a,"Fée_sensi"]=sp.loc[a,"Fée_sensi"]/2
                sp.loc[a,"Feu_sensi"]=sp.loc[a,"Feu_sensi"]/2
                sp.loc[a,"Glace_sensi"]=sp.loc[a,"Glace_sensi"]/2
                sp.loc[a,"Insecte_sensi"]=sp.loc[a,"Insecte_sensi"]/2
                sp.loc[a,"Plante_sensi"]=sp.loc[a,"Plante_sensi"]/2 
                sp.loc[a,"Eau_sensi"]=sp.loc[a,"Eau_sensi"]*2
                sp.loc[a,"Roche_sensi"]=sp.loc[a,"Roche_sensi"]*2
                sp.loc[a,"Sol_sensi"]=sp.loc[a,"Sol_sensi"]*2
            elif sp.loc[a,"Type2"]=="Eau":
                sp.loc[a,"Acier_sensi"]=sp.loc[a,"Acier_sensi"]/2
                sp.loc[a,"Eau_sensi"]=sp.loc[a,"Eau_sensi"]/2
                sp.loc[a,"Feu_sensi"]=sp.loc[a,"Feu_sensi"]/2
                sp.loc[a,"Glace_sensi"]=sp.loc[a,"Glace_sensi"]/2
                sp.loc[a,"Electrik_sensi"]=sp.loc[a,"Electrik_sensi"]*2
                sp.loc[a,"Plante_sensi"]=sp.loc[a,"Plante_sensi"]*2
            elif sp.loc[a,"Type2"]=="Électrik":
                sp.loc[a,"Acier_sensi"]=sp.loc[a,"Acier_sensi"]/2
                sp.loc[a,"Electrik_sensi"]=sp.loc[a,"Electrik_sensi"]/2
                sp.loc[a,"Vol_sensi"]=sp.loc[a,"Vol_sensi"]/2
                sp.loc[a,"Sol_sensi"]=sp.loc[a,"Sol_sensi"]*2
            elif sp.loc[a,"Type2"]=="Glace":
                sp.loc[a,"Glace_sensi"]=sp.loc[a,"Glace_sensi"]/2
                sp.loc[a,"Acier_sensi"]=sp.loc[a,"Acier_sensi"]*2
                sp.loc[a,"Combat_sensi"]=sp.loc[a,"Combat_sensi"]*2
                sp.loc[a,"Feu_sensi"]=sp.loc[a,"Feu_sensi"]*2
                sp.loc[a,"Roche_sensi"]=sp.loc[a,"Roche_sensi"]*2
            elif sp.loc[a,"Type2"]=="Combat":
                sp.loc[a,"Insecte_sensi"]=sp.loc[a,"Insecte_sensi"]/2
                sp.loc[a,"Roche_sensi"]=sp.loc[a,"Roche_sensi"]/2
                sp.loc[a,"Ténèbres_sensi"]=sp.loc[a,"Ténèbres_sensi"]/2
                sp.loc[a,"Fée_sensi"]=sp.loc[a,"Fée_sensi"]*2
                sp.loc[a,"Psy_sensi"]=sp.loc[a,"Psy_sensi"]*2
                sp.loc[a,"Vol_sensi"]=sp.loc[a,"Vol_sensi"]*2
            elif sp.loc[a,"Type2"]=="Poison":
                sp.loc[a,"Combat_sensi"]=sp.loc[a,"Combat_sensi"]/2
                sp.loc[a,"Fée_sensi"]=sp.loc[a,"Fée_sensi"]/2
                sp.loc[a,"Insecte_sensi"]=sp.loc[a,"Insecte_sensi"]/2
                sp.loc[a,"Plante_sensi"]=sp.loc[a,"Plante_sensi"]/2
                sp.loc[a,"Poison_sensi"]=sp.loc[a,"Poison_sensi"]/2
                sp.loc[a,"Psy_sensi"]=sp.loc[a,"Psy_sensi"]*2
                sp.loc[a,"Sol_sensi"]=sp.loc[a,"Sol_sensi"]*2
            elif sp.loc[a,"Type2"]=="Sol":
                sp.loc[a,"Electrik_sensi"]=sp.loc[a,"Electrik_sensi"]*0
                sp.loc[a,"Poison_sensi"]=sp.loc[a,"Poison_sensi"]/2
                sp.loc[a,"Roche_sensi"]=sp.loc[a,"Roche_sensi"]/2
                sp.loc[a,"Eau_sensi"]=sp.loc[a,"Eau_sensi"]*2
                sp.loc[a,"Glace_sensi"]=sp.loc[a,"Glace_sensi"]*2
                sp.loc[a,"Plante_sensi"]=sp.loc[a,"Plante_sensi"]*2
            elif sp.loc[a,"Type2"]=="Vol":
                sp.loc[a,"Combat_sensi"]=sp.loc[a,"Combat_sensi"]/2
                sp.loc[a,"Insecte_sensi"]=sp.loc[a,"Insecte_sensi"]/2
                sp.loc[a,"Plante_sensi"]=sp.loc[a,"Plante_sensi"]/2
                sp.loc[a,"Sol_sensi"]=sp.loc[a,"Sol_sensi"]*0
                sp.loc[a,"Electrik_sensi"]=sp.loc[a,"Electrik_sensi"]*2
                sp.loc[a,"Glace_sensi"]=sp.loc[a,"Glace_sensi"]*2
                sp.loc[a,"Roche_sensi"]=sp.loc[a,"Roche_sensi"]*2
            elif sp.loc[a,"Type2"]=="Psy":
                sp.loc[a,"Combat_sensi"]=sp.loc[a,"Combat_sensi"]/2
                sp.loc[a,"Psy_sensi"]=sp.loc[a,"Psy_sensi"]/2
                sp.loc[a,"Insecte_sensi"]=sp.loc[a,"Insecte_sensi"]*2
                sp.loc[a,"Spectre_sensi"]=sp.loc[a,"Spectre_sensi"]*2
                sp.loc[a,"Ténèbres_sensi"]=sp.loc[a,"Ténèbres_sensi"]*2
            elif sp.loc[a,"Type2"]=="Insecte":
                sp.loc[a,"Combat_sensi"]=sp.loc[a,"Combat_sensi"]/2
                sp.loc[a,"Plante_sensi"]=sp.loc[a,"Plante_sensi"]/2
                sp.loc[a,"Sol_sensi"]=sp.loc[a,"Sol_sensi"]/2
                sp.loc[a,"Feu_sensi"]=sp.loc[a,"Feu_sensi"]*2
                sp.loc[a,"Roche_sensi"]=sp.loc[a,"Roche_sensi"]*2
                sp.loc[a,"Vol_sensi"]=sp.loc[a,"Vol_sensi"]*2
            elif sp.loc[a,"Type2"]=="Roche":
                sp.loc[a,"Feu_sensi"]=sp.loc[a,"Feu_sensi"]/2
                sp.loc[a,"Normal_sensi"]=sp.loc[a,"Normal_sensi"]/2
                sp.loc[a,"Poison_sensi"]=sp.loc[a,"Poison_sensi"]/2
                sp.loc[a,"Vol_sensi"]=sp.loc[a,"Vol_sensi"]/2
                sp.loc[a,"Acier_sensi"]=sp.loc[a,"Acier_sensi"]*2
                sp.loc[a,"Combat_sensi"]=sp.loc[a,"Combat_sensi"]*2
                sp.loc[a,"Eau_sensi"]=sp.loc[a,"Eau_sensi"]*2
                sp.loc[a,"Plante_sensi"]=sp.loc[a,"Plante_sensi"]*2
                sp.loc[a,"Sol_sensi"]=sp.loc[a,"Sol_sensi"]*2
            elif sp.loc[a,"Type2"]=="Spectre":
                sp.loc[a,"Combat_sensi"]=sp.loc[a,"Combat_sensi"]*0
                sp.loc[a,"Normal_sensi"]=sp.loc[a,"Normal_sensi"]*0
                sp.loc[a,"Insecte_sensi"]=sp.loc[a,"Insecte_sensi"]/2
                sp.loc[a,"Poison_sensi"]=sp.loc[a,"Poison_sensi"]/2
                sp.loc[a,"Spectre_sensi"]=sp.loc[a,"Spectre_sensi"]*2
                sp.loc[a,"Ténèbres_sensi"]=sp.loc[a,"Ténèbres_sensi"]*2
            elif sp.loc[a,"Type2"]=="Dragon":
                sp.loc[a,"Eau_sensi"]=sp.loc[a,"Eau_sensi"]/2
                sp.loc[a,"Electrik_sensi"]=sp.loc[a,"Electrik_sensi"]/2
                sp.loc[a,"Feu_sensi"]=sp.loc[a,"Feu_sensi"]/2
                sp.loc[a,"Plante_sensi"]=sp.loc[a,"Plante_sensi"]/2
                sp.loc[a,"Dragon_sensi"]=sp.loc[a,"Dragon_sensi"]*2
                sp.loc[a,"Fée_sensi"]=sp.loc[a,"Fée_sensi"]*2
                sp.loc[a,"Glace_sensi"]=sp.loc[a,"Glace_sensi"]*2
            elif sp.loc[a,"Type2"]=="Ténèbres":
                sp.loc[a,"Psy_sensi"]=sp.loc[a,"Psy_sensi"]*0
                sp.loc[a,"Spectre_sensi"]=sp.loc[a,"Spectre_sensi"]/2
                sp.loc[a,"Ténèbres_sensi"]=sp.loc[a,"Ténèbres_sensi"]/2
                sp.loc[a,"Fée_sensi"]=sp.loc[a,"Fée_sensi"]*2 
                sp.loc[a,"Insecte_sensi"]=sp.loc[a,"Insecte_sensi"]*2
                sp.loc[a,"Combat_sensi"]=sp.loc[a,"Combat_sensi"]*2
            elif sp.loc[a,"Type2"]=="Acier":
                sp.loc[a,"Poison_sensi"]=sp.loc[a,"Poison_sensi"]*0
                sp.loc[a,"Acier_sensi"]=sp.loc[a,"Acier_sensi"]/2
                sp.loc[a,"Dragon_sensi"]=sp.loc[a,"Dragon_sensi"]/2
                sp.loc[a,"Fée_sensi"]=sp.loc[a,"Fée_sensi"]/2
                sp.loc[a,"Insecte_sensi"]=sp.loc[a,"Insecte_sensi"]/2
                sp.loc[a,"Glace_sensi"]=sp.loc[a,"Glace_sensi"]/2
                sp.loc[a,"Normal_sensi"]=sp.loc[a,"Normal_sensi"]/2
                sp.loc[a,"Plante_sensi"]=sp.loc[a,"Plante_sensi"]/2
                sp.loc[a,"Psy_sensi"]=sp.loc[a,"Psy_sensi"]/2
                sp.loc[a,"Roche_sensi"]=sp.loc[a,"Roche_sensi"]/2
                sp.loc[a,"Vol_sensi"]=sp.loc[a,"Vol_sensi"]/2
                sp.loc[a,"Combat_sensi"]=sp.loc[a,"Combat_sensi"]*2
                sp.loc[a,"Feu_sensi"]=sp.loc[a,"Feu_sensi"]*2
                sp.loc[a,"Sol_sensi"]=sp.loc[a,"Sol_sensi"]*2
            elif sp.loc[a,"Type2"]=="Fée":
                sp.loc[a,"Combat_sensi"]=sp.loc[a,"Combat_sensi"]/2
                sp.loc[a,"Dragon_sensi"]=sp.loc[a,"Dragon_sensi"]*0
                sp.loc[a,"Insecte_sensi"]=sp.loc[a,"Insecte_sensi"]/2
                sp.loc[a,"Ténèbres_sensi"]=sp.loc[a,"Ténèbres_sensi"]/2
                sp.loc[a,"Acier_sensi"]=sp.loc[a,"Acier_sensi"]*2
                sp.loc[a,"Poison_sensi"]=sp.loc[a,"Poison_sensi"]*2
    else:
        pass
 
    
#Pour quelques cas le talent léviation rend innofensif les attaques de types sol :
        
for i in sp.index:
    if type(sp.loc[i,"Talents"])==str:
        if sp.loc[i,"Talents"]=="Lévitation":
             sp.loc[i,"Sol_sensi"]=sp.loc[i,"Sol_sensi"]*0
        else:
            pass
    else:
        pass
    
#On a aussi un cas exeptionel, munja qui ne subit des débat que si c'est super efficace
        
sp.loc[292,"Normal_sensi"]=0
sp.loc[292,"Fée_sensi"]=0
sp.loc[292,"Acier_sensi"]=0
sp.loc[292,"Dragon_sensi"]=0
sp.loc[292,"Insecte_sensi"]=0
sp.loc[292,"Psy_sensi"]=0
sp.loc[292,"Sol_sensi"]=0
sp.loc[292,"Poison_sensi"]=0
sp.loc[292,"Combat_sensi"]=0
sp.loc[292,"Glace_sensi"]=0
sp.loc[292,"Electrik_sensi"]=0
sp.loc[292,"Eau_sensi"]=0
sp.loc[292,"Plante_sensi"]=0
    
#Enfin on crée une variable qui indique la somme total des sensibilité, cela nous permettra
#de comparer les sensibilité selon le type et de trouver un type idéal         
    
for s in sp.index:
    sp.loc[s,"Somme des sensibilité"]=sp.loc[s,"Normal_sensi"]+sp.loc[s,"Plante_sensi"]+sp.loc[s,"Feu_sensi"]+sp.loc[s,"Eau_sensi"]+sp.loc[s,"Electrik_sensi"]+sp.loc[s,"Glace_sensi"]+sp.loc[s,"Combat_sensi"]+sp.loc[s,"Poison_sensi"]+sp.loc[s,"Sol_sensi"]+sp.loc[s,"Vol_sensi"]+sp.loc[s,"Psy_sensi"]+sp.loc[s,"Insecte_sensi"]+sp.loc[s,"Roche_sensi"]+sp.loc[s,"Spectre_sensi"]+sp.loc[s,"Dragon_sensi"]+sp.loc[s,"Ténèbres_sensi"]+sp.loc[s,"Acier_sensi"]+sp.loc[s,"Fée_sensi"]
    
        
        
#2) On crée une colonne vide génération et on la rempli selon le numero du pokémon dans le 
#   Pokédex national (qui correspond ici a l'index)
sp["Génération"]=""
for i in range(1,152):
    sp["Génération"][i]=1
for i in range(152,252):
    sp["Génération"][i]=2
for i in range(252,387):
    sp["Génération"][i]=3
for i in range(387,494):
    sp["Génération"][i]=4
for i in range(494,650):
    sp["Génération"][i]=5
for i in range(650,722):
    sp["Génération"][i]=6
for i in range(722,810):
    sp["Génération"][i]=7
for i in range(810,891):
    sp["Génération"][i]=8
sp["Génération"]=sp["Génération"].astype(float)


#3) je prend la base de kaggle pour prendre les infos sur la "légendarité" du pokémon pour les
#   7 premiere générations (cela m'évite de trop en faire a la main), et je complete le reste   

Kaggledex=pd.read_csv(r'C:\Users\Yanis\Documents\Cours\Master\Master 1 Econometrie statistique\M1-S2\Python\Data\pokemon.csv')
Kaggledex.index+=1
Kaggledex.info()

sp["Légendaire"]=Kaggledex["is_legendary"]
sp.loc[802:890,"Légendaire"]=0
sp.loc[888:890,"Légendaire"]=1
sp.loc[802:807,"Légendaire"]=1

#4) je crée une variable qui indique si le pokémon a un deuxieme type ou non, dans le but
#de faire des statistiques dessus plus tard

for i in sp.index:
    if type(sp.loc[i,"Type2"])==type(np.nan):
        sp.loc[i,"A 2 types ?"]=0
    else:
        sp.loc[i,"A 2 types ?"]=1
        


###################################################################################
# Je contemple le travail avec les stats descriptive de base et j'enregistre

sp.dtypes
sp.info()
sp.shape
Stats=sp.describe()

sp.to_excel(r'C:\Users\Yanis\Scrapédex_final.xlsx')
sp.to_csv(r'C:\Users\Yanis\Scrapédex_final.csv')
sp.to_pickle(r'C:\Users\Yanis\Scrapédex_final.pkl')


###################################################################################
#BONUS

#J'avais calculer l'IMC des pokémons a un moment (IMC= Poids/taille**2)
#Cette stat n'a purement aucun interet (car cela ne veut rien dire vu les 
#différentes morphologie des pokémons) si ce n'est dire que : 
#Mr mime avec un IMC de 32 est considérer comme obèse
#Lippoutou avec un imc de 20 est dans son poids de forme

sp["IMC"]=""
for i in range(1,891):
    sp["IMC"][i]=sp["Poids"][i]/sp["Taille"][i]**2
sp["IMC"]=sp["IMC"].astype(float)
    

maskIMCideal=((sp["IMC"]>18) & (sp["IMC"]<24))
spIMC=sp[maskIMCideal]
#sur 890 pokémons seuls 121 on un imc ideal (cette stat est profondément inutile)

maskhumanoid=sp["Groupe Oeuf"].isin(["Humanoïde"])
sp_HUMAIN=sp[maskhumanoid]

#Ici je crée un sous data-frame avec les pokémons de types humanoide (le groupe d'oeufs)
#mais je n'ai pas reussi a trouver une condition indiquant que si "Humanoide" est contenu dans 
#la liste des groupes d'oeufs alors la condition est valider, il me retourne simplement
#les cas ou il y a juste humanoide d'ou la stat suivante (toujours inutile bien sur)
sp_HUMAIN_IDEAL=sp_HUMAIN[maskIMCideal]
#Sur les 37 pokémons humanoïdes , seuls 5 on un poids de forme ...

#Pour décomposer correctement je vais devoir passer par les variables "GroupeOeuf1" et
# "GroupeOeuf2" que j'avais crée avant  :

mask_Mi_Humain_et_humain=((sp["GroupeOeuf1"]=="Humanoïde") | (sp["GroupeOeuf2"]=="Humanoïde"))
sp_Mi_Humain_et_humain=sp[mask_Mi_Humain_et_humain]

#Et la ca marche, on trouve enfin comme résultat (toujours inutilement unutile)
sp_Mi_Humain_et_humain_IDEAL=sp_Mi_Humain_et_humain[maskIMCideal]
#11/65 , le poids de forme n'et definitivement pas un objectif des pokémons.

