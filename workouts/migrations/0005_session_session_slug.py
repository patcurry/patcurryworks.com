# Generated by Django 2.0.4 on 2018-04-12 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0004_auto_20180412_0910'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='session_slug',
            field=models.SlugField(blank=True, max_length=100, null=True),
        ),
    ]
