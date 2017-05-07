
# coding: utf-8

# # Przetwarzanie tekstu na przykładzie strumienia danych z Twittera
# 

# ## 1. Przetwarzanie tekstu (NLP)

# ### 1.1 Przykładowe przetwarzanie tekstu
# 
# Poniższa komórka implementuje funkcję, która przyjmuje ciąg znaków (zmienną typu STRING) jako argument, modyfikuje ją i zwraca zmodyfikowaną wersję

# In[3]:

def sample_processing(text):
    pass

sample_text = "This is a sample text. It will be modified by sample_processing function."
processed_text = sample_processing(sample_text)
print processed_text


# ### 1.2 Ekstrakcja hashtagów za pomocą wyrażeń regularnych
# 
# Poniższa komórka implementuje funkcję, która tworzy listę hashtagów występujących w tweecie.
# 
# https://docs.python.org/2/library/re.html

# In[4]:

import re

def get_hashtags_list(tweet_text):
    pass


# ### 1.3 Czyszczenie tweetów za pomocą wyrażeń regularnych
# Poniższa komórka implementuje funkcję, która za pomocą wyrażeń regularnych czyści tweety z linków, nazw użytkowników, itp.

# In[ ]:

# wpisz tutaj swoją funkcję


# ### 1.3 Tokenizacja tweetów
# Poniższa komórka implementuje funkcję, która dzieli tekst tweeta na listę tokenów.
# 
# http://www.nltk.org/api/nltk.tokenize.html

# In[5]:

import nltk

# wpisz tutaj swoją funkcję


# ### 1.4 Stemming tokenów
# Poniższa komórka implementuje funkcję, która bierze jako argument listę tokenów i zwraca listę stemów.
# 
# http://www.nltk.org/api/nltk.stem.html<br>
# http://www.nltk.org/howto/stem.html

# In[6]:

# wpisz tutaj swoją funkcję


# ### 1.5 Lematyzacja tweetów
# Poniższa komórka implementuje funkcję, która przyjmuje tekst tweeta jako argument i zwraca jego zlematyzowaną wersję.
# 
# http://www.nltk.org/_modules/nltk/stem/wordnet.html

# In[7]:

# wpisz tutaj swoją funkcję


# ### 1.6 Lematyzacja przy użyciu części zdania (PoS tagging)
# Poniższa komórka implementuje funkcję, która przyjmuje tekst tweeta jako argument i zwraca listę par (token, część zdania).
# Następnie kolejna funkcja lematyzuje parę token w oparciu o rozpoznaną część zdania.
# 
# http://www.nltk.org/api/nltk.tag.html<br>
# http://www.nltk.org/book/ch05.html

# In[8]:

# wpisz tutaj swoją funkcję


# ### 1.7 Filtrowanie tokenów nie zawierających słów
# 
# Poniższa komórka implementuje funkcję, która filtruje z listy tokenów tokeny nie zawierające żadnego znaku alfanumerycznego.

# In[9]:

# wpisz tutaj swoją funkcję


# ### 1.8 Filtrowanie słów o małym znaczeniu 
# 
# Filtrowanie słów o małym znaczeniu odbywa się przy wykorzystaniu stop-list (ang. stopwords). Poniższa komórka wczytuje zapisaną na dysku listę z pliku tekstowego oraz implementuje funkcję, która w oparciu o tę listę filtruje słowa o małym znaczeniu.

# In[10]:

clear_regex = re.compile(ur'\w')

def filter_tokens(token_list):
    filtered_tokens = []
    for token in token_list:
        if clear_regex.search(token):
            filtered_tokens.append(token)
    
    return filtered_tokens

lemma_tokens = [u'i', u'be', u'meeting', u'you', u'tomorrow', u'.', u'where', u'do', u'we', u'have', u'our', u'meeting', u'?', u'some', u'sample', u'tweet', u'with', u'some', u'#hashtag', u',', u'then', u'some', u'text', u'and', u'then', u'#anotherhashtag', u'again', u'#yolo', u'.', u'you', u"aren't", u'a', u'bad', u'pyprogrammer']
print filter_tokens(lemma_tokens)


# ### 1.9 Analiza sentymentalna tweetów
# Analiza sentymentalna polega na rozpoznaniu emocji występujących w tekście. Poniższa komórka implementuje metodę obliczającą pewną miarę liczbową sentymentu.
# 
# https://github.com/cjhutto/vaderSentiment<br>
# http://www.nltk.org/_modules/nltk/sentiment/vader.html

# In[16]:

# wpisz tutaj swoją funkcję


# ### 1.10 Rozpoznawanie encji (ang. Named entity recognition)
# Rozpoznawanie encji polega na indentyfikacji w zdaniach tokenów posiadających szczególne znaczenie. Typowe encje, które rozpoznaje się w tym procesie to: Osoba, Miejsce, Organizacja, Czas.
# Poniższa komórka implementuje metodę, która zwraca listy osób, miejsc i organizacji w danym tweecie.

# In[12]:

# wpisz tutaj swoją funkcję


# ## 2. Streaming danych z Twittera

# ### 2.1 Ustawienia kluczy i tokenów dla API Twittera
# 
# W poniższej komórce ustawiane są zmienne niezbędne do uzyskania połączenia z API Twittera. Uzupełnij zmienne o swoje wartości kluczy i tokenów

# In[13]:

access_token = "FILL IN WITH YOUR ACCESS TOKEN"
access_token_secret = "FILL IN WITH YOUR ACCESS TOKEN SECRET"
consumer_key = "FILL IN WITH YOUR CONSUMER KEY"
consumer_secret = "FILL IN WITH YOUR CONSUMER KEY SECRET"


# ### 2.2 Implementacja klasy służącej do Streamingu danych z Twittera
# 
# W poniższej komórce implementowana jest klasa służąca do pobierania streamu danych z Twittera. Klasa ta dziedziczy klasę StreamListener pochodzącą z biblioteki tweepy (biblioteki służącej do łączenia się z API Twittera za pomocą Pythona).
# Implementacja poniższej klasy modyfikuje domyślną metodę on_status(), która uruchamiana jest przy pojawieniu się każdego nowego statusu (tweeta) na Twitterze. 
# 
# Funkcja on_status() zapisuje każdego tweeta do bazy danych Elasticsearch.

# In[14]:

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


# ### 2.3 Nawiązanie połączenia z API Twittera i uruchomienie stremingu
# 
# W poniższej komórce nawiązywane jest połączenie z Twitterem za pomocą danych uwierzytelniających użytkownika a następnie uruchamiany jest 20 sekundowy streaming danych z przykładowym filtrem.

# In[15]:

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

