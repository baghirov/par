from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

doc = """ Principal agent game Treatment 3

"""


class Constants(BaseConstants):
    name_in_url = 'part1'
    players_per_group = 2
    num_rounds = 20
    instructions_template = 'part1/Instructions.html'

    endowment = c(0)
    bad_payment_1 = c(-20)
    good_payment_1 = c(10)
    
    # in treatment 1, stakes are same across periods
    bad_payment_2 = bad_payment_1
    good_payment_2 = good_payment_1
    bad_payment_3 = bad_payment_2
    good_payment_3 = good_payment_2 

    # for the instructions:
    bad_1 = -20
    good_1 = 10
    bad_2 = bad_1
    good_2 = good_1
    bad_3 =  bad_2
    good_3 = good_2
        
    # in quiz, each question worths 2TL:
    point_per_question = c (6) 
    outside_payment = c(0)
    belief_payment = c(1)
    probability_unbiased = 0.1
    probability_biased = 1 - probability_unbiased
    color_0 = 'Yeşil'
    color_1 = 'Mavi'
    
    agent_action_choices = [
            [0, color_0],
            [1, color_1],
        ]
    state_of_world_choices = [
            [0, color_0],
            [1, color_1],
        ]
    
    good_return_1 = [
            [good_payment_1, bad_payment_1],
            [bad_payment_1, good_payment_1],
        ]
    bad_return_1 = [
            [bad_payment_1, bad_payment_1] ,
            [good_payment_1, good_payment_1],
        ]
    good_return_2 = [
            [good_payment_2, bad_payment_2],
            [bad_payment_2, good_payment_2],
        ]
    bad_return_2 = [
            [bad_payment_2, bad_payment_2] ,
            [good_payment_2, good_payment_2],
        ]
    good_return_3 = [
            [good_payment_3, bad_payment_3],
            [bad_payment_3, good_payment_3],
        ]
    bad_return_3 = [
            [bad_payment_3, bad_payment_3] ,
            [good_payment_3, good_payment_3],
        ]
    num_rounds_to_pay = 2

    rounds_to_pay = random.sample(range(0, num_rounds), num_rounds_to_pay) 
    # selects 2 periods to pay out of total number of periods
    rounds_to_pay.sort()
    print ("rounds to pay:", rounds_to_pay)
    

class Subsession(BaseSubsession):

    def creating_session(self):
        self.group_randomly(fixed_id_in_group=True)
        print(self.get_group_matrix())
        #group_randomly() -> built-in function that  shuffles players. fixed id in groups
        # so that roles (principal or agent) remain fixed.
        rdm = random.uniform(0,1)
        # to be used to define unb and b types
        for g in self.get_groups():
            agent = g.get_player_by_role('agent')
            if self.round_number == 1:
                if g.id_in_subsession == 1:
                    agent.type = 0
                        # the agent is assigned to type "unbiased Agent"
                else:
                    agent.type = 1
                agent.participant.vars['Type'] = agent.type
            else:
                agent.type =  agent.participant.vars['Type']
            g.agent_type = agent.type

        for g in self.get_groups():
            g.state_of_world_1 = random.randint(0,1)
            g.state_1 = Constants.state_of_world_choices[g.state_of_world_1][1]
            g.state_of_world_2 = random.randint(0,1)
            g.state_2 = Constants.state_of_world_choices[g.state_of_world_2][1]
            g.state_of_world_3 = random.randint(0,1)
            g.state_3 = Constants.state_of_world_choices[g.state_of_world_3][1]
                            
def unbiased_return (action, state):
    if action == state:
        return Constants.good_payment_1
    else:
        return Constants.bad_payment_1

def biased_return (action):
    if action == 1:
        return Constants.good_payment_1
    else:
        return Constants.bad_payment_1 
    

