from django.shortcuts import render
from .models import aboutme, experience, skill
import urllib.request as ur
import json

# Create your views here.

def index(request):

    # longitude = []
    # latitude = []

    # response = ur.urlopen("https://api.wheretheiss.at/v1/satellites/25544")
    # json_content = json.loads(response.read())
    # longitude.append(json_content['longitude'])
    # latitude.append(json_content['latitude'])


    about = aboutme.objects.all()
    myexperience = experience.objects.all()
    myskill = skill.objects.all()

    context = {
        'aboutme':about,
        'experience':myexperience,
        'skill':myskill,
        # 'lon':longitude,
        # 'lat':latitude
    }
    return render(request, 'portfolioapp/index.html', context)