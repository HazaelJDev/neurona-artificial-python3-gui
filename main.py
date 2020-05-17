from Neurona import Neuron
"""@aurhor: Hazael Jiménez"""

def main():
    #       [Umbral, X1, X2]
    inputs = [[1,0,0],[1,1,0],[1,0,1],[1,1,1]]
    #Contador para los inputs
    i = 0
    weights = [3.77,0.36,-5.43]
    outputs = []
    #AND
    #learning = [-1,-1,-1,1]
    #OR
    learning = [-1,1,1,1]
    lcont=0
    mainProcess = True
    back = True
    ajuste = False
    numOutputs = 1
    numGeneration = 0

    neuron = Neuron(inputs,weights,numOutputs)
    while mainProcess:
        if ajuste:
            lcont=0
            i=0
            back = True
            neuron.outputs = []
        print("")
        print("".center(30,"⚡"))
        print("Generación ".center(40," "),numGeneration)
        print("".center(30,"⚡"))
        while back and lcont < len(learning):
            neuron.seeInputs(i)
            neuron.seeWeights()
            print("\n\tSalida esperada: ",learning[lcont])
            neuron.activationFunc(i)
            outputs = neuron.getOutputs() 
            neuron.seeOutputs()
            if outputs[-1] == learning[lcont]:
                lcont+=1
                i+=1
            else:
                print("")
                print("Ajuste de pesos".center(50," "))
                for j in range(0,len(weights)):
                    neuron.weights[j] = neuron.weights[j]+(learning[lcont]*neuron.inputs[i][j])
                    print("peso "+str(j)+" --> ",weights[j])
                back = False
                ajuste = True
        if lcont >= len(learning):
            print("")
            print("Proceso Terminado".center(50," "))
            print("\tGeneración "+str(numGeneration))
            print("\tPesos correctos: "+str(neuron.weights))
            mainProcess = False
        numGeneration += 1
if __name__ == "__main__":
    main()
    