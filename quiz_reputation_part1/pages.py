from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants

class WELCOME(Page):
    def is_displayed(self):
        return self.round_number == 1
    
    
    

class Introduction1(Page):
    form_model = 'player'
    form_fields = ['onay_1',
                    'onay_2',
                    'onay_3',
                    'onay_4']

class Introduction2(Page):
    timeout_seconds = 600

class Question1(Page):
    form_model = 'player'
    form_fields = ['q1']
    timeout_seconds = 120
    def before_next_page(self):
        self.player.check_correct_q1()

class Question2(Page):
    form_model = 'player'
    form_fields = ['q2']
    timeout_seconds = 120
    def before_next_page(self):
        self.player.check_correct_q2()

class Question3(Page):
    form_model = 'player'
    form_fields = ['q3']
    timeout_seconds = 120
    def before_next_page(self):
        self.player.check_correct_q3()

class Question4(Page):
    form_model = 'player'
    form_fields = ['q4']
    timeout_seconds = 120
    def before_next_page(self):
        self.player.check_correct_q4()

class Question5(Page):
    form_model = 'player'
    form_fields = ['q5']
    timeout_seconds = 120
    def before_next_page(self):
        self.player.check_correct_q5()

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.q_correct()

class Results(Page):
    timeout_seconds = 300
    """def error_message(self, values):
        import time
        if time.time <= 120:
            return 'Süre bitene kadar soruları inceleyin' """
    

page_sequence = [
    WELCOME,
    Introduction1,
    Introduction2,
    Question1,
    Question2,
    Question3,
    Question4,
    Question5,
    ResultsWaitPage,
    Results
]
