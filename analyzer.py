with open("logfile.txt", "r") as file:
    print(f"total records found: {sum(1 for line in file)}")
    file.seek(0)#already reads the whole file, seek(0) moves the file cursor back to position 0(beginning of the file)
    print(file.read())