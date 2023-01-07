import random

def pick_unique_items(items):
  picked_items = []
  remaining_items = items[:]
  while remaining_items:
    # Pick a random item from the list of remaining items
    random_item = random.choice(remaining_items)
    # Add it to the list of picked items
    picked_items.append(random_item)
    # Remove it from the list of remaining items
    remaining_items.remove(random_item)
  return picked_items

# Test the function with a list of integers
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
print(pick_unique_items(themes))
