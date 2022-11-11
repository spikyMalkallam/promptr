import os
import sys

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        raise Exception("Usage: ./promptr <script_name>")
    #Open the script
    script = open(sys.argv[1],"r",encoding="utf-8")

    #Read first line
    currentLine = script.readline()
    
    #Read while there is content in the file
    while currentLine != "":
        print(currentLine)

        
        #Read next line
        currentLine = script.readline()

