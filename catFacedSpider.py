# Sama Rahimian, 0.1
# Access, pull, clean, & store ??????? posts

from urllib import request as request
from bs4 import BeautifulSoup
import nltk


print("Araneus gemmoides (\"Cat-faced Spider\") :: For ??????")


# Pull website information
url = 'https://www.facebook.com/groups/508623379505116/permalink/589202604780526/'

response = request.urlopen(url)
rawData = response.read().decode('utf-8')

print("%s, len: %s" % (type(rawData), len(rawData)))

soup = BeautifulSoup(rawData, 'html.parser')

edibleSoup = soup.prettify()

# print(edibleSoup)

if edibleSoup.find("Sam Joseph") == "Sam Joesph":
    print(True)
else:
    print(False)
