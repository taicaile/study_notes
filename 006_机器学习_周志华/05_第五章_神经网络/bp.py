import numpy as np 

class SimpleNeuralNetwork():
    """
    A simple one-hidden-layer neural network  
    """ 
    def __init__(self, inputDim, hiddenDim, outputDim):

        self._input_dim = inputDim
        self._hidden_dim = hiddenDim
        self._output_dim = outputDim 

        # Randomly initialize weights and bias
        self.para = {}
        # weight from input to hidden layer
        self.para['W1'] = np.random.random((self._hidden_dim, self._input_dim)) * 0.1 - 0.05
        self.para['b1'] = np.zeros((self._hidden_dim, 1)) 
        # weight from hidden layer to output layer
        self.para['W2'] = np.random.random((self._output_dim, self._hidden_dim)) *0.1 - 0.05
        self.para['b2'] = np.zeros((self._output_dim, 1))
        # Activation function -> Sigmoid function
        self.activation = lambda x:1/(1+np.exp(-x))

    def infer(self, X):
        # predict y 
        alpha = self.activation(self.para['W1'].dot(X) + self.para['b1'])
        y = self.activation(self.para['W2'].dot(alpha) + self.para['b2'])
        return y
    
    def train(self, X, y, eta=0.1, epoch_num=20, batch_size=1):
        """
        eta = learning rate
        """
        def get_batch(a, b, batch_size):
            for i in range(int(np.ceil(a.shape[1] / batch_size))):
                if batch_size * (i+1) > a.shape[1]:
                    yield a[:, batch_size*i:], b[:, batch_size*i:]
                else:
                    yield a[:, batch_size*i:batch_size*(i+1)], b[:, batch_size*i:batch_size*(i+1)]
        # calculate initial loss
        haty = self.infer(X)
        cur_loss = np.sum((haty - y) ** 2)  
        cur_res = 1
        print('initial loss:', cur_loss)
        # update weights 
        for epoch in range(epoch_num):
            for batchx, batchy in get_batch(X, y, batch_size):
                # print(batch.shape)
                grad  = self.get_grad(batchx, batchy)
                for para in self.para.keys():
                    # update 
                    self.para[para] -=  eta * grad[para]
                haty = self.infer(X)
                loss = np.sum((haty - y) ** 2)
            
            haty = self.infer(X)
            loss = np.sum((haty - y) ** 2)
            if epoch % 5000 == 0:
                print("epoch ", epoch, ": ")
                print("loss: ", loss)
            res = np.abs(cur_loss - loss)  

            if (res < 1e-6)and (cur_res < 1e-6):
                print('已收敛，经过',epoch, 'epoch')
                return epoch
                break
            cur_loss = loss
            cur_res = res

    def get_grad(self, batchX, y):
        b = self.activation(self.para['W1'].dot(batchX) + self.para['b1'])
        haty = self.activation(self.para['W2'].dot(b) + self.para['b2'])
        g = haty * (1 - haty) * (y - haty)
        e = b * (1-b) * self.para['W2'].T.dot(g)

        grad = {}
        grad['W2'] = - g.dot(b.T)
        grad['b2'] = - g.sum(axis=1, keepdims=True)
        grad['W1'] = - e.dot(batchX.T)
        grad['b1'] = - e.sum(axis=1, keepdims=True)

        return grad
