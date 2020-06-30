# Generated by Django 2.2.13 on 2020-06-30 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0016_auto_20200630_0829'),
    ]

    operations = [
        migrations.CreateModel(
            name='twitterInstagram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Twitter', models.CharField(default='', max_length=20)),
                ('Instagram', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='aboutme',
            name='Instagram',
        ),
        migrations.RemoveField(
            model_name='aboutme',
            name='Twitter',
        ),
        migrations.AlterField(
            model_name='skill',
            name='icon',
            field=models.CharField(choices=[('flaticon-flasks', 'flaticon-flasks'), ('flaticon-ideas', 'flaticon-ideas'), ('flaticon-web-design', 'flaticon-web-design'), ('flaticon-analysis', 'flaticon-analysis'), ('flaticon-idea', 'flaticon-idea'), ('flaticon-innovation', 'flaticon-innovation'), ('flaticon-ux-design', 'flaticon-ux-design')], default='flaticon-ideas', max_length=100),
        ),
    ]