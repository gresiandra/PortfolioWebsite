from django.db import models

# Create your models here.

class aboutme(models.Model):
    Name = models.CharField(max_length=50)
    Title = models.CharField(max_length=50)
    DateofBirth = models.DateField()
    Address = models.CharField(max_length=50)
    Email = models.EmailField(max_length=254)
    Phone = models.CharField(max_length=50)

    def __str__(self):
        return "{}. {}".format(self.id, self.Name)

class experience(models.Model):
    Years = models.CharField(max_length=50)
    Position = models.CharField(max_length=100)
    Office = models.CharField(max_length=40)
    Description = models.TextField()

    def __str__(self):
        return "{}. {}".format(self.id, self.Years)

class skill(models.Model):
    skills = models.CharField(max_length=100)

    icon_type = {
        ('flaticon-ideas','flaticon-ideas'),
        ('flaticon-flasks','flaticon-flasks'),
        ('flaticon-analysis','flaticon-analysis'),
        ('flaticon-ux-design','flaticon-ux-design'),
        ('flaticon-web-design','flaticon-web-design'),
        ('flaticon-idea','flaticon-idea'),
        ('flaticon-innovation','flaticon-innovation'),
    }

    icon = models.CharField(max_length=100, choices=icon_type, default='flaticon-ideas')

    def __str__(self):
        return "{}. {}".format(self.id, self.skills)