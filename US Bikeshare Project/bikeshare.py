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
    
    print('----->>> Hello! Let\'s explore some US bikeshare data! <<<-----\n\n')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # by using str() we avoid the user entering a numeric value
    
    print("Would you like to see data for Chicago, New York City, Washington?")
    city = str(input("Your Answer: ")).lower()
    print('\n')
    
    while city not in CITY_DATA.keys():
        print("Please select city from this cities (Chicago, New York City, Washington)")
        city = str(input("Your Answer: ")).lower()
        print('\n')
    
    # get user input for month (all, january, february, ... , june)
    print("Which month would you like to filter the data by? Choose month from (January to June) | \'All\':Do not filter by month")
    month = str(input("Your Answer: ")).lower()
    months = ['january','february','march','april','may','june','all']
    print('\n')
    while month not in months:
        print("Please choose from this (January, February, March, April , May, June) | \'All\':Do not filter by month")
        month = str(input("Your Answer: ")).lower()
        print('\n')
           
    # get user input for day of week (all, monday, tuesday, ... sunday)
    print("Which day would you like to filter the data by? For Example: Saturday, Sunday. | \'All\':Do not filter by day")
    day = str(input("Your Answer: ")).lower()
    print('\n')
    days = ['saturday' , 'sunday' , 'monday' , 'tuesday' , 'wednesday' , 'thursday' , 'friday' , 'all']
    while day not in days:
        print("please choose from this (Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday) | \'All\':Do not filter by day")
        day = str(input("Your Answer: ")).lower()
        print('\n')
        
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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['start_hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    frequent_month = df['month'].mode()[0]
    print("The Most Frequent Month:",frequent_month)
    
    # TO DO: display the most common day of week
    frequent_day = df['day_of_week'].mode()[0]
    print("The Most Frequent Day of Week:",frequent_day)
    
    # TO DO: display the most common start hour
    frequent_start_hour = df['start_hour'].mode()[0]
    print("The Most Frequent Start Hour:",frequent_start_hour)
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("The Most Popular Start Station:",popular_start_station)
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("The Most Popular End Station:",popular_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    popular_start_and_end_stations = (df['Start Station'] + " | " + df['End Station']).mode()[0]
    print("The Most Popular Start & End Stations:",popular_start_and_end_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_duration = df['Trip Duration'].sum()
    print("The Total Trip Duration:",total_trip_duration)
    # TO DO: display mean travel time
    avg_trip_duration = df['Trip Duration'].mean()
    print("The Average Trip Duration:",avg_trip_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print("The User Types Counts:")
    print(user_type,'\n')
    
    # TO DO: Display counts of gender
    # Washington does NOT have 'Gender' column
    if 'Gender' in df:
        user_gender = df['Gender'].value_counts()
        print("The User Gender Counts:")
        print(user_gender,'\n')
    
    # TO DO: Display earliest, most recent, and most common year of birth
    # Washington does NOT have 'Birth Year' column
    if 'Birth Year' in df:
        earliest_year = df['Birth Year'].min()
        print("Earliest Year of Birth:",earliest_year)
        print('\n')
        
        recent_year = df['Birth Year'].max()
        print("Recent Year of Birth:",recent_year)
        print('\n')
        
        birth_year = df['Birth Year'].mode()[0]
        print("Most Common Year:",birth_year) 
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    """ Raw data is displayed upon request by the user """
    
    print("\nWould you like to see first 5 lines of the data? (yes|no)")
    display = str(input("Your Answer: ")).lower()
    print('\n')
    i = 0
    while display != 'no':
        print(df.iloc[i:i+5])
        i = i + 5
        print("\nWould you like to see next 5 lines of the data? (yes|no)")  
        display = str(input("Your Answer: ")).lower()
        print('\n')
        
   
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        
        print('Would you like to restart? Enter (yes|no)')
        restart = str(input("Your Answer: ")).lower()
        if restart.lower() != 'yes':
            print("\n----->>>  See you next time!  <<<-----\n")
            break


if __name__ == "__main__":
	main()
