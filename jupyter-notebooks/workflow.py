
# coding: utf-8

# # Przetwarzanie tekstu na przykładzie strumienia danych z Twittera
# 

# ## 1. Przetwarzanie tekstu (NLP)

# ### 1.1 Przykładowe przetwarzanie tekstu
# 
# Poniższa komórka implementuje funkcję, która przyjmuje ciąg znaków (zmienną typu STRING) jako argument, modyfikuje ją i zwraca zmodyfikowaną wersję

# In[5]:

def sample_processing(text):
    return text + ur" #uam #bigdata #postgraduaté"

sample_text = "This is a sample text. It will be modified by sample_processing function."
processed_text = sample_processing(sample_text)
print processed_text


# ### 1.2 Ekstrakcja hashtagów za pomocą wyrażeń regularnych
# 
# Poniższa komórka implementuje funkcję, która tworzy listę hashtagów występujących w tweecie.
# 
# https://docs.python.org/2/library/re.html

# In[6]:

import re

def get_hashtags_list(tweet_text):
    m = re.findall(ur'#\w+', tweet_text, re.LOCALE)
    return m

print get_hashtags_list("Some sample tweet with some #hashtag, then some text and then #anotherhashtag again #YOLO")


# ### 1.3 Tokenizacja tweetów
# Poniższa komórka implementuje funkcję, która dzieli tekst tweeta na listę tokenów.
# 
# http://www.nltk.org/api/nltk.tokenize.html

# In[48]:

import nltk
import re
from nltk.tokenize import TweetTokenizer


tokenizer = TweetTokenizer()

def tokenize_tweets(tweet_text):
    tokens = tokenizer.tokenize(tweet_text.lower())
#     filtered_tokens = []
#     for token in tokens:
#         if clear_regex.search(token):
#             filtered_tokens.append(token)
    return tokens

print tokenize_tweets("What is going on here? We went there yesterday. Where have you gone? I am meeting you tomorrow. Where do we have our meeting? Some sample tweet with some #hashtag, then some text and then #anotherhashtag again #YOLO. You aren't a bad Pyprogrammer")
# wpisz tutaj swoją funkcję


# ### 1.4 Stemming tokenów
# Poniższa komórka implementuje funkcję, która bierze jako argument listę tokenów i zwraca listę stemów.
# 
# http://www.nltk.org/api/nltk.stem.html<br>
# http://www.nltk.org/howto/stem.html

# In[50]:

from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("english")

def stem_tokens(token_list):
    stem_list = []
    for token in token_list:
        stem_list.append(stemmer.stem(token))
        
    return stem_list

my_token_list = [u'what', u'is', u'going', u'on', u'here', u'?', u'we', u'went', u'there', u'yesterday', u'.', u'where', u'have', u'you', u'gone', u'?', u'i', u'am', u'meeting', u'you', u'tomorrow', u'.', u'where', u'do', u'we', u'have', u'our', u'meeting', u'?', u'some', u'sample', u'tweet', u'with', u'some', u'#hashtag', u',', u'then', u'some', u'text', u'and', u'then', u'#anotherhashtag', u'again', u'#yolo', u'.', u'you', u"aren't", u'a', u'bad', u'pyprogrammer']

print stem_tokens(my_token_list)


# ### 1.5 Lematyzacja tweetów
# Poniższa komórka implementuje funkcję, która przyjmuje tekst tweeta jako argument i zwraca jego zlematyzowaną wersję.
# 
# http://www.nltk.org/_modules/nltk/stem/wordnet.html

# In[59]:

from nltk import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

def lemmatize_tokens(token_list):
    lemma_list = []
    for token in token_list:
        lemma_list.append(lemmatizer.lemmatize(token))
        
    return lemma_list

