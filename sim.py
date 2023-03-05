import collections
import time
import jsoneng

inspector1Inputs = []
inspector2Inputs = []

"""
state
0, inspector free, initial state
1, inspector inspecting component
2, inspector waiting because buffer full
3, input list empty, end

"""
inspector1State = 0
inspector2State = 0

bufferC1 = [0,0,0]
bufferC2 = 0
bufferC3 = 0

workstation1Outputs = 0
workstation2Outputs = 0
workstation3Outputs = 0
workstation1State = 0
workstation2State = 0
workstation3State = 0

jsoneng.create({})

def readDatFiles(fileName):
    datalist = open(fileName).read().splitlines()
    datalist = [i.strip() for i in datalist]
    datalist = list(filter(None, datalist))
    datalist = [float(i) for i in datalist]
    return datalist

inspector1Inputs = readDatFiles('input files/servinsp1.dat')
inspector2Inputs = readDatFiles('input files/servinsp2.dat')
workstation1Inputs = readDatFiles('input files/ws1.dat')
workstation2Inputs = readDatFiles('input files/ws2.dat')
workstation3Inputs = readDatFiles('input files/ws3.dat')

def ins_1(inputList):
    global inspector1State
    global bufferC1
    inputIndex = 0

    while True:
        if inspector1State == 0:
            """
            inspector free
            """
            status = "inspector 1 is free"

            if inputIndex == len(inspector1Inputs)-1: # reached input end
                inspector1State = 3

            elif bufferC1[0] >= 2 and bufferC1[0] >= 2 and bufferC1[0] >= 2: # if all buffers full
                inspector1State = 2

            else:
                inspector1State = 1 # inspector starts working

        elif inspector1State == 1:
            """
            inspector working
            """
            status = "inspector 1 is working"

            # find smallest buffer
            min = float('inf')
            bestBuffer = -1
            if bufferC1[0] < min:
                min = bufferC1[0]
                bestBuffer = 0
            if bufferC1[1] < min:
                min = bufferC1[1]
                bestBuffer = 1
            if bufferC1[2] < min:
                min = bufferC1[2]
                bestBuffer = 2

            if min < 2:
                bufferC1[bestBuffer] += 1
                time.sleep(inputList[inputIndex]/100) # inspector does work
                jsoneng.patch_kv(inputIndex, inputList[inputIndex])

            if bufferC1[0] >= 2 and bufferC1[1] >= 2 and bufferC1[2] >= 2:
                inspector1State = 2 # inspector will wait next
            else:
                inspector1State = 1 # inspector will work next
            inputIndex+=1

        elif inspector1State == 2:
            """
            inspector waiting
            """
            status = "inspector 1 is waiting"
            pass

        elif inspector1State == 3:
            """
            inspector waiting
            """
            status = "inspector 1 has finished"
            break

def works_1(inputList):
    global workstation1State
    global bufferC1
    inputIndex = 0

    while True:
        if workstation1State == 0:
            if inputIndex == len(workstation1Inputs)-1: # reached input end
                workstation1State = 3
            
            


ins_1(inspector1Inputs)
works_1(workstation1Inputs)
