# Generated by Django 2.2.12 on 2020-12-19 18:21

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('part3', '0008_auto_20201218_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='payround2',
            field=otree.db.models.IntegerField(default=5, null=True),
        ),
    ]