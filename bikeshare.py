import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

listOfCities = ['chicago', 'new_york_city', 'washington']
listOfMonths = ['january', 'february', 'march', 'april', 'may', 'june']
listOfDays = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    city = ''
    month = ''
    day = ''
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while (city not in listOfCities):
        city = input("Select the city. Type Chicago, New York City, or Washington and press Enter. \n").lower()
        if city == 'new york city':
            city = 'new_york_city'

    # TO DO: get user input for month (all, january, february, ... , june)
    while (month not in listOfMonths and month != 'all'):
        month = input("Select the month. Type the name a month, January - June, and press Enter. \nIf you want to view data for all months, type All and press Enter. \n").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while (day not in listOfDays and day != 'all'): 
        day = input("Select the day of the week. Type the name of the day, Monday - Sunday, and press Enter. \nIf you want to view data for all days of the week, type All and press Enter. \n").lower()
    

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
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv('{}.csv'.format(city))


    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = listOfMonths.index(month)
        
    
        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month]
        

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        print(df)
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    try: 
        # find the most common month
        popular_month = df['month'].mode()[0]
        
        #display most common month
        print("The most common month is: {}".format(popular_month))
    except Exception as e: 
        print("Exception occurred: {}".format(e)) 
        
    # TO DO: display the most common day of week
    try: 
        # find the most common day
        popular_day = df['day_of_week'].mode()[0]
        
        #display most common day of week
        print("The most common day of the week is: {}".format(popular_day))
    except Exception as e: 
        print("Exception occurred: {}".format(e)) 

    # TO DO: display the most common start hour
    try: 
        # convert the Start Time column to datetime
        df['Start Time'] = pd.to_datetime(df['Start Time'])

        # extract hour from the Start Time column to create an hour column
        df['hour'] = df['Start Time'].dt.hour

        # find the most common hour (from 0 to 23)
        popular_hour = df['hour'].mode()[0]
        
        #display most common start hour
        print("The most common start hour is: {}".format(popular_hour))
    except Exception as e: 
        print("Exception occurred: {}".format(e)) 
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('The most commonly used start station is: {}'.format(common_start))

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('The most commonly used end station is: {}'.format(common_end))

    # TO DO: display most frequent combination of start station and end station trip
    common_combo = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('Most common combination of start/end stations: {} to {}'.format(common_combo[0], common_combo[1]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum(skipna = True)
    print('The total travel time for your selection is: {}'.format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean(skipna = True)
    print('The average travel time for your selection is: {}'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    # print value counts for each user type
    user_types = df['User Type'].value_counts()
    print("Counts of user types:\n{}".format(user_types))

    # TO DO: Display counts of gender
    if city != 'washington': 
        gender_types = df['Gender'].value_counts()
        print("\nCounts of gender:\n{}".format(gender_types))

    # TO DO: Display earliest, most recent, and most common year of birth
    if city != 'washington':
        earliest_birth = df['Birth Year'].min()
        recent_birth = df['Birth Year'].max()
        common_birth = df['Birth Year'].mode()[0]
    
        print('\nThe earliest year of birth is: {}'.format(earliest_birth))
        print('The most recent year of birth is: {}'.format(recent_birth))
        print('The most common year of birth is: {}'.format(common_birth))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        if df.empty: 
            print('There are no search results for the filters you applied! Restart and try a different search selection.')
        else: 
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df, city)
        
            counter = 0
            view_data = input('\nWould you like to view the data? Enter yes or no. \n')
            while view_data.lower() == 'yes':
                print(df.iloc[counter:counter + 5])
                counter += 5
                view_data = input('\nWould you like to view more data? Enter yes or no. \n')
            
            

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
            


if __name__ == "__main__":
	main()
