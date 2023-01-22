import requests
import json
import time
from pathlib import Path
from PIL import Image
# using the ygoprodeck api https://ygoprodeck.com/api-guide/ to scrape every card image and a database of all card texts


class Scraper:
    def __init__(self):
        self.url = "https://images.ygoprodeck.com/images/cards/"
        self.counter = 0

    '''requests image from api and saves in Cards/<card_id>.jpg'''
    def get_image(self, card_id):
        new_url = self.url+card_id+".jpg"
        r = requests.get(new_url)
        print(r)
        self.counter += 1
        print(self.counter)
        file_name = "Data/Cards/"+card_id+".jpg"
        with open(file_name, 'wb') as f:
            f.write(r.content)

    '''creates_up to date database'''
    def create_card_db(self):
        r = requests.get("https://db.ygoprodeck.com/api/v7/cardinfo.php")
        with open("Data/card_db.json", 'wb') as f:
            f.write(r.content)

    ''' Checks db for images that have not been downloaded and calls get_images for those 
        Throttled since api allows max 20 calls per second
        Possibly use worker model instead of sleeps
        '''
    def get_images(self):
        with open("Data/card_db.json") as f:
            f = json.load(f)
            for card in f['data']:
                card_id = str(card['id'])
                if not Path('Data/Cards/'+card_id+'.jpg').is_file():
                    print("downloading:")
                    print(card_id)
                    self.get_image(card_id)
                    time.sleep(0.04)
                else:
                    print("already downloaded:")
                    print(card_id)


if __name__ == '__main__':
    s = Scraper()
    s.create_card_db()
    s.get_images()