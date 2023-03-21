import json

Albert_authors = [
    {      
    "fullname": "Albert Einstein",
    "born_date": "March 14, 1879",
    "born_location": "in Ulm, Germany",
    "description": "In 1879, Albert Einstein was born in Ulm, Germany. He completed his Ph.D. at the University of Zurich by 1909. His 1905 paper explaining the photoelectric effect, the basis of electronics, earned him the Nobel Prize in 1921. His first paper on Special Relativity Theory, also published in 1905, changed the world. After the rise of the Nazi party, Einstein made Princeton his permanent home, becoming a U.S. citizen in 1940."
    }
             ]

Steve_authors = [
{
      "fullname": "Steve Martin",
      "born_date": "August 14, 1945",
      "born_location": "in Waco, Texas, The United States",
      "description": "Stephen Glenn \"Steve\" Martin is an American actor, comedian, writer, playwright, producer, musician, and composer. He was raised in Southern California in a Baptist family, where his early influences were working at Disneyland and Knott's Berry Farm and working magic and comedy acts at these and other smaller venues in the area. His ascent to fame picked up when he became a writer for the Smothers Brothers Comedy Hour, and later became a frequent guest on the Tonight Show."
    }
]

to_json = {'Albert': Albert_authors, 'Steve': Steve_authors}

with open('authors.json', 'w') as f:
    json.dump(to_json, f, sort_keys=True, indent=2)

with open('authors.json') as f:
    print(f.read())


