try:
    with open('myfile.txt','r') as myfile:
        data=myfile.read()
        reading_file=file.read()
except FileNotFoundError:
    print("Error: The file 'samples.txt' was not found")


