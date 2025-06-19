with open("k.txt", "r") as f:  #with is a context manager
    content = f.read()
    print(content)

#no need to write f.close() because file is already closed by default when using "with syntax"

