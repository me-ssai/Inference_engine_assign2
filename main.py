import sys
import os

def readFile(file_name):
    file=open(file_name,"r")
    KB=''
    data=file.read().splitlines()
    
    for val in range(len(data)):
        if(data[val]=="TELL"):
            KB=data[val+1].split(';')
            KB=[string for string in KB if string!='']
   

    print(KB)
    
       
def main():
    
    #readFile(readFile(str(sys.argv[1])))
    readFile("test_HornKB.txt")

if __name__ == "__main__":
    main()
