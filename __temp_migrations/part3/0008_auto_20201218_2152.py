# Generated by Django 2.2.12 on 2020-12-18 18:52

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('part3', '0007_auto_20201218_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='payround1',
            field=otree.db.models.IntegerField(default=1, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='payround2',
            field=otree.db.models.IntegerField(default=10, null=True),
        ),
    ]