my_token_list = [u'i', u'am', u'meeting', u'you', u'tomorrow', u'.', u'where', u'do', u'we', u'have', u'our', u'meeting', u'?', u'some', u'sample', u'tweet', u'with', u'some', u'#hashtag', u',', u'then', u'some', u'text', u'and', u'then', u'#anotherhashtag', u'again', u'#yolo', u'.', u'you', u"aren't", u'a', u'bad', u'pyprogrammer']
print lemmatize_tokens(my_token_list)


# ### 1.6 Lematyzacja przy użyciu części zdania (PoS tagging)
# Poniższa komórka implementuje funkcję, która przyjmuje tekst tweeta jako argument i zwraca listę par (token, część zdania).
# Następnie kolejna funkcja lematyzuje parę token w oparciu o rozpoznaną część zdania.
# 
# http://www.nltk.org/api/nltk.tag.html<br>
# http://www.nltk.org/book/ch05.html

# In[60]:

print lemmatizer.lemmatize('meeting')
print lemmatizer.lemmatize('meeting', 'v')

from nltk import pos_tag

from nltk.corpus import wordnet

def get_wordnet_pos(treebank_tag):

    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN


pos_tagger = FeaturesetTaggerI()

def lemmatize_tokens_pos(token_list):
    token_pos_list = pos_tag(token_list)
    lemma_list = []
    for token_pos in token_pos_list:
        word = token_pos[0]
        treebank_pos = token_pos[1]
        wordnet_pos = get_wordnet_pos(treebank_pos)
        lemma_list.append(lemmatizer.lemmatize(word, wordnet_pos))
        
    return lemma_list

my_token_list = [u'i', u'am', u'meeting', u'you', u'tomorrow', u'.', u'where', u'do', u'we', u'have', u'our', u'meeting', u'?', u'some', u'sample', u'tweet', u'with', u'some', u'#hashtag', u',', u'then', u'some', u'text', u'and', u'then', u'#anotherhashtag', u'again', u'#yolo', u'.', u'you', u"aren't", u'a', u'bad', u'pyprogrammer']

print lemmatize_tokens_pos(my_token_list)


# ### 1.7 Filtrowanie tokenów nie zawierających słów
# 
# Poniższa komórka implementuje funkcję, która filtruje z listy tokenów tokeny nie zawierające żadnego znaku alfanumerycznego.

# In[80]:

clear_regex = re.compile(ur'\w')

def filter_punctuation(token_list):
    filtered_tokens = []
    for token in token_list:
        if clear_regex.search(token):
            filtered_tokens.append(token)
    
    return filtered_tokens

lemma_tokens = [u'i', u'be', u'meeting', u'you', u'tomorrow', u'.', u'where', u'do', u'we', u'have', u'our', u'meeting', u'?', u'some', u'sample', u'tweet', u'with', u'some', u'#hashtag', u',', u'then', u'some', u'text', u'and', u'then', u'#anotherhashtag', u'again', u'#yolo', u'.', u'you', u"aren't", u'a', u'bad', u'pyprogrammer']
print filter_punctuation(lemma_tokens)


# ### 1.8 Filtrowanie słów o małym znaczeniu 
# 
# Filtrowanie słów o małym znaczeniu odbywa się przy wykorzystaniu stop-list (ang. stopwords). Poniższa komórka wczytuje zapisaną na dysku listę z pliku tekstowego oraz implementuje funkcję, która w oparciu o tę listę filtruje słowa o małym znaczeniu.

# In[75]:

with open ('common-english-words.txt', 'r') as stopwords_file:
    raw_stopwords = stopwords_file.readlines()
    
stopwords = raw_stopwords[0].split(',')

def filter_stopwords(token_list, stopwords_list):
    filtered_tokens = []
    for token in token_list:
        if token not in stopwords_list:
            filtered_tokens.append(token)
    return filtered_tokens

lemma_tokens = [u'i', u'be', u'meeting', u'you', u'tomorrow', u'where', u'do', u'we', u'have', u'our', u'meeting', u'some', u'sample', u'tweet', u'with', u'some', u'#hashtag', u'then', u'some', u'text', u'and', u'then', u'#anotherhashtag', u'again', u'#yolo', u'you', u"aren't", u'a', u'bad', u'pyprogrammer']
print filter_stopwords(lemma_tokens, stopwords)


