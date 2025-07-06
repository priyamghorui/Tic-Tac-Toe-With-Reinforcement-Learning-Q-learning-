import random
import numpy as np

def userInput(r,c,arr):
    arr[r][c]=-1
    return arr

def sysInput(arr):
    num1 = random.randint(0, 2)
    num2 = random.randint(0, 2)
    if(arr[num1][num2]==1 or arr[num1][num2]==-1):
        return sysInput()
    else:
        arr[num1][num2]=-1
        return 1
def agentInput(a,b,arr):
    arr[a][b]=1
    return arr

def checkWin(arr):
    target_400 = [1, 1, 1]
    target_200 = [-1, -1, -1]

    for row in arr:
        if np.array_equal(row, target_400):
            return 4
        elif np.array_equal(row, target_200):
            return 2

    for col in arr.T:
        if np.array_equal(col, target_400):
            return 4
        elif np.array_equal(col, target_200):
            return 2

    main_diag = arr.diagonal()
    if np.array_equal(main_diag, target_400):
        return 4
    elif np.array_equal(main_diag, target_200):
        return 2

    anti_diag = np.fliplr(arr).diagonal()
    if np.array_equal(anti_diag, target_400):
        return 4
    elif np.array_equal(anti_diag, target_200):
        return 2

    return 0  # No match found
def contains_zero(arr):
    return np.any(arr == 0)

def resetBoard():
  resetArr=np.zeros((3, 3))
  return resetArr
def get_valid_actions(arr):
    valid_actions = []
    for i in range(3):
        for j in range(3):
            if arr[i][j] == 0:
                valid_actions.append((i, j))

    return valid_actions

def realuser(input,arr):
    # user1=int(input("Enter positio >> "))
    match input:
        case 1:
            arr[0][0]=-1
            return arr
        case 2:
            arr[0][1]=-1
            return arr
        case 3:
            arr[0][2]=-1
            return arr
        case 4:
            arr[1][0]=-1
            return arr
        case 5:
            arr[1][1]=-1
            return arr
        case 6:
            arr[1][2]=-1
            return arr
        case 7:
            arr[2][0]=-1
            return arr
        case 8:
            arr[2][1]=-1
            return arr
        case 9:
            arr[2][2]=-1
            return arr
def checkcell(action):
    # user1=int(input("Enter positio >> "))
    match action:
        case (0,0):
            return 1
        case (0,1):
            return 2
        case (0,2):
            return 3
        case (1,0):
            return 4
        case (1,1):
            return 5
        case (1,2):
            return 6
        case (2,0):
            return 7
        case (2,1):
            return 8
        case (2,2):
            return 9