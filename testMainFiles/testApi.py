#!/usr/bin/python3
from isbnlib import meta, cover, desc
from isbnlib.registry import bibformatters

SERVICE = "openl"

try:
    x = meta(isbn, SERVICE)
    print(x.get('Title'))
    print(x.get('Authors')[0])
    print(x.get('Description'))
except:
    pass
