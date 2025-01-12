import sys

args = sys.argv

if len(args) < 2:
    print("Usage: python main.py <file>")
    sys.exit(1)
else:
    print(args)
    
    
    
    
def getFileContent(file_path):
    