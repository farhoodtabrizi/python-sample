# Type your code here
def list_from_file(books):
    # Make a connection to the file
    file_pointer = open('books.txt', 'r')
    # You can use either .read() or .readline() or .readlines()
    data = file_pointer.readlines()
    # NOW CONTINUE YOUR CODE FROM HERE!!!
    res = []
    for i in data:
        stripped_line = i.strip('\n')
        res.append(stripped_line)
    print (res)
        
list_from_file ('books.txt')