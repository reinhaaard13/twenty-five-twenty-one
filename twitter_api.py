import tweepy
import csv
import os

from constants import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_SECRET_TOKEN

class Tweepy:
  def __init__(self):
    self.T = tweepy.API(self.auth())
    self.recent_tweet = None

  def auth(self):
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET_TOKEN)
    return auth

  def getUserByID(self, id):
    return self.T.get_user(id)
    
  def getUsername(self, id):
    return self.getUserByID(id).screen_name
  
  def splitListByFourElement(self, l):
    return [l[i:i+4] for i in range(0, len(l), 4)]

  def loadLinks(self, version, numbers):
    links = [f"{version}/{version}{x}.jpg" for x in range(1, numbers+1)]
    links = self.splitListByFourElement(links)
    return links

  def postTweetWithImage(self, text, imagePath):
    if self.recent_tweet:
      return self.T.update_status_with_media(text, imagePath, in_reply_to_status_id=self.recent_tweet.id_str)
    title = "✨Twenty Five Twenty One Quotes✨\n#kimtaeri #namjoohyuk #twentyfivetwentyone\n\A thread by a bot by @reicehhh\n(every 30 minutes)"
    return self.T.update_status_with_media(title, imagePath)
  
  def mediaUpload(self, imagePaths):
    medias = []
    medias.append(self.T.media_upload(imagePaths))
    return medias
  
  def postTweetWithMultipleImage(self, text, media_ids_string, reply_to):
    if reply_to:
      return self.T.update_status(status=text, in_reply_to_status_id=reply_to, media_ids=media_ids_string)
    else:
      return self.T.update_status(status=text, media_ids=media_ids_string)

def pick_image():
  filename = os.listdir("images")[0]

  return f"images/{filename}"

def delete_image(filename):
  os.remove(f"{filename}")

def get_one_quote():
  with open('quotes.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='\n')
    quote = next(reader)
    
    updated_quotes = []
    for line in reader:
      try:
        updated_quotes.append(line[0])
      except IndexError:
        continue

  with open('quotes.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter='\n')
    writer.writerow(updated_quotes)

  return quote[0]

def twitter_post(bot):
  filename = pick_image()

  # === Upload media ===
  # medias = bot.mediaUpload(filename)

  quote = get_one_quote()
  print(f"Posting {filename} dengan quote: {quote}")
  quote = quote.split('–')
  quote_tweet = f"{quote[0]}\n\n–{quote[1]}"

  bot.recent_tweet = bot.postTweetWithImage(quote_tweet, filename)

  delete_image(filename) # Delete image after upload

if __name__ == "__main__":
  bot = Tweepy()
  twitter_post(bot)


    