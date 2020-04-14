from textgenrnn import textgenrnn
import tkinter as tk
from tkinter import filedialog

textgen = textgenrnn()

def main():
    exit = False
    while exit == False:
        print("////////// Textgenrnn //////////\n")
        print("1 - Generate random samples")
        print("2 - Generate prefixed sample")
        print("3 - Interactive sample")
        print("4 - Train model on text input")
        print("5 - Reset model")
        print("6 - Exit\n")
        choice  = int(input("Please choose an option: "))
        if choice == 1:
            try:
                randomSamples()
            except:
                print("An error occured returning to menu")
        elif choice == 2:
            try:
                prefixedSamples()
            except:
                print("An error occured returning to menu")
        elif choice == 3:
            try:
                interactiveSample()
            except:
                print("An error occured returning to menu")
        elif choice == 4:
            try:
                trainOnFile()
            except:
                print("An error occured returning to menu")
        elif choice == 5:
            try:
                resetModel()
            except:
                print("An error occured returning to menu")
        elif choice == 6:
            return
        else:
            print("Please enter a number 1-3")

#produce a set amount of random samples
def randomSamples():
    samples = int(input("How many samples would you like to produce? (Default 5): "))

    if samples <= 0 or samples == None:
        samples = 5

    textgen.generate(int(samples))

#produce a prefixed sample
def prefixedSamples():
    prefix = input("What would you like to prefix your samples with? (Default apple): ")

    if prefix == None:
        prefix = "Apple"

    number = int(input("How many samples would you like to produce? (Default 5): "))

    if number <= 0 or number == None:
        number = 5

    generated_texts = textgen.generate(n=number, prefix=prefix,temperature=0.2,return_as_list=True)
    for i in range(len(generated_texts)):
        print(i+1, " - " ,generated_texts[i], "\n")

#train on a text file
def trainOnFile():
    readyToTrain = False
    hasFile = False
    while readyToTrain == False:
        #get a file to train from
        while hasFile == False:
            print("###################################################")
            print("# For training select a .txt file                 #")
            print("# The first line of the text file MUST BE 'title' #")
            print("###################################################")

            root = tk.Tk()
            root.withdraw()

            filePath = filedialog.askopenfilename()

            correctFile = input("Is this the correct file?(Y/N) : " + filePath + ": ")
            if correctFile == "Y":
                hasFile = True
            else:
                hasFile = False

        #make sure the file is in the correct format
        file = open(filePath, "r")
        firstLine = file.readline().strip()
        print(firstLine)

        if firstLine == "title":
            readyToTrain = True
        else:
            print("File is in incorrect format")

            getNewFile = input("Would you like to select a new file (Y/N) : ")
            if getNewFile == "Y":
                hasFile = False
            elif getNewFile == "N":
                return

        #get number of epochs
        noOfEpochs = int(input("How many training epochs do you want to train in this dataset (default 50) : "))

        if noOfEpochs <= 0 or noOfEpochs == None:
            noOfEpochs = 50

        #train on the data
        textgen.train_from_file(filePath, num_epochs=noOfEpochs)      
    
#interactive sample
def interactiveSample():
    options = int(input("How many options would you like to choose from? (default 5): "))

    if options <= 0 or options == None:
        options = 5

    textgen.generate(interactive=True, top_n=options)

#reset model to pretrained state
def resetModel():
    reset = input("This will reset the model back to its pretrained state, do you want to continue? (Y/N) : ")
    if reset == "Y":
        textgen.reset
        print("Model has been reset")
    else:
        return
        
#run the menu
main()
