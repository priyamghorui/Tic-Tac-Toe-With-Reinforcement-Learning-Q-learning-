from django.shortcuts import render
from django.http import JsonResponse
from modelComponents import *
import pickle
import os
import json
from django.conf import settings
from django.http import HttpResponseRedirect
from django.views.decorators.cache import never_cache
@never_cache
def index(request):
    return render(request,"index.html")
def agentmovesecond(request):
    return render(request,"agentmovesecond.html")
def randommove(request):
    board = request.session.get('board') 
    if board is not None:
        arr = np.array(board)
    else:
        arr = resetBoard()
    state = tuple(arr.flatten())
    valid_actions = get_valid_actions(arr)
    # Always exploit (no exploration)
    action = random.choice(valid_actions)
    # print("Agent best_actions:", best_actions)
    result=agentInput(action[0], action[1],arr)
    # print("Agent move:", action)
    # print(arr)
    request.session.clear()
    request.session['board'] = result.tolist()
    if checkWin(arr) == 4:
        # print("Agent Wins!")
        return JsonResponse({"cell":checkcell(action),"result":"Agent Win"}) 
    elif not contains_zero(arr):
        # print("Draw!")
        return JsonResponse({"cell":checkcell(action),"result":"Draw"}) 
    else:
        return JsonResponse({"cell":checkcell(action),"result":"online"}) 
def agentMove(request):
    
    file_path_second = os.path.join(settings.BASE_DIR, 'ticTactoe', 'q_table_# Agent play move second 100000.pkl')
    file_path_first = os.path.join(settings.BASE_DIR, 'ticTactoe', 'q_table_# Agent play move first ##modify1000000.pkl')
    if(request.GET.get('term')=="second"):
        with open(file_path_second, "rb") as f:
            QL = pickle.load(f)
    else:
        with open(file_path_first, "rb") as f:
            QL = pickle.load(f)
    board = request.session.get('board') 
    if board is not None:
        arr = np.array(board)
    else:
        arr = resetBoard()
    state = tuple(arr.flatten())
    valid_actions = get_valid_actions(arr)
    # Always exploit (no exploration)
    q_values = [QL.get((state, a), 0) for a in valid_actions]
    max_q = max(q_values)
    best_actions = [a for a, q in zip(valid_actions, q_values) if q == max_q]
    action = random.choice(best_actions)
    # print("Agent best_actions:", best_actions)
    result=agentInput(action[0], action[1],arr)
    # print("Agent move:", action)
    # print(arr)
    request.session.clear()
    request.session['board'] = result.tolist()
    if checkWin(arr) == 4:
        # print("Agent Wins!")
        return JsonResponse({"cell":checkcell(action),"result":"Agent Win"}) 
    elif not contains_zero(arr):
        # print("Draw!")
        return JsonResponse({"cell":checkcell(action),"result":"Draw"}) 
    else:
        return JsonResponse({"cell":checkcell(action),"result":"online"}) 
def userMove(request):
    # print(request.GET.get('cell'))
    board = request.session.get('board')  
    if board is not None:
        board = np.array(board)
    else:
        board = resetBoard()
    # board = np.array(board)
    result=realuser(int(request.GET.get('cell')),board)
    # print(type(result)) 
    request.session.clear()
    request.session['board'] = result.tolist()
    # return JsonResponse({'result':"Done"}) 
    if checkWin(board) == 2:
        # print("Agent Loses!")
        return JsonResponse({"result":"Agent Loss"}) 
    elif not contains_zero(board):
        # print("Draw!")
        return JsonResponse({"result":"Draw"}) 
    else:
        return JsonResponse({"result":"online"}) 
       
def sessionClear(request):
    try:
        request.session.clear()
        return JsonResponse({'result':"Done"}) 
    except:
        return JsonResponse({'result':"false"}) 


def move(request):
    request.session.clear()
    return HttpResponseRedirect(f'/')
def status(request):
    board = request.session.get('board', [[0]*3 for _ in range(3)])  # default if not found
    board = np.array(board)
    # print(board)
    return JsonResponse({'result':board.tolist()}) 


