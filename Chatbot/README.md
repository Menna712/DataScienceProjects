# General Purpose Chatbot

### General Purpose Chatbot is a bot implemented using deep learning NLP "Naural Lguage Pocessing" for genersl purpose as :
* Greetings
* Goodbyes
* Chatting about it's Identity
* Asking Questions about it's owner


------------------

## Getting Started
 ```py:
pip install numpy
pip install pickle-mixin
pip install nltk
pip install load
pip install tensorflow
pip install keras
pip install pandas
pip install torch
```

## Intents.Json
Intents.json is a JSON file containing all the words that chatbot can learn and predict.
Intents.json can be categorized to 3 Sub Categories:
* Tag : category of the Class
* Patterns : Training Words for the Chatbot to categorize the Class
* Responses : The response by the Chatbot according to the Class

##### For Example:
![image](https://user-images.githubusercontent.com/105871377/184518064-957f8cb4-c0a3-46ad-aeb8-5c6c53e33b63.png)



## Preparation.ipynb
### Description
Prepare the Data by splitting "Patterns" from "Intents" into smaller words as following


| words | word_patterns | 
| --- | --- | 
| [''s','how','you','are'] | ['hello']['hey']['what's up']  

then covert the words into integer values to prepare for Deep Learning Step as follows

![image](https://user-images.githubusercontent.com/105871377/184518229-884f0ecd-6cd4-48e6-a238-3de44e94a2c0.png)


the Model then is trained with accuracy of 86%
![image](https://user-images.githubusercontent.com/105871377/184518250-3ac11475-c3bf-47bc-a019-98ffa19ee49b.png)


## Chatbot.py
### Description
Chatbot.py is for creating the chatbot functions as:
* def Cleanup_Sentence : lemmatize words in the sentence
* def bagOfWords : function carrying the list of words in a sentence
* predictClass : function Predicting the class of the words extracted from bagOfWords Function
* get_response : Chooses and Prints Response from "Responses" in "Intents" JSON file according to the predicted Class
* main : Reads Input and Prints the Response according to Prediction


# Demo Result
### This is sample Result of Chatting with the General Purpose Chatbot

![image](https://user-images.githubusercontent.com/105871377/184518445-d42df7e0-3a63-44ce-9c5e-6780107ad3f3.png)
