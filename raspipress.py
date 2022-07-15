#!/usr/bin/python
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

print('Files will be written to \'' + localPath + '\'\n')
for publication in catalog:
    for volume in publication.iter('ITEM'):
        url = volume.findtext('PDF')
        fileName = os.path.basename(urlparse(url).path)
        title = volume.findtext('TITLE')
        label='[' + publication.tag + ' ' + title + ']: '
        if os.path.exists(localPath + fileName):
            print(label + fileName + ' already exists')
        else:
            file = requests.get(url, stream=True)
            size = file.headers.get('content-length')
            print(label + 'Downloading \'' + fileName + '\' (' + size + ' bytes)')
            open(localPath + fileName, 'wb').write(file.content)
