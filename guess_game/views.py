from django.http import HttpResponse
from django.shortcuts import render, redirect
from random import randint
from django.views.decorators.csrf import csrf_exempt

secret_num = randint(0, 100)
turn = 0
success = False


# Create your views here.


@csrf_exempt
def guess_game(request):
    global secret_num, turn, success
    context = {

    }
    hint = ''
    guessed_number = None

    if request.method == 'POST' and request.POST.get('guess_number'):
        guessed_number = int(request.POST['guess_number'])
        turn += 1
        if guessed_number == secret_num:
            success = True
        else:
            if guessed_number > secret_num:
                hint = 'lower'
            else:
                hint = 'higher'

    else:
        secret_num = randint(0, 100)
        turn = 0
        success = False
        hint = ''
        guessed_number = None

    context['success'] = success
    context['turn'] = turn
    context['hint'] = hint
    context['guessed_number'] = guessed_number

    return render(request, 'guess_game/game.html', context)
