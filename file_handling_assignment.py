#File creation
def create_file():
    try:
        with open("my_file.txt", 'w') as file:
            file.write("My name is Faith\n")
            file.write("I come from Kenya\n")
            file.write("My phone number is: 012345678\n")
            
        print("File 'my_file.txt' created successfully.")
        
    except PermissionError:
        print("Permission denied to create the file.")
        
    except Exception as e:
        print("An error occurred:", e)
        
#File Reading and Display
def read_file():
    try:
        with open("my_file.txt", 'r') as file:
            content = file.read()
            print("Content of 'my_file.txt':")
            print(content)
            
    except FileNotFoundError:
        print("File 'my_file.txt' not found.")
        
    except Exception as e:
        print("An error occurred: ", e)
        
#File Appending
def append_to_file():
    try:
        with open("my_file.txt", 'a') as file:
            file.write("I live in Nairobi\n")
            file.write("I am currently studying under the PLP\n")
            file.write("I am doing a python project\n")
        print("Content appended to 'my_file_txt' successfully.")
        
    except PermissionError:
        print("Permission denied to append to the file.")
        
    except Exception as e:
        print("An error ocurred:", e)
        
#Error Handling
def main():
    create_file()
    read_file()
    append_to_file()
    

if __name__ == "__main__":
    main()
 
 #           