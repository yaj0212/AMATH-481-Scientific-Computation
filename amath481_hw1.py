# -*- coding: utf-8 -*-
"""AMATH481-HW1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wQ_sKWlb8ByLECdSpLYLA-QxRTFFqonc
"""

import numpy as np
import matplotlib.pyplot as plt

# x'(t) = -4*x*np.sin(t) = f(x, t)
# true solution np.exp(4 * (np.cos(t) - 1))
# x(0) = 1
# t0 = 0, tN = 8, dt = 2**(-5)

x0 = 1
t0 = 0
tN = 8
dt = 2**(-5)

def f(x, t):
    return -4 * x * np.sin(t)

def true_solution(t):
    return np.exp(4 * (np.cos(t) - 1))

t = np.arange(t0, tN + dt / 2, dt)
x = np.zeros_like(t)
x[0] = x0
x_true = np.zeros_like(t)
x_true[0] = x0
GE = 0

for k in range(len(t) - 1):
    x[k + 1] = x[k] + dt * f(x[k], t[k])

# local truncation error
LTE = np.absolute(true_solution(dt) - x[1])
A1 = LTE
print(A1)

# global truncation error
GE = abs(x[len(t) - 1] - true_solution(t[len(t) - 1]))
A2 = GE
print(GE)

print(np.log(dt))
print(np.log(GE))

import numpy as np
import matplotlib.pyplot as plt

x0 = 1
t0 = 0
tN = 8
dt = 2**(-6)

def f(x, t):
    return -4 * x * np.sin(t)

def true_solution(t):
    return np.exp(4 * (np.cos(t) - 1))

def error(dt, x0):
    error = list()
    for k in range(0,7):
      t = np.arange(t0, tN + dt / 2, dt)
      x = np.zeros_like(t)
      x[0] = x0
      for i in range(len(t) - 1):
        x[i + 1] = x[i] + dt * f(x[i], t[i])
        LTE = abs(x[1]- true_solution(t[1]))
        GE = abs(x[len(t)-1] - true_solution(t[-1]))
        error.append(LTE)
        error.append(GE)
    return error

for k in range(len(t) - 1):
    x[k + 1] = x[k] + dt * f(x[k], t[k])

# local truncation error
LTE = np.absolute(true_solution(dt) - x[1])
A3 = LTE
print(A3)

# global truncation error
GE = abs(x[len(t) - 1] - true_solution(t[len(t) - 1]))
A4 = GE
print(A4)

dt_set = [2**(-5), 2**(-6), 2**(-7), 2**(-8), 2**(-9), 2**(-10), 2**(-11)]
GE_log = [0, 0, 0, 0, 0, 0, 0]
for j in range(0, 7):
  error = error(dt_set[j], x0)
print(error)
print(len(error))

import numpy as np
import matplotlib.pyplot as plt

x0 = 1
t0 = 0
tN = 8
dt = 2**(-10)

def f(x, t):
    return -4 * x * np.sin(t)

def true_solution(t):
    return np.exp(4 * (np.cos(t) - 1))

t = np.arange(t0, tN + dt / 2, dt)
x = np.zeros_like(t)
x[0] = x0

for k in range(len(t) - 1):
    x[k + 1] = x[k] + dt * (1/2 * f(x[k], t[k]) + 1/2 * f(x[k] + dt * f(x[k], t[k]), t[k] + dt))

# local truncation error
LTE = abs(true_solution(dt) - x[1])
A5 = LTE
print(A5)

# global truncation error
GE = abs(x[len(t) - 1] - true_solution(t[len(t) - 1]))
A6 = GE
print(A6)

print(np.log(dt))
print(np.log(GE))

import numpy as np
import matplotlib.pyplot as plt

x0 = 1
t0 = 0
tN = 8
dt = 2**(-6)

def f(x, t):
    return -4 * x * np.sin(t)

def true_solution(t):
    return np.exp(4 * (np.cos(t) - 1))

t = np.arange(t0, tN + dt / 2, dt)
x = np.zeros_like(t)
x[0] = x0

