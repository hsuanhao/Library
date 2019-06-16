"""
Check whether the squared matrix is singular or not
"""
__author__ = "Hsuan-Hao Fan"

import numpy as np

class MatrixIsSingular(Exception): 
    """
    This class defines our error flag when things go wrong if the matrix is singular.
    """
    pass



def isSingular(A, print_steps = False):
    """
    Check whether the squared matrix is singular or not
    by applying Gaussian elimination
    
    https://en.wikipedia.org/wiki/Gaussian_elimination
    
    Parameters:
    ----------
    A: squared matrix
    print_steps: bollen (Default is False)
                 Print out resulting matrix in each step
    
    Returns
    -------
    True or False: 
      
    True: A is singular.
    Fales: A is not singular.
    """
    # Make B as a copy of A, since we are going to alter its values
    B = np.array(A, dtype=np.float_)
    
    # total rows of B
    tot_row = len(B)
    
    try:
        n_row = 0
        while (n_row < tot_row):
            fix_row(B, n_row, tot_row)
            n_row += 1
            if print_steps: print(B)
    except MatrixIsSingular:
        if print_steps: print(B)
        return True
    return False
    
def fix_row(A, n_row, tot_row):
    """
    Make A[n_row] with A[j,n_row]=0 if j < n_row, and A[n_row, n_row] = 1, but 
    if in the end, A[n_row, n_row] = 0, then stop function and return error flag, MatrixIsSingular
    
    Parameters:
    -----------
    A: squared matrix
    n_row: the row 
    tot_row: total number of rows of matrix A
    
    Return
    ------
    A: A[n_row] with A[j,n_row]=0 if j < n_row, and A[n_row, n_row] = 1
    
    Note that if A[n_row, n_row] = 0, then stop function and return error flag, MatrixIsSingular
    """
    
    last_row = tot_row - 1
    if n_row == 0:
        # For Row Zero, all we require is the first element is equal to 1.
        # We'll divide the row by the value of the first element in the first row, A[0, 0].
        # This will get us in trouble though if A[0, 0] equals 0, so first we'll test for that,
        # and if this is true, we'll add one of the lower rows to the first one before the division.
        # We'll repeat the test going down each lower row until we can do the division.
        i = n_row + 1
        while (A[0,0] == 0):
            A[0] = A[0] + A[i]
            i += 1
            if (i== (tot_row - 1)) and (A[0,0] == 0):
                # The first colum of A has all 0 elements so A is singular.
                raise MatrixIsSingular()
        A[0] = A[0]/A[0,0]
    elif n_row == last_row:
        A = elimination(A, n_row)
        # Complete the if statement to test if the diagonal element is zero.
        if A[last_row,last_row] == 0:
            raise MatrixIsSingular()
        # Transform the row to set the diagonal element to one.
        A[last_row] = A[last_row]/ A[last_row,last_row]
    else:
        # First, we'll set the sub-diagonal elements to zero, i.e. A[i,j]=0 if i < j.
        # Next, we want the diagonal element to be equal to one.
        # We'll divide the row by the value of A[i, i].
        # Again, we need to test if this is zero.
        # If so, we'll add a lower row and repeat setting the sub-diagonal elements to zero.
        A = elimination(A, n_row)
        i = n_row + 1
        while (A[n_row,n_row] == 0):
            A[n_row] = A[n_row] + A[i]
            A = elimination(A, n_row)
            i += 1
            if (i== (tot_row - 1)) and (A[n_row,n_rwo] == 0):
                # The first colum of A has all 0 elements so A is singular.
                raise MatrixIsSingular()
        A[n_row] = A[n_row]/A[n_row,n_row] 
        
    return A


def elimination(A, n_row):
    """
    Make A[n_row] with A[j,n_row]=0 if j < n_row by Gaussian elimination
    
    https://en.wikipedia.org/wiki/Gaussian_elimination
    
    Parameters
    ----------
    A: squared matrix
    n_row: row index of matrix A (n_row > 1)
    
    Return
    ------
    A: matrix after elimination
    """
    i = 0
    while (i < n_row) :
        A[n_row] = A[n_row] - A[n_row, i] * A[i]
        i += 1
        
    return A
    
