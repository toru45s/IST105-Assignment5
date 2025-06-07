from django.shortcuts import render
from .forms import PuzzleForm
import math
import random

def puzzle_view(request):
    result = None
    if request.method == 'POST':
        form = PuzzleForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            text = form.cleaned_data['text']

            # Number Puzzle
            if number % 2 == 0:  # even
                number_result = {
                    'type': 'even',
                    'value': math.sqrt(number)
                }
            else:  # odd
                number_result = {
                    'type': 'odd',
                    'value': number ** 3
                }

            # Text Puzzle
            binary_text = ' '.join(format(ord(c), '08b') for c in text)
            vowels = 'aeiouAEIOU'
            vowel_count = sum(c in vowels for c in text)

            # Treasure Hunt simulation
            target = random.randint(1, 100)
            guesses = []
            won = False
            max_tries = 5

            for i in range(max_tries):
                guess = random.randint(1, 100)
                guesses.append(guess)
                if guess == target:
                    won = True
                    break

            treasure_result = {
                'target': target,
                'guesses': guesses,
                'won': won,
                'tries': len(guesses)
            }

            result = {
                'number_result': number_result,
                'binary_text': binary_text,
                'vowel_count': vowel_count,
                'treasure_result': treasure_result,
            }
    else:
        form = PuzzleForm()

    return render(request, 'puzzle/puzzle.html', {'form': form, 'result': result})
