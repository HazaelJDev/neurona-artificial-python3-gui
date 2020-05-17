from funcionActivacion import activationFunction
class Neuron:
    activation = 0
    inputs = []
    weights = []
    outputs = []
    numOutputs = 0
    function = ''

    def __init__(self, inputs, weights, numOutputs):
        self.weights = weights
        self.inputs = inputs
        self.numOutputs = numOutputs
        self.function = activationFunction()

    def activationFunc(self,i):
        suma = 0
        for j in range(0,len(self.inputs[i])):
            suma += (self.inputs[i][j] * self.weights[j])
        print("\tSuma antes de la función de activación: ",suma)
        self.activation = self.function.signFunction(suma)
        self.__fillOutputs()

    def __fillOutputs(self):
        for i in range(0,self.numOutputs):
            self.outputs.append(self.activation)
    
    def seeInputs(self,i):
        print("")
        print("Entradas".center(50," "))
        for j in self.inputs[i]:
            print("\t"+str(j))
    
    def seeWeights(self):
        print("")
        print("Pesos".center(50," "))
        for i in self.weights:
            print("\t"+str(i))
    
    def seeOutputs(self):
        print("")
        print("Salidas".center(50," "))
        for i in self.outputs:
            print("\t",i)
        print("".center(30,"⚡"))
    
    def getOutputs(self):
        return self.outputs
        