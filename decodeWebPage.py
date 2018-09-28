# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.

from bs4 import BeautifulSoup
import requests

def web_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    print("Here are the news headlines from NYtimes: ")

    for title in soup.find_all('h2', {'class': "css-78b01r esl82me2"}):
        t = title.string
        if t is not None:
            print(t)

    for title in soup.find_all('h2', {'class': "css-8uvv5f esl82me2"}):
        t = title.string
        if t is not None:
            print(t)

web_page('http://www.nytimes.com')
