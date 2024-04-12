import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

def create_playlist(url):
    playlist = "#EXTM3U\n"

    for page_num in range(1, 41):

        page_url = f"{url}?page{page_num}"


        response = requests.get(page_url)
        soup = BeautifulSoup(response.text, 'html.parser')


        track_items = soup.select("track-items.js-item")

        for track_item in track_items:
            track_url = track_item['data-track']
            track_title = track_item['data-title']
            track_artist = track_item['data-artist']

            playlist += f"#EXTINF:-1, {track_artist} - {track_title}\n{track_url}\n"

    parsed_url = urlparse(url)
    filename = parsed_url.path.split('/')[-1]

    with open(f"{filename}.m3u", "w", encoding="utf-8") as f:
        f.write(playlist)

    print(f"Плейлист успешно создан и сохранен в файле {filename}.m3u!")

if __name__ == "__main__":
    user_url = input("Введите URL страницы с музыкой: ")
    create_playlist(user_url)