for k in range(len(t) - 1):
    x[k + 1] = x[k] + dt * (1/2 * f(x[k], t[k]) + 1/2 * f(x[k] + dt * f(x[k], t[k]), t[k] + dt))

# local truncation error
LTE = np.absolute(true_solution(dt) - x[1])
A7 = LTE
print(A7)

# global truncation error
GE = abs(x[len(t) - 1]- true_solution(t[len(t) - 1]))
A8 = GE
print(A8)

import numpy as np
import matplotlib.pyplot as plt

x0 = 1
t0 = 0
tN = 8
dt = 2**(-11)

def f(x, t):
    return -4 * x * np.sin(t)

def true_solution(t):
    return np.exp(4 * (np.cos(t) - 1))

t = np.arange(t0, tN + dt / 2, dt)
x = np.zeros_like(t)
x[0] = x0

for k in range(len(t) - 1):
    x[k + 1] = x[k] + dt * f(x[k] + dt/2 * f(x[k], t[k]), t[k] + dt/2)

# local truncation error
LTE = np.absolute(true_solution(dt) - x[1])
A9 = LTE
print(A9)

# global truncation error
GE = abs(x[len(t) - 1] - true_solution(t[len(t) - 1]))
A10 = GE
print(A10)

print(np.log(dt))
print(np.log(GE))

import numpy as np
import matplotlib.pyplot as plt

# x'(t) = -4*x*np.sin(t) = f(x, t)
# true solution np.exp(4 * (np.cos(t) - 1))
# x(0) = 1
# t0 = 0, tN = 8, dt = 2**(-5)

x0 = 1
t0 = 0
tN = 8
dt = 2**(-6)

def f(x, t):
    return -4 * x * np.sin(t)

def true_solution(t):
    return np.exp(4 * (np.cos(t) - 1))

t = np.arange(t0, tN + dt / 2, dt)
x = np.zeros_like(t)
x[0] = x0

for k in range(len(t) - 1):
    x[k + 1] = x[k] + dt * f(x[k] + dt/2 * f(x[k], t[k]), t[k] + dt/2)

# local truncation error
LTE = np.absolute(true_solution(dt) - x[1])
A11 = LTE
print(A11)

# global truncation error
GE = abs(x[len(t) - 1] - true_solution(t[len(t) - 1]))
A12 = GE
print(A12)

# Probelm 2
import numpy as np
import matplotlib.pyplot as plt

# x'(t) = 8*np.sin(x) = f(x, t)
# true solution 2 * np.arctan(np.exp(8 * t) / (1 + np.sqrt(2)))
# x(0) = np.pi / 4
# t0 = 0, tN = 2, dt = 0.1

x0 = np.pi / 4
t0 = 0
tN = 2
dt = 0.1

def f(x, t):
    return 8 * np.sin(x)

def true_solution(t):
    return 2 * np.arctan(np.exp(8 * t) / (1 + np.sqrt(2)))

t = np.arange(t0, tN + dt / 2, dt)
x = np.zeros_like(t)
x_p = np.zeros_like(t)
x[0] = x0
x[1] = x0 + dt * f(x0 + dt / 2 * f(x0, t0), t0 + dt / 2)

for k in range(1, len(t) - 1):
    x_p[k + 1] = x[k] + (dt / 2) * (3 * f(x[k], t[k]) - f(x[k - 1], t[k - 1]))
    x[k + 1] = x[k] + (dt / 2) * (f(x_p[k + 1], t[k + 1]) + f(x[k], t[k]))

A13 = x[len(t) - 1]
print(A13)

A14 = abs(true_solution(t[len(t) - 1]) - x[len(t) - 1])
print(A14)

import numpy as np
import matplotlib.pyplot as plt

# x'(t) = 8*np.sin(x) = f(x, t)
# true solution 2 * np.arctan(np.exp(8 * t) / (1 + np.sqrt(2)))
# x(0) = np.pi / 4
# t0 = 0, tN = 2, dt = 0.01

x0 = np.pi / 4
t0 = 0
tN = 2
dt = 0.01

def f(x, t):
    return 8 * np.sin(x)

