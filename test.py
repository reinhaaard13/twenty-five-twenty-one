# import csv

# with open('quotes.csv', 'r', encoding='utf-8') as f:
#   reader = csv.reader(f, delimiter='\n')
#   quote = next(reader)
  
#   updated_quotes = []
#   for line in reader:
#     try:
#       updated_quotes.append(line[0]) if line[0].startswith('“') else None
#     except IndexError:
#       continue

# with open('quotes.csv', 'w', encoding='utf-8') as f:
#   writer = csv.writer(f, delimiter='\n')
#   writer.writerow(updated_quotes)

import json

# with open('recent_tweet.json', 'r') as f:
#   recent_tweet = json.load(f)['recent_id_str']

recent_tweet = { "id_str": '151231231231231239'}
# 1513583793319337989
with open('recent_tweet.json', 'w') as f:
    json.dump({'recent_id_str': recent_tweet['id_str']}, f)

print(recent_tweet)

# print(quote[0].split('–'))

# import os

# filename = os.listdir("images")[0]

# print(filename)

# os.remove(f"images/{filename}")