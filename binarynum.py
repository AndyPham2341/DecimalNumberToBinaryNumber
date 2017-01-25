import sys
#check for two arguments: input file and output file
if(len(sys.argv) != 3):
    print("usage: python binarynum.py inputfile outputfile")
    quit()
    
#open the input file and get the numbers
with open(sys.argv[1]) as f:
    numbers = [int(x) for x in f]
    
#print the input number
print("input number {0}".format(numbers))
#open the place to write the file

with open(sys.argv[2],"w") as file:
    #loop through number, write decimal numbers as 32 bits
    for idx, num in enumerate(numbers):
        #convert decimal number to binary number with padding so it's 32 bits
        binNum = "{:0>32}".format(bin(num)[2:])
        #write to file
        file.write(binNum + "\n")
        #write to console
        print("index{0}: Binary number of {1} is {2}".format(idx,num,binNum))