def true_solution(t):
    return 2 * np.arctan(np.exp(8 * t) / (1 + np.sqrt(2)))

t = np.arange(t0, tN + dt / 2, dt)
x = np.zeros_like(t)
x_p = np.zeros_like(t)
x[0] = x0
x[1] = x0 + dt * f(x0 + dt / 2 * f(x0, t0), t0 + dt / 2)

for k in range(1, len(t) - 1):
    x_p[k + 1] = x[k] + (dt / 2) * (3 * f(x[k], t[k]) - f(x[k - 1], t[k - 1]))
    x[k + 1] = x[k] + (dt / 2) * (f(x_p[k + 1], t[k + 1]) + f(x[k], t[k]))

A15 = x[len(t) - 1]
print(A15)

A16 = abs(true_solution(t[len(t) - 1]) - x[len(t) - 1])
print(A16)

# Problem 3
import numpy as np
import matplotlib.pyplot as plt
import scipy

v0 = 0.1
w0 = 1
t0 = 0
tN = 100

t = np.array([0, 100])
x0 = np.array([v0, w0])
I = np.zeros_like(t)

def I(t):
    return 1/10 * (5 + np.sin(np.pi * t / 10))

def fv(t, x):
    v = x[0]
    w = x[1]
    return v - 1/3 * (v ** 3) - w + I(t)

def fw(x):
    a = 0.7
    b = 1
    T = 12
    v = x[0]
    w = x[1]
    return (a + v - b * w) / T

def f(t, x):
    return np.array([fv(t, x), fw(x)])

sol = scipy.integrate.solve_ivp(f, t, x0, atol=1e-4, rtol=1e-4)
T = sol.t
X = sol.y
sum = 0
N = len(T)

for k in range(1, len(T) - 1):
  sum = sum + T[k] - T[k - 1]

A17 = X[0][-1]
print(A17)
A18 = sum/len(T)
print(A18)

import numpy as np
import matplotlib.pyplot as plt
import scipy

v0 = 0.1
w0 = 1
t0 = 0
tN = 100

t = np.array([0, 100])
x0 = np.array([v0, w0])
I = np.zeros_like(t)

def I(t):
    return 1/10 * (5 + np.sin(np.pi * t / 10))

def fv(t, x):
    v = x[0]
    w = x[1]
    return v - 1/3 * (v ** 3) - w + I(t)

def fw(x):
    a = 0.7
    b = 1
    T = 12
    v = x[0]
    w = x[1]
    return (a + v - b * w) / T

def f(t, x):
    return np.array([fv(t, x), fw(x)])

sol = scipy.integrate.solve_ivp(f, t, x0, atol=1e-9, rtol=1e-9)
T = sol.t
X = sol.y
sum = 0
N = len(T)

for k in range(1, len(T) - 1):
  sum = sum + T[k] - T[k - 1]

A19 = X[0][-1]
print(A19)
A20 = sum/len(T)
print(A20)

import numpy as np
import matplotlib.pyplot as plt

# x'(t) = 0.5 * x = f(x, t)
# x(0) = 0.1
# t0 = 0, tN = 2, dt = 0.5

x0 = 0.1
t0 = 0
tN = 2
dt = 0.5

def f(x, t):
    return 0.5 * x

def true_solution(t):
    return x0 * np.exp(0.5 * t)

tplot = np.linspace(t0, tN, 1000)
xplot = true_solution(tplot)
plt.plot(tplot, xplot, 'k')

# plt.plot(t0, x0, 'ro')
#
# x1 = x0 + dt * f(x0, t0)
# t1 = t0 + dt
# plt.plot(t1, x1, 'ro')
#
# x2 = x1 + dt * f(x1, t1)
# t2 = t1 + dt
# plt.plot(t2, x2, 'ro')

t = np.arange(t0, tN + dt / 2, dt)
x = np.zeros_like(t)
x[0] = x0

for k in range(len(t) - 1):
    x[k + 1] = x[k] + dt * f(x[k], t[k])

plt.plot(t, x, 'ro')
plt.show()