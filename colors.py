import numpy as np

MAX_GRAY = 256
MIN_GRAY = 0

def tri_factors(n):
    mmc = []
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            mmc.append(divisor)
            n = n/divisor
        else:
            divisor += 1

    if len(mmc) < 3:
        mmc.extend([1 for i in range(3 - len(mmc))])
    elif len(mmc) > 3:
        step = len(mmc)//3
        mmc = [np.prod(mmc[:step]), np.prod(
            mmc[step:step*2+1]), np.prod(mmc[step*2+1:])]
    return mmc

def get_n_colors(n):
    global MAX_GRAY, MIN_GRAY
    a, b, c = tri_factors(n)

    a = np.linspace(MIN_GRAY, MAX_GRAY-1, a, dtype=int)
    b = np.linspace(MIN_GRAY, MAX_GRAY-1, b, dtype=int)
    c = np.linspace(MIN_GRAY, MAX_GRAY-1, c, dtype=int)

    return np.array(np.meshgrid(a, b, c)).T.reshape(-1, 3)
