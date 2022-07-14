from email import message
from imp import load_module
from pyexpat import model
import random
import json
from unittest import result
import numpy as np
import pickle
import nltk  #natural language toolkit
from nltk.stem import WordNetLemmatizer
from yaml import load  #all words from same stem are the same . ex:work,worked,working
import keras.models as mdl


lemmatizer=WordNetLemmatizer()

intents=json.loads(open('intents.json').read())

words=pickle.load(open('words.pkl','rb'))
classes=pickle.load(open('classes.pkl','rb'))
modell=mdl.load_model('Chatbot_Model.h5')


############ functions ################

def Cleanup_Sentence(sentence):
    sentence_words=nltk.word_tokenize(sentence)
    sentence_words=[lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words


def bagOfWords(sentence):
    bag=[0] * len(words)
    sentence_words=Cleanup_Sentence(sentence)
    for wrd in sentence_words:
        for i , word in enumerate(words):
            if word==wrd:
                bag[i]=1
    return np.array(bag)

def predictClass(sentence):
    BOW=bagOfWords(sentence)
    res=modell.predict(np.array([BOW]))[0]
    error_threshold=0.25
    results=[[i,r] for i , r in enumerate(res) if r>error_threshold]


    results.sort(key=lambda x:x[1],reverse=True)
    result_list=[]
    for r in results: 
        result_list.append({'intent':classes[r[0]],'probability':str(r[1])})
    return result_list

def get_response(intents_list,intents_json):
    tag=intents_list[0]['intent']
    listOfIntents=intents_json['intents']
    for i in listOfIntents:
        if i['tag']==tag:
            result=random.choice(i['responses'])
            break
    return result


########### main ##############

print("Talk to the bot! :)")
while True:
    message=input("")
    inst=predictClass(message)
    res= get_response(inst,intents)
    print(res)