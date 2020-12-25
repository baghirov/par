from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants
from datetime import date


class PaymentInfoWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.setkazanc()    
        

class PaymentInfo(Page):
    
    
    form_model = 'player'
    form_fields = ["iban",
                   "name",
                   "surname",
                   'payment_method',
                   "own_iban",
                   "other_iban",
                   "other_name",
                   "other_surname",
                   'other_relation']
    def vars_for_template(self):
        participant = self.participant
        return {
            'redemption_code': participant.label or participant.code,
            'id': participant.id_in_session,
            'date': str(date.today()),
            'final_payoff_with_showup': self.participant.payoff_plus_participation_fee()
        }
    def error_message(self, values):
        if values['payment_method'] and values['own_iban'] and values['name'] == None:
            return 'Lütfen isim bilgisi giriniz.'
        if values['payment_method'] and values['own_iban'] and values['iban'] == None:
            return 'Lütfen IBAN bilgisi giriniz.'
        if values['payment_method'] and values['own_iban'] and values['surname'] == None:
            return 'Lütfen soyisim bilgisi giriniz.'
        if values['payment_method'] and values['own_iban'] == False and values['other_relation'] == None:
            return 'Lütfen yakınlık bilgisi giriniz.'
        if values['payment_method'] and values['own_iban'] == False and values['other_name'] == None:
            return 'Lütfen isim bilgisi giriniz.'
        if values['payment_method'] and values['own_iban'] == False and values['other_surname'] == None:
            return 'Lütfen soyisim bilgisi giriniz.'
        if values['payment_method'] and values['own_iban'] == False and values['other_iban'] == None:
            return 'Lütfen IBAN bilgisi giriniz.'        
  
        
        


page_sequence = [PaymentInfoWaitPage,
                 PaymentInfo]
