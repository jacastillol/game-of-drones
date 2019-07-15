from django.shortcuts import render


action_choices = {
    'R': 'rock',
    'S': 'scissors',
    'P': 'paper',
}
result_game = {
    'Draw': -1,
    'P1': 0,
    'P2': 1,
}

def make_match(player1_move, player2_move):
    if player1_move=="rock" and player2_move=="rock":
        result = result_game['Draw']
    elif player1_move=="rock" and player2_move=="paper":
        result = result_game['P2']
    elif player1_move=="rock" and player2_move=="scissors":
        result = result_game['P1']
    elif player1_move=="paper" and player2_move=="rock":
        result = result_game['P1']
    elif player1_move=="paper" and player2_move=="paper":
        result = result_game['Draw']
    elif player1_move=="paper" and player2_move=="scissors":
        result = result_game['P2']
    elif player1_move=="scissors" and player2_move=="rock":
        result = result_game['P2']
    elif player1_move=="scissors" and player2_move=="paper":
        result = result_game['P1']
    elif player1_move=="scissors" and player2_move=="scissors":
        result = result_game['Draw']
    else:
        result = -2
    return result

def index(request):
    request.session['num_run'] = 0
    request.session['player1'] = None
    request.session['player2'] = None
    request.session['action_prev'] = None
    request.session['action_curr'] = None
    request.session['games'] = None
    request.session['wins1'] = 0
    request.session['wins2'] = 0
    
    context = {}
    return render(request, 'pages/index.html', context)

def play(request):
    request.session['num_run'] += 1
    games_list = request.session['games']

    if 'player1' in request.GET:
        request.session['player1'] = request.GET['player1']

    if 'player2' in request.GET:
        request.session['player2'] = request.GET['player2']

    turn_name = request.session['player1'] \
        if request.session['num_run'] % 2 else request.session['player2']

    if 'state' in request.GET:
        if (request.session['num_run'] % 2) == 0:
            request.session['action_prev'] = request.GET['state']
            request.session['action_curr'] = None
        else:
            request.session['action_curr'] = request.GET['state']
        if (request.session['num_run'] % 2) == 1:
            result = make_match(action_choices[request.session['action_prev']],
                                action_choices[request.session['action_curr']])
            players = {
                0: request.session['player1'], 
                1: request.session['player2'],
                -1: 'Draw',
            }
            round_id = (request.session['num_run']-1) // 2
            winner = players[result]
            if not 'games' in request.session or not request.session['games']:
                request.session['games'] = [(round_id, winner)]
            else:
                games_list.append((round_id, winner))
                request.session['games'] = games_list
            if result == 0:
                request.session['wins1'] += 1
            if result == 1:
                request.session['wins2'] += 1
            if request.session['wins1'] == 3 or request.session['wins2'] == 3:
                context = {
                    'winner': winner,
                    'score1': request.session['wins1'],
                    'score2': request.session['wins2'],
                }
                return render(request, 'pages/winner.html', context)
        else:
            result = "WAIT"
            winner = "WAIT"
    else:
        result = "WAIT"
        winner = "WAIT"

    context = {
        'players': [request.session['player1'], request.session['player2']],
        'num_run': request.session['num_run'],
        'num_round': (request.session['num_run']-1) // 2 + 1,
        'turn_name': turn_name,
        'action_choices': action_choices,
        'action_prev': request.session['action_prev'],
        'action_curr': request.session['action_curr'],
        'result': result,
        'winner': winner,
        'games_list': games_list,
        'wins1': request.session['wins1'],
        'wins2': request.session['wins2'],
    }
    return render(request, 'pages/play.html', context)

def winner(request):
    return render(request, 'pages/winner.html')

def about(request):
    return render(request, 'pages/about.html')
