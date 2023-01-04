import datetime

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

print('| Day         | Level       | Theme       |')
print('| ----------- | ----------- | ----------- |')

for i in range(1, 365):
    if i > 1:
        date = start_date + datetime.timedelta(i)
    else:
        date = start_date

    if i == 1:
        week_num = 1
    else:
        week_num = date.isocalendar()[1]

    print('| ' + str(i) + ' | ' + str(date.month) + ' | ' + themes[week_num-1] + ' |')
