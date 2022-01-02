import numpy as np

# float 64
largest_64 = 2.*2.**1023
## find the largest (approximate) value that caues underflow
smallest_64 = 1e-324
print('largest 64 bit float:', largest_64)
print('smallest 64 bit float:', smallest_64)


# float 32
largest_32 = np.float32(2.*2.**127)
smallest_32 = np.float32(1e-126)
## find the largest (approximate) value that caues underflow(alternative)
x32_smallest = np.float32(1.)/np.float32(1e38)/np.float32(1e8) 
print('largest 32 bit float:', largest_32)
print('smallest 32 bit float:', smallest_32)