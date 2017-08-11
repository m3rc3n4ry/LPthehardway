from sys import argv
from sys import exit

def gold_room():
    print "The room is filled of gold. How much do you take?"

    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy. You win!"
        exit(0)
    else:
        dead("You greedy bastard!")

def dead(why):
    print why, "Good Job!"
    exit(0)

def start():
    print "You are in a dark swampy forest."
    print "There's an axe in-front of you in a plank."
    print "What do you do? Take it, or go ahead?"

    next = raw_input("> ")
    if "take" in next or "pick" in next:
        taken = 1
    elif "go" in next:
        dead("An Anaconda comes out of nowhere and eats you alive.")
    else:
        print "Nice! %s is probably a good idea! Low tide hits and you reach the gold room!" % next
        gold_room()

    if taken == 1:
        dead("Nice, you can now defend yourself from sea Monsters! You die in water.")


start()
