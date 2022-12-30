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
import pickle
import re
import string

def clear_input_string(s):
    d = re.sub(" +", " ", s)
    d =d.strip()
    d=d.translate(str.maketrans('', '', string.punctuation))
    d=d.lower()
    return d

def create_lemma_string(d):
    result=''
    for token in doc:
        result=result+token.lemma_+' '
    return result

    
def create_lexical_entry(du,doc,index,indexdata,ld):
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
  
    lexical_entry['le'+"_"+str(index)+"_"+str(indexdata)]=[du,lexical_tree,ld]
    
    
    
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
    
    rb1=str(row['RISPOSTA BOT 1'])
    rb2=str(row['RISPOSTA BOT 2'])
    rb3=str(row['RISPOSTA BOT 3'])
    
    db=str(row['DOMANDA BOT'])
    ob=str(row['OPZIONE BOTTONE'])
    
    rb11=str(row['RISPOSTA BOT 1.1'])
    rb21=str(row['RISPOSTA BOT 2.1'])
    rb31=str(row['RISPOSTA BOT 2.1'])
    
    lexical_data={}
    lexical_data['domanda']=db
    lexical_data['opzioni']=ob
    lexical_data['rb1']=rb1
    lexical_data['rb2']=rb2
    lexical_data['rb3']=rb3
    lexical_data['rb11']=rb11.split(';')
    lexical_data['rb21']=rb21.split(';')
    lexical_data['rb31']=rb21.split(';')
    lexical_data['w']=1
    lexical_data['rank']=-1
    
    
    if du1!=du1:
         du1=''
    if du2!=du2:
         du2=''
    if du3!=du3:
         du3=''
         
    du1=clear_input_string(du1) 
    du2=clear_input_string(du2) 
    du3=clear_input_string(du3) 
    du = du1 + ' ' + du2 +' ' +  du3  
    du=clear_input_string(du)
    
    doc = nlp(du)
    create_lexical_entry(du,doc,index,9999,lexical_data)
 
    sinon_cont=0
    for index_data,row_data in df_data.iterrows():
        lexical_data['far']=''
        lemma_du=create_lemma_string(doc)
        sinon=row_data['sinonimi'].split(";")
        chiave=sinon[0]
        if sinon[0] in lemma_du:
            
            for j in sinon[1:]:
                lemma_du=create_lemma_string(doc)
                lemma_du=lemma_du.replace(sinon[0],(' '+j+' '))
                lemma_du=clear_input_string(lemma_du)
                lemma_doc = nlp(lemma_du)
                create_lexical_entry(lemma_du,lemma_doc,index,sinon_cont,lexical_data)
                sinon_cont+=1
            if row_data['espressioni']!='none':
               lemma_du=create_lemma_string(doc)
               j=row_data['espressioni']
               lemma_du=lemma_du.replace(sinon[0],(' '+j+' '))
               lemma_du=clear_input_string(lemma_du)
               lemma_doc = nlp(lemma_du)
               create_lexical_entry(du,lemma_doc,index,sinon_cont,lexical_data)
               sinon_cont+=1
           
                

        

json = json.dumps(lexical_entry)
f = open("dict.json","w")
f.write(json)
f.close()

 
f = open("dict.pkl","wb")
pickle.dump(lexical_entry,f)
f.close()





    
# for ent in doc.ents:
#     print(ent.text, ent.start_char, ent.end_char, ent.label_)    

#nlp = spacy.load('it')