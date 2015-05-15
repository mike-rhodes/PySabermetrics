__author__ = 'mrhodes'

# The module where actual analysis will take place

# Load in module with data pull functions
import pullData


# Pull some sample data
# game_summary_data = pullData.get_games_summary_data(5, 10, 2015)

# Write the resulting JSON to a file so you dont have to keep sending requests to server
# with open('game_summary_data.json', 'a') as the_file:
#     json.dump(game_summary_data, the_file)

# Open above file
with open('game_summary_data.json') as example_json:
    test_data = json.load(example_json)

for g in test_data['data']['games']['game']:
    print g['game_data_directory']

print json.dumps(test_data['data']['games'], indent=4, sort_keys=True)