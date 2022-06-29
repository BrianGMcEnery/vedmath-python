from .vm_triples import Triple, Quadruple, Quintuple
from .vm_codenumbers import CodeNumber, QuadCodeNumber

def code_number_of(t:Triple) -> CodeNumber:
    '''Return the codenumber corresponding to a triple, pp 68 in 
    Triples book.'''
    x, y, r = t.get_values()
    return CodeNumber(x + r, y).reduce()

def quad_code_number_of(q:Quadruple) -> QuadCodeNumber:
    '''Return the codenumber corresponding to a quadruple, pp 163 in 
    Triples book.'''
    x, y, z, r = q.get_values()
    return QuadCodeNumber(y, r - x, z).reduce()

def triple_of(cn:CodeNumber) -> Triple:
    '''Return a triple corresponding to the codenumbers cn = (c, d), as per 
    formula on pp67 of the Triple book.'''
    c, d = cn.get_values()
    return Triple(c * c - d * d, 2 * c * d, c * c + d * d).reduce()

def quadruple_of(qn:QuadCodeNumber) -> Quadruple:
    '''Return a quadruple corresponding to the quadcodenumbers qn = (c, d, e), 
    as per formula on pp163 of the Triple book.'''
    c, d, e = qn.get_values()
    return Quadruple(
        c * c - d * d + e * e, 
        2 * c * d, 
        2 * d * e, 
        c * c + d * d + e * e
        ).reduce()

def sub_quadruples(q1:Quadruple, q2:Quadruple) -> Quintuple:
    '''Subtract two quadruples, pp164, the Triples book.'''

    x1, y1, z1, r1 = q1.get_values()
    x2, y2, z2, r2 = q2.get_values()

    return Quintuple(
        x1 * x2 + y1 * y2 + z1 * z2,
        y1 * x2 - x1 * y2,
        z1 * x2 - x1 * z2,
        z1 * y2 - y1 * z2,
        r1 * r2
    ).reduce()