from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, "poker/login.html")

def test(request):
    return render(request, "poker/poker_cards.html")