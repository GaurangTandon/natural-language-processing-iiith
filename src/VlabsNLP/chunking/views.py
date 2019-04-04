from django.http import HttpRequest
from django.shortcuts import render

from .models import Sentence, Chunk


def introduction(request):
    return render(request, 'introduction.html')

def experiment(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'experiment.html', {
            'sentences': Sentence.objects.all(),
            'chunks': Chunk.objects.all(),
        })

def theory(request):
    return render(request, 'theory.html')

def objective(request):
    return render(request, 'objective.html')

def quizzes(request):
    return render(request, 'quizzes.html')

def procedure(request):
    return render(request, 'procedure.html')

def readings(request):
    return render(request, 'readings.html')
