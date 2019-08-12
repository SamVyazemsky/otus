with open("mynewtextfile.txt",mode="r") as file:
    print("Default encoding:", file.encoding)
    file.close()

# change encoding to utf-8
with open("mynewtextfile.txt",mode="r",encoding="utf-8") as file:
    print("New encoding:", file.encoding)
    file.close()
