from auto_class import Autodiff_Node, Add

# simple example
w = Input_Variable(1.2)
u = Input_Variable(2.)
b = Input_Variable(-3.)

s1 = Multiply(w, u)
s2 = Add(s1, b)

L = Tanh(s2)
# gradient 
L.compute_gradient()
# final evaluation
L.eval()

# exact gradient for comparison
_g1 = 1./cosh(w.eval()*u.eval() + b.eval())**2
print('gradient (w, u, b):', _g1*u.eval(), _g1*w.eval(), _g1)


# to evaluate at a node
s2.eval()
s2.compute_gradient()


# example where an input variable is an input into more than one node
w = Input_Variable(1.2)
u = Input_Variable(2.)
b = Input_Variable(-10.)

s1 = Multiply(w, u)
s2 = Add(s1, b)

s3 = Multiply(s2, u)

L = Tanh(s3)

L.eval()
L.compute_gradient()

