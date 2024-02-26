print("I am module_2_A_1")
var = 1

def documented_function(a, b, c=50, mode='sum'):
    """Compute either the sum or the product of its arguments, 
    depending on parameter `mode`.

    Parameters
    ----------
    a : float
        first parameter of the operation
    b : float
        second parameter of the operation
    c : float, optional
        third parameter of the operation, by default 50
    mode : {'sum', 'product'}
        operation to run on `a`, `b` and `c`

    Returns
    -------
    float
        The result of operation described by `mode`

    Raises
    ------
    ValueError
        If mode is not one of 'sum' or 'product'
    """
    if mode == 'sum':
        return a + b + c
    else:
        if mode != 'product':
            raise ValueError(f"""`mode` be either 
                             'product' or 'sum', 
                             got {mode}""")
        else:
            return a * b * c
        
    
    