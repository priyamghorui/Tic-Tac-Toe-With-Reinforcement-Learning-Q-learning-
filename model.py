# # ******************** Here 1 for agent move and -1 for user or system move who play against the agent **************************
# # ******************** Here 4 for agent win and 2 for user or system win who play against the agent **************************

# import numpy as np
# import random
# arr = np.zeros((3, 3))
# print(arr)
# def userInput(r,c):
#     arr[r][c]=-1

# def sysInput():
#     num1 = random.randint(0, 2)
#     num2 = random.randint(0, 2)
#     if(arr[num1][num2]==1 or arr[num1][num2]==-1):
#         return sysInput()
#     else:
#         arr[num1][num2]=-1
#         return 1
# def agentInput(a,b):
#     arr[a][b]=1

# def checkWin():
#     target_400 = [1, 1, 1]
#     target_200 = [-1, -1, -1]

#     # Check rows
#     for row in arr:
#         if np.array_equal(row, target_400):
#             return 4
#         elif np.array_equal(row, target_200):
#             return 2

#     # Check columns
#     for col in arr.T:
#         if np.array_equal(col, target_400):
#             return 4
#         elif np.array_equal(col, target_200):
#             return 2

#     # Check main diagonal
#     main_diag = arr.diagonal()
#     if np.array_equal(main_diag, target_400):
#         return 4
#     elif np.array_equal(main_diag, target_200):
#         return 2

#     # Check anti-diagonal
#     anti_diag = np.fliplr(arr).diagonal()
#     if np.array_equal(anti_diag, target_400):
#         return 4
#     elif np.array_equal(anti_diag, target_200):
#         return 2

#     return 0  # No match found
# def contains_zero():
#     return np.any(arr == 0)

# def resetBoard():
#   global arr
#   arr=np.zeros((3, 3))

# def get_valid_actions():
#     valid_actions = []
#     for i in range(3):
#         for j in range(3):
#             if arr[i][j] == 0:
#                 valid_actions.append((i, j))

#     return valid_actions
# def realuser():
#     user1=int(input("Enter positio >> "))
#     match user1:
#         case 1:
#             userInput(0,0)
#             pass
#         case 2:
#             userInput(0,1)
#             pass
#         case 3:
#             userInput(0,2)
#             pass
#         case 4:
#             userInput(1,0)
#             pass
#         case 5:
#             userInput(1,1)
#             pass
#         case 6:
#             userInput(1,2)
#             pass
#         case 7:
#             userInput(2,0)
#             pass
#         case 8:
#             userInput(2,1)
#             pass
#         case 9:
#             userInput(2,2)
#             pass





# # ************** This is for training phase **********************
# # Agent play move first :
# epsilon = 1.0
# min_epsilon = 0.01
# decay_rate = 0.995
# Q = {}
# alpha = 0.1
# gamma = 0.9

# for episode in range(500000):
#     resetBoard()
#     while contains_zero():
#         state = tuple(arr.flatten())
#         valid_actions = get_valid_actions()


#         if random.random() < epsilon:
#             action = random.choice(valid_actions)
#             print("Explore:", action)
#         else:
#             q_values = [Q.get((state, a), 0) for a in valid_actions]
#             max_q = max(q_values)
#             best_actions = [a for a, q in zip(valid_actions, q_values) if q == max_q]
#             action = random.choice(best_actions)
#             print("Exploit:", action)

#         agentInput(action[0], action[1])


#         done = False
#         reward = 0

#         if checkWin() == 4:
#             reward = 1
#             done = True
#             print("Agent Wins!")
#         elif not contains_zero():
#             reward = 0.5
#             done = True
#             print("Draw!")
#         else:
#             sysInput()
#             if checkWin() == 2:
#                 reward = -1
#                 done = True
#                 print("Agent Loses!")
#             elif not contains_zero():
#                 reward = 0.5
#                 done = True
#                 print("Draw!")
#             else:
#                 reward = 0
#                 done = False


#         next_state = tuple(arr.flatten())
#         next_valid_actions = get_valid_actions()
#         max_next_q = max([Q.get((next_state, a), 0) for a in next_valid_actions], default=0)
#         old_q = Q.get((state, action), 0)
#         Q[(state, action)] = old_q + alpha * (reward + gamma * max_next_q - old_q)
#         print(f"Q[{state}, {action}] = {Q[(state, action)]:.3f}")

