""" read() - Return entire file
    seek(offset) - Change the current position to offset
    seek(0) - Go to the beginning of the file
    seek(5) - Go to the 5th byte of the file
    tell() - DEtermine the current position of file
"""
input_file = open('D:\LEARNING\PYTHON\Python Cognizant\input.txt')
print("Current position is : {}".format(input_file.tell()))

print(input_file.read())
print("Current position is : {}".format(input_file.tell()))

input_file.seek(5)
print("Current position is : {}".format(input_file.tell()))
print(input_file.read())
print("Current position is : {}".format(input_file.tell()))

# WE can tell the read function from where it has to read the file
input_file = open('D:\LEARNING\PYTHON\Python Cognizant\input.txt')
print(input_file.read(5))
print(input_file.tell())

# Always remember to close or use 'with' as it would automatically close the file when block of code is executed.
input_file.close()
print("\n Using with : ")
with open('D:\LEARNING\PYTHON\Python Cognizant\input.txt') as input_file_ptr :
    print(input_file_ptr.read())
    input_file_ptr.seek(0)
    print(input_file_ptr.read(5))
    print(input_file_ptr.tell())

# demonstration of closing using closed attribute
print("File closed : {}".format(input_file_ptr.closed))

# For opening a file and reading it line by line we use for line loop
with open('D:\LEARNING\PYTHON\Python Cognizant\input.txt') as input_file_ptr :
    for line in input_file_ptr:
        print(line) 
    print("The previous one prints the new line charactor too so use rstrip()")
    input_file_ptr.seek(0)
    for line in input_file_ptr:
        print(line.rstrip())

# Writing to a file
with open('D:\LEARNING\PYTHON\Python Cognizant\input.txt','w') as input_file_ptr :
    input_file_ptr.write('\n Excited for learning.')

with open('D:\LEARNING\PYTHON\Python Cognizant\input.txt') as input_file_ptr :
    print(input_file_ptr.read())