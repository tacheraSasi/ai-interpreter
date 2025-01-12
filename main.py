import sys

args = sys.argv

if len(args) < 2:
    print("Usage: python main.py <file>")
    sys.exit(1)
else:
    print(args)
    
           
def getFileContent(file_path):
    try:
        with open(file_path,'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File {file_path} does not exist")
    except Exception as e:
        print(f"An error occurred while reading the file: {file_path} ERR:{e}")