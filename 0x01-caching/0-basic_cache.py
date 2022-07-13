#!/usr/bin/env python3
from base_caching import BaseCaching
"""
Basic dictionary
"""

class BasicCache(BaseCaching):
    '''Caching system inheriting from
       BaseCaching'''

    def put(self,key, item):
        '''Assign to the dictionary'''
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        '''Get an item by key'''
        if key is None or self.cache_data.get(key) is None:
            return None
        else:
            return self.cache_data[key]
