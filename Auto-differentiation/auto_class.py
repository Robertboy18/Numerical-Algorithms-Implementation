# original author : Professor Jay Newby
class Autodiff_Node(object): 
    ## A class is a recipe for creating objects (with methods and atributes).
    ## This is called a 'base class', which is like a boiler plate recipe that 
    ## many other classes will use a starting point, each making specific 
    ## changes.


    ## All methods (unless otherwise specified) must have the first argument
    ## a variable called `self`, which is a copy of the object itself. Hence,
    ## one can access any method or atribute in the object throught the `self`
    ## variable.
    def __init__(self, parents): 
        """Parameters:
        ---------------
        `parents` a list of `Autodiff_Node` objects corresponding to the graph
            parents."""
        ## initializer gets called once when you create (or instantiate) an 
        ## object
        self._set_parents(parents)
        self._output_data = None
    def _set_parents(self, parents):
        self.parents = parents
        return None
    def set_output_data(self, y):
        self._output_data = y
        return None
    def get_output_data(self):
        return self._output_data
    ## a static modthod just means it doesn't depend on the data in `self`, so 
    ## `self` does not need to be an argument
    @staticmethod 
    def function(x): 
        """Given input `x` return output `y`"""
        ## this is just a place holder (or template) to be used to create 
        ## specific types of Node objects
        return NotImplementedError
    ## a static modthod just means it doesn't depend on the data in `self`, so 
    ## `self` does not need to be an argument
    @staticmethod
    def backpropagation_function(x, y, output_gradient): 
        """
        Parameters:
        --------------------
        `x` is the input variable(s): a list of tensors one for each input from 
            a graph parent.
        `y` is the output variable(s): a list of tensors one for each ouput to 
            a graph child.
        `output_gradient` is the gradient (list of partial derivatives) of a 
            scalar function with respect to one or more output variables.
        
        Returns:
        --------------------
        `input_gradient` is the gradient (list of partial derivatives) of a 
            scalar function with respect to one or more input variables."""
        ## this is just a place holder (or template) to be used to create 
        ## specific types of Node objects
        return NotImplementedError
    def eval(self):
        """Evaluate the output of the node, moving from necessary inputs 
        through the DAG in the forward direction."""
        ## recursively call eval for each node until input variables are reached
        x = [node.eval() for node in self.parents] 
        return self.function(x)
    def _eval_and_save_output(self):
        ## this is a stateful approach and should be used with care. This method 
        ## will alter one of the atributes. This can lead to confusing and hard 
        ## to diagnose bugs. It is best to avoid doing this whenever possible.

        ## recursively call eval for each node until inputs are reached
        x = [node._eval_and_save_output() for node in self.parents]
        y = self.function(x)
        ## internal data, or state, is modified here. Specifically the 
        ## `self._output_data` attribute.
        self.set_output_data(y) 
        return y
    def _get_gradient(self, output_gradient):
        ## This is a helper function to assemble the gradients, moving backward 
        ## through the DAG. We must call `_eval_and_save_output()` before 
        ## using this method
        x = [node.get_output_data() for node in self.parents]
        ## We use internal state here, which assumes that 
        ## `_eval_and_save_output()` was called before using this method
        y = self.get_output_data() 
        input_gradient = self.backpropagation_function(x, y, output_gradient)
        ## We use recursion combined with generators (see examples at the end of 
        ## this notebook)
        for node, sub_gradient in zip(self.parents, input_gradient):
            ## recursive call to the same method attached to the parent nodes
            for inner_gradient in node._get_gradient(sub_gradient): 
                yield inner_gradient
    def compute_gradient(self): 
        """Assumes the node has scalar output"""
        ## computing gradients is very simple with the `Autodiff_node` class

        ## the dangerous stateful call must precede the gradient calculation
        self._eval_and_save_output() 
        ## the input is always simply `1.0` because partial_L/partial_L = 1
        return [g for g in self._get_gradient(1.)] 

class Add(Autodiff_Node):
    """Add two input nodes"""
    ## this defines a node type specifically for addition, it 'inherits' all 
    ## of the methods and atributes from its base class, `Autodiff_Node`. Think
    ## of these as default methods. Any methods that are redefined here are used 
    ## instead of the default methods from the base class
    def __init__(self, a, b):
        ## initializer gets called once when you create (or instantiate) an 
        ## object
        parents = [a, b]
        super().__init__(parents) ## calls `__init__` method of the base class
    ## a static modthod just means it doesn't depend on the data in `self`, so 
    ## `self` does not need to be an argument
    @staticmethod
    def function(x):
        a = x[0]
        b = x[1]
        return a + b
    @staticmethod
    def backpropagation_function(x, y, output_gradient):
        input_gradient = [output_gradient*1, output_gradient*1]
        return input_gradient

class Multiply(Autodiff_Node):
    """Multiply two input nodes"""
    def __init__(self, a, b):
        parents = [a, b]
        super().__init__(parents)
    @staticmethod
    def function(x):
        a = x[0]
        b = x[1]
        return a*b
    @staticmethod
    def backpropagation_function(x, y, output_gradient):
        a = x[0]
        b = x[1]
        input_gradient = [output_gradient*b, output_gradient*a]
        return input_gradient

class Tanh(Autodiff_Node):
    """Apply the `tanh` function to an input node"""
    def __init__(self, x):
        parents = [x]
        super().__init__(parents)
    @staticmethod
    def function(x):
        return np.tanh(x[0])
    @staticmethod
    def backpropagation_function(x, y, output_gradient):
        dydx = 1./np.cosh(x[0])**2
        input_gradient = [output_gradient*dydx]
        return input_gradient

class Input_Variable(Autodiff_Node):
    """Input Variables have a specific fixed value. Use these to hold parameters 
    and variables. Gradient of a node with a scalar output will be a list of 
    partial derivatives with respect to these Input Variables.
    
    Parameters:
    ---------------
    `value` the numerical value of the variable (scalar in this example)."""
    def __init__(self, value):
        self.value = value
        parents = []
        super().__init__(parents)
    @staticmethod
    def function(x):
        return self.value
    @staticmethod
    def backpropagation_function(x, y, output_gradient):
        input_gradient = output_gradient
        return input_gradient
    def eval(self): 
        ## this overrides the default `eval` method defined in `Autodiff_Node`
        ## base class
        return self.value
    def _eval_and_save_output(self): ## another override
        self.set_output_data(self.value)
        return self.value
    def _get_gradient(self, output_gradient): ## another override
        yield output_gradient