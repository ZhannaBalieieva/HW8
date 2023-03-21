import pymongo
import json

    
with open('authors_many.json') as file:
    file_authors = json.load(file)
    
with open('quotes_many.json') as file:
    file_quotes = json.load(file)
    
# вставить данные из JSON в MongoDB Python, используя приведенный ниже код.(вставить в т3 терминал от test db)
#collection.insert_one(authors_data)
#    
    #quotes.json