import time
import pandas as pd
import numpy as np

#Hello and welcome! Feel free to copy this file and utilize it to analyze data.

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_user_input():
    """
    Asks the user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of the week to filter by, or "all" to apply no day filter
    """
    print("Hello! Let's explore some US bikeshare data!")

    # Function to validate user input
    def validate_input(prompt, valid_options):
        while True:
            user_input = input(prompt).strip().lower()
            if user_input in valid_options:
                return user_input
            print(f"Invalid input. Please choose from: {', '.join(valid_options)}.")

    # Get user input for city
    cities = ['chicago', 'new york city', 'washington']
    city = validate_input("Please select a city (chicago, new york city, washington): ", cities)

    # Get user input for month
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    month = validate_input("Please select a month (january to june) or 'all' for no filter: ", months)

    # Get user input for day of the week
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    day = validate_input("Please select a day of the week or 'all' for no filter: ", days)

 # Get user input for day of the week
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    day = validate_input("Please select a day of the week or 'all' for no filter: ", days)

    # Ask for additional filters
    user_types = ['subscriber', 'customer', 'all']
    user_type = validate_input("Filter by user type (subscriber, customer, or 'all'): ", user_types)

    station = input("Would you like to filter by a specific station? Enter the station name or 'all' for no preference: ").strip()

    print(f"\nYour selections:\nCity = {city.title()}, Month = {month.title()}, Day = {day.title()}, User Type = {user_type.title()}, Station = {station.title()}")
    return city, month, day, user_type, station

    print(f"\nYou selected: City = {city.title()}, Month = {month.title()}, Day = {day.title()}")
    return city, month, day
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month


    # display the most common day of week


    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
