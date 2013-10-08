import urllib
import urllib2
import re
import csv

class ProcessLinks:
    def __init__(self, filename, domain, flag='rU', delimiter=','):
        self.filename   = filename
        self.domain     = domain
        self.flag       = flag
        self.delimiter  = delimiter

    def get_live_links(self):
        with open(self.filename, self.flag) as file:
            links = csv.reader(file, delimiter=self.delimiter)
            for link in links:
                url = link[0]
                try:
                    req = urllib.urlopen(url)
                    if req.getcode() == 200:
                        html = req.read()
                        if re.search(self.domain, html):
                            print url

                except IOError:
                    pass
