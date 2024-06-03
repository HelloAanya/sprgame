from django.shortcuts import render
import random

def index(request):
    return render(request, 'index.html')

def play_game(request):
    player_choice = request.POST.get('choice')
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    result = ''

    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        result = 'You win!'
    else:
        result = 'You lose!'

    context = {
        'player_choice': player_choice,
        'computer_choice': computer_choice,
        'result': result,
    }
    return render(request, 'result.html', context)
    
