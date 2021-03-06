# Generated by Django 2.2.13 on 2020-06-30 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0017_auto_20200630_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='icon',
            field=models.CharField(choices=[('flaticon-analysis', 'flaticon-analysis'), ('flaticon-idea', 'flaticon-idea'), ('flaticon-innovation', 'flaticon-innovation'), ('flaticon-ideas', 'flaticon-ideas'), ('flaticon-web-design', 'flaticon-web-design'), ('flaticon-flasks', 'flaticon-flasks'), ('flaticon-ux-design', 'flaticon-ux-design')], default='flaticon-ideas', max_length=100),
        ),
        migrations.AlterField(
            model_name='twitterinstagram',
            name='Instagram',
            field=models.CharField(default='', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='twitterinstagram',
            name='Twitter',
            field=models.CharField(default='', max_length=20, null=True),
        ),
    ]
