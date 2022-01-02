import scipy.special
import numpy as np
import matplotlib

def function(x0):
    return np.sin(x0)

def function_derivative(x0):
    return np.cos(x0)

x0 = 1.2 ## point that we compute the derivative at (ie d/dx sin(x) at x = x0)
f0 = function(x0) ## f(x0)
fp = function_derivative(x0) ## f'(x0) the `p` means 'prime'
fpp = -function(x0) ## f''(x0)
i = linspace(-20, 0, 40) ## `linspace` gives a range of values between two end points
##                          in this case 40 points, between -20 and 0
h = 10.0**i ## this is our approx parameter, it is an array of values 
##             between 10^(-20) and 10^(0)

# Remember we are using the forward difference formula
fp_approx = (sin(x0 + h) - f0)/h ## the derivative approximation

# To use the central difference formula
# Absolute error in 0(h^2) as long as f'''(x) is bounded 
# fp_approx = (sin(x0 + h) - sin(x0 - h))/(2*h)

# To use the backward difference formula
# fp_approx = (f0 - sin(x0 - h))/h

# Forward difference formula
err = absolute(fp - fp_approx) ## the full absolute error
d_err = h/2*absolute(fpp) ## the formula for the discretization error, derived above
            
figure(1, [7, 5]) ## creates a blank figure 7 inches (wide) by 5 inches (height)
loglog(h, err, '-*') ## makes a plot with a log scale on both the x and y axis
loglog(h, d_err, 'r-', label=r'$\frac{h}{2}\vert f^{\prime\prime}(x) \vert $')
xlabel('h', fontsize=20) ## puts a label on the x axis
ylabel('absolute error', fontsize=20) ## puts a label on the y axis
ylim(1e-15, 1) ## places limits on the yaxis for our plot
legend(fontsize=24); ## creates a figure legend (uses the `label=...` arguments in the plot command)
 
# notes : For  ℎ  small but not too small, the absolute error is dominated by the discretization error,  
# ℎ|𝑓″(𝑥)|/2 , which is larger than other sources of error such as roundoff error.
#  Once  ℎ<10−8 , the discretization error becomes smaller than the roundoff error, and the roundoff error continues to get larger as  ℎ→0 .


# Centered Difference Formula
x0 = 1.2 ## point that we compute the derivative at (ie d/dx sin(x) at x = x0)
f0 = sin(x0) ## f(x0)
fp = cos(x0) ## f'(x0) the `p` means 'prime'
fpp = -sin(x0) ## f''(x0)
fppp = -cos(x0) ## f'''(x0)
i = linspace(-20, -1, 40) ## `linspace` gives a range of values between two end points
##                          in this case 40 points, between -20 and 0
h = 10.0**i ## this is our approx parameter, it is an array of values 
##             between 10^(-20) and 10^(0)
fp_approx_q1 = (sin(x0 + h) - sin(x0 - h))/(2*h) ## the derivative approximation
fp_approx_example = (sin(x0 + h) - f0)/h
print("Derivative Approximation " , fp_approx_q1)

err = absolute(fp - fp_approx_q1) ## the full absolute error
err1 = absolute(fp - fp_approx_example)
print("Absolute Error", err)
d_err_q1 = (h**2/6)*absolute(fppp) ## the formula for the discretization error, derived above
d_err_example = (h/2) * absolute(fpp)
print("Exact Derivative",d_err)


# Comparison Plots of the two methods
plt.figure(1, [10, 5])
loglog(h, err, '-*') ## makes a plot with a log scale on both the x and y axis
loglog(h, d_err_q1, 'r-', label=r'$\frac{h^2}{6}\vert f^{\prime\prime\prime}(x) \vert $')
plt.title("Q1 - Derivative Approximation")
xlabel('h', fontsize=20) ## puts a label on the x axis
ylabel('absolute error', fontsize=20) ## puts a label on the y axis
ylim(1e-15, 1) ## places limits on the yaxis for our plot
legend(fontsize=24); ## creates a figure legend


plt.figure(2, [10,5])
loglog(h, err1, '-*') ## makes a plot with a log scale on both the x and y axis
loglog(h, d_err_example, 'r-', label=r'$\frac{h}{2}\vert f^{\prime\prime}(x) \vert $')
plt.title("Example 2 - Derivative Approximation")
xlabel('h', fontsize=20) ## puts a label on the x axis
ylabel('absolute error', fontsize=20) ## puts a label on the y axis
ylim(1e-15, 1) ## places limits on the yaxis for our plot
legend(fontsize=24); ## creates a figure legend