$ import random
# The game starts here.




# persistent variables
default persistent.secret_unlocked = False
default persistent.parallax_on = True 


# this set of variables is just a bunch of fun stats
define total_rolled = 0 # this is the total for the dice you've ever ever rolled!!!!
define total_rolls = 0 # total amount of times you've rolled individual dice (if your stat is 4, it will add 4)
define total_rtimes = 0 # total amount of times you've done a roll (no matter your stat, it will add 1 each time)
# maybe I will add persistence, or maybe not.


# this set of variables controls the "free", "easy", "medium", "hard", "veryhard", "impossible"
define free = 1
define easy = 6
define avg = 12
define hard = 18
define stp = 24
define imp = 30
define ezd = {"free" : free, "easy" : easy, "avg" : avg, "hard" : hard, "stp" : stp, "imp" : imp }

# this set of variables is the five stats. the stats are around 1-7, but players can choose to surpass the limit of 20 if they wish
define p = 4
define a = 4
define w = 4
define g = 4
define t = 4
# maybe I should use a dictionary?
define statd = { "p" : 4, "a" : 4, "w" : 4, "g" : 4, "t" : 4 }


# these are boolean values for the fundamentals of the game
define default_stats = True # usually will always be true, player can customize though?

# this is a list of special ability things???????????????????????????
# I should add special abilities to the shapeshifting presets.
define specials = []

# specific boosts on certain actions in the PAWGT???? requires more thinking tho
# + too much balancing that I don't want to do

# this is a variable displaying the affection that the burden has for cori. rico? iro?
# uses the same scaling as pawgt. can be negative? (so I don't have to balance too hard)
define caff = 4 # "cori affection"

# this is a list of lists of the possible dishes that the burden may ask cori to pick up, indexes based on caff
define dishes = [
    [
        
    ]
]

# this is a list: index of number is the adjective describing the thing
define statjudge = ["completely nonexistent", "horribly lacking", "two","three","average","five","six","perfect","more than perfect"]

# this is a function to roll things.
# inside this init python is a bunch of functions, classes and stuff.
init python:

    def roll_dice(n):
        # n is the stat of pawgt, returns the total from rolling
        tot = 0
        for i in range(n):
            tot += random.randint(1,6)
        return tot
    def stat_check(s):
        # s is a string containing one of "pawgt"
        return roll_dice(statd[s])
    def passed_check(s,t):
        # s is a string free, easy, avg, hard, stp or imp
        # t is an int containing what the roll_dice returned
        # this returns a boolean True/False
        # greater than OR equal to will work
        return t >= ezd[s]


label start:
    # add parallaxes this time :))
    # dissolve for cool things
    # better UI too (need to plan that out)
    # better names

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
