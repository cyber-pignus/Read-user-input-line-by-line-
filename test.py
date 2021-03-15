import sys
import pathlib
i = 1
while i == 1:
 inputdata = input()
 if( inputdata == 'exit'):
       i = 0
       break
 inputda = inputdata.split()
 first_arg = inputda[0]
 second_arg = inputda[1]
 file = pathlib.Path(second_arg)
 if file.exists ():
    def numrows(fname):
        with open(fname) as f:
                for i, l in enumerate(f):
                        pass
        return(i + 1)


    def numcols(fname):
        max1 = 0
        with open(fname) as f:
           for i, l in enumerate(f):
                  a = len(l.split())
                  if(max1 < a):
                     max1 = a

        return(max1)
    if( first_arg == 'numrows'):
       print(numrows(second_arg))
    elif( first_arg == 'numcols'):
       print(numcols(second_arg))
    else:
      print("Incorrect Command") 
 else:
    print ("File not found")


