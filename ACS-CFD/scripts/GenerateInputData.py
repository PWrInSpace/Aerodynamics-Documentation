# GenerateInputData.py

# Script for generation of input tables for parametric simulations
# Input: Sets or Number of random points with ranges
# Output: CSV file with Product of Sets or Random points

from random import triangular, uniform
import string
import pandas as pd
import itertools
import sys
import ast

Output = pd.DataFrame()

Argument = None

try:
    Argument = sys.argv[1]
except IndexError:
    pass

if(Argument == "-h" or Argument =="--help"):
    print("Usage: python3 " + sys.argv[0] + " <command>")
    print("Commands:")
    print("-h or --help     help")
    print("-rd              random gausian")
    print("-ru              random uniform")
    print("<noCommand>      product")
    print()
    print("Script for generation of input tables for parametric simulations")
    print("Input: Sets or Number of random points with ranges")
    print("Output: CSV file with Product of Sets or Random points")
    exit()
elif(Argument == "-rd"):
    print("Number of parameters:")
    parametersNum = int(input())

    print("Number of samples:")
    samplesNum = int(input())
    
    rangeTable = [[None for _ in range(parametersNum)] for _ in range(2)]

    for i in range(parametersNum):
        print("Range parameter " + str(i))
        minVal = float(input())
        maxVal = float(input())


        ColumnList = []
        for k in range(samplesNum):
            ColumnList.append(triangular(minVal, maxVal))

        Output[i] = ColumnList
   

elif(Argument == "-ru"):
    print("Number of parameters:")
    parametersNum = int(input())

    print("Number of samples:")
    samplesNum = int(input())
    
    rangeTable = [[None for _ in range(parametersNum)] for _ in range(2)]

    for i in range(parametersNum):
        print("Range parameter " + str(i))
        minVal = float(input())
        maxVal = float(input())


        ColumnList = []
        for k in range(samplesNum):
            ColumnList.append(uniform(minVal, maxVal))

        Output[i] = ColumnList



else: 
    print("Number of parameters:")
    parametersNum = int(input())
    print("Insert sets in form: [<float>, <float>, ...]")

    Flist = []

    CollumnName = [i for i in range(parametersNum)]

    for i in range(parametersNum):
        print("Set " + str(i))
        helperList = ast.literal_eval(input())
        Flist.append(helperList)

    Product = list(itertools.product(*Flist, repeat=1))

    Output = pd.DataFrame(Product)


print(Output)

Output.to_csv('output.csv', index=False, decimal=',')

    
    
        
