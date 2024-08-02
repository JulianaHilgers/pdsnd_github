
import time
import calendar
import pandas as pd
import numpy as np

## Filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'


def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n')
    

def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        
    '''
    time_period = input('\nWould you like to filter the data by month, day, or not at'
                        ' all? Type "none" for no filter.\n')
    


def get_month():
    '''Asks the user for a month and returns the specified month.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    month = input('\nWhich month? January, February, March, April, May, or June?\n')
    


def get_day(month):
    '''Asks the user for a day and returns the specified day.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    day = input('\nWhich day? Please type your response as an integer.\n')
    


def popular_month(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular month for start time?
    '''
    


def popular_day(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    '''
    


def popular_hour(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular hour of day for start time?
    '''
    


def trip_duration(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the total trip duration and average trip duration?
    '''
    


def popular_stations(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular start station and most popular end station?
    '''
    


def popular_trip(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular trip?
    '''
    


def users(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of each user type?
    '''
    


def gender(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of gender?
    '''
    


def birth_years(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the earliest (i.e. oldest user), most recent (i.e. youngest user),
    and most popular birth years?
    '''
   


def display_data():
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    display = input('\nWould you like to view individual trip data?'
                    'Type \'yes\' or \'no\'.\n')
    


def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''
    # Filter by city (Chicago, New York, Washington)
    city = get_city()

    # Filter by time period (month, day, none)
    time_period = get_time_period()

    print('Calculating the first statistic...')

    # What is the most popular month for start time?
    if time_period == 'none':
        start_time = time.time()
        
        
        
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    if time_period == 'none' or time_period == 'month':
        start_time = time.time()
        
        
        
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")    

    start_time = time.time()

    # What is the most popular hour of day for start time?
    

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the total trip duration and average trip duration?
    

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular start station and most popular end station?
    

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular trip?
    

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of each user type?
    

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of gender?
    
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
    # most popular birth years?
    

    print("That took %s seconds." % (time.time() - start_time))

    # Display five lines of data at a time if user specifies that they would like to
    display_data()

    # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        statistics()


if __name__ == "__main__":
	statistics()