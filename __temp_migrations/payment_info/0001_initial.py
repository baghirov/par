# Generated by Django 2.2.12 on 2023-05-01 19:32

from django.db import migrations, models
import django.db.models.deletion
import otree.db.idmap
import otree.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_info_group', to='otree.Session')),
            ],
            options={
                'db_table': 'payment_info_group',
            },
            bases=(models.Model, otree.db.idmap.GroupIDMapMixin),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payment_info_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'payment_info_subsession',
            },
            bases=(models.Model, otree.db.idmap.SubsessionIDMapMixin),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_role', otree.db.models.StringField(max_length=10000, null=True)),
                ('kazanc', otree.db.models.FloatField(null=True)),
                ('iban', otree.db.models.StringField(blank=True, max_length=10000, null=True, verbose_name='IBAN')),
                ('name', otree.db.models.StringField(blank=True, max_length=10000, null=True, verbose_name='İsim')),
                ('surname', otree.db.models.StringField(blank=True, max_length=10000, null=True, verbose_name='Soyisim')),
                ('payment_method', otree.db.models.BooleanField(choices=[[True, 'Deney kazancımın aşağıda bildireceğim hesaba gönderilmesini onaylıyorum.'], [False, 'Deney kazancımı BELİS laboratuvarından almak istiyorum']], null=True, verbose_name='Tercih ettiğiniz ödeme yöntemini seçiniz.')),
                ('own_iban', otree.db.models.BooleanField(blank=True, choices=[[True, 'Deney kazancımın aşağıda bildireceğim kişisel hesabıma gönderilmesini onaylıyorum.'], [False, 'Deney kazancımın aşağıda bildireceğim 3. kişi hesabına gönderilmesini onaylıyorum.']], null=True, verbose_name='Ödeme kişisel hesabınıza mı yapılacak?')),
                ('other_relation', otree.db.models.StringField(blank=True, max_length=10000, null=True, verbose_name='Yakınlık derecesi')),
                ('other_iban', otree.db.models.StringField(blank=True, max_length=10000, null=True, verbose_name='IBAN')),
                ('other_name', otree.db.models.StringField(blank=True, max_length=10000, null=True, verbose_name='İsim')),
                ('other_surname', otree.db.models.StringField(blank=True, max_length=10000, null=True, verbose_name='Soyisim')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='payment_info.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_info_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_info_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment_info.Subsession')),
            ],
            options={
                'db_table': 'payment_info_player',
            },
            bases=(models.Model, otree.db.idmap.PlayerIDMapMixin),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment_info.Subsession'),
        ),
    ]
