
# coding: utf-8

# # Przetwarzanie tekstu na przykładzie strumienia danych z Twittera
# 

# ## Przykładowe przetwarzanie tekstu
# 
# Poniższa komórka implementuje funkcję, która przyjmuje ciąg znaków (zmienną typu STRING) jako argument, modyfikuje ją i zwraca zmodyfikowaną wersję

# In[59]:

def sample_processing(text):
    return text + ur" #uam #bigdata #postgraduaté"

sample_text = "This is a sample text. It will be modified by sample_processing function."
processed_text = sample_processing(sample_text)
print processed_text


# ## Ekstrakcja hashtagów za pomocą wyrażeń regularnych
# 
# Poniższa komórka implementuje funkcję, która tworzy listę hashtagów występujących w tweecie.
# 
# https://docs.python.org/2/library/re.html

# In[60]:

import re

def get_hashtags_list(tweet_text):
    m = re.findall(ur'#\w+', tweet_text, re.LOCALE)
    return m

print get_hashtags_list("Some sample tweet with some #hashtag, then some text and then #anotherhashtag again #YOLO")


# In[ ]:




# ## Tokenizacja tweetów
# Poniższa komórka implementuje funkcję, która dzieli tekst tweeta na listę tokenów.
# 
# http://www.nltk.org/api/nltk.tokenize.html

# In[61]:

import nltk

# wpisz tutaj swoją funkcję


# ## Stemming tokenów
# Poniższa komórka implementuje funkcję, która bierze jako argument listę tokenów i zwraca listę stemów.
# 
# http://www.nltk.org/api/nltk.stem.html<br>
# http://www.nltk.org/howto/stem.html

# In[62]:

# wpisz tutaj swoją funkcję


# ## Lematyzacja tweetów
# Poniższa komórka implementuje funkcję, która przyjmuje tekst tweeta jako argument i zwraca jego zlematyzowaną wersję.
# 
# http://www.nltk.org/_modules/nltk/stem/wordnet.html

# In[63]:

# wpisz tutaj swoją funkcję


# ## Lematyzacja przy użyciu części zdania (PoS tagging)
# Poniższa komórka implementuje funkcję, która przyjmuje tekst tweeta jako argument i zwraca listę par (token, część zdania).
# Następnie kolejna funkcja lematyzuje parę token w oparciu o rozpoznaną część zdania.
# 
# http://www.nltk.org/api/nltk.tag.html<br>
# http://www.nltk.org/book/ch05.html

# In[64]:

# wpisz tutaj swoją funkcję


# ## Analiza sentymentalna tweetów

# In[65]:

# wpisz tutaj swoją funkcję


# In[66]:

import re

def get_hashtags_list(tweet_text):
    m = re.findall(ur'#\w+', tweet_text, re.LOCALE)
    print m
    return m

get_hashtags_list("some tweet #hashtag, some sample text #andhashtagagain")


# ## Ustawienia kluczy i tokenów dla API Twittera
# 
# W poniższej komórce ustawiane są zmienne niezbędne do uzyskania połączenia z API Twittera. Uzupełnij zmienne o swoje wartości kluczy i tokenów

# In[67]:

access_token = "2362404584-MJuLY5ISJq3CFxyDTVhuhI6rRjygCDxd9QYEzWg"
access_token_secret = "pGD3PyMuz5M6YxzCkAryaytkPD0Eb2lF8q2aI9mNgg07o"
consumer_key = "uOO1duKiGl0jaRBA9dRvewGXd"
consumer_secret = "Odsld4Q5fAB9mk9VSJQUPYGDWcepOOUEZZk08Ya9CIR54szd4k"


# ## Implementacja klasy służącej do Streamingu danych z Twittera
# 
# W poniższej komórce implementowana jest klasa służąca do pobierania streamu danych z Twittera. Klasa ta dziedziczy klasę StreamListener pochodzącą z biblioteki tweepy (biblioteki służącej do łączenia się z API Twittera za pomocą Pythona).
# Implementacja poniższej klasy modyfikuje domyślną metodę on_status(), która uruchamiana jest przy pojawieniu się każdego nowego statusu (tweeta) na Twitterze. 
# 
# Funkcja on_status() zapisuje każdego tweeta do bazy danych Elasticsearch.

# In[68]:

#Import the necessary methods from tweepy library
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200/")


class StreamProcessingListener(StreamListener):

     def on_status(self, status):
        created_at = status.created_at
        text = status.text
        user_description = status.user.description
        user_location = status.user.location
        coords = status.coordinates
        user_name = status.user.screen_name
        user_created = status.user.created_at
        followers = status.user.followers_count
        id_str = status.id_str
        retweets = status.retweet_count
        bg_color = status.user.profile_background_color
        
        processed_text = sample_processing(text)
        hashtags_list = get_hashtags_list(processed_text)
        
        es.index(index="twitter",
             doc_type="tweet",
             body={
                "created_at": created_at,
                "text": text,
                "user_description": user_description,
                "user_location": user_location,
                "coords": coords,
                "user_name": user_name,
                "user_created": user_created,
                "followers": followers,
                "id_str": id_str,
                "retweets": retweets,
                "bg_color": bg_color,
                "processed_text": processed_text,
                "hashtags_list": hashtags_list})
        
        print text
        
        return True
    
     def on_error(self, status):
        print(status)


# ## Nawiązanie połączenia z API Twittera i uruchomienie stremingu
# 
# W poniższej komórce nawiązywane jest połączenie z Twitterem za pomocą danych uwierzytelniających użytkownika a następnie uruchamiany jest 20 sekundowy streaming danych z przykładowym filtrem.

# In[69]:

import time

#This handles Twitter authetification and the connection to Twitter Streaming API
listener = StreamProcessingListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, listener)

#This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
stream.filter(track=['LePen'], async=True)
time.sleep(20)
stream.disconnect()

