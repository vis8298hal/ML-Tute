def read_file():
    file = open("./sample.txt", "r")
    if file.mode == "r":
        contents = file.readlines()
        print(contents)
def append_file():
    file = open("./sample.txt", "a")
    for i in range(10):
        file.write("This is appended Text\n")
    file.close() 
def read_write_file():
    file = open("./sample.txt", "w+")
    for i in range(10):
        file.write("This is simple text\n")
    file.close()
def main():
    # Read File
    read_file()

if __name__ == "__main__":
    main()