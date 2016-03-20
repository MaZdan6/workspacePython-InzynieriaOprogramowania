__author__ = '23901'


def a(n):
    if n == 0:
        return 10
    else:
        return 7 + a(n - 1)


w = 16
ciag = a(w)
print("a(", w, ")", a(1))
