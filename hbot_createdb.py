# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 12:13:10 2022

@author: federico
"""

import spacy
import pandas as pd
import numpy as np
import sklearn as sk
import it_core_news_sm
import json
import PySimpleGUI as sg
import os.path



def create_lexical_entry(du,doc,index,indexdata):
    lexical_tree=[]

    for token in doc:
        #print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
        #      token.shape_, token.is_alpha, token.is_stop)
        lexical_tree.append([token.lemma_,
                       token.pos_,
                       token.dep_,
                       token.tag_,
                       token.shape_,
                       token.is_alpha,
                       token.is_stop])
  
    lexical_entry['le'+str(index)+str(index_data)]=[du,lexical_tree]
    
    
    
df = pd.read_excel('C:/Users/federico/Dropbox/Modelli/qbt/reftree_centralino_poc_bot/bot_data/botdata.xlsx',
                   sheet_name='Foglio1')
df_data =pd.read_excel('C:/Users/federico/Dropbox/Modelli/qbt/reftree_centralino_poc_bot/bot_data/botdata.xlsx',
                   sheet_name='Foglio2')

nlp = it_core_news_sm.load()

lexical_entry ={}
for index, row in df.iterrows():
    print(index)
    
    du1=row['DOMANDA UTENTE BASE 1']
    du2=row['DOMANDA UTENTE BASE 2']
    du3=row['DOMANDA UTENTE BASE 3']
    
    rb1=row['RISPOSTA BOT 1']
    rb2=row['RISPOSTA BOT 2']
    rb3=row['RISPOSTA BOT 3']
    
    if du1!=du1:
         du1=''
    if du2!=du2:
         du2=''
    if du3!=du3:
         du3=''
    du = du1 + ' ' + du2 +' ' +  du3  
    
    for index_data,row_data in df_data.iterrows():
       
        doc = nlp(du)
        create_lexical_entry(du,doc,index,9999)

        

json = json.dumps(lexical_entry)
f = open("dict.json","w")
f.write(json)
f.close()





    
# for ent in doc.ents:
#     print(ent.text, ent.start_char, ent.end_char, ent.label_)    

#nlp = spacy.load('it')