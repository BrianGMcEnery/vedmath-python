from .vm_triples import Triple
from .vm_codenumbers import CodeNumber

def code_number_of(t:Triple) -> CodeNumber:
    '''Return the codenumber corresponding to a triple, pp 68 in 
    Triples book.'''
    x, y, r = t.get_values()
    return CodeNumber(x + r, y).reduce()

def triple_of(cn:CodeNumber) -> Triple:
    '''Return a triple corresponding to the codenumbers cn = (c, d), as per 
    formula on pp67 of the Triple book.'''
    c, d = cn.get_values()
    return Triple(c * c - d * d, 2 * c * d, c * c + d * d).reduce()