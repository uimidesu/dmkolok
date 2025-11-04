from z1 import ABS_Z_Z
from z2 import SGN_Z_D
from z3 import MUL_ZM_Z
from natural.n1 import COM_NN_D
from natural.n4 import ADD_NN_N
from natural.n5 import SUB_NN_N

def SUB_ZZ_Z(z1, z2):
    """
    z1 - z2 = z1 + (-z2)
    """
    s1 = SGN_Z_D(z1)
    s2 = SGN_Z_D(z2)
    a1 = ABS_Z_Z(z1)
    a2 = ABS_Z_Z(z2)

    z2_neg = MUL_ZM_Z(z2) if s2 >= 0 else (0, a2[0], a2[1])

    s2_neg = SGN_Z_D(z2_neg)

    if s1 == s2_neg:
        # одинаковый знак => складываем модули
        res_abs = ADD_NN_N(a1, a2)
        return (0, res_abs[0], res_abs[1]) if s1 >= 0 else MUL_ZM_Z((0, res_abs[0], res_abs[1]))
    else:
        # разные знаки => вычитаем модули
        cmp = COM_NN_D(a1, a2)
        if cmp == 0:
            return (0, 1, [0])
        elif cmp == 2:  # |z1| > |z2|
            res_abs = SUB_NN_N(a1, a2)
            return (0, res_abs[0], res_abs[1]) if s1 > 0 else MUL_ZM_Z((0, res_abs[0], res_abs[1]))
        else:  # |z1| < |z2|
            res_abs = SUB_NN_N(a2, a1)
            return (0, res_abs[0], res_abs[1]) if s2_neg > 0 else MUL_ZM_Z((0, res_abs[0], res_abs[1]))