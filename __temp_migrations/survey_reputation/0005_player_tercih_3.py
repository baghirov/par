# Generated by Django 2.2.12 on 2020-12-16 19:47

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey_reputation', '0004_auto_20201216_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='tercih_3',
            field=otree.db.models.StringField(max_length=10000, null=True, verbose_name=' Birden fazla seçenek işaretleyebilirsiniz. '),
        ),
    ]
