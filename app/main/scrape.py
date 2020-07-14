from bs4 import BeautifulSoup
import requests


HEADERS =  {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36"}


def get_story_thenews(url):

    soup = BeautifulSoup(requests.get(url,headers=HEADERS,timeout=160).text,'html.parser')
    story_div = soup.find('div',class_="story-detail")
    story_date = soup.find('div',class_="category-date").text
    heading = soup.find('div',class_='detail-heading').find('h1').text
    all_p = story_div.find_all('p')
    story = ""
    for p in all_p:
        story = story + p.text
    print(heading,story)
    print('------------------------')
    print(story_date)



def get_story_express(url):

    soup = BeautifulSoup(requests.get(url,headers=HEADERS,timeout=160).text,'html.parser')
    story_div = soup.find('span',class_="story-text")
    story_date = soup.find('div',class_="left-authorbox").find_all('span')[1].text
    heading = soup.find('div',class_='maincontent-customwidth storypage').find('h1').text
    all_p = story_div.find_all('p')
    story = ""
    for p in all_p:
        story = story + p.text
    print(heading,story)
    print('------------------------')
    print(story_date)    



def get_story_dawn(url):

    soup = BeautifulSoup(requests.get(url,headers=HEADERS,timeout=160).text,'html.parser')
    story_div = soup.find('article',class_="story")
    story_date = soup.find('span',class_="story__time").text
    heading = soup.find('h2',class_='story__title').find('a').text
    all_p = story_div.find_all('p')
    story = ""
    for p in all_p:
        story = story + p.text
    print(heading,story)
    print('------------------------')
    print(story_date)