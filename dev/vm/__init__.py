from .vm_numbers import (int_to_digits, negate_digits, all_from_9_last_from_10, 
        find_truth_changes, to_vinculum, from_vinculum, 
        VDigit, digits_from_vdigits, VInt)

from .vm_triples import (Triple, TRIPLE_0, TRIPLE_90, TRIPLE_180, TRIPLE_270,
                        TRIPLE_360, TRIPLE_30, TRIPLE_45, TRIPLE_60, 
                        Quadruple, QUAD_POSX, QUAD_NEGX, QUAD_POSY, QUAD_NEGY,
                        QUAD_POSZ, QUAD_NEGZ)

from .vm_codenumbers import(CodeNumber, CODENUMBER_0, CODENUMBER_90, 
                            CODENUMBER_180, CODENUMBER_270, CODENUMBER_360, 
                            CODENUMBER_30, CODENUMBER_45, CODENUMBER_60,
                            QuadCodeNumber, QCN_POSX, QCN_NEGX, QCN_POSY, 
                            QCN_NEGY, QCN_POSZ, QCN_NEGZ)

from .vm_util import code_number_of, triple_of, quad_code_number_of, quadruple_of