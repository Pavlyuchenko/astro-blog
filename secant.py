import math

xs = [1, 4]


def fun(x):
    return (3*x+4-math.exp(x))


for i in range(1, 10):
    slope = ((xs[i]-xs[i - 1]) / (fun(xs[i]) -
                                  fun(xs[i - 1])))

    res = xs[i] - slope * fun(xs[i])
    xs.append(res)

print(xs)
