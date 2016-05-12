"""Configuration file."""

"""Account Credentials"""
sabersim_creds = {
    "username": "kevin.a.meurer@gmail.com",
    "password": "cowbell1"
}

google_creds = {
    "email": "kevin.a.meurer",
    "password": "cowbell453"
}

"""Local Paths"""
chromedriver_path = './chromedriver'

# 'fanduel' or 'draftkings'
site = 'fanduel'
include_numberfire = False

"""Web Paths"""
rotogrinder_hitter_path =\
    'http://rotogrinders.com/projected-stats/mlb-hitter.csv?site=%s' % site
rotogrinder_pitcher_path =\
    'http://rotogrinders.com/projected-stats/mlb-pitcher.csv?site=%s' % site
rotogrinder_nba_path =\
    'http://rotogrinders.com/projected-stats/nba-player.csv?site=%s' % site

"""General Info"""
nba_max_salary = 60000
if site == 'fanduel':
    mlb_max_salary = 35000
elif site == 'draftkings':
    mlb_max_salary = 50000

# determines how much negative weight to assign to
# teams that play themselves
"""General Genetic Settings"""
"""
genetic_generations = 1000
retain = .6
random_select = .07
mutate_chance = 0.04
population_size = 150
"""

# how to sort the results: can be 'cost', 'points', 'cost-points', 'cost-fitness', 'fitness'
sort_by = 'cost-fitness'

"""
Original settings:
"""
genetic_generations = 75
retain = 0.35
random_select = 0.05
mutate_chance = 0.015
population_size = 10000


"""MLB-specific Genetic Settings"""
limit_conflicting_teams = True
self_defeating_weight = 3.0
same_team_bonus = True
same_team_weight = 3.0
stack_bonus = 25.0
min_different_teams = 3
excluded_pitchers = []
excluded_batters = ['Chris Young']
excluded_teams = ['BAL', 'MIN', 'SDP', 'CHC', 'CWS', 'TEX',
                  'CLE', 'HOU', 'ARI', 'COL', 'TB', 'SEA',
                  'TOR', 'SF']

"""NBA-specific Genetic Settings"""
excluded_nba_players = []
excluded_nba_teams = []
