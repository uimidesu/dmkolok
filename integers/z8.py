from z1 import ABS_Z_Z
from z2 import SGN_Z_D
from z3 import MUL_ZM_Z
from natural.n8 import MUL_NN_N

def MUL_ZZ_Z(z1, z2):
    """
    z1 * z2
    """
    s1, s2 = SGN_Z_D(z1), SGN_Z_D(z2)
    a1, a2 = ABS_Z_Z(z1), ABS_Z_Z(z2)
    res_abs = MUL_NN_N(a1, a2)
    if s1 * s2 >= 0:
        return (0, res_abs[0], res_abs[1])
    else:
        return MUL_ZM_Z((0, res_abs[0], res_abs[1]))