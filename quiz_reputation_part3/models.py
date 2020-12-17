from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import csv

author = 'Shahin Baghirov'

doc = """
A quiz app
"""


class Constants(BaseConstants):
    name_in_url = 'quiz_reputation_part3'
    players_per_group = None
    
    num_rounds = 1
    numquestions = 5
    
    instructions_template = 'part3/Instructions.html'
    bad_payment_1 = c(-20)
    good_payment_1 = c(10)
    multiplier = 3
    bad_payment_2 = multiplier * bad_payment_1
    good_payment_2 = multiplier * good_payment_1
    bad_payment_3 = multiplier * bad_payment_2
    good_payment_3 = multiplier * good_payment_2 
### points without currency unit to show in the table
    bad_1 = -20
    good_1 = 10
    bad_2 = multiplier * bad_1
    good_2 = multiplier * good_1
    bad_3 = multiplier * bad_2
    good_3 = multiplier * good_2
    
    outside_payment = c(0)
    
    probability_unbiased = 0.1
    probability_biased = 1 - probability_unbiased

   # in quiz, each question worths 2 Tl. exchange rate is 1/13 hence 26 points:
    point_per_question = c (26) 
    color_0 = 'Yeşil'
    color_1 = 'Mavi'
    question_1 = '2. Tip  Çalışan, bilgisayar {} seçtiğinde hangisini seçerse Tur kazancını maksimize eder?'.format(color_0)
    q1_choices = [ color_0, color_1]
    s1 = color_1

    question_2 =  "1. Tip çalışan, bilgisayar {} seçtiğinde hangisini seçerse Tur kazancını maksimize eder?".format(color_0)
    q2_choices = [ color_0, color_1]
    s2 = color_0

    question_3 =  "Geçmiş tur seçimlerinden bağımsız olarak bilgisayarın her iki rengi seçme ihtimali eşittir."
    q3_choices = [ 
        'Doğru',
        'Yanlış']
    s3 = 'Doğru'

    question_4 =  "İfadenin doğru mu yanlış mı olduğunu seçin: Deney süresince rolünüz (işveren veya çalışan) ve tipiniz (1. Tip veya 2. Tip çalışan) sabit kalacaktır."
    q4_choices = [ 
        'Doğru',
        'Yanlış']
    s4 = 'Doğru'

    question_5 =  "İfadenin doğru mu yanlış mı olduğunu seçin: İşverenin 1. Tip ve 2. Tip çalışan ile eşleşme ihtimali eşittir."
    q5_choices = [ 
        'Doğru',
        'Yanlış']
    s5 = 'Yanlış'




class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    onay_1 =  models.StringField(
        choices=['Deney linkimi kimseyle paylaşmayacağımı onaylıyorum'],
        widget=widgets.RadioSelect) 
    
    onay_2 =  models.StringField(
        choices=['Deney süresince Zoom oturumunu terketmeyeceğim ve cihazın sesini duyuruları işitecek şekilde açık tutacağım'],
        widget=widgets.RadioSelect) 

    onay_3 =  models.StringField(
        choices=['Deney süresince diğer katılımcılarla iletişim kurmayacağımı onaylıyorum.'],
        widget=widgets.RadioSelect) 
    
    onay_4 =  models.StringField(
        choices=['Deney tamamlanmadan deneyi terketmeyeceğimi onaylıyorum.'],
        widget=widgets.RadioSelect) 

    q1 = models.StringField(
        choices=Constants.q1_choices,
        label= Constants.question_1, 
        widget=widgets.RadioSelect)
    
    q1_is_correct = models.BooleanField()
    q1_dogru = models.StringField()
    def check_correct_q1(self):
        self.q1_is_correct = (self.q1 == Constants.s1)
        if self.q1_is_correct:
            self.q1_dogru = "Doğru"
        else:
            self.q1_dogru = "Yanlış"
    q2 = models.StringField(
        choices=Constants.q2_choices,
        label= Constants.question_2, 
        widget=widgets.RadioSelect)
    
    q2_is_correct = models.BooleanField()
    q2_dogru = models.StringField()
    def check_correct_q2(self):
        self.q2_is_correct = (self.q2 == Constants.s2)
        if self.q2_is_correct:
            self.q2_dogru = "Doğru"
        else:
            self.q2_dogru = "Yanlış"
    
    q3 = models.StringField(
        choices=Constants.q3_choices,
        label= Constants.question_3, 
        widget=widgets.RadioSelect)
    
    q3_is_correct = models.BooleanField()
    q3_dogru = models.StringField()
    def check_correct_q3(self):
        self.q3_is_correct = (self.q3 == Constants.s3)
        if self.q3_is_correct:
            self.q3_dogru = "Doğru"
        else:
            self.q3_dogru = "Yanlış"
    q4 = models.StringField(
        choices=Constants.q4_choices,
        label= Constants.question_4, 
        widget=widgets.RadioSelect)
    
    q4_is_correct = models.BooleanField()
    q4_dogru = models.StringField()
    def check_correct_q4(self):
        self.q4_is_correct = (self.q4 == Constants.s4)
        if self.q4_is_correct:
            self.q4_dogru = "Doğru"
        else:
            self.q4_dogru = "Yanlış"

    q5 = models.StringField(
        choices=Constants.q5_choices,
        label= Constants.question_5, 
        widget=widgets.RadioSelect)
    
    q5_is_correct = models.BooleanField()
    q5_dogru = models.StringField()
    def check_correct_q5(self):
        self.q5_is_correct = (self.q5 == Constants.s5)
        if self.q5_is_correct:
            self.q5_dogru = "Doğru"
        else:
            self.q5_dogru = "Yanlış"
    
    questions_correct = models.IntegerField()
    def q_correct(self):
        self.questions_correct = self.q1_is_correct + self.q2_is_correct + self.q3_is_correct + self.q4_is_correct + self.q5_is_correct
        self.payoff = Constants.point_per_question * self.questions_correct


