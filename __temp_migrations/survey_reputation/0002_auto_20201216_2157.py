# Generated by Django 2.2.12 on 2020-12-16 18:57

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey_reputation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='tercih2',
        ),
        migrations.AddField(
            model_name='player',
            name='tercih_2',
            field=otree.db.models.StringField(max_length=10000, null=True, verbose_name='Easily choose multiple answers!'),
        ),
    ]
