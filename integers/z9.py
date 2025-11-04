from z1 import ABS_Z_Z
from z2 import SGN_Z_D
from natural.n3 import ADD_1N_N
from natural.n11 import DIV_NN_N

def DIV_ZZ_Z(z1, z2):
    """
    z1 // z2
    """
    if z2[1][0] == 0 and z2[0] == 1:
        raise ValueError("Нельзя делить на ноль")

    s1 = SGN_Z_D(z1)
    s2 = SGN_Z_D(z2)
    a1 = ABS_Z_Z(z1)
    a2 = ABS_Z_Z(z2)

    if a1[0] == 1 and a1[1][0] == 0:
        return (0, 1, [0])

    q_abs = DIV_NN_N(a1, a2)
    sign_res = 0 if s1 * s2 >= 0 else 1
    flag = True

    if s1 * s2 < 0 and flag:
        q_abs = ADD_1N_N(q_abs)
        sign_res = 1 - sign_res

    return (sign_res, q_abs[0], q_abs[1])