# ### 1.9 Analiza sentymentalna tweetów

# In[79]:

from nltk.sentiment.vader import SentimentIntensityAnalyzer

sentiment_analyzer = SentimentIntensityAnalyzer()

def calculate_tweet_sentiment(tweet_sentence):
    scores = sentiment_analyzer.polarity_scores(tweet_sentence)
    return scores['compound']

print calculate_tweet_sentiment("What is going on here? We went there yesterday. Where have you gone? I am meeting you tomorrow. Where do we have our meeting? Some sample tweet with some #hashtag, then some text and then #anotherhashtag again #YOLO. You aren't a bad Pyprogrammer")


# ### 1.10 Rozpoznawanie encji (ang. Named entity recognition)
# Rozpoznawanie encji polega na indentyfikacji w zdaniach tokenów posiadających szczególne znaczenie. Typowe encje, które rozpoznaje się w tym procesie to: Osoba, Miejsce, Organizacja, Czas.
# Poniższa komórka implementuje metodę, która zwraca listy osób, miejsc i organizacji w danym tweecie.

# In[76]:

# wpisz tutaj swoją funkcję


# ## 2. Streaming danych z Twittera

# ### 2.1 Ustawienia kluczy i tokenów dla API Twittera
# 
# W poniższej komórce ustawiane są zmienne niezbędne do uzyskania połączenia z API Twittera. Uzupełnij zmienne o swoje wartości kluczy i tokenów

# In[12]:

access_token = "2362404584-MJuLY5ISJq3CFxyDTVhuhI6rRjygCDxd9QYEzWg"
access_token_secret = "pGD3PyMuz5M6YxzCkAryaytkPD0Eb2lF8q2aI9mNgg07o"
consumer_key = "uOO1duKiGl0jaRBA9dRvewGXd"
consumer_secret = "Odsld4Q5fAB9mk9VSJQUPYGDWcepOOUEZZk08Ya9CIR54szd4k"


# ### 2.2 Implementacja klasy służącej do Streamingu danych z Twittera
# 
# W poniższej komórce implementowana jest klasa służąca do pobierania streamu danych z Twittera. Klasa ta dziedziczy klasę StreamListener pochodzącą z biblioteki tweepy (biblioteki służącej do łączenia się z API Twittera za pomocą Pythona).
# Implementacja poniższej klasy modyfikuje domyślną metodę on_status(), która uruchamiana jest przy pojawieniu się każdego nowego statusu (tweeta) na Twitterze. 
# 
# Funkcja on_status() zapisuje każdego tweeta do bazy danych Elasticsearch.

# In[111]:

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
        tokens = tokenize_tweets(processed_text)
        stems = stem_tokens(tokens)
        lemmas = lemmatize_tokens_pos(tokens)
        filtered_tokens = filter_punctuation(tokens)
        filtered_tokens = filter_stopwords(filtered_tokens, stopwords)
        sentiment = calculate_tweet_sentiment(processed_text)        
        
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
                "hashtags_list": hashtags_list,
#                 "stems": stems,
#                 "lemmas": lemmas,
                "tokens": filtered_tokens,
                "sentiment": sentiment})

        
        print "text" + text
        print sentiment
        
        return True
    
    def on_error(self, status):
        print(status)


# ### 2.3 Nawiązanie połączenia z API Twittera i uruchomienie stremingu
# 
# W poniższej komórce nawiązywane jest połączenie z Twitterem za pomocą danych uwierzytelniających użytkownika a następnie uruchamiany jest 20 sekundowy streaming danych z przykładowym filtrem.

# In[112]:

import time

#This handles Twitter authetification and the connection to Twitter Streaming API
listener = StreamProcessingListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, listener)

#This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
stream.filter(track=['LePen'], languages=['en'], async=True)
time.sleep(60)
stream.disconnect()

