from Neurona import Neuron
from tkinter import ttk
from tkinter import *
"""@author: Hazael Jiménez"""

class App:
    def __init__(self, window):
        # Initializations 
        self.wind = window
        self.wind.title('Aplicación de Neurona Artificial')

        # Creating a Frame Container 
        frame = LabelFrame(self.wind, text = 'Ingresa los pesos iniciales:')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        # W1 Input
        Label(frame, text = 'W1: ').grid(row = 1, column = 0)
        self.w1 = Entry(frame,justify=CENTER)
        self.w1.focus()
        self.w1.grid(row = 1, column = 1)

        # W2 Input
        Label(frame, text = 'W2: ').grid(row = 2, column = 0)
        self.w2 = Entry(frame,justify=CENTER)
        self.w2.grid(row = 2, column = 1)
        
        # W3 Input
        Label(frame, text = 'W3: ').grid(row = 3, column = 0)
        self.w3 = Entry(frame,justify=CENTER)
        self.w3.grid(row = 3, column = 1)

        self.opc = IntVar()
        self.opc.set(1)
        #RadioButton
        self.R1 = Radiobutton(frame, text="AND", variable=self.opc, value=1)
        self.R1.grid(row = 4, column = 1)
        self.R2 = Radiobutton(frame, text="OR ", variable=self.opc, value=2)
        self.R2.grid(row = 5, column = 1)   

        # Button Calcular 
        Button(frame, text = 'Calcular', command = self.main).grid(row = 6, columnspan = 2, sticky = W + E)
        Button(frame, text = 'Limpiar', command = self.reset).grid(row = 6, column=4, columnspan = 2, sticky = W + E)

        # Table
        self.tree = ttk.Treeview(height = 13)
        self.tree["columns"]=("one","two","three","four","five","six","seven","eight","nine","ten")
        self.tree.column("#0", width=80, minwidth=50, stretch=NO, anchor = CENTER)
        self.tree.column("one", width=80, minwidth=50, stretch=NO, anchor = CENTER)
        self.tree.column("two", width=80, minwidth=50,stretch=NO, anchor = CENTER)
        self.tree.column("three", width=80, minwidth=50,stretch=NO, anchor = CENTER)
        self.tree.column("four", width=150, minwidth=50,stretch=NO, anchor = CENTER)
        self.tree.column("five", width=150, minwidth=50,stretch=NO, anchor = CENTER)
        self.tree.column("six", width=150, minwidth=50,stretch=NO, anchor = CENTER)
        self.tree.column("seven", width=150, minwidth=50,stretch=NO, anchor = CENTER)
        self.tree.column("eight", width=80, minwidth=50,stretch=NO, anchor = CENTER)
        self.tree.column("nine", width=100, minwidth=50,stretch=NO, anchor = CENTER)
        self.tree.column("ten", width=80, minwidth=50,stretch=NO, anchor = CENTER)

        self.tree.heading('#0', text = 'Generación', anchor = CENTER)
        self.tree.heading('one', text = 'Umbral', anchor = CENTER)
        self.tree.heading('two', text = 'X1', anchor = CENTER)
        self.tree.heading('three', text = 'X2', anchor = CENTER)
        self.tree.heading('four', text = 'W1', anchor = CENTER)
        self.tree.heading('five', text = 'W2', anchor = CENTER)
        self.tree.heading('six', text = 'W3', anchor = CENTER)
        self.tree.heading('seven', text = 'Suma', anchor = CENTER)
        self.tree.heading('eight', text = 'Salida', anchor = CENTER)
        self.tree.heading('nine', text = 'Salida esperada', anchor = CENTER)
        self.tree.heading('ten', text = '¿Correcto?', anchor = CENTER)
        
        self.tree.grid(row = 7, column = 0, columnspan = 2, pady = 20)
       
        #Add Theme
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background="black", fieldbackground="black", foreground="white", relief="flat")
        self.tree.tag_configure("CORRECT", background="green")
        self.tree.tag_configure("ERROR", background="red")

        # Output Messages 
        self.message = Label(text = '', fg = 'green')
        self.message.grid(row = 8, column = 0, columnspan = 2, sticky = W + E)

        self.author = Label(self.wind, text = 'Hazael Jiménez')
        self.author.grid(row=9,column = 1, pady = 20) 

    def reset(self):
        self.w1.delete(0,END)
        self.w2.delete(0,END)
        self.w3.delete(0,END)
        self.opc.set(1)
        self.w1.focus()
        #Cleaning table
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        #Cleaning Label
        self.message["text"] = ""
    
    def main(self):
        if self.opc.get() == 1:
            #AND
            learning = [-1,-1,-1,1]
        else:
            #OR
            learning = [-1,1,1,1]
        
        #       [Umbral, X1, X2]
        inputs = [[1,0,0],[1,1,0],[1,0,1],[1,1,1]]
        #Contador para los inputs
        i = 0

        weights = [float(self.w1.get()),float(self.w2.get()),float(self.w3.get())]
        outputs = []
        lcont=0
        mainProcess = True
        back = True
        ajuste = False
        numOutputs = 1
        numGeneration = 0

        neuron = Neuron(inputs,weights,numOutputs)
        data = []
        while mainProcess:
            if ajuste:
                lcont=0
                i=0
                back = True
                neuron.outputs = []
            print("")
            print("".center(30,"⚡"))
            data.append(str(numGeneration))
            print("Generación ".center(40," "),numGeneration)
            print("".center(30,"⚡"))
            while back and lcont < len(learning):
                neuron.seeInputs(i)
                for j in neuron.inputs[i]:
                    data.append(j)
                neuron.seeWeights()
                for j in neuron.weights:
                    data.append(j)
                print("\n\tSalida esperada: ",learning[lcont])
                neuron.activationFunc(i)
                outputs = neuron.getOutputs() 
                data.append(neuron.suma)
                data.append(outputs[-1])
                data.append(learning[lcont])
                neuron.seeOutputs()
                if outputs[-1] == learning[lcont]:
                    lcont+=1
                    i+=1
                    data.append("Si")
                    if len(data) < 11:
                        data.insert(0,"")
                    #Insert row inside treeview
                    self.tree.insert("", END , text=data[0], values=tuple(data[1:]), tags=["CORRECT"])
                    data = []
                else:
                    data.append("No")
                    print("")
                    print("Ajuste de pesos".center(50," "))
                    for j in range(0,len(weights)):
                        neuron.weights[j] = neuron.weights[j]+(learning[lcont]*neuron.inputs[i][j])
                        print("peso "+str(j)+" --> ",weights[j])
                    back = False
                    ajuste = True
                    if len(data) < 11:
                        data.insert(0,"")
                    #Insert row inside treeview
                    self.tree.insert("", END , text=data[0], values=tuple(data[1:]), tags=["ERROR"])
                    data = []
            if lcont >= len(learning):
                print("")
                print("Proceso Terminado".center(50," "))
                print("\tGeneración "+str(numGeneration))
                print("\tPesos correctos: "+str(neuron.weights))
                self.message['text'] = 'Generación {} \nPesos Correctos: {}'.format(numGeneration, neuron.weights)
                mainProcess = False
            numGeneration += 1

if __name__ == "__main__":
    #main()
    window = Tk()
    application = App(window)
    window.mainloop()
    