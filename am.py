import math


def fun(t, y):
    return math.pow(y+t, 2) - 1


h = 0.25

w0 = 2/3

# round 4 decimal places
k_0 = h * fun(0, w0)
k_1 = h * fun(0.5*h, w0 + k_0/2)
k_2 = h * fun(h, w0 - k_0 + 2 * k_1)


# print(k_0)
# print(k_1)
# print(k_2)
w1 = 2/3 + 1/6 * (k_0 + 4 * k_1 + k_2)
print("w1: " + str(w1))


# Heun's method
k_0 = h * fun(0, 2/3)
k_0 = round(k_0, 4)
k_1 = h * fun((1/3)*h, 2/3 + k_0/3)
k_1 = round(k_1, 4)
k_2 = h * fun((2/3) * h, 2/3 + (2/3) * k_1)
k_2 = round(k_2, 4)


# print(k_0)
# print(k_1)
# print(k_2)
w1 = 2/3 + 1/4 * (k_0 + 3 * k_2)
w1 = round(w1, 4)
print("w1: " + str(w1))


def ab2(w1, w0, h, t1):
    return w1 + (h/2) * (3 * fun(t1, w1) - fun(t1 - h, w0))


def am2(w2, w1, w0, h, t1):
    return w1 + (h/12) * (5 * fun(t1 + h, w2) + 8 * fun(t1, w1) - fun(t1 - h, w0))


# w2
w2 = ab2(w1, w0, h, h * 1)
w2 = round(w2, 4)
print("Predictor w2: " + str(w2))


w2 = am2(w2, w1, w0, h, h * 1)
w2 = round(w2, 4)
print("Corrector w2: " + str(w2))

print("")
# w3
w3 = ab2(w2, w1, h, h * 2)
w3 = round(w3, 4)
print("Predictor w3: " + str(w3))

w3 = am2(w3, w2, w1, h, h * 2)
w3 = round(w3, 4)
print("Corrector w3: " + str(w3))

print("")
# w4
w4 = ab2(w3, w2, h, h * 3)
w4 = round(w4, 4)
print("Predictor w4: " + str(w4))

w4 = am2(w4, w3, w2, h, h * 3)
w4 = round(w4, 4)
print("Corrector w4: " + str(w4))


exact = 2/(3-2)-1
print("Exact: " + str(exact))
