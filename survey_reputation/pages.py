from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants

class Intro(Page):
    pass

class Risk(Page):
    form_model = 'player'
    form_fields = ['risk',
                   'loss1',
                   'loss2']

class Demographics(Page):
    form_model = 'player'
    form_fields = ['age',
                   'gender',
                   'year',
                   'dept',
                   'scholarship',
                   'father',
                   'mother',
                   'experiment',
                   'tercih']

page_sequence = [
    Intro,
    Risk,
    Demographics,
]
