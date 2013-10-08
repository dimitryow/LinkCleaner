import json

import os

from urlparse \
        import urlparse

import urllib

import urllib2


"""
CONSTANTS
"""
API_KEY = os.environ['AHREFS_API_KEY']


"""
GLOBAL FUNCTIONS
"""
def get_api_units_left():
    """
    A simple call to Ahrefs API. Returns number of API calls available.
    REQUIRES AHREFS_API_KEY in the environment!
    """
    json_obj = json.load(
                urllib2.urlopen(
                'http://api.ahrefs.com/get_units_left.php?output=json&AhrefsKey='
                 + API_KEY 
                )
            )
    count_data = json_obj['AhrefsApiResponse']['api_units_left']
    print count_data

"""
CLASSES
"""
class LiveLinks:
    """
    Takes a Plaintext list of URLs, checks for a 200 HTTP response, and if 200, parses
    the url into a ParseURL objects and stores it in an array
    """
    def __init__(self, filename, flag='rU'):
        self.filename = filename
        self.flag = flag
        self.link_list = []
        with open(filename, flag) as file:
            for line in file:
                link = urlparse(line)
                self.link_list.append(link)

    def get_list(self):
        return self.link_list

    def print_list(self):
        for link in self.link_list:
            print item.netloc

class AhrefsInterface:
    def __init__(self, link_list, page_list):
        self.api_key = API_KEY
        self.link_list = link_list
        self.page_list = page_list

    def identify_spam(self):
        pass



