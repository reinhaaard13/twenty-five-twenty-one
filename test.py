import csv

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

print(quote[0].split('–'))

# import os

# filename = os.listdir("images")[0]

# print(filename)

# os.remove(f"images/{filename}")