import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def main():
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
    url = "https://www.imdb.com/chart/boxoffice/?ref_=hm_cht_sm"
    response = requests.get(url, headers = headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        get_top_10 = soup.find_all('div', class_='ipc-metadata-list-summary-item__tc')
        movie_data = []
        rank = 1
        for movie in get_top_10:
            movie_dic = {}
            movie_dic['Rank'] = rank
            rank += 1
            #Movie Name
            movie_name = movie.find('h3', class_='ipc-title__text')
            movie_name = re.sub(r'^\d+\.\s', '', movie_name.text.strip())
            movie_dic['Movie Name'] = movie_name if movie_name else 'unknown movie name'
            # Extracting the specific 'li' elements for weekend gross, total gross, and weeks released
            box_office_data = movie.find('ul', {'data-testid': 'title-metadata-box-office-data-container'})
            if box_office_data:
                for li in box_office_data.find_all('li'):
                    key = li.find('span').get_text(strip=True).replace(':', '')
                    value = li.find('span', class_='sc-8f57e62c-2 elpuzG').get_text(strip=True)
                    movie_dic[key] = value

            # Ensuring keys are present even if not found
            movie_dic['Weekend Gross'] = movie_dic.get('Weekend Gross', 'unknown weekend gross')
            movie_dic['Total Gross'] = movie_dic.get('Total Gross', 'unknown total gross')
            movie_dic['Weeks Released'] = movie_dic.get('Weeks Released', 'unknown weeks released')


            movie_data.append(movie_dic)
     


        df = pd.DataFrame(movie_data)
        print(df)
 




        
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

if __name__ == '__main__':
    main()