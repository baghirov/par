# Generated by Django 2.2.12 on 2020-12-25 18:26

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('part4', '0032_auto_20201225_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='payround1',
            field=otree.db.models.IntegerField(default=6, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='payround2',
            field=otree.db.models.IntegerField(default=13, null=True),
        ),
    ]
