import requests
from bs4 import BeautifulSoup
from collections import Counter

newList = []  #list to store the links
title = []    #list to store the titles

def getLinksfromDomain(domain) :
    page = requests.get(domain)
    bsoup = BeautifulSoup(page.content, 'html.parser')
    links = bsoup.find_all('a')

    for link in links :
        if 'href' in link.attrs :
            newList.append(str(link.attrs['href'])) #Storing the ResultSet to a List
    print("Loading the titles... \n")
    getTitle()
        

def getTitle() :
    try :
        for sublink in newList :
            title.append(extractTitle(sublink)) #this is right

        print(*title, sep="\n") #to display all the titles from the list called 'title'
    except :
        print("Something went wrong")
    finally :
        # for x in title :
        #     print(x.get_text())
        print(*title, sep="\n") #print the list anyways
        a = ' '.join(title)
        freq = Counter(a.split()).most_common()
        print("\n")
        print(freq)
        # print(a)


def extractTitle(sub_link) :
    webpage = requests.get(sub_link)
    bsoup2 = BeautifulSoup(webpage.content, 'html.parser')
    title_text = bsoup2.find('title')
    return title_text.get_text() #get only the text and exclude the <tags>

getLinksfromDomain("https://www.tutorialspoint.com")   #calling the 1st method