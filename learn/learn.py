# With KeyWord in Python:
'''
    for file handling (open, write, ...)
'''
## Without with keyword:
file = open("./file.txt")
try:
    content = file.read()
    print(content) 
except:
    file.close()
    print('Error in File Opening')


## With with keyword --> this close file auto
with open("file.txt") as file:
    content = file.read()
    print(content)



# DataFrame (is 2 dimentional Object)


 