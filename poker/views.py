from django.http import HttpResponse
from django.shortcuts import render
import django.conf

# Create your views here.
def login(request):
    return render(request, "poker/login.html")

def test(request):
    ctx = default_ctx()
    return render(request, "poker/poker_cards.html", ctx)

def default_ctx(*args):
    if len(args)>1:
        out = args[1]
    else:
        out = {}
    out["cards_nrows"] = django.conf.settings.CARDS_NROWS
    out["cards"] = []
    for i in django.conf.settings.CARDS:
        card = {}
        card["num"] = i
        out["cards"].append(card)
    return out
    