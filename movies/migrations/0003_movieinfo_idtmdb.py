# Generated by Django 4.0.4 on 2022-06-05 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_movieinfo_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='movieinfo',
            name='idTMDB',
            field=models.IntegerField(default=0),
        ),
    ]