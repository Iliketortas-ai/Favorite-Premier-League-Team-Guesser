# Premier League Team Guesser - Works for all groups

# Groups of teams based on 2024–25 standings
groups = {
    "1": ["Liverpool", "Arsenal", "Manchester City", "Chelsea", "Newcastle United"],
    "2": ["Aston Villa", "Nottingham Forest", "Brighton & Hove Albion", "Bournemouth", "Brentford"],
    "3": ["Fulham", "Crystal Palace", "Everton", "West Ham United", "Manchester United"],
    "4": ["Wolverhampton Wanderers", "Tottenham Hotspur", "Leicester City", "Ipswich Town", "Southampton"],
    "5": ["Promoted / Not in Premier League last year"]
}

print("Welcome to the Premier League Team Guesser!")
print("I will try to guess your favorite team based on your answers.\n")

# Step 1: Ask which group their team was in
print("Which group best fits your favorite team last season?")
print("""
1 - Top of the table (1st–5th)
2 - High mid-table (6th–10th)
3 - Mid-table (11th–15th)
4 - Lower table (16th–20th)
5 - They were not in the Premier League last year
""")

group_choice = input("Enter the number of your choice (1–5): ").strip()

# Make sure input is valid
if group_choice not in groups:
    print("That is not a valid choice. Please run the program again.")
    exit()

teams = groups[group_choice]

# Step 2: If group 5 (not in the Prem), ask directly
if group_choice == "5":
    team = input("What is the name of your team? ").title()
    print("Got it! Your favorite team must be " + team + ".")
else:
    print("\nHere are the teams in your group:")
    for t in teams:
        print("-", t)

    print("\nLet's see if I can guess your favorite team!")
    # Loop through each team and ask if it's their favorite
    for team in teams:
        answer = input("Is your favorite team " + team + "? (yes/no): ").lower()
        if answer == "yes":
            print("\nI guessed it! Your favorite team is " + team + ".")
            break
    else:
        print("\nHmm, looks like your team isn't in this group.")

print("\nThanks for playing the Premier League Team Guesser!")
