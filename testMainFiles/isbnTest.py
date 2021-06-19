#!/usr/bin/python3
import requests

ISBN = "9780439708180"
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
url = 'https://www.googleapis.com/books/v1/volumes?q=isbn:{}'

print("Google")
r = requests.get(url.format(ISBN), allow_redirects=False, headers=header)
r2 = requests.get(url.format(ISBN), allow_redirects=False, headers=header)

Title = r.json().get('items')[0].get('volumeInfo').get('title')
Description = r.json().get('items')[0].get('volumeInfo').get('description')
print(Title)
print(Description)

print("openlibray")
url = 'https://openlibrary.org/isbn/{}.json'
cover = 'https://covers.openlibrary.org/b/id/{}-L.jpg'
r2 = requests.get(url.format(ISBN), allow_redirects=True, headers=header)
ISBN = "ISBN:{}".format(ISBN)
cover = (r2.json().get('covers'))
print(cover)
# https://covers.openlibrary.org/b/id/{}-L.jpg'.format(cover)
