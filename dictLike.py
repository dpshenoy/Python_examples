'''Module containing a class to create dict-like objects'''

class FixedNumKeys:
    '''A dict-like object that contains up to k key-value pairs where k is an integer.

    Attributes:
        k:  an integer specifying the max number of key-value pairs an instance may have
    '''

    def __init__(self, k):
        '''Initializer checks if supplied k is an integer > 0; if yes, returns
            a FixedNumKeys object permitted to hold up to k key-value pairs.'''
        if not isinstance(k, int):
            raise ValueError('Supplied value of k is not an integer')
        elif k < 0:
            raise ValueError('Supplied value of k is less than zero')
        else:
            self._k = k
            self.keyValPairs = {}     # empty dict

    def k(self):
        '''Method for retrieving max number of keys this dict-like object may have'''
        return self._k

    def addKeyValPair(self, key, value):
        '''Method for adding key-value pairs, unless already contains k pairs'''
        if len( self.keyValPairs.keys() ) >= self._k:
            raise AttributeError('Max number k = {} key-value pairs already reached'.format(self._k))
        else:
            self.keyValPairs[key] = value
