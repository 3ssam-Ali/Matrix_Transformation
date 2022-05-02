import numpy as np

class MatList:
    '''
        An object contains flattened matrix and stored in one dimensional array.


        Attributes
        ----------
        matShape : tuple
            The shape of the matrix.

        Methods
        -------
        __init__(self, li=None) -> None:
            Optionally Takes takes the matrix when constructing the object
            or 'setList' function can be used instead later

        setList(self, li): 
            Takes the matrix as array_like object.

        getItem(self, z, y, x):
            Return an item from the list given it's indices.
    '''
    __vector = None  # Flattened Matrix with q length
    matShape = 0    # original size of matrix before flattening

    def setList(self, li):
        '''
        Take a matrix to store as a flattened vector. 

        Parameters
        ----------
        li: array_like object.
        '''

        li = np.array(li)
        self.matShape = li.shape
        self.__vector = np.reshape(li, [-1])

    def __init__(self, li=None) -> None:
        if li != None:
            self.setList(li)

    def getItem(self, z, y, x):
        '''
        Return an item from the matrix using it's indices. 

        Parameters
        ----------
        z, y, x: integers representing the indices with z being depth, y is the row 
                 and x is the column.
        '''
        if self.__vector is None:
            return None
        sz, sy, sx = self.matShape
        return self.__vector[(z*sy*sx)+y*sx+x]