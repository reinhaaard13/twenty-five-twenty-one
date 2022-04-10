from bs4 import BeautifulSoup
import requests
from urllib.request import URLopener

URL =  "https://www.hancinema.net/korean_drama_Twenty_Five_Twenty_One-picture_gallery.html"

def get_links_per_page(page_num):
  response = requests.get(URL + f'?p={page_num}', headers={'User-Agent': 'Mozilla/5.0'})
  
  if response.status_code != 200:
    print("Error: ", response.status_code)
    return None

  content = response.content
  soup = BeautifulSoup(content, "html.parser")

  main_div = soup.find_all("a", href=True)
  links = [x['href'] for x in main_div if x['href'].startswith('//photos.hancinema.net/photos/')]
  links = ["https:" + "/".join(x.split("/")[:-1]) + "/large" + x.split("/")[-1] for x in links]
  return links

def get_all_links():
  iteration = 15

  print("Starts scraping links...")
  links = []
  for i in range(iteration):
    print("Get links for page", i+1)
    page_links = get_links_per_page(i+1)
    links += page_links

  print("Finished scraping links...")
  return links

def download_images(links):
  print("Downloading images...")
  for link in links:
    try:
      opener = URLopener()
      opener.addheader('User-Agent', 'Mozilla/5.0')
      opener.retrieve(link, "images/" + link.split("/")[-1])
    except:
      continue

if __name__ == "__main__":
  links = get_all_links()
  download_images(links)
