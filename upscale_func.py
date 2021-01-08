import random
import scipy
import numpy
from scipy.ndimage import gaussian_filter

def upscale(a, sx, sy):
    p = [0] * len(a[0]) * sx
    a2 = []
    for i in range(len(a) * sy):
        a2.append(p[:])
    for i in range(len(a)):
        for j in range(len(a[0])):
            for y in range(sy):
                for x in range(sx):
                    a2[i * sy + y][j * sx + x] = a[i][j]
    return a2


def blur(a, s):
    a2 = a[:]
    for i in range(len(a)):
        for j in range(len(a[0])):
            p = 0
            n = 0
            for y in range(-s, s + 1):
                for x in range(-s, s + 1):
                    try:
                        p += a2[i + y][j + x]
                        n += 1
                    except:
                        pass
            a[i][j] = (p + a2[i][j]) / (n + 1)
    return a


def add(a, b, k):
    for i in range(len(a)):
        for j in range(len(a[0])):
            a[i][j] = a[i][j] * k + b[i][j] * (1 - k)
    return a


def convert_color():
    pass


def generate(sx, sy, scale=1, blur_sigma=0, is_int=0):
    a = []
    if is_int == 0:
        for i in range(sy):
            s = []
            for j in range(sx):
                s.append(random.randint(0, 100) / 100)
            a.append(s)
    else:
        for i in range(sy):
            s = []
            for j in range(sx):
                s.append(random.randint(0, 1))
            a.append(s)
    a = upscale(a, scale, scale)
    a = scipy.ndimage.gaussian_filter(numpy.array(a,'float'), sigma=blur_sigma)
    return a
