# Generated by Django 2.2.12 on 2020-12-17 19:07

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('part3', '0002_auto_20201217_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='payround2',
            field=otree.db.models.IntegerField(default=2, null=True),
        ),
    ]
