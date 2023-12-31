# Obtain list of five words with more than 8 letters from random wikipedia page
# Steps: get page, get text, conver to list, get 5 random numbers, get five words

import requests
from bs4 import BeautifulSoup

def get_url():
    #set up scraper for page
    response = requests.get(
        url="https://en.wikipedia.org/wiki/Special:Random",
    )

    # verify getting valid response back and proceed if yes
    if (response.status_code) == 200:

        # Return url
        return response

    # try later if not working
    else:
        return 'Try again later'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # set up scraper for page
    response = requests.get(
        url="https://en.wikipedia.org/wiki/Special:Random",
    )
    # Get page and text
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()
    # Turn page text into list
    text_list = text.split()
    # Get 5 random numbers between

    print(text_list)
