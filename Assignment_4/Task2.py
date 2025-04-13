#Taking the user input to write in text file.
a=input("Enter the text to write in the file : ")
#file is open in write mode.
with open ('Output.txt','w') as f:
    f.write(a)
    print("Data successfully written to Output.txt")
    f.close()

#The user input text is going to append in the existing text file.
b=input("Enter the text to append : ")
with open('Output.txt','a') as f1:
    f1.write(b)
    print("Data Successfully append to Output.txt")
    f1.close()

#Opening the file in read mode.
with open('Output.txt','r') as file :
    reading_file = file.read()
    print("Final content of output.txt : ",reading_file)
