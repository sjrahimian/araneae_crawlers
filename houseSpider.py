# Sama Rahimian, v0.1
#
# a common house spider worldwide.
# currently does: access (url given by user), pull information, & search (arg) if data contains desired element
# future direction: clean/remove unwanted tags, and store user information in format choice
#

import requests
from bs4 import BeautifulSoup
import sys

print("Chiracanthium inclusum -- Yellow sac spider --\n\t\t For any HTML based web pages")


def magic():

    # Pull website information
    # url = "http://www-rohan.sdsu.edu/~gawron/index.html"
    # url = 'https://www.facebook.com/groups/508623379505116/permalink/589202604780526/'
    url = "http://" + sys.argv[2]

    response = requests.get(url)
    raw_data = response.content.decode('utf-8','ignore')

    print("%s, len: %s" % (type(raw_data), len(raw_data)))

    soup = BeautifulSoup(raw_data, 'html.parser')

    edibleSoup = soup.prettify()

    # print(edibleSoup)
    findArg = str(sys.argv[1])
    if edibleSoup.find(findArg.lower()):
        print(True)
        print(edibleSoup.find(sys.argv[1]))
    else:
        print(False)
        print(edibleSoup)


def main():
    print('Number of arg: ', len(sys.argv), "\nList of arg: ", str(sys.argv))
    magic()


main()