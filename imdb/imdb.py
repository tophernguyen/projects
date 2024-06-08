
# $ pip install BeautifulSoup4
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re




def main():
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}

    url = "https://www.imdb.com/title/tt0374900/"
    page = requests.get(url, headers = headers)
    soup = BeautifulSoup(page.text,"html.parser")

    if page.status_code == 200:
        soup = BeautifulSoup(page.content, 'html.parser')
        title = soup.find('h1').text.strip()
        popularity = soup.find('div', class_="sc-5f7fb5b4-1 fTREEx").text
        summary = soup.find('span', {"data-testid": "plot-xs_to_m"}).text.strip()
        directors = [a.text for a in soup.find_all('a', class_="ipc-metadata-list-item__list-content-item")]
        cast_list = soup.find_all('a', {"data-testid": "title-cast-item__actor"})
        cast = [actor.text.strip() for actor in cast_list]
        top_review = soup.find('div', class_= "ipc-html-content ipc-html-content--base").text
        
        print(f"Title: {title}\n")
        print(f"Popularity: {popularity}\n")
        print(f"Summary: {summary}\n")
        print(f"Directors: {directors[0]}\n")
        print(f"Cast: {', '.join(cast)}\n")
        print(f"Top Review: {top_review}")

    else:
        print(f"Failed to retrieve the webpage. Status code: {page.status_code}")


if __name__ == '__main__':
    main()