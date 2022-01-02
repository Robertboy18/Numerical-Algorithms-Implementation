import numpy
import matplotlib

fig = plt.figure(figsize=(6,5))
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
ax = fig.add_axes([left, bottom, width, height]) 

start, stop, n_values = -2, 2, 800

x_vals = np.linspace(start, stop, n_values)
y_vals = np.linspace(start, stop, n_values)
X, Y = np.meshgrid(x_vals, y_vals)


# define the function to be plotted
Z = 2*X**3 - 3*X**2 - 6*X*Y*(X - Y - 1)

cp = plt.contourf(X, Y, Z)
plt.colorbar(cp)

# plot critical points
plot(0, 0, '*w')
plot(0, -1, '*w')
plot(1, 0, '*w')
plot(-1, -1, '*w')

ax.set_title('Contour Plot')
ax.set_xlabel('x (cm)')
ax.set_ylabel('y (cm)')
plt.show()
