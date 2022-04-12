from time import timezone
import os
from apscheduler.schedulers.blocking import BlockingScheduler

from image_scraping import get_all_links, download_images
from twitter_api import Tweepy, twitter_post
from quote_scraping import get_quotes, saveToCsv

def main():
  # Check if quotes.csv is present
  if not os.path.isfile('quotes.csv'):
  # Scrape the quotes
    quotes = get_quotes()
    saveToCsv(quotes)

    # Scrape the images
    links = get_all_links()
    download_images(links)

  # Upload the images to Twitter
  bot = Tweepy()
  twitter_post(bot)

  sched = BlockingScheduler(timezone="Asia/Jakarta")

  sched.add_job(twitter_post, 'interval', minutes=30, args=[bot])
  sched.print_jobs()

  sched.start()

if __name__ == "__main__":
  main()