#!/usr/bin/env python3
"""
Bookshelf batch downloader for Raspberry Pi Press publications
Author: Traek Malan
License: MIT
"""

import xml.etree.ElementTree as xt
from urllib.parse import urlparse
import os
import requests

bookshelf = requests.get('https://magpi.raspberrypi.com/bookshelf.xml')
catalog = xt.ElementTree(xt.fromstring(bookshelf.content)).getroot()
localPath = os.path.expanduser('~/Bookshelf/')

print('Library location: \'' + localPath + '\'\n')
for publication in catalog:
    pubName = publication.findtext('NAME').replace('_','')
    for volume in publication.iter('ITEM'):
        url = volume.findtext('PDF')
        fileName = os.path.basename(urlparse(url).path)
        title = volume.findtext('TITLE')
        label='[' + pubName + ' ' + title + ']: '
        if os.path.exists(localPath + fileName):
            print(label + fileName + ' found')
        else:
            file = requests.get(url, stream=True)
            size = file.headers.get('content-length')
            print(label + 'Downloading \'' + fileName + '\' (' + size + ' bytes)')
            open(localPath + fileName, 'wb').write(file.content)
