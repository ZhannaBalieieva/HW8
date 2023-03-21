from mongoengine import connect, Document, CASCADE, ListField, StringField, ReferenceField

connect(host="mongodb://127.0.0.1:27017/my_db")

class Authors(Document):
    fullname = StringField()
    born_date = StringField(max_length=100)
    location = StringField(max_length=100)
    description = StringField(max_length=1000, min_length=5)
    meta = {'allow_inheritance': True}
    
class Quotes(Document):
    author = ReferenceField(Authors, reverse_delete_rule=CASCADE)
    quotes = StringField()
    tags = ListField()
    meta = {'allow_inheritance': True}


class TagQuotes(Quotes):
    name = ListField()
    tag1_quote = ListField()
    tag2_quote = ListField()
    tag3_quote = ListField()
    tag4_quote = ListField()
    
    
    
class QuotQuotes(Quotes):
    tags = ListField()
    description = StringField()
    quote_1 = StringField()
    quote_2 = StringField()
    quote_3 = StringField()
    quote_4 = StringField()




    

















