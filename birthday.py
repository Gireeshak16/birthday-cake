import time
import random

WISHES = [
    "May this year bring you laughter and good health!",
    "Another year older, another year brighter!",
    "Wishing you a day full of cake and smiles!",
    "Here's to new adventures and big dreams!",
]

def cake(lit=True):
    if lit:
        flames = " ( )    ( )    ( )"
    else:
        flames = "                   "

    print(f"""
      {flames}
        |      |      |
      __|______|______|__
     | ~ ~ ~ ~ ~ ~ ~ ~ ~ |
    |_____________________|
    |                     |
    |_____________________|
    """)

def main():
    name = input("Whose birthday : ").strip()
    
    if name:
        title = f"Happy Birthday, {name}!"
    else:
        title = "Happy Birthday!"

    # Show cake with candles lit
    cake(lit=True)
    print("   " + title)
    print()

    input("Make a wish, then press Enter to blow out the candles... ")

    # Show cake with candles out
    cake(lit=False)
    print()

    # Random wish
    wish = random.choice(WISHES)
    print("   " + wish)
    print()

if __name__ == "__main__":
    main()