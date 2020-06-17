from django.contrib import admin

from .models import aboutme, experience, skill

# Register your models here.


admin.site.register(aboutme)
admin.site.register(experience)
admin.site.register(skill)