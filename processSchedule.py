"""
    Processor Scheduling Simulation
    By: Corey A. Greene
    CS 410 - Operating Systems
    Python 3.0-Interpreter
"""

import numpy as np
import matplotlib.pyplot as plt
import copy

originalData = []
answerArray = []
numProcess = input('Enter The Number of Processes: ')

"""get data"""
for i in range(0, int(numProcess)):
    temp = []
    arrivalTime = input('Enter Arrival Time for Process ' + str(i+1) + ': ')
    serviceTime = input('Enter Service Time for Process ' + str(i+1) + ': ')
    temp.append(int(arrivalTime))
    temp.append(int(serviceTime))
    originalData.append(temp)

"""display the entered data"""
for i in range(0, len(originalData)):
    print(originalData[i])

timeLength = input('Enter the amount of time to run the simulation: ')
choice = input('type FCFS or SPN: ')

"""create answer array"""
for i in range(0, len(originalData)):
    insideArray = []
    for j in range(0, int(timeLength)):
        insideArray.append(0)
    answerArray.append(insideArray)

fcfsData = copy.deepcopy(originalData)
fcfsAnswers = copy.deepcopy(answerArray)
spnData = copy.deepcopy(originalData)
spnAnswers = copy.deepcopy(answerArray)

"""First Come First Serve Algorithm"""
if choice == 'FCFS':
    for i in range(0, int(timeLength)):
        """finds the next process to run """
        currentProcessToRun = 10000
        smallest = 10000
        for x in range(0, len(fcfsData)):
            if fcfsData[x][0] < smallest and fcfsData[x][0] <= i:
                if fcfsData[x][1] > 0:
                    smallest = fcfsData[x][0]
                    currentProcessToRun = x
        """checks that a value is found, and makes the changes"""
        if currentProcessToRun != 10000:
            fcfsData[currentProcessToRun][1] = int(fcfsData[currentProcessToRun][1]) - 1
            fcfsAnswers[currentProcessToRun][i] = 1

    print('********** First Come First Serve ********')
    for i in range(0, len(fcfsData)):
        for j in range(0, int(timeLength)):
            print(fcfsAnswers[i][j], end="")
        print()

    data = np.array(fcfsAnswers)
    # get the indices where data is 1
    x, y = np.argwhere(data == 1).T
    plt.matshow(data)
    plt.show()

"""Shortest Process Next Algorithm"""

if choice == 'SPN':
    i = 0
    while i < int(timeLength):
        """finds the next process to run """
        currentProcessToRun = 10000
        smallest = 10000
        smallestTTR = 10000
        for x in range(0, len(spnData)):
            if spnData[x][0] < smallest and spnData[x][0] <= i:
                if spnData[x][1] < smallestTTR:
                    if spnData[x][1] > 0:
                        smallestTTR = spnData[x][1]
                        currentProcessToRun = x
        """checks that a value is found, and makes the changes"""
        if currentProcessToRun != 10000:
            for y in range(i, i+smallestTTR):
                spnData[currentProcessToRun][1] = int(spnData[currentProcessToRun][1]) - 1
                spnAnswers[currentProcessToRun][y] = 1
            i += smallestTTR
        else:
            i += 1
    print('********** Shortest Process Next *************')
    for i in range(0, len(spnData)):
        for j in range(0, int(timeLength)):
            print(spnAnswers[i][j], end="")
        print()

    otherData = np.array(spnAnswers)
    # get the indices where data is 1
    x, y = np.argwhere(otherData == 1).T
    plt.matshow(otherData)
    plt.show()

