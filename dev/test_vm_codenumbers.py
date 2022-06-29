from math import sqrt
from vm import (CodeNumber, CODENUMBER_0, CODENUMBER_90, CODENUMBER_180, 
                CODENUMBER_270, CODENUMBER_360, CODENUMBER_30, CODENUMBER_45, 
                CODENUMBER_60,
                QuadCodeNumber, QCN_POSX, QCN_NEGX, QCN_POSY, QCN_NEGY, 
                QCN_POSZ, QCN_NEGZ)

class Test_CodeNumber:
    def test_creation(self):
        assert CodeNumber(7, 3).get_values() == (7, 3)
    
    def test_repr(self):
        assert repr(CodeNumber(7, 3)) == 'CodeNumber(7, 3)'

    def test_constant_codenumbers(self):
        assert CODENUMBER_0 == CodeNumber(1, 0)
        assert CODENUMBER_90 == CodeNumber(1, 1)
        assert CODENUMBER_180 == CodeNumber(0, 1)
        assert CODENUMBER_270 == CodeNumber(1, -1)
        assert CODENUMBER_360 == CodeNumber(1, 0)

        assert CODENUMBER_30 == CodeNumber(2 + sqrt(3))
        assert CODENUMBER_45 == CodeNumber(1 + sqrt(2))
        assert CODENUMBER_60 == CodeNumber(sqrt(3))

        assert CODENUMBER_45 + CODENUMBER_45 == CODENUMBER_90
        assert CODENUMBER_90 - CODENUMBER_30 == CODENUMBER_60 

    def test_arithmetic(self):
        assert CodeNumber(5, 2) + CodeNumber(3, 1) == CodeNumber(13, 11)
        assert CodeNumber(5, 3) - CodeNumber(9, 2) == CodeNumber(3, 1)

        # sum of complimentary triples, see following test.
        assert CodeNumber(20, 9) + CodeNumber(29, 11) == CODENUMBER_90

        # sum of supplimentary triples, see following test.
        assert CodeNumber(20, 9) + CodeNumber(9, 20) == CODENUMBER_180

    def test_complimentary_supplimentary(self):
        assert CodeNumber(20, 9).complimentary() == CodeNumber(29, 11)
        assert CodeNumber(5, -2).complimentary() == CodeNumber(3, 7)
        assert CodeNumber(20, 9).supplimentary() == CodeNumber(9, 20)
        assert CodeNumber(7).supplimentary() == CodeNumber(1, 7)

class Test_QuadCodeNumber:
    def test_creation(self):
        assert QuadCodeNumber(3, 1, 2).get_values() == (3, 1, 2)
    
    def test_repr(self):
        assert repr(QuadCodeNumber(3, 1, 2)) == 'QuadCodeNumber(3, 1, 2)'

    def test_constant_codenumbers(self):
        assert QCN_POSX == QuadCodeNumber(1, 0, 1)
        assert QCN_NEGX == QuadCodeNumber(0, 1, 0)
        assert QCN_POSY == QuadCodeNumber(1, 1, 0)
        assert QCN_NEGY == QuadCodeNumber(1, -1, 0)
        assert QCN_POSZ == QuadCodeNumber(0, 1, 1)
        assert QCN_NEGZ == QuadCodeNumber(0, -1, 1)

    def test_reduction(self):
        assert QuadCodeNumber(12, 4, 8).reduce() == QuadCodeNumber(3, 1, 2)