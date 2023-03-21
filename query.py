import argparse
from functools import wraps 
from pymongo import MongoClient
from pymongo.server_api import ServerApi


client = MongoClient("mongodb+srv://janna:1234@janna.km1452z.mongodb.net/test?retryWrites=true&w=majority", server_api=ServerApi('1'))

db = client.test

#пошуку цитат за тегом, за ім'ям автора або набором тегів. 

parser = argparse.ArgumentParser(description='CRUD quotes')
parser.add_argument('--action', help='Command: create, remove, find, update')
parser.add_argument('--id')
parser.add_argument('--quote')
parser.add_argument('--author')
parser.add_argument('--tags', nargs='+')


arguments = vars(parser.parse_args())

action = arguments.get('action') 
id_ = arguments.get('id')
quote = arguments.get('quote')
author = arguments.get('author')
tags = arguments.get('tags')

def create(author: str, quote: str, tags: list):
    result_many = db.quotes.insert_many(
    [
        
        {
          "tags": [
            "change",
            "deep-thoughts",
            "thinking",
            "world"
          ],
          "author": "Albert Einstein",
          "quote": "“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”"
        },
        {
          "tags": [
            "inspirational",
            "life",
            "live",
            "miracle",
            "miracles"
          ],
          "author": "Albert Einstein",
          "quote": "“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”"
        },
        {
          "tags": [
            "adulthood",
            "success",
            "value"
          ],
          "author": "Albert Einstein",
          "quote": "“Try not to become a man of success. Rather become a man of value.”"
        },
        {
          "tags": [
            "humor",
            "obvious",
            "simile"
          ],
          "author": "Steve Martin",
          "quote": "“A day without sunshine is like, you know, night.”"
        }
  ]  
)

    print(result_many.inserted_ids)

def find():
    return db.quotes.find()


































#from models import Quotes

#s#################  ОТРИМАННЯ ДАННИХ  ####################
 
##Скрипт виконується в нескінченному циклі і за допомогою звичайного оператора input приймає команди у наступному форматі

###https://www.youtube.com/watch?v=GQcLR9ELI2M  33:30

##пошук за набором тегів.       
#if __name__=='__main__':
#    tags = Quotes.objects()
#    for tag in tags:
#        print(tag.to_json())
#
##пошук цитат за тегом
#if __name__=='__main__':
#    quotes = Quotes.objects(tags)
#    for tag in quotes:
#        print(tag.to_json())


