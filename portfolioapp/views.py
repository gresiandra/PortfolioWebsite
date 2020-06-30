from django.shortcuts import render
from .models import aboutme, experience, skill, twitterInstagram
import urllib.request as ur
import json

def index(request):


    about = aboutme.objects.all()
    myexperience = experience.objects.all()
    myskill = skill.objects.all()
    tg = twitterInstagram.objects.all()

    context = {
        'aboutme':about,
        'experience':myexperience,
        'skill':myskill,
        'twitterInstagram':tg,
    }
    return render(request, 'portfolioapp/index.html', context)