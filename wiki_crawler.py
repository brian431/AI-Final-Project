import requests
from bs4 import BeautifulSoup
import imdb
ia = imdb.IMDb()

def GetWikiURL(name):

    search_result = requests.get("https://en.wikipedia.org/w/index.php?search=" + name)

    if(search_result.status_code != 200):
        print("Some error Occured. Check the wiki website by your browser.")
        return ""

    if(search_result.url.find("search") != -1):
        soup = BeautifulSoup(search_result.text, "html.parser")
        a = soup.find("li" ,class_ = "mw-search-result mw-search-result-ns-0").findChild("div", class_="mw-search-result-heading").find("a")
        return("https://en.wikipedia.org" + a["href"]) 

    else:
        return search_result.url

def GetWikiPhotoURL(soup):
    
    a = soup.find("table",class_="infobox biography vcard").findChild("td",class_="infobox-image").findChild("a").findChild("img")
    return "https:"+a["src"]

def GetBirthDay(soup):
    return soup.find('span', class_ = 'bday').contents[0]


def GetIMDbPersonID(name):
    search = ia.search_person(name)
    return search[0].personID

def GetLatestMovies(personID):
    movies = []
    actor_results = ia.get_person_filmography(personID)

    for i in range(3):
        movie_name = actor_results['data']['filmography']['actor'][i]
        movies.append(movie_name)

    return movies