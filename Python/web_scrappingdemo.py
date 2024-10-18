#what is web scrapping ?
'''
Request Module for making HTTP Requested to the desired website .
BeautifulSoup module for python that allows get the data from the desired web page.
'''
from gettext import textdomain

#Example of applying scrapping on some web sites.
import requests
from bs4 import BeautifulSoup
import pandas as pd
#Have the page to scarp
url="http://www.bbc.com/news"
response=requests.get(url)

if response.status_code == 200:
    print("The page is avialable")
    soup = BeautifulSoup(response.content, 'html.parser')
    headlines=soup.find_all('h2',class_="sc-1207bea1-3 cZBSm")
    headlines_list=[]
    for headline in headlines:
        headlines_list.append(headline.getText())
    df=pd.DataFrame(headlines_list)
    print(df)
else:
    print(f"Failed to get the page:Status Code:{response.status_code}")
##################Reading Rest API########################
rest_url='http://localhost:1234/emplist'
rest_response=requests.get(rest_url)
if rest_response.status_code == 200:
    data = rest_response.json()
    for row in data:
        print(row)
#Etiquettes to be followed while doing web scrapping.
'''
1.API Rate Limiting :When you are accessing web apis, there shall be acertain 
linit within a time frame for allowing anonymous users access 
2.Ethical Scrapping:U may have to chek if the website allows scapping.U can review the websites's terms
'''
def scrap_page(url, parser = 'html.parser'):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, parser)
        return soup
    else:
        print(f"Failed to get the valid response:Status Code:{response.status_code}")
        return None
def scrap_wiki():
    url = "https://en.wikipedia.org/wiki/Web_scraping"
    soup = scrap_page(url)

    if soup:
        title = soup.find('h1, {'id : 'firstHeading'}).text
        print(f"Title:{title}")

        first_paragraph = soup.find("p").text
        print(f"Content:{first_paragraph}")
def scap_flipkart():
    url = "https://www.flipkart.com/search?q=Iphone"
    soup = scrap_page(url)
    if soup:
        containers = soup.find_all("div")
    else:
        print("Not available for scrapping")


#scap_wiki





