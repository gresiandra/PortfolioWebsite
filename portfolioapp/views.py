from django.shortcuts import render
from .models import aboutme, experience, skill

def index(request):


    about = aboutme.objects.all()
    myexperience = experience.objects.all()
    myskill = skill.objects.all()

    context = {
        'aboutme':about,
        'experience':myexperience,
        'skill':myskill,
    }
    return render(request, 'portfolioapp/index.html', context)