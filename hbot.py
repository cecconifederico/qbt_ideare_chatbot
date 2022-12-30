# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 10:39:54 2022

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
from operator import itemgetter


def clear_input_string(s):
    d = re.sub(" +", " ", s)
    d =d.strip()
    d=d.translate(str.maketrans('', '', string.punctuation))
    d=d.lower()
    return d

def create_lemma_string(d):
    result=''
    for token in d:
        result=result+token.lemma_+' '
    return result

    
def create_lexical_input(du,doc,index,indexdata,ld):
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
    lexical_input['le'+"_"+str(index)+"_"+str(indexdata)]=[du,lexical_tree,ld]


def find_root_indexes(input_list,base_list):
     input_root_index=-1
     root_pos=0
     for i in input_list:
         if i[2]=='ROOT':
             input_root_index=root_pos
         root_pos+=1
     base_root_index=-1    
     root_pos=0
     for i in base_list:
         if i[2]=='ROOT':
             base_root_index=root_pos
         root_pos+=1 
     return [input_root_index,base_root_index]    
 
def pattern_match_1(index1,index2,l1,l2):
    if l1[index1][0]==l2[index2][0]:
        return 100
    else:
        return 0
    
def pattern_match_2(index1,index2,l1,l2):
    v=0
    for i in l1[index1:]:
     for j in l2[index2:]:
         if i[0]==j[0]:
             v+=25
    return v         

def bot_engine(input_string):
   q_string = input_string
   q_string = clear_input_string(q_string)
   q_doc=nlp(q_string)
   q_lemma=create_lemma_string(q_doc)
   lexical_data={}
   create_lexical_input(q_string,q_doc,0,0,lexical_data)

   for lexical_key in lexical_entry:
       lexical_value=lexical_entry[lexical_key]
       input_value=lexical_input['le_0_0']
       #print(lexical_value[0])
       r_ids=find_root_indexes(input_value[1],lexical_value[1])
       r_value_1=pattern_match_1(r_ids[0],r_ids[1],input_value[1],lexical_value[1])
       #print(r_value_1)
       r_value_2=pattern_match_2(r_ids[0],r_ids[1],input_value[1],lexical_value[1])
       r_value=r_value_1+r_value_2
       if r_value > 0:
        output_list_tag_rank.append([lexical_key,lexical_value[0],r_value])

        
nlp = it_core_news_sm.load()

file_to_read = open("dict.pkl", "rb")
lexical_entry = pickle.load(file_to_read)
lexical_input={}
output_list_tag_rank=[]

#bot_engine('vorrei inserire le anagrafiche')
#bot_engine("vorrei modificare  elenco delle anagrafiche")

sg.theme('BluePurple')

layout = [[sg.Text('BOT'), sg.Text(size=(60,30), key='-OUTPUT-')],
          [sg.Input(key='-IN-')],
          [sg.Button('Help'), sg.Button('Exit')]]

window = sg.Window('Pattern 2B', layout)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Help':
        # Update the "output" text element to be the value of "input" element
        # window['-OUTPUT-'].update(values['-IN-'])
        output_list_tag_rank=[]
        bot_engine(values['-IN-'])
        output_list_tag_rank=sorted(output_list_tag_rank, key=itemgetter(2),reverse=True)
        listToStr=''
        for k in output_list_tag_rank:
            riga = ' '.join([str(elem) for elem in k])
            listToStr=listToStr + riga + '\n'
        window['-OUTPUT-'].update(listToStr)

window.close()


    
    
    
    
    
    
    
    