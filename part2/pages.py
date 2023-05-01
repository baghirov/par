from ._builtin import Page, WaitPage
from .models import Constants 

class A1_role(Page):
    timeout_seconds = 10
    def is_displayed(self):
        return self.round_number == 1
 

class Hire_1(Page):
    def is_displayed(self):
        return self.player.role() == 'principal'
    form_model = 'group'
    form_fields = ['agent_hired_1','belief_1']

class Hire_1WaitPage(WaitPage):
    def vars_for_template(self):
        if self.player.role() =='agent':
            body_text = "Çalışan Rolündesiniz. İşveren bekleniyor."
        else:
            body_text = "İşveren bekleniyor."
        return {'body_text': body_text}


class Action_1(Page):
    def is_displayed(self):
        return self.group.agent_hired_1 and self.player.role() == 'agent' 
    form_model = 'group'
    form_fields = ['agent_action_1']

class Results_1WaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_return_1()
        self.group.set_action_1()

class Results_1(Page):
    timeout_seconds = 20

class Hire_2(Page):
    def is_displayed(self):
        return self.group.agent_hired_1 and self.player.role() == 'principal'
    form_model = 'group'
    form_fields = ['agent_hired_2','belief_2']

class Hire_2WaitPage(WaitPage):
    def vars_for_template(self):
        if self.player.role() =='agent':
            body_text = "Çalışan Rolündesiniz. İşveren bekleniyor."
        else:
            body_text = "İşveren bekleniyor."
        return {'body_text': body_text}

class Action_2(Page):
    def is_displayed(self):
        return self.group.agent_hired_1 and self.group.agent_hired_2 and self.player.role() == 'agent' 
    form_model = 'group'
    form_fields = ['agent_action_2']
    def error_message(self, values):
        if values['agent_action_2'] == None:
            return 'Tercih yapın.'

class Results_2WaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_return_2()
        self.group.set_action_2()

class Results_2(Page):
    def is_displayed(self):
        return self.group.agent_hired_1 
    timeout_seconds = 20

class Hire_3(Page):
    def is_displayed(self):
        return self.group.agent_hired_1 and self.group.agent_hired_2 and self.player.role() == 'principal'
    form_model = 'group'
    form_fields = ['agent_hired_3','belief_3']


class Hire_3WaitPage(WaitPage):
    def vars_for_template(self):
        if self.player.role() =='agent':
            body_text = "Çalışan Rolündesiniz. İşveren bekleniyor."
        else:
            body_text = "İşveren bekleniyor."
        return {'body_text': body_text}


class Action_3(Page):
    def is_displayed(self):
        return self.group.agent_hired_1 and self.group.agent_hired_2 and self.group.agent_hired_3 and self.player.role() == 'agent' 
    form_model = 'group'
    form_fields = ['agent_action_3']

    def error_message(self, values):
        if values['agent_action_3'] == None:
            return 'Tercih yapın.'

class Results_3WaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_return_3()
        self.group.set_action_3()

class Results_3(Page):
    def is_displayed(self):
        return self.group.agent_hired_1 and self.group.agent_hired_2 
    timeout_seconds = 20

class Results_TotalWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_round_payoffs()

class Results_Total(Page):
    timeout_seconds = 60

class End_of_round(WaitPage):
    title_text = "BÖLÜM BİTTİ"
    body_text = "Rastgele bir katılımcı ile yeniden eşleştirileceksiniz. Lütfen Bekleyin."

class ShuffleWaitPage(WaitPage):
    wait_for_all_groups = True
    def after_all_players_arrive(self):
        if self.round_number < Constants.num_rounds:
            "creating.session"

class Results_FinalWaitPage(WaitPage):
    def after_all_players_arrive(self):
        if self.round_number == Constants.num_rounds:
            for p in self.group.get_players():
                payoff_list = p.participant.vars.get('payoffs', [])
                # now saving to otree's payoff variable for currency calculations
                for r in Constants.rounds_to_pay:
                    p.payoff += payoff_list[r]
                print( 'player payoff:',  p.payoff )            
            # p.dollars = p.participant.payoff_plus_participation_fee().to_real_world_currency(self.session)

class Results_Final(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    timeout_seconds = 60
    def vars_for_template(self):
        payoff_list = self.player.participant.vars.get('payoffs', [])
        rounds_list = []
        display_list = []
        temp_list = []      
        for r in range(len(Constants.rounds_to_pay)):
            rounds_list.append(Constants.rounds_to_pay[r]+1)  
            # we need to add 1 so that rounds line up with a 1 instead of 0 index 
            temp_list.append(int(payoff_list[Constants.rounds_to_pay[r]]))
        display_list = [[rounds_list, temp_list]]
        print ("rounds_list:", rounds_list)    
        print ('temp_list:', temp_list)
        print ("display_list:", display_list)  
        return dict(display_list=display_list)

page_sequence = [A1_role,
                 Hire_1,
                 Hire_1WaitPage,
                 Action_1,
                 Results_1WaitPage,
                 Results_1,
                 Hire_2,
                 Hire_2WaitPage,
                 Action_2,
                 Results_2WaitPage,
                 Results_2,
                 Hire_3,
                 Hire_3WaitPage,
                 Action_3,
                 Results_3WaitPage,
                 Results_3,
                 Results_TotalWaitPage,
                 Results_Total,
                 End_of_round,
                 ShuffleWaitPage,
                 Results_FinalWaitPage,
                 Results_Final]
