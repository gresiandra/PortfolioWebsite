# Generated by Django 2.2.13 on 2020-06-30 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0007_auto_20200630_0717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='Instagram',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='Twitter',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='skill',
            name='icon',
            field=models.CharField(choices=[('flaticon-flasks', 'flaticon-flasks'), ('flaticon-innovation', 'flaticon-innovation'), ('flaticon-analysis', 'flaticon-analysis'), ('flaticon-ideas', 'flaticon-ideas'), ('flaticon-ux-design', 'flaticon-ux-design'), ('flaticon-idea', 'flaticon-idea'), ('flaticon-web-design', 'flaticon-web-design')], default='flaticon-ideas', max_length=100),
        ),
    ]
