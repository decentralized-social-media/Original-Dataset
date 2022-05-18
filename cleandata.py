#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 20:33:29 2022

@author: catherine
"""

import pandas as pd
data_df = pd.read_csv("/Users/catherine/Desktop/2.20.csv")
data_df.body=data_df.body.astype(str)

# Apply a first round of text cleaning techniques
import re
import string

CLEANR = re.compile('<.*?>') 

def cleanhtml(raw_html):
  cleantext = re.sub(CLEANR, '', raw_html)
  return cleantext

import emoji

def strip_emoji(text):
    new_text = emoji.replace_emoji(text, replace='')
    return new_text

def deEmojify(text):
    returnString = ""
    for character in text:
        try:
            character.encode("ascii")
            returnString += character
        except UnicodeEncodeError:
            returnString += ''
    return returnString

for each in range(0,len(data_df)):
    commenteach = re.sub(r"\S*https?:\S*", "", str(data_df['body'][each]))
    commenteach = cleanhtml(commenteach)
    commenteach = strip_emoji(commenteach)
    commenteach = deEmojify(commenteach)
    data_df['body'][each] = commenteach
  
def clean_text_round1(text):
    text = str(text)
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

round1 = lambda x: clean_text_round1(x)

data_clean = pd.DataFrame(data_df.body.apply(round1))
data_clean_location = pd.DataFrame(data_df.location.apply(round1))

def clean_text_round2(text):
    text = re.sub('[‘’“”…]', '', text)
    text = re.sub('\n',' ',text)
    text = re.sub(' +', ' ', text)
    return text

round2 = lambda x: clean_text_round2(x)
data_clean2 = pd.DataFrame(data_clean.body.apply(round2))
data_clean2.to_excel('/Users/catherine/Desktop/winterolympics1.xlsx')

