
import numpy as np
import matplotlib.pyplot as plt
N = 682
P = 5

def fig(N, P, e):

	F = []
	F.append(P)
	i = 1
	print(N - F[-1])
	while N - F[-1] > e:
		#print(F[-1])
		F.append(F[-1] + P * (N - F[-1]) / N)

	return F


x = [1,.5,.2,.1,.05,.01]
for X in x:
	print(X, len(fig(N, P, X)))