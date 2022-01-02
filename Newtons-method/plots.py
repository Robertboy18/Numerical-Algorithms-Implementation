# Change for any of the other files according to the need

xplot = np.linspace(-1, 1, 100)
x = np.linspace(-1, 1, 100)
xhat = 2 # remember that f(xhat) = 0 implies we set xhat = some value
# example f(x) = x^2 - 3
# then xhat = 3^0.5

# standard figures
figure(1, [7, 4])
xplot = linspace(-1, 2, 200)
plot(xplot, 0*xplot, 'k') ## plot the line y=0
plot(xplot, f(xplot)) ## plot f(x)
plot(x, f(x), '*') ## plot the iterates of bisection
xlabel(r'$x$', fontsize=24) ## x axis label
ylabel(r'$f(x)$', fontsize=24); ## y axis label

## Convergence plot
figure(2, [7, 4])
err = absolute(x - xhat)
loglog(err[:-1], err[1:], '*') ## plot the iterates of bisection
err_plot = array([1e-3, 1e-2, 1e-1, 1.]) # change values to ur need

# if you want to plot along with the theoritical convergence
conv = err_plot**3  # quadratic. the theoretecal convergence curve
loglog(err_plot, conv, 'k')
xlim(1e-3, 1)
xlabel(r'x', fontsize=24) ## x axis label
ylabel(r'f(x)', fontsize=24) ## y axis label
title('convergence');