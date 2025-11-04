from n1 import COM_NN_D
from n2 import NZER_N_B
from n12 import MOD_NN_N

def GCF_NN_N(a, b):
    """
    НОД по алгоритму Евклида: gcd(a,b) = gcd(b, a mod b)
    """
    a, b = a, b
    while NZER_N_B(b):
        if COM_NN_D(a, b) == 1:
            a, b = b, a
        b = MOD_NN_N(a, b)
        a, b = b, a
    return a