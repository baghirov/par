from os import environ


SESSION_CONFIGS = [
    dict(
        name='quiz_principal_agent_reputation_t1_all_in',
        display_name="Treatment 1 with quiz, risk,survey and payment info",
        num_demo_participants=2,
        app_sequence=['quiz_reputation_part1','part1','risk_part1','survey_reputation','payment_info'],
     ),
     dict(
        name='riskt1',
        display_name="risk Treatment 1",
        num_demo_participants=2,
        app_sequence=['risk_part1','payment_info'],
    ), 
    dict(
        name='quiz_principal_agent_reputation_t4_all_in',
        display_name="Treatment 4 with quiz, risk,survey and payment info",
        num_demo_participants=2,
        app_sequence=['quiz_reputation_part4','part4','risk_part4','survey_reputation','payment_info'],
    ),
    dict(
        name='survey_reputation',
        display_name="survey_reputation",
        num_demo_participants=2,
        app_sequence=['survey_reputation',"payment_info"],
    ),    

 ]   

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1/21, participation_fee=30.00, doc=""
)
OTREE_PRODUCTION = True

# exchange rates for treatments:
## PART1: 1/3
## PART2: 1/7
## PART3: 1/13
## PART4: 1/21

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'tr'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'TL'
USE_POINTS = True
POINTS_CUSTOM_NAME = 'PUAN'
ROOMS = [
    dict(
        name='belis',
        display_name='BELİS',
        participant_label_file='_rooms/belis.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ A repeated principal agent game with varying stakes.
"""

# don't share this with anybody.
SECRET_KEY = 'n0&zhjus4p%t)unjf#vn0@lt(9m91st2y7-j1u!-b)h^$l8nbn'

INSTALLED_APPS = ['otree']

# inactive session configs


#  dict(
#         name='principal_agent_reputation_t1',
#         display_name="Treatment 1 with payment",
#         num_demo_participants=2,
#         app_sequence=['part1','payment_info'],
 #    ),
#
# dict(
#        name='principal_agent_reputation_t3',
#        display_name="Treatment 3 with payment",
#        num_demo_participants=2,
#        app_sequence=['part3','payment_info'],
#    ),  
#    
#    dict(
#        name='treatment_3_quiz',
#        display_name="Treatment 3  quiz",
#        num_demo_participants=1,
#        app_sequence=['quiz_reputation_part3'],
#    ),
#    dict(
#        name='payment',
#        display_name="payment",
#        num_demo_participants=1,
#        app_sequence=['payment_info'],
#    ),
#  
#    dict(
#        name='survey_reputation',
#        display_name="survey_reputation",
#        num_demo_participants=1,
#        app_sequence=['survey_reputation'],
#    ),    
#  
 #   dict(
 #       name='quiz_principal_agent_reputation_t1_all_in',
 #       display_name="Treatment 1 with quiz, risk,survey and payment info",
 #       num_demo_participants=2,
 #       app_sequence=['quiz_reputation_part1','part1','survey_reputation','payment_info'],
 #    ),
 #   dict(
 #       name='treatment_1_quiz',
 #       display_name="Treatment 1  quiz",
 #       num_demo_participants=1,
 #       app_sequence=['quiz_reputation_part1'],
 #   ),
    

#     dict(
#        name='principal_agent_reputation_t2',
#        display_name="Treatment 2 with payment",
#        num_demo_participants=2,
#        app_sequence=['part2','payment_info'],
#    ),   
#    
#    dict(
#        name='treatment_2_quiz',
#        display_name="Treatment 2  quiz",
#        num_demo_participants=1,
#        app_sequence=['quiz_reputation_part2'],
#    ),

# dict(name='trust', display_name="Trust Game", num_demo_participants=2, app_sequence=['trust', 'payment_info']),
# dict(name='prisoner', display_name="Prisoner's Dilemma", num_demo_participants=2,
#      app_sequence=['prisoner', 'payment_info']),
# dict(name='volunteer_dilemma', display_name="Volunteer's Dilemma", num_demo_participants=3,
#      app_sequence=['volunteer_dilemma', 'payment_info']),
# dict(name='cournot', display_name="Cournot Competition", num_demo_participants=2, app_sequence=[
#     'cournot', 'payment_info'
# ]),
# dict(name='dictator', display_name="Dictator Game", num_demo_participants=2,
#      app_sequence=['dictator', 'payment_info']),
# dict(name='matching_pennies', display_name="Matching Pennies", num_demo_participants=2, app_sequence=[
#     'matching_pennies',
# ]),
# dict(name='traveler_dilemma', display_name="Traveler's Dilemma", num_demo_participants=2,
#      app_sequence=['traveler_dilemma', 'payment_info']),
# dict(name='bargaining', display_name="Bargaining Game", num_demo_participants=2,
#      app_sequence=['bargaining', 'payment_info']),
# dict(name='common_value_auction', display_name="Common Value Auction", num_demo_participants=3,
#      app_sequence=['common_value_auction', 'payment_info']),
# dict(name='bertrand', display_name="Bertrand Competition", num_demo_participants=2, app_sequence=[
#     'bertrand', 'payment_info'
# ]),
# dict(name='public_goods_simple', display_name="Public Goods (simple version from tutorial)",
#      num_demo_participants=3, app_sequence=['public_goods_simple', 'payment_info']),
# dict(name='trust_simple', display_name="Trust Game (simple version from tutorial)", num_demo_participants=2,
#      app_sequence=['trust_simple']),