class Group(BaseGroup):
    agent_type = models.IntegerField(
        doc="""0 if agent is unbiased (Tip 1), 1 if baised (Tip2). Type define for group for ease of coding"""
    )
    ### PERIOD 1 ###
    belief_1 = models.IntegerField(
        doc="""Principal's belief on agent being unbiased in period 1""",
        min=0, max=100,  
    )

    agent_hired_1 = models.BooleanField(
        doc="""Whether principal hires the agent""",
        widget=widgets.RadioSelect,
        choices=[
            [True, 'İşi ver'],
            [False, 'İşi verme'],
        ]
    )
    state_of_world_1 = models.IntegerField(
        doc="""state of world period 1"""
    )
    agent_action_1 = models.IntegerField(
        choices=Constants.agent_action_choices,
        doc="""Agent's action choice""",
        widget=widgets.RadioSelectHorizontal
    )
    #### choices=[0, 5, 10, 15, 20,25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],
           
    
    ### PERIOD 2 ###
    belief_2 = models.IntegerField(
        min=0, max=100,   
    )
    agent_hired_2 = models.BooleanField(
        widget=widgets.RadioSelect,
        choices=[
            [True, 'İşi ver'],
            [False, 'İşi verme'],
        ]
    )
    state_of_world_2 = models.IntegerField()
    agent_action_2 = models.IntegerField(
        choices=Constants.agent_action_choices,
        widget=widgets.RadioSelectHorizontal
    )
    
    ### PERIOD 3 ###
    belief_3 = models.IntegerField(
        min=0, max=100,  
    )
    agent_hired_3 = models.BooleanField(
        widget=widgets.RadioSelect,
        choices=[
            [True, 'İşi ver'],
            [False, 'İşi verme'],
        ]
    )
    state_of_world_3 = models.IntegerField()
    agent_action_3 = models.IntegerField(
        choices=Constants.agent_action_choices,
        widget=widgets.RadioSelectHorizontal
    )
    

    ### VISUAL STUFF ###
    state_1 = models.StringField()
    state_2 = models.StringField()
    state_3 = models.StringField()

    action_1 = models.StringField()
    def set_action_1(self):
        if self.agent_hired_1:
            self.action_1 = Constants.agent_action_choices [self.agent_action_1][1]
        else:
            self.action_1 = "İşe alınmadı"
    action_2 = models.StringField()
    def set_action_2(self):
        if self.agent_hired_2:
            self.action_2 = Constants.agent_action_choices [self.agent_action_2][1]
        else:
            self.action_2 = "İşe alınmadı"
    action_3 = models.StringField()
    def set_action_3(self):
        if self.agent_hired_3:
            self.action_3 = Constants.agent_action_choices [self.agent_action_3][1]
        else:
            self.action_3 = "İşe alınmadı"
    
    ### PERIOD PAYOFFS ###
    def set_return_1(self):
        principal = self.get_player_by_role('principal')
        agent = self.get_player_by_role('agent')
        
        if self.agent_hired_1:
            principal.pyf_1 = unbiased_return(self.agent_action_1, self.state_of_world_1)
            if self.agent_type == 0:
                agent.pyf_1 = unbiased_return(self.agent_action_1, self.state_of_world_1)
            else: 
                agent.pyf_1 = biased_return(self.agent_action_1)
        else:
            principal.pyf_1 = c(0)
            agent.pyf_1 = c(0)
        
   
    def set_return_2(self):
        principal = self.get_player_by_role('principal')
        agent = self.get_player_by_role('agent')
       
        if self.agent_hired_2:
            principal.pyf_2 = unbiased_return(self.agent_action_2, self.state_of_world_2)
            if self.agent_type == 0:
                agent.pyf_2 = unbiased_return(self.agent_action_2, self.state_of_world_2)
            else: 
                agent.pyf_2 = biased_return(self.agent_action_2)   
        else:
            principal.pyf_2 = c(0)
            agent.pyf_2 = c(0)
       

    def set_return_3(self):
        principal = self.get_player_by_role('principal')
        agent = self.get_player_by_role('agent')
        
        if self.agent_hired_3:
            principal.pyf_3 = unbiased_return(self.agent_action_3, self.state_of_world_3)
            
            if self.agent_type == 0:
                agent.pyf_3 = unbiased_return(self.agent_action_3, self.state_of_world_3)
            else: 
                agent.pyf_3 = biased_return(self.agent_action_3)   

        else:
            principal.pyf_3 = c(0)
            agent.pyf_3 = c(0)
        
    ### SUPERGAME PAYOFFS ###   
    def set_round_payoffs(self):
        players = self.get_players()
        for p in players:
            
            p.pyf = p.pyf_1 + p.pyf_2 + p.pyf_3 
            print ("player  payoff", p.pyf)
            
            payoff_list = p.participant.vars.get('payoffs', [])
            payoff_list.append(p.pyf)
            p.participant.vars['payoffs'] = payoff_list
            print ("player participation variables", p.participant.vars)
            print ("payoff list", payoff_list)
            

class Player(BasePlayer):

    def role(self):
        if self.id_in_group == 1:
            return 'principal'
        if self.id_in_group == 2:
            return 'agent'
    type = models.IntegerField(
        doc="""0 if agent is unbiased (Tip 1), 1 if baised (Tip2). Type define for group for ease of coding"""
    )
    dollars = models.CurrencyField()    
    
    pyf_1 = models.CurrencyField(
        doc=""" return from agent's action period 1"""
    )
    pyf_2 = models.CurrencyField()
    pyf_3 = models.CurrencyField()
    pyf = models.CurrencyField( 
        doc=""" RAW PAYOFF: principal's payoff without endowment and belief
        agent's payoff without endowment""")

    payrounds = Constants.rounds_to_pay
    