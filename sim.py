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

bufferC1_1 = 0
bufferC1_2 = 0
bufferC1_3 = 0
bufferC2 = []
bufferC3 = []

workstation1Outputs = []
workstation2Outputs = []
workstation3Outputs = []
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

inspector1Inputs = collections.deque(readDatFiles('InputFiles/servinsp1.dat'))
inspector2Inputs = collections.deque(readDatFiles('InputFiles/servinsp1.dat'))

print(inspector1Inputs)

def ins_1(inputList):
    global inspector1State
    global bufferC1_1
    global bufferC1_2
    global bufferC1_3
    inputIndex = 0

    while True:
        if inspector1State == 0:
            """
            inspector free
            """
            # print(inspector1State)

            if inputIndex == len(inspector1Inputs)-1: # reached input end
                inspector1State = 3

            elif bufferC1_1 >= 2 and bufferC1_2 >= 2 and bufferC1_3 >= 2: # if all buffers full
                inspector1State = 2

            else:
                inspector1State = 1 # inspector starts working

        elif inspector1State == 1:
            """
            inspector working
            """
            # print(inspector1State)
            
            buffer = min(bufferC1_1,bufferC1_2,bufferC1_3) # find smallest buffer
            print(buffer)
            buffer += 1
            time.sleep(inputList[inputIndex]/100) # inspector does work
            
            jsoneng.patch_kv(inputIndex, inputList[inputIndex])

            if bufferC1_1 >= 2 and bufferC1_2 >= 2 and bufferC1_3 >= 2: # if all buffers full
                inspector1State = 2 # inspector will wait next
            else:
                inspector1State = 1 # inspector will work next
            inputIndex+=1

        elif inspector1State == 2:
            """
            inspector waiting
            """
            # print(inspector1State)
            break



ins_1(inspector1Inputs)
