__author__ = 'mrhodes'

# Import libraries
import requests
import json
import bs4 as bs

# Function to pull data
def get_games_summary_data(s_month, s_day, s_year, e_month = None, e_day = None, e_year = None):
    """
    Returns a JSON file containing the summary of the games played on a specified day. Currently working on
    allowing the user to specify a date range.

    :param s_month: Start month
    :param s_day: Start day
    :param s_year: Start year
    :param e_month: End month
    :param e_day: End day
    :param e_year: End year
    :return:
    """

    # Specify the URL to pull data from. Months and days must have leading zeroes if single digit
    mlbam_url = 'http://gd2.mlb.com/components/game/mlb/year_' + str(s_year) + \
                '/month_' + str("%02d" % s_month) +\
                '/day_' + str("%02d" % s_day) + '/miniscoreboard.json'

    # Get the request
    mlbam_response = requests.get(mlbam_url)

    return json.loads(mlbam_response.content)
