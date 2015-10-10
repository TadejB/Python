import random

"""cilj igre je, da dva tekmovalca tekmujeta med seboj v tekmovanju
metanja kock. Zmaga tisti, ki prvi doseze 20 ali vec pik"""

#za dve kocki
sum_dice = 0
tabel = []
sum_dice2 = 0
tabel2 = []

while sum_dice <= 20 and sum_dice2 <= 20:
    dice_result = random.randint(1,6)
    sum_dice += dice_result
    tabel.append(dice_result)
    dice_result2 = random.randint(1,6)
    sum_dice2 += dice_result2
    tabel2.append(dice_result2)

    print "Results of player1 ----> " + str(tabel).strip('[]')
    print "Sum Player1 ---> " + str(sum_dice)
    print "Results of player2 ----> " + str(tabel2).strip('[]')
    print "Sum Player2 ---> " + str(sum_dice2)


if sum_dice == sum_dice2:
    print "It's a tie"
elif sum_dice > sum_dice2:
    print "Player1 wins"
else:
    print "Player2 wins"

#za eno kocko
"""
sum_dice = 0
tabel = []

while sum_dice < 20:
    dice_result = random.randint(1,6)
    sum_dice += dice_result
    tabel.append(dice_result)
    print tabel
    print sum_dice"""





