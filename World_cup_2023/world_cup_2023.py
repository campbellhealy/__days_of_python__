# world_cup_2023
'''
     With this data set there is a vast amount of data. I am only touching on a little.
     There is a little bit of repeating code pulled out to another function
     There is an example of splitting a function up into 3, for easy reading of the main code.
'''
import pandas as pd


data = pd.read_csv('data.csv')

# print(data)
# print(data.columns)
# print(data.head)

def count_the_teams(data):
    # Use set to keep only unique entries
    teams1 = set(data.team1)
    teams2 = set(data.team2) #Just in case a team only played away :)
    teams1.union(teams2) # Using union gets the intersection
    print(f'Number of teams on 2023 World Cup is {len(teams1)}')


def string_int_columns(data):
    # This used in more than one function
    data = (
                data
                .astype
                (
                    {
                        'own goals team1':'int',
                        'own goals team2':'int'
                    }
                )
            )
    return data


def teams1_renamer(data):
    # This is a function pulled out of the main function
    data = data.rename(
    columns= 
        {
            'team1': 'Country', 
            'number of goals team1': 'Goals'
        }
        )
    return data


def teams2_renamer(data):
    # This is a function pulled out of the main function
    data = data.rename(
    columns= 
        {
            'team2': 'Country', 
            'number of goals team1': 'Goals'
        }
        )
    return data


def own_goals(data):
    # Get all the countries that OG and the amount by
    # String to int
    data = string_int_columns(data)
    # Get Home team OG
    teams1=(
        data[[
            'team1', 
            'own goals team1'
            ]]
        .copy()
        .sort_values(by='team1')
        )
   # Get Away team OG
    teams2= (
        data[[
            'team2', 
            'own goals team2'
            ]]
        .copy()
        .sort_values(by='team2')
        )
    # Rename columns prior to merge
    teams1 = teams1.rename(
        columns= 
            {
                'team1': 'Country', 
                'own goals team1': 'Own Goals'
            }
            )
    teams2 = teams2.rename(
        columns= 
            {
                'team2': 'Country', 
                'own goals team2': 'Own Goals'
            }
            )
    total_og = pd.concat([teams1, teams2])
    # Remove own goals zero
    total_og = total_og.loc[total_og['Own Goals'] >0]
    print(total_og)


def goals_scored(data):
    # Totsl goals scored by each country
    # String to int
    data = string_int_columns(data)
    # Get Home team Goals
    teams1=(
        data[[
            'team1', 
            'number of goals team1'
            ]]
        .copy()
        .sort_values(by='team1')
        )
   # Get Away team Goals
    teams2= (
        data[[
            'team2', 
            'number of goals team2'
            ]]
        .copy()
        .sort_values(by='team2')
        )

    # Rename columns
    teams1 = teams1_renamer(data)   
    teams2 = teams2_renamer(data)   
    # Full dataset
    total_goals = pd.concat([teams1, teams2])
    print(
        total_goals  # DataFrame
        .groupby(by='Country') # Initial grouping
        ['Goals'] # Value to be summed
        .sum()
        )


def more_than_n_goals(data, goals):
    # Countries scoring above a certain value
    # String to int
    data = string_int_columns(data)
    # Get Home team Goals
    teams1=(
        data[[
            'team1', 
            'number of goals team1'
            ]]
        .copy()
        .sort_values(by='team1')
        )
   # Get Away team Goals
    teams2= (
        data[[
            'team2', 
            'number of goals team2'
            ]]
        .copy()
        .sort_values(by='team2')
        )

    # Rename columns        
    teams1 = teams1.rename(
        columns= 
            {
                'team1': 'Country', 
                'number of goals team1': 'Goals'
            }
            )
    teams2 = teams2.rename(
        columns= 
            {
                'team2': 'Country', 
                'number of goals team2': 'Goals'
            }
            )
    # Full dataset
    total_goals = pd.concat([teams1, teams2])
    # Totals per country
    total_goals= (
        total_goals  # DataFrame
        .groupby(by='Country') # Initial grouping
        ['Goals'] # Value to be summed
        .sum()
        .to_frame()
        )
    # Filter out low scoring countries
    total_goals= total_goals[total_goals.Goals > goals] # Filter out teams that score less than variable
    print(total_goals)


# count_the_teams(data)
# own_goals(data)
# goals_scored(data)
# more_than_n_goals(data, 10)