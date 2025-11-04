from z3 import MUL_ZM_Z
from z7 import SUB_ZZ_Z
from z8 import MUL_ZZ_Z
from z9 import DIV_ZZ_Z

def MOD_ZZ_Z(z1, z2):
    """
    z1 mod z2 = z1 - (z1 // z2) * z2
    """
    if z2[1][0] == 0 and z2[0] == 1:
        raise ValueError("Нельзя делить на ноль")

    q = DIV_ZZ_Z(z1, z2)
    product = MUL_ZZ_Z(q, z2)
    return SUB_ZZ_Z(z1, product)