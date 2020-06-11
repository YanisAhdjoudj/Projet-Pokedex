# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 19:49:14 2020

@author: Yanis
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import seaborn as sns
import statsmodels.api as sm
from sklearn import linear_model

path=r'C:/Users/Yanis/Documents/Projet Pokédex/Data/Scrapédex_final.pkl'
Scrapédex_final=pd.read_pickle(path)
Scrapédex_final.info()
sp=Scrapédex_final.copy()


users = {}
for i in range(1,4):
    users["User"+str(i)]=0  
print (users)
# {'User1': 0, 'User2': 0, 'User3': 0}



sptesttype=sp[['Type1','Type2','Moyenne des statistiques de base']]
Types=['Plante','Feu','Eau','Insecte','Normal','Poison',"Électrik","Sol",'Fée','Combat','Psy','Roche','Spectre','Glace','Dragon','Ténèbres','Acier','Vol']

typesdict = {}

for i in Types:
    mask=((sptesttype["Type1"]==i))|(sptesttype["Type2"]==i)
    typesdict["sp"+str(i)]=sptesttype[mask]
  


Typesbox = pd.DataFrame()
sptesttype=sp[['Type1','Type2','Moyenne des statistiques de base']]
Types=['Plante','Feu','Eau','Insecte','Normal','Poison',"Électrik","Sol",'Fée','Combat','Psy','Roche','Spectre','Glace','Dragon','Ténèbres','Acier','Vol']

typesdict = {}

for i in Types:
    mask=((sptesttype["Type1"]==i))|(sptesttype["Type2"]==i)
    typesdict["sp"+str(i)]=sptesttype[mask]
    typesdict["sp"+str(i)]=typesdict["sp"+str(i)]["Moyenne des statistiques de base"]
    
Typesbox=Typesbox.from_dict(typesdict)



Typesbox = pd.DataFrame()
sptesttype=sp.copy()
Types=['Plante','Feu','Eau','Insecte','Normal','Poison',"Électrik","Sol",'Fée','Combat','Psy','Roche','Spectre','Glace','Dragon','Ténèbres','Acier','Vol']

typesdict = {}
for i in Types:
    mask=((sptesttype["Type1"]==i))|(sptesttype["Type2"]==i)
    typesdict[str(i)]=sptesttype[mask]
    typesdict[str(i)]=typesdict[str(i)]["Moyenne des statistiques de base"]

Typesbox=Typesbox.from_dict(typesdict)
sns.set(rc={'figure.figsize':(12,8.27)})
ax=sns.boxplot(data=Typesbox,palette="Set3")
ax.set(xlabel='Type du pokémon', ylabel='Moyenne des statistiques de base')
plt.show()

sp["Constante"]=1
maskleg=sp["Légendaire"]==0
sp2=sp[maskleg]


y=sp2["Somme des statistiques de base"]
X=sp2[["Constante","Poids","Taille","Taux de capture","A 2 types ?"]]
model=sm.OLS(y,X)
results = model.fit()
print(results.summary())


residuals=results.resid
yhat=results.fittedvalues

sns.scatterplot(yhat,residuals, color="g")
sns.distplot(residuals,color="g")
stats.probplot(residuals, plot=sns.mpl.pyplot,)




# Plot the residuals after fitting a linear model

résidus=model.resi

sm.qqplot(model)

true_val = sp['Moyenne des statistiques de base'].values.copy()
sns.set(rc={'figure.figsize':(10,8.27)})
fig, ax = plt.subplots(figsize=(6,2.5))
_ = ax.scatter(residuals, yhat)



sp['Légendaire'].value_counts()
#On a 79 pokémon légendaire
maskleg=sp['Génération']!=7
spTest=sp[maskleg]
#et seulement 56 quand on retire la 7 eme gen(ou le nombre de pokémon légendaire est abuser)


