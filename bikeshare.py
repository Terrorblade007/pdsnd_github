import time
import pandas as pd
import numpy as np
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city= input('Please choose a City name from Chicago, New York City, Washington: ').lower()
        if city not in CITY_DATA:
            print('Please choose CITY from CITY DATA')
        else:
            break
# get user input for month (all, january, february, ... , june)
    while True:
        month= input('Please choose a month from January, February, March, April, May, June or Choose All Months: ').lower()
        months = ['january', 'feburary', 'march', 'april', 'may', 'june', 'july']
        if month != 'all' and month not in months:
                  print('Please choose correct month name')
        else:
                  break
# get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day= input('Please choose a day of the week or choose all days to view data on all days: ').lower()
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        if day != 'all' and day not in days:
                  print('Please choose correct day name')
        else:
            break
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
        

    return df
def display_raw_data(df):
    i = 0
    answer = input('Do you want to see first 5 rows of raw data? yes/no: ').lower()
    pd.set_option('display.max_columns',None)

    while True:
        if answer == 'no':
            break
        print(df[i:i+5])
        answer = input('Would you like to see next 5 rows of raw  data? yes/no: ').lower()
        i += 5    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # display the most common month
    most_common_month = df['month'].mode()[0]
    print('Most Common Month', most_common_month)
    # display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('Most Common Day:', most_common_day)
    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print(' Most Common Start Hour:', most_common_start_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most Commonly Used Start Station:', common_start_station)
    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most Commonly Used End Station:', common_end_station)
    # display most frequent combination of start station and end station trip
    combination_start_end = df.groupby(['Start Station', 'End Station']).count().idxmax()[0]
    print('Most Frequent Combination of Start and End Stations:', combination_start_end)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:',total_travel_time)
    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time:',mean_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
     # Display counts of user types
    print('Count of User Types:\n', df['User Type'].value_counts());
    # Display counts of gender
    if 'Gender' in df:
        print('\n Counts of Gender:\n', df['Gender'].value_counts())
        # Display earliest, most recent, and most commong year of birth
        if 'Birth Year' in df:
            earliest_byear = int(df['Birth Year'].min())
            print('\n Earliest Year of Birth:\n', earliest_byear)
            recent_byear = int(df['Birth Year'].max())
            print('\n Most Recent Year of Birth:\n', recent_byear)
            common_byear = int(df['Birth Year'].mode()[0])
            print('\n Most Common Year of Birth:\n', common_byear)
                
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
    main()
