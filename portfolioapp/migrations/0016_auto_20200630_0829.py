# Generated by Django 2.2.13 on 2020-06-30 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0015_auto_20200630_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='icon',
            field=models.CharField(choices=[('flaticon-web-design', 'flaticon-web-design'), ('flaticon-ideas', 'flaticon-ideas'), ('flaticon-flasks', 'flaticon-flasks'), ('flaticon-idea', 'flaticon-idea'), ('flaticon-ux-design', 'flaticon-ux-design'), ('flaticon-analysis', 'flaticon-analysis'), ('flaticon-innovation', 'flaticon-innovation')], default='flaticon-ideas', max_length=100),
        ),
    ]