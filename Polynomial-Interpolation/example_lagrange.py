import numpy 
from functions import f
from Langrange_Polynomials import centrix_weights, evaluation

# example xnodes
xnodes1 = [-j/8 for i in range(0,100)]
xnodes2 = [1 + j/8 for i in range(0,100)]
weights1 = centrix_weights(xnodes1)
weights2 = centrix_weights(xnodes2)

# plots
fig = figure(1, [20, 10])
fig.add_subplot(121)
plot(xnodes1, weights1, 'k', label='1')
plot(xnodes2, weights2, label='2')
xlabel('x', fontsize=24)
ylabel('y', fontsize=24)
legend(fontsize=18)

# evaluation and plots
x = linspace(-1., 1., 101)

fvalues1 = [f(i) for i in xnodes1]
fvalues2 = [f(i) for i in xnodes2]
yexact1 = [f(i) for i in x]
yexact2 = [f(i) for i in x]
yinterp1 = [baryeval(xnodes1,weights1,fvalues1,i) for i in x]
yinterp2 = [baryeval(xnodes2,weights2,fvalues2,i) for i in x]
abs1 = [abs(yexact1[j] - yinterp1[j]) for j in range(len(x))]
abs2 = [abs(yexact2[j] - yinterp2[j]) for j in range(len(x))]

fig = figure(1, [20, 10])
fig.add_subplot(122)
plot(x, abs1, label='error1')
plot(x, abs2, label='error2')
xlabel('x', fontsize=24)
ylabel('error', fontsize=24);
legend(fontsize=18);
