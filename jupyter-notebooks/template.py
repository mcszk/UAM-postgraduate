
# coding: utf-8

# # Przetwarzanie tekstu na przykładzie strumienia danych z Twittera
# 

# ## Przykładowe przetwarzanie tekstu
# 
# Poniższa komórka implementuje funkcję, która przyjmuje ciąg znaków (zmienną typu STRING) jako argument, modyfikuje ją i zwraca zmodyfikowaną wersję

# In[10]:

def sample_processing(text):
    pass

sample_text = "This is a sample text. It will be modified by sample_processing function."
processed_text = sample_processing(sample_text)
print processed_text


# ## Ekstrakcja hashtagów za pomocą wyrażeń regularnych
# 
# Poniższa komórka implementuje funkcję, która tworzy listę hashtagów występujących w tweecie.
# 
# https://docs.python.org/2/library/re.html

# In[2]:

import re

def get_hashtags_list(tweet_text):
    pass


# ## Tokenizacja tweetów
# Poniższa komórka implementuje funkcję, która dzieli tekst tweeta na listę tokenów.
# 
# http://www.nltk.org/api/nltk.tokenize.html

# In[4]:

import nltk

# wpisz tutaj swoją funkcję


# ## Stemming tokenów
# Poniższa komórka implementuje funkcję, która bierze jako argument listę tokenów i zwraca listę stemów.
# 
# http://www.nltk.org/api/nltk.stem.html<br>
# http://www.nltk.org/howto/stem.html

# In[ ]:

# wpisz tutaj swoją funkcję


# ## Lematyzacja tweetów
# Poniższa komórka implementuje funkcję, która przyjmuje tekst tweeta jako argument i zwraca jego zlematyzowaną wersję.
# 
# http://www.nltk.org/_modules/nltk/stem/wordnet.html

# In[ ]:

# wpisz tutaj swoją funkcję


# ## Lematyzacja przy użyciu części zdania (PoS tagging)
# Poniższa komórka implementuje funkcję, która przyjmuje tekst tweeta jako argument i zwraca listę par (token, część zdania).
# Następnie kolejna funkcja lematyzuje parę token w oparciu o rozpoznaną część zdania.
# 
# http://www.nltk.org/api/nltk.tag.html<br>
# http://www.nltk.org/book/ch05.html

# In[6]:

# wpisz tutaj swoją funkcję


# ## Analiza sentymentalna tweetów

# In[7]:

# wpisz tutaj swoją funkcję


# ## Ustawienia kluczy i tokenów dla API Twittera
# 
# W poniższej komórce ustawiane są zmienne niezbędne do uzyskania połączenia z API Twittera. Uzupełnij zmienne o swoje wartości kluczy i tokenów

# In[11]:

access_token = "FILL IN WITH YOUR ACCESS TOKEN"
access_token_secret = "FILL IN WITH YOUR ACCESS TOKEN SECRET"
consumer_key = "FILL IN WITH YOUR CONSUMER KEY"
consumer_secret = "FILL IN WITH YOUR CONSUMER KEY SECRET"


# ## Implementacja klasy służącej do Streamingu danych z Twittera
# 
# W poniższej komórce implementowana jest klasa służąca do pobierania streamu danych z Twittera. Klasa ta dziedziczy klasę StreamListener pochodzącą z biblioteki tweepy (biblioteki służącej do łączenia się z API Twittera za pomocą Pythona).
# Implementacja poniższej klasy modyfikuje domyślną metodę on_status(), która uruchamiana jest przy pojawieniu się każdego nowego statusu (tweeta) na Twitterze. 
# 
# Funkcja on_status() zapisuje każdego tweeta do bazy danych Elasticsearch.

# In[9]:

#Import the necessary methods from tweepy library
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

class StreamProcessingListener(StreamListener):

     def on_status(self, status):
        description = status.user.description
        loc = status.user.location
        text = status.text
        coords = status.coordinates
        name = status.user.screen_name
        user_created = status.user.created_at
        followers = status.user.followers_count
        id_str = status.id_str
        created = status.created_at
        retweets = status.retweet_count
        bg_color = status.user.profile_background_color
        
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
                "bg_color": bg_color})
        
        print text
        
        return True
    
     def on_error(self, status):
        print(status)


# ## Nawiązanie połączenia z API Twittera i uruchomienie stremingu
# 
# W poniższej komórce nawiązywane jest połączenie z Twitterem za pomocą danych uwierzytelniających użytkownika a następnie uruchamiany jest 20 sekundowy streaming danych z przykładowym filtrem.

# In[10]:

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