#         if done:
#             break

#     epsilon = max(min_epsilon, epsilon * decay_rate)






# # ************** This is for training phase **********************
# # Agent play move second :
# epsilon = 1.0
# min_epsilon = 0.01
# decay_rate = 0.995
# Q = {}
# alpha = 0.1
# gamma = 0.9

# wins = 0
# losses = 0
# draws = 0

# for episode in range(100000):
#     resetBoard()
#     action = None
#     result = None

#     while contains_zero():
#         sysInput()

#         if checkWin() == 2:
#             reward = -1
#             # print("loss")
#             result = True
#         elif not contains_zero():
#             reward = 0.5
#             result = True
#         else:
#             state = tuple(arr.flatten())
#             valid_actions = get_valid_actions()
#             if random.random() < epsilon:
#                 action = random.choice(valid_actions)
#             else:
#                 q_values = [Q.get((state, a), 0) for a in valid_actions]
#                 max_q = max(q_values)
#                 best_actions = [a for a, q in zip(valid_actions, q_values) if q == max_q]
#                 action = random.choice(best_actions)
#             # print(arr)
#             # print(">>")
#             agentInput(action[0], action[1])
#             # print(arr)

#             if checkWin() == 4:
#                 reward = 1
#                 result = True
#                 # print("win")
#             elif not contains_zero():
#                 reward = 0.5
#                 result = True
#             else:
#                 reward = 0
#                 result = False

#         next_state = tuple(arr.flatten())
#         next_valid_actions = get_valid_actions()
#         max_next_q = max([Q.get((next_state, a), 0) for a in next_valid_actions], default=0)
#         old_q = Q.get((state, action), 0)
#         Q[(state, action)] = old_q + alpha * (reward + gamma * max_next_q - old_q)

#         if result:
#             break

#     epsilon = max(min_epsilon, epsilon * decay_rate)
# import pickle





# # ************** This is phase where save the model **********************

# with open("q_table_# Agent play move first #500000.pkl", "wb") as f:
#     pickle.dump(Q, f)




# # ************** This is phase where load the model **********************

# with open("model path", "rb") as f:
#     QL = pickle.load(f)




# # ******************* This is for testing phase **********************
# # Agent play move first :

# resetBoard()

# while contains_zero():
#     state = tuple(arr.flatten())
#     valid_actions = get_valid_actions()

#     q_values = [QL.get((state, a), 0) for a in valid_actions]
#     max_q = max(q_values)
#     best_actions = [a for a, q in zip(valid_actions, q_values) if q == max_q]
#     action = random.choice(best_actions)
#     print("Agent best_actions:", best_actions)
#     agentInput(action[0], action[1])
#     print("Agent move:", action)

#     if checkWin() == 4:
#         print("Agent Wins!")
#         break
#     elif not contains_zero():
#         print("Draw!")
#         break
#     print(arr)
#     # sysInput()
#     realuser()
#     print(arr)
#     print("Opponent moved.")

#     if checkWin() == 2:
#         print("Agent Loses!")
#         break
#     elif not contains_zero():
#         print("Draw!")
#         break





# # ******************* This is for testing phase **********************
# # Agent play move second :

# resetBoard()

# while contains_zero():
    
#     print(arr)
#     realuser()

#     if checkWin() == 2:
#         print("Agent Loss!")
#         break
#     elif not contains_zero():
#         print("Draw!")
#         break
#     else:
#         print("Board after user move:")
#         print(arr)

      
#         state = tuple(arr.flatten())
#         valid_actions = get_valid_actions()
#         print(valid_actions)
#         if not valid_actions:
#             print("No valid agent moves left!")
#             break

#         q_values = [QL.get((state, a), 0) for a in valid_actions]
#         max_q = max(q_values)
#         best_actions = [a for a, q in zip(valid_actions, q_values) if q == max_q]
#         action = random.choice(best_actions)
#         print("Agent best actions", best_actions)
#         agentInput(action[0], action[1])

#         print("Board after agent move:")
#         print(arr)

#         if checkWin() == 4:
#             print("Agent Wins!")
#             break
#         elif not contains_zero():
#             print("Draw!")
#             break
