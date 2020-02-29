import numpy, random, os
lr = 0.5 #Learning rate
bias = 1 #value of bias
weights = [random.random(),random.random(),random.random()] #The connection weights generated as a list 3 total weights 2 neurons and a bias

print("Before training:", weights[0], " ",weights[1], " ",weights[2])
                                                            
def Perceptron(input1, input2, ExpOutput) :
    output = input1*weights[0] + input2*weights[1]+bias*weights[2]
    
    #Activation function
    if output > 0 : 
        output = 1
    else :
        output = 0

    error = ExpOutput - output
    weights[0] += error * input1 * lr
    weights[1] += error * input2 * lr
    weights[2] += error * bias * lr

for i in range(50):
        Perceptron(1,1,1) #true or true
        Perceptron(1,0,1) #true or false
        Perceptron(0,1,1) #false or true
        Perceptron(0,0,0) #false or false  

print("After training:", weights[0], " ",weights[1], " ",weights[2])

exit = False

while exit == False :
    print("input var X:")
    x = int(input())
    print("input var Y:")
    y = int(input())

    output = x*weights[0] + y*weights[1] + bias*weights[2]

    #Activation function
    if output > 0 : 
        output = 1
    else :
        output = 0

    print(x, "or", y, "is : ", output)

    if exit == True :
        break


