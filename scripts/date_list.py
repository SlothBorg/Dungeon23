import datetime
import calendar

start_date = datetime.datetime.strptime('01/01/23', "%m/%d/%y")
themes = [
    'Ancient',
    'Death',
    'Sunken',
    'Love',
    'Empire',
    'Heavy',
    'Rural',
    'Darkness',
    'Bloom',
    'Rust',
    'Noise',
    'Childhood',
    'Time',
    'Excess',
    'Decay',
    'City',
    'Factory',
    'Flood',
    'Sleep',
    'Cold',
    'Ash',
    'Touch',
    'Meat',
    'Solitude',
    'Growth',
    'Greed',
    'Luck',
    'Fall',
    'Pit',
    'Chaos',
    'Laughter',
    'Smoke',
    'Forgotten',
    'Library',
    'Ocean',
    'Song',
    'Roots',
    'Bones',
    'Hangman',
    'Blood',
    'Prophet',
    'Idol',
    'Door',
    'Light',
    'Stars',
    'Bridge',
    'Mask',
    'Cut',
    'Sacrifice',
    'Incense',
    'Rise',
    'Gold'
]

for i in range(1, 365):
    if i > 1:
        date = start_date + datetime.timedelta(i)
    else:
        date = start_date

    week_num = min(date.isocalendar()[1] - 1, 0)

    print('**Day**: ' + str(i))
    print('* **Level**: ' + str(date.month))
    print('* **Theme**: ' + themes[week_num])
    print()
