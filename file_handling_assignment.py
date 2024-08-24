def create_file():
    try:
        with open('my_file.txt', 'w') as file:
            file.write("This is the first line of text.\n")
            file.write("Here is the second line with a number: 123\n")
            file.write("Finally, this is the third line with more text.\n")
        print("File 'my_file.txt' created and initial content written.")
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")

def read_file():
    try:
        with open('my_file.txt', 'r') as file:
            content = file.read()
            print("\nFile Content After Initial Write:\n")
            print(content)
    except FileNotFoundError:
        print("The file does not exist.")
    except PermissionError:
        print("You do not have permission to read the file.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

def append_to_file():
    try:
        with open('my_file.txt', 'a') as file:
            file.write("Appending the fourth line.\n")
            file.write("Adding the fifth line with more text.\n")
            file.write("This is the sixth line added to the file.\n")
        print("Additional lines appended to 'my_file.txt'.")
    except FileNotFoundError:
        print("The file does not exist.")
    except PermissionError:
        print("You do not have permission to write to the file.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")

def main():
    create_file()
    read_file()
    append_to_file()
    read_file()

if __name__ == "__main__":
    main()
