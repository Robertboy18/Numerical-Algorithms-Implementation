import numpy
import matplotlib

x0 = 1.2 ## point that we compute the derivative at (ie d/dx sin(x) at x = x0)
f0 = sin(x0) ## f(x0)
fp = cos(x0) ## f'(x0) the `p` means 'prime'
fpp = -sin(x0) ## f''(x0)''
M = abs(fpp)
epsilon = 10**-16
final_min = 2*(10**-8)*M
i = linspace(-20, 0, 100) ## `linspace` gives a range of values between two end points
##                          in this case 40 points, between -20 and 0
h = 10.0**i ## this is our approx parameter, it is an array of values 
error = (M*h/2 + 2*epsilon/h)
##             between 10^(-20) and 10^(0)
fp_approx = (sin(x0 + h) - f0)/h ## the derivative approximation
err = absolute(fp - fp_approx) ## the full absolute error
d_err = h/2*absolute(fpp) ## the formula for the discretization error, derived above
            
figure(1, [20, 10]) ## creates a blank figure 7 inches (wide) by 5 inches (height)
loglog(h, err, '-*') ## makes a plot with a log scale on both the x and y axis
loglog(h, error, '-*', label=r'$ \frac{Mh}{2} + \frac{2\epsilon}{h}$') 
loglog(h, d_err, 'r-', label=r'$\frac{h}{2}\vert f^{\prime\prime}(x) \vert $')
plt.plot(final_min,final_min, marker='o', markersize=10, color="red")
xlabel('h', fontsize=30) ## puts a label on the x axis
ylabel('absolute error', fontsize=20) ## puts a label on the y axis
ylim(1e-15, 1) ## places limits on the yaxis for our plot
legend(fontsize=30); ## creates a figure legend (uses the `label=...` arguments in the plot command)