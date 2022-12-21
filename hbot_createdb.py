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

df = pd.read_excel('C:/Users/federico/Dropbox/Modelli/qbt/reftree_centralino_poc_bot/bot_data/BOT-Q&A-011222 (1).xlsx')

nlp = it_core_news_sm.load()

doc = nlp("Federico è molto stupido")

for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
            token.shape_, token.is_alpha, token.is_stop)

