# Generated by Django 2.2.12 on 2020-12-25 15:51

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('part4', '0010_auto_20201225_1849'),
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
            field=otree.db.models.IntegerField(default=5, null=True),
        ),
    ]