#New Sample.txt is created then trying to read it.
#'try' block is used to handle the exception
try :
    #file handling method.
    #Opening the file in read mode.
    file1 = open('Sample.txt','r')
    read_file = file1.read()
    print(read_file)
    file1.close()
#Handling the exception is file is not exist.
except FileNotFoundError:
    print("Error : The file 'Sample.txt' was not found")
