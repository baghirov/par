# Generated by Django 2.2.12 on 2020-12-25 15:44

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('part1', '0016_auto_20201225_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='payround2',
            field=otree.db.models.IntegerField(default=3, null=True),
        ),
    ]