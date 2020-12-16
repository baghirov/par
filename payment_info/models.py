from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


doc = """
This application provides a webpage instructing participants how to get paid.
Examples are given for the lab and Amazon Mechanical Turk (AMT).
"""


class Constants(BaseConstants):
    name_in_url = 'payment_info'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    def setkazanc(self):
        players = self.get_players()
        for p in players:
            kazanc = p.participant.payoff_plus_participation_fee()
            p.kazanc = float(kazanc)
            print ("participant payoff", p.participant.payoff_plus_participation_fee())
            print ("kazanc", kazanc)

class Player(BasePlayer):
    kazanc = models.FloatField()
    iban = models.StringField(
        label='IBAN',
        blank=True)
    name = models.StringField(
        label='İsim',
        blank=True)
    surname = models.StringField(
        label='Soyisim',
        blank=True)
        
    payment_method = models.BooleanField(
        doc="""the payment method that the subject prefers""",
        label='Tercih ettiğiniz ödeme yöntemini seçiniz.',
        widget=widgets.RadioSelect,
        choices=[
            [True, 'Deney kazancımın aşağıda bildireceğim hesaba gönderilmesini onaylıyorum.'],
            [False, 'Deney kazancımı BELİS laboratuvarından almak istiyorum'],
        ]
    )
    own_iban = models.BooleanField(
        doc="""the iban that the subject prefers""",
        label='Ödeme kişisel hesabınıza mı yapılacak?',
        widget=widgets.RadioSelect,
        blank=True,
        choices=[
            [True, 'Deney kazancımın aşağıda bildireceğim kişisel hesabıma gönderilmesini onaylıyorum.'],
            [False, 'Deney kazancımın aşağıda bildireceğim 3. kişi hesabına gönderilmesini onaylıyorum.'],
        ]
    )

    other_relation = models.StringField(
        label='Yakınlık derecesi',
        blank=True)
    other_iban = models.StringField(
        label='IBAN',
        blank=True)
    other_name = models.StringField(
        label='İsim',
        blank=True)
    other_surname = models.StringField(
        label='Soyisim',
        blank=True)

    
   

    



