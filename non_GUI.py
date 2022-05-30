import random

def intro():
    print("""
    \tWelcome to TebakAngka Game's!\n
    Guess a number in radius 1 - 50!
    there are some rules :
        - have 5 chances to guess,
        - will win if u guess the number.\n
    Good Luck!
    """)


def helper(ply_numb, random_numb) :
    global help
    if ply_numb > random_numb :
        help = ply_numb - random_numb
    elif ply_numb < random_numb :
        help = random_numb - ply_numb
    else: help = 0

    if help == 0 :
        pass
    elif help <= 2 :
        help = "hampir tepat!"
    elif help > 2 and help < 5 :
        help = "dekat sekali.."
    elif help >= 5 and help <= 8 :
        help = " mendekati,"
    else :
        help = "sangat jauh."


def start_game() :
    the_number =  random.randint(1,50)
    chance = 5
    while chance > 0 :
        try :
            player = int(input("\nMasukan pilihan mu : "))
            helper(player, the_number)
            if player == the_number :
                print("\n\ttebakan mu benar!\n\tangka-nya adalah : {}".format(the_number))
                a = input("\n\tmain lagi?\n\tketik y untuk main lagi : ")
                if a == "y" :
                    the_number =  random.randint(1,50)
                    chance = 5
                else : return

            elif player > the_number :
                chance -= 1
                print("\nsalah, pilihan mu lebih besar")
                print("petunjuk : {}".format(help))
                print("\n\tsisa kesempatan : {}x".format(chance))
            
            else :
                chance -= 1
                print("\nsalah, pilihan mu lebih kecil")
                print("petunjuk : {}".format(help))
                print("\n\tsisa kesempatan : {}x".format(chance))
        except ValueError :
            print("\nYang kamu masukan bukan angka")
            a = input("\n\tmasukan ulang?\n\tketik y untuk memasukan ulang : ")
            if a != "y" : return

        if chance == 0 :
            print("\nKamu kalah!")
            a = input("\n\tCoba ulang?\n\tketik y untuk coba ulang : ")
            if a == "y" :
                chance = 5
                the_number =  random.randint(1,50)
            else: chance = 0

    print("\n\n\tthank u")

if __name__ == "__main__" :
    intro()
    start_game()