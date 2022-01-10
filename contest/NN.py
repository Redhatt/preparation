# genral NN
import numpy as np

class NN:
    def __init__(self, input_size, output_size=1, no_of_hid=1, size_of_hiddens=[2], active='sig'):
        """
        @param: input_size; input size, other dimension should be 1
        @param: output_size; output_size other dimension should be 1
        @param: no_of_hid=1; number of hidden layers, default is 1
        @param: size_of_hiddens=[2]; sequence-wise no of nodes in each hidden layer.
        eg: if no_of_hid is 3 then size_of_hiddens layer should look like [3,4,5] 
        where 3, 4, 5 are no of nodes in each hidden layer in order.
        """
        self.input_size = input_size
        self.output = None
        self.output_size = output_size
        self.no_of_hid = no_of_hid
        self.hidden_y = []
        self.hidden_z = []
        self.size_of_hiddens = [self.input_size] + size_of_hiddens + [self.output_size]
        self.active = active
        if self.active=='sig':
            self.activate = self.sigmoid
            self.activate_prime = self.sigmoid_prime
        elif self.active=='relu':
            self.activate = self.relu
            self.activate_prime = self.relu_prime
        elif self.active=='tanh':
            self.activate = self.tanh
            self.activate_prime = self.tanh_prime
        else:
            self.activate = self.sigmoid
            self.activate_prime = self.sigmoid_prime
            
        self.intialize_weights()
        self.intialize_biases()
        print("NOTE: Please try to give input as numpy array with defined shape eg: (2,1) and try to avoid shape like (2,)")

    def intialize_weights(self):
        self.weights = []
        for i in range(self.no_of_hid+1):
            in_size = self.size_of_hiddens[i]
            ou_size = self.size_of_hiddens[i+1]
            w = np.random.rand(ou_size, in_size)
            self.weights.append(w)

    def intialize_biases(self):
        self.bias = []
        for i in range(self.no_of_hid+1):
            size = self.size_of_hiddens[i+1]
            b = np.random.rand(size, 1)
            self.bias.append(b)

    def sigmoid(self, x):
        z = 1/(1 + np.exp(-x))
        return z

    def sigmoid_prime(self, x):
        y = self.sigmoid(x)
        z = y*(1-y)
        z.reshape(x.shape[0], 1)
        return z
    
    def relu(self, x):
        x[x<0] = 0
        return x
        
    def relu_prime(self, x):
        x[x>=0] = 1
        x[x<0] = 0
        return x
    
    def tanh(self, x):
        z = np.tanh(x)
        return z
        
    def tanh_prime(self, x):
        y = np.tanh(x)
        z = 1-np.square(y)
        z.reshape(x.shape[0], 1)
        return z
    
    def forward_prop(self, x):
        self.hidden_y.clear()
        self.hidden_z.clear()
        for i in range(self.no_of_hid+1):
            y = self.weights[i]@x + self.bias[i]
            z = self.activate(y)
            x = z
            self.hidden_y.append(y)
            self.hidden_z.append(z)
        self.output = x


    def cost(self, y_hatt):
        z = np.sum((0.5*np.square(y_hatt - self.output))/(self.output_size))
        return z

    def cost_prime(self, y_hatt):
        z = (self.output - y_hatt)*(1/self.output_size)
        return z

    def back_prop(self, x, y, rate):
        DJDW = [None]*(self.no_of_hid+1)
        DJDB = [None]*(self.no_of_hid+1)
        DJDB[-1] = np.multiply(self.cost_prime(y), self.activate_prime(self.hidden_y[-1]))
        for i in range(self.no_of_hid-1, -1, -1):
            DJDB[i] = np.multiply(self.weights[i+1].T@DJDB[i+1], self.activate_prime(self.hidden_y[i]))

        DJDW[0] = DJDB[0]@x.T
        for i in range(1, self.no_of_hid+1):
            DJDW[i] = DJDB[i]@self.hidden_z[i-1].T

        for i in range(self.no_of_hid+1):
            self.weights[i] -= rate*DJDW[i]
            self.bias[i] -= rate*DJDB[i]

    def train(self, X, Y, epochs = 60000, rate=0.4):
        n, m = X.shape
        for i in range(1, epochs+1):
            k = np.random.randint(n)
            x = X[k].reshape(self.input_size, 1)
            y = Y[k].reshape(self.output_size, 1)
            self.forward_prop(x)
            self.back_prop(x, y, rate)
            if i%(epochs//10)==0: print(f"epoch: {i}, cost: {self.cost(y)}, {i*100//epochs}% complete...")

    def predict(self, X, symbols=None):
        x = X.reshape(self.input_size, 1)
        self.forward_prop(x)
        var = np.var(self.output)
        pos = np.argmax(self.output)
        symbol=None
        if symbols and len(symbols) == self.output.shape[0]:symbol = symbols[pos]
        return {"out": self.output, "pos": pos, "var": var, "symbol": symbol}