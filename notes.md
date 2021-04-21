
having the static data isn't as important as being able to repeatedly create the data 
we want from the original CSVs
    
lower case names are much easier to work with, anything else is like having different electrical outlet types in each room
in your house

it's not critical because we don't have a finished product / completed project, yet still true 
that jupyter notebooks are best used as sorta substitutes for websites or other frames to put
findings and plots and visualizations, equations describing models, etc. inside of

parts like data cleaning are best placed in separate files that we, or anyone who else wants to run the
code for the project, can deal with separately
findings that ultimately form the core of jupyter notebooks are unecessarily attenuated when there's
a whole bunch of uninteresting code dealing with standardizing dataframes and preprocessing
I love the code but putting cleaning steps in jupyter nbs isn't as helpful in communicating results 
as removing them to a separate file and at the end of the day jupyter notebooks are best when communicating results

lines like these are much easier to do with a function:
a_16 = os.path.join("Resources", "2016_team_data.csv")
a_17 = os.path.join("Resources", "2017_team_data.csv")
a_18 = os.path.join("Resources", "2018_team_data.csv")
a_19 = os.path.join("Resources", "2019_team_data.csv")
a_20 = os.path.join("Resources", "2020_team_data.csv")

that way we only have to change code in one place rather than in 21-16 = 5 places if our code gets snapped up for whatever reason or if we just want to play around with 
the code 

I'm going to look into 'sportsreference' the python package
i feel like a great stat would be average run differentials per inning
or pythagorean win % with inning fixed effects?
this way we could distinguish runs scored when a team is down 9-2 in the seventh 
playing a sub-500 team in septemeber after the team that's down 9-2 has
already made the plaoyoffs
runs scored ** 1.83 / runs scored ** 1.83 + allowed ** 1.83 counts all runs scored and runs allowed 
as equal, idk
