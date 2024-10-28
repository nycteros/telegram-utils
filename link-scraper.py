import requests
from bs4 import BeautifulSoup
import time

url = "https://t.me/LINKGOESHERE"

def scrape_telegram(url):
    start_time = time.time()
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Failed to retrieve the page")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    info = {'photo': 'n/a', 'description': 'n/a', 'elapsed': f"{round((time.time() - start_time) * 1000)}ms"}

    try:
        additional = soup.find('div', class_='tgme_page_additional').text.strip()
        info['type'] = 'channel' if 'view and join' in additional else 'user' if 'contact' in additional else None
        info['name'] = soup.find('div', class_='tgme_page_title').text.strip()
        
        description_tag = soup.find('div', class_='tgme_page_description')
        info['description'] = description_tag.text.strip() if description_tag else 'n/a'
        photo_tag = soup.find('div', class_='tgme_page_photo')
        info['photo'] = photo_tag.find('img')['src'] if photo_tag and photo_tag.find('img') else 'n/a'
        extra_tag = soup.find('div', class_='tgme_page_extra')
        info['extra'] = extra_tag.text.strip() if extra_tag else 'n/a'

        return {
            **info,
            'subscribers': info['extra'] if info['type'] == 'channel' else None,
            'username': info['extra'] if info['type'] == 'user' else None
        }
        
    except:
        return None

if __name__ == "__main__":

    channel_info = scrape_telegram(url)
    if channel_info:
        print("Link Type:", channel_info['type'])
        if channel_info['type'] == 'channel':
            print("Channel Name:", channel_info['name'])
            print("Photo:", channel_info['photo'])
            print("Subscribers:", channel_info['subscribers'])
            print("Description:", channel_info['description'])
        elif channel_info['type'] == 'user':
            print("Displayname:", channel_info['name'])
            print("Username:", channel_info['username'])
            print("Photo:", channel_info['photo'])
            print("Bio:", channel_info['description'])
        print("Elapsed Time:", channel_info['elapsed'])

    else:
        print("Link Type: invalid")

#                                   888           d88P  .d8888b. 
#                                   888          d88P  d88P  Y88b
#                                   888         d88P        .d88P
#        88888b.  888  888  .d8888b 888888     d88P        8888" 
#        888 "88b 888  888 d88P"    888        Y88b         "Y8b.
#        888  888 888  888 888      888         Y88b   888    888
#        888  888 Y88b 888 Y88b.    Y88b.        Y88b  Y88b  d88P
#        888  888  "Y88888  "Y8888P  "Y888        Y88b  "Y8888P" 
#                      888                                       
#                 Y8b d88P                                       
#                  "Y88P"                                        