maskIMCideal=((sp["IMC"]>18) & (sp["IMC"]<24))
spIMC=sp[maskIMCideal]
#sur 890 pokémons seuls 121 on un imc ideal (cette stat est profondément inutile)


sp['Secondtype'].value_counts()
#on a presque autent de pokémon avec 2 type que de pokémon avec 1type 
#446 vs 444

Types=sp['Type1'].value_counts()+sp['Type2'].value_counts()
print(Types)
#on a 18 types, la serie Types nous indique le nombre de pokémon de chaque type
#en comptant ici les doubles types, si on est eau en premier ou en second type
#n'a pas d'importance
#on constate donc que le type eau est le plus représenter avec 141 pokemons,
#suivi de prés par les pokémons normals (115) puis les pokémons plante et vol (106 et 103)
#Dans le bas du tableau on retrouve les pokémons glace (40)

mask2types=sp["Secondtype"]==1
sp_secondtype=sp[mask2types]
sp_secondtype.mean()

mask_untype=sp["Secondtype"]==0
sp_unseultype=sp[mask_untype]
sp_unseultype.mean()

#en comparant ces deux résultats on trouve que:
#les pokemons qui on deux type sont en moyenne meilleurs que les pokémons qui n'en on qu'un
#ils ont des moyenne et sommes de base stat qui sont plus éléver que les 1 seul type
# 73 vs 66 pour les moyenne et 440 vs 401 pour les sommes
#la somme des résistances sont aussi meilleur chez les second type (19,22 vs 18,65)
#Ce qui laisse présager que avoir 2 type a un meilleur effet sur la sensibilité que
# juste en avoir 1, on a gagne donc plus a avoir 2 type que 1 seul

#Pour voir si ces interprétation sont fondé on vas regarder en detail les ecarts type


stat_untype=sp_unseultype.describe()
stat_deuxtypes=sp_secondtype.describe()
#On observe les memes variance entre les deux groupes concernant les sommes et moyennes
# des bases stat, cepandant on remarque que des le premier quantile les moyenne et les 
#sommes sont plus élever chez les bi_types, on a une dominance large

#Cepandant dans la somme des sensibilité on a une variance plus élever chez les bi-type
#que les 1 seul types, meme si on gagne en moyenne a avoir 2 types on a une plus
#grande chance d'avoir des faiblesse et des avantages, les max et min sont plus grand pour
#les bi-types et la concentration autour de la moyenne plus faible
#malgré tout le jeu est globalement bien équilibré, 50% des pokémons on des sommes de sensi
#comprise entre 18 et 20,5 pour les bitypes et entre 18 et 19,5 pour les uns seuls types

#Pour présenter un résultat plus honnete nous allons retirer les pokémons légendaire 
#en effet on sait qu'ils ont des stats de base au dessus de la moyenne (d'ou le terme 
#legendaire)

maskpasleg=(sp["Légendaire"]==0)
sppasleg=sp[maskleg]
sppasleg.mean()

maskleg=(sp["Légendaire"]==1)
spleg=sp[maskleg]
splegst=spleg.mean()

#on a des différences relativement importantes en terme de somme/moyenne des base stat
# moyenne => 67 vs 99 , somme=> 403 vs 599 


mask2types=((sp["Secondtype"]==1) & (sp["Légendaire"]==0))
sp_secondtype=sp[mask2types]
sp_secondtype.mean()

mask_untype=((sp["Secondtype"]==0) & (sp["Légendaire"]==0))
sp_unseultype=sp[mask_untype]
sp_unseultype.mean()

#On trouve des choses ( a revoir)




spBT=sp.sort_values(by=["Somme des sensibilité"])
spBT.head(10)

#concernant le meilleur type on trouve que le duo fée/acier est le double type qui garantit 
#la plus grande résistance aux attaques adverses, suivi par le double type acier vol
#le type acier est surreprésenter, dans le haut du classement, juste avoir le type acier seul
#place en haut du classement

