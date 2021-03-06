from PyML import *
from math import *
import sys
import os

## Check arguments
def die():
    print "Usage: python pySVM.py -a <Path to training data> <path to binary data\nuse -a if the path is to ~/FreePizza/data/txt/";
    exit()


if len(sys.argv) < 3:
    die()

mypath = os.getenv("HOME")

#If -a flag is used, prepend string with home data
if sys.argv[1] == "-a":
    path1 = mypath + "/FreePizza/data/txt/" + sys.argv[2]
    path2 = mypath + "/FreePizza/data/txt/" + sys.argv[3]
else:
    path1 = sys.argv[1]
    path2 = sys.argv[2]


## Let's grab the data and put it into a list of lists for the SVM

#Initialize
X = []

#Now read the data
with open('/home/shawn/FreePizza/data/txt/upvsdown.txt','r') as f:

    #Keep a counter
    i = 0;

    #Now read in line per line
    for line in f:

        #Split the data inside of the brackets
        if i < 5670:
            temp = line[1:-2].split(", ");
        else:
            temp = line[1:-1].split(", ");

        #Replace a*^b to aeb to be read in scientific notation
        temp = [t.replace('*^','e') for t in temp];
        temp = map( lambda x: float(x), temp);

        #Now, append our vector X with the data
        X.append(temp)

        i = i + 1

## Now we load in the got_pizza dataset

#Initialize
y = []
with open('/home/shawn/FreePizza/data/txt/gotpizza.txt','r') as gp:

    for line in gp:
        # Turn string to boolean
        if line.rstrip() == 'True':
            temp = 'True'
        else:
            temp = 'False'

        y.append(temp)

## Now it's time to load our data into PyML's vector objects

data = VectorDataSet(X2,L=y2)

#Create SVM object, then train our set
s = SVM()
s.train(data)
s.save("freePizza")

## Yay!

# Now to cross-validate the data; we first take the other set
X3 = X[fifth+1:-1];
y3 = y[fifth+1:-1];

print y3
#Load our training data
from PyML.classifiers.svm import loadSVM
loadedSVM = loadSVM("freePizza",data)

testData = VectorDataSet(X3,L=y3)
r = loadedSVM.test(testData)
print r
