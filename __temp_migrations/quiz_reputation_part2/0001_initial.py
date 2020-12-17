# Generated by Django 2.2.12 on 2020-12-17 13:03

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
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_reputation_part2_group', to='otree.Session')),
            ],
            options={
                'db_table': 'quiz_reputation_part2_group',
            },
            bases=(models.Model, otree.db.idmap.GroupIDMapMixin),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quiz_reputation_part2_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'quiz_reputation_part2_subsession',
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
                ('onay_1', otree.db.models.StringField(choices=[('Deney linkimi kimseyle paylaşmayacağımı onaylıyorum', 'Deney linkimi kimseyle paylaşmayacağımı onaylıyorum')], max_length=10000, null=True)),
                ('onay_2', otree.db.models.StringField(choices=[('Deney süresince Zoom oturumunu terketmeyeceğim ve cihazın sesini duyuruları işitecek şekilde açık tutacağım', 'Deney süresince Zoom oturumunu terketmeyeceğim ve cihazın sesini duyuruları işitecek şekilde açık tutacağım')], max_length=10000, null=True)),
                ('onay_3', otree.db.models.StringField(choices=[('Deney süresince diğer katılımcılarla iletişim kurmayacağımı onaylıyorum.', 'Deney süresince diğer katılımcılarla iletişim kurmayacağımı onaylıyorum.')], max_length=10000, null=True)),
                ('onay_4', otree.db.models.StringField(choices=[('Deney tamamlanmadan deneyi terketmeyeceğimi onaylıyorum.', 'Deney tamamlanmadan deneyi terketmeyeceğimi onaylıyorum.')], max_length=10000, null=True)),
                ('q1', otree.db.models.StringField(choices=[('Yeşil', 'Yeşil'), ('Mavi', 'Mavi')], max_length=10000, null=True, verbose_name='2. Tip  Çalışan, bilgisayar Yeşil seçtiğinde hangisini seçerse Tur kazancını maksimize eder?')),
                ('q1_is_correct', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True)),
                ('q1_dogru', otree.db.models.StringField(max_length=10000, null=True)),
                ('q2', otree.db.models.StringField(choices=[('Yeşil', 'Yeşil'), ('Mavi', 'Mavi')], max_length=10000, null=True, verbose_name='1. Tip çalışan, bilgisayar Yeşil seçtiğinde hangisini seçerse Tur kazancını maksimize eder?')),
                ('q2_is_correct', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True)),
                ('q2_dogru', otree.db.models.StringField(max_length=10000, null=True)),
                ('q3', otree.db.models.StringField(choices=[('Doğru', 'Doğru'), ('Yanlış', 'Yanlış')], max_length=10000, null=True, verbose_name='Geçmiş tur seçimlerinden bağımsız olarak bilgisayarın her iki rengi seçme ihtimali eşittir.')),
                ('q3_is_correct', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True)),
                ('q3_dogru', otree.db.models.StringField(max_length=10000, null=True)),
                ('q4', otree.db.models.StringField(choices=[('Doğru', 'Doğru'), ('Yanlış', 'Yanlış')], max_length=10000, null=True, verbose_name='İfadenin doğru mu yanlış mı olduğunu seçin: Deney süresince rolünüz (işveren veya çalışan) ve tipiniz (1. Tip veya 2. Tip çalışan) sabit kalacaktır.')),
                ('q4_is_correct', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True)),
                ('q4_dogru', otree.db.models.StringField(max_length=10000, null=True)),
                ('q5', otree.db.models.StringField(choices=[('Doğru', 'Doğru'), ('Yanlış', 'Yanlış')], max_length=10000, null=True, verbose_name='İfadenin doğru mu yanlış mı olduğunu seçin: İşverenin 1. Tip ve 2. Tip çalışan ile eşleşme ihtimali eşittir.')),
                ('q5_is_correct', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True)),
                ('q5_dogru', otree.db.models.StringField(max_length=10000, null=True)),
                ('questions_correct', otree.db.models.IntegerField(null=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz_reputation_part2.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_reputation_part2_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_reputation_part2_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz_reputation_part2.Subsession')),
            ],
            options={
                'db_table': 'quiz_reputation_part2_player',
            },
            bases=(models.Model, otree.db.idmap.PlayerIDMapMixin),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz_reputation_part2.Subsession'),
        ),
    ]
