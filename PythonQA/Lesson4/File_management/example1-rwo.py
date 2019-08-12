with open('data.txt', 'w') as f:
    data = 'some data to be written to the file'
    f.write(data)
    s = f.read()
    print(s)

