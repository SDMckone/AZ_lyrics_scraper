import requests
from bs4 import BeautifulSoup


# Author: Sean McKone
# Simple lyrics scraper
# Scrapes from azlyrics.com using Requests and BeautifulSoup4

def scraper(artist_name, song_name):
    try:
        artist_name = artist_name.replace(" ", "").lower()
        song_name = song_name.replace(" ", "").lower()

        URL = 'https://www.azlyrics.com/lyrics/' + artist_name + '/' + song_name + '.html'
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find('div', class_='col-xs-12 col-lg-8 text-center')
        nextResults = results.find_all("div")
        songLyrics = nextResults[5].get_text().strip()

        return songLyrics

    except AttributeError:
        return 'Not a valid artist/song combination.'


def main():
    print('Enter artist name and song title to get lyrics, enter "q" to quit.')
    while True:
        artist_name = input("Enter artist name: ")
        if artist_name == 'q':
            break

        song_name = input("Enter song name: ")
        if song_name == 'q':
            break

        print('-' * 50)
        print(scraper(artist_name, song_name))
        print('-' * 50)


if __name__ == '__main__':
    main()
