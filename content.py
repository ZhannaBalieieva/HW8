from models import Authors, Quotes, TagQuotes, QuotQuotes



if __name__=='__main__':
    albert = Authors(fullname = 'Albert Einstein', born_date = 'March 14, 1879', location ='Ulm, Germany', description = 'He completed his Ph.D. at the University of Zurich by 1909. His 1905 paper explaining the photoelectric effect, the basis of electronics, earned him the Nobel Prize in 1921. His first paper on Special Relativity Theory, also published in 1905, changed the world. After the rise of the Nazi party, Einstein made Princeton his permanent home, becoming a U.S. citizen in 1940.').save()

if __name__=='__main__':
    steve = Authors(fullname = 'Steve Martin', born_date ="August 14, 1945", location="in Waco, Texas, The United States", description='Martin is an American actor, comedian, writer, playwright, producer, musician, and composer.').save()


tag1_quote = TagQuotes(name='change, deep-thoughts, thinking, world') #einstein
tag2_quote = TagQuotes(name='inspirational, life, live, miracle, miracles') #einstein
tag3_quote = TagQuotes(name='adulthood, success, value') #einstein
tag4_quote = TagQuotes(name='humor, obvious, simile') #Steve



quote_1 = QuotQuotes(description='The world as we have created it is a process of our thinking.') 
quote_2 = QuotQuotes(description='There are only two ways to live your life.') 
quote_3 = QuotQuotes(description='Try not to become a man of success. Rather become a man of value') 
quote_4 = QuotQuotes(description='A day without sunshine is like, you know, night.') 
  

tags = [tag1_quote, tag2_quote, tag3_quote, tag4_quote]
quotes = [quote_1, quote_2, quote_3, quote_4]

Quotes(author = 'Albert Einstein', tags = [tag1_quote, tag2_quote, tag3_quote], quotes = [quote_1, quote_2, quote_3]).save()
Quotes(author = 'Steve Martin', tags = [tag4_quote, ], quotes = [quote_4, ]).save()
   


