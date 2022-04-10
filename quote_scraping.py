from bs4 import BeautifulSoup
import requests

URL =  "https://korean-binge.com/2022/02/14/100-quotes-from-twenty-five-twenty-one-korean-drama-2022/"

def get_quotes():
  response = requests.get(URL)
  
  if response.status_code != 200:
    print("Error: ", response.status_code)
    return None

  content = response.content
  soup = BeautifulSoup(content, "html.parser")

  main_div = soup.find("div", attrs={"class": "entry-content"})
  quotes_from_p = main_div.find_all("p")
  quotes_from_li = main_div.find_all("li")
  
  quotes = []
  for i in quotes_from_li + quotes_from_p:
    try:
      quotes.append(i.b.text)
    except:
      quotes.append(i.text)

  quotes = quotes[:len(quotes)-2]
  return quotes

def saveToCsv(quotes):
  with open("quotes.csv", "w", encoding='utf-8') as f:
    for quote in quotes:
      f.write(quote + "\n")

if __name__ == "__main__":
  quotes = get_quotes()
  saveToCsv(quotes)
