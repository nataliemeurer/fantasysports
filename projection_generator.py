"""Runs game simulations and write the results to files."""
from __future__ import division
from baseball_simulator.simulation_runner import run_simulated_games
import sys
import util.prep_projections as pp
import util.data_loader as dl
import datetime as dt
import conf
import csv

# LOAD NUMBER OF SIMULATIONS
print sys.argv
conf.simulated_game_count = int(sys.argv[1])
conf.proj_date = str(sys.argv[2])
conf.proj_iteration = str(sys.argv[3])

start_time = dt.datetime.now()

schedule = dl.load_mlb_schedule()
fmt_date = conf.proj_date.replace('_', '')
current_time = dt.datetime.now().strftime('%H:%M')
games = schedule.loc[fmt_date]

fd_proj_file = open(
    '%sfanduel_%s_%s.csv' % (
        conf.projection_output_dir, conf.proj_date,
        conf.proj_iteration), 'w')
writer_fd = csv.DictWriter(fd_proj_file,
                           fieldnames=['name'] +
                           range(conf.simulated_game_count))
writer_fd.writeheader()
dk_proj_file = open(
    '%sdraftkings_%s_%s.csv' % (
        conf.projection_output_dir, conf.proj_date,
        conf.proj_iteration), 'w')
writer_dk = csv.DictWriter(dk_proj_file,
                           fieldnames=['name'] +
                           range(conf.simulated_game_count))
writer_dk.writeheader()
home_teams = games.at[fmt_date, 'home_team']
away_teams = games.at[fmt_date, 'away_team']
for idx, t in enumerate(home_teams):
    h_team = t
    a_team = away_teams[idx]
    if conf.proj_use_inclusion is True and (
            h_team not in conf.proj_included_teams or
            a_team not in conf.proj_included_teams):
        print "Matchup of %s vs. %s not included.  Skipping projections." % (
            a_team, h_team)
        continue
    results = run_simulated_games(a_team, h_team, conf.simulated_game_count)
    for name in results['batters_fd']:
        fd = dict(enumerate(results['batters_fd'][name]))
        fd['name'] = name
        dk = dict(enumerate(results['batters_dk'][name]))
        dk['name'] = name
        writer_fd.writerow(fd)
        writer_dk.writerow(dk)
    for name in results['pitchers_fd']:
        fd = dict(enumerate(results['pitchers_fd'][name]))
        fd['name'] = name
        dk = dict(enumerate(results['pitchers_dk'][name]))
        dk['name'] = name
        writer_fd.writerow(fd)
        writer_dk.writerow(dk)

print "\n\nCreating Simplified Projections"
pp.create_simplified_projections()

print "Projections generated for %d games.  Total time: %d seconds." % (
    conf.simulated_game_count, (dt.datetime.now() - start_time).seconds)
