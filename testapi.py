#!/usr/bin/python3

import requests

def apiGoogle(ISBN):
    """ Get info from Google API """
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
    url= 'https://www.googleapis.com/books/v1/volumes?q=isbn:{}'
    r = requests.get(url.format(ISBN), allow_redirects=False, headers=header).json()
    items = r.get('items')
    id = items[0].get('id')
    url2 = 'https://www.googleapis.com/books/v1/volumes/{}'
    r2 = requests.get(url2.format(id), allow_redirects=False, headers=header).json()
    Title = r2.get('volumeInfo').get('title')
    authorsList = r2.get('volumeInfo').get('authors')
    Authors = ""
    for name in authorsList:
        if len(authorsList) == 1:
            Authors = name
        elif len(authorsList) > 1 and name == authorsList[-2]:
            Authors += '{} '.format(name)
        elif len(authorsList) > 1 and name == authorsList[-1]:
            Authors += '& {}'.format(name)
        else:
            Authors += '{}, '.format(name)
    Description  = r2.get('volumeInfo').get('description')
    if r2.get('volumeInfo').get('imageLinks'):
        Cover = r2.get('volumeInfo').get('imageLinks').get('thumbnail')
    # url3 = 'https://openlibrary.org/isbn/{}.json'
    # r3 = requests.get(url3.format(ISBN), allow_redirects=True, headers=header)
    # if r3.get('covers'):
    #     idCover = r3.get('covers')[0]
    #     Cover = 'https://covers.openlibrary.org/b/id/{}.jpg'.format(idCover)
    #else:
    #    url3 = 'https://openlibrary.org/isbn/{}.json'
    #    r3 = requests.get(url3.format(ISBN), allow_redirects=True, headers=header)
    #    print(r3)
    #    if r3.get('covers'):
    #        idCover = r3.get('covers')[0]
    #        Cover = 'https://covers.openlibrary.org/b/id/{}.jpg'.format(idCover)
    else:
        Cover = 'https://bit.ly/3vdMcEB'
    newDict = {'Title': Title, 'Authors': Authors, 'Description': Description, 'Status': 'Available', 'Cover': Cover}
    return newDict

main = apiGoogle('9788432232374')
print(main)
