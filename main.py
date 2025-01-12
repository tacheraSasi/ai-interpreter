# import os
import sys
from interpreter import interpret

args = sys.argv

def getFileContent(file_path):
    try:
        with open(file_path,'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File {file_path} does not exist")
    except Exception as e:
        print(f"An error occurred while reading the file: {file_path} ERR:{e}")


if len(args) < 2:
    print("Usage: python main.py <file>")
    sys.exit(1)
else:
    file_name = (args[1])
    if  file_name.endswith(".vint"):
        content = getFileContent(file_name)
        output = interpret(content)
        print(output)
        sys.exit(1)

    print("The file should end with '.ai'")
