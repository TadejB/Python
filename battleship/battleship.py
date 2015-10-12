from random import randint

boatField = []

for i in range(0, 31):
	boatField.append(False)

# Pick number one between 0 and 50, then pick
# number 2 between the first picked number and
# 100. Make sure that the ship size is at least
# 5 and not bigger than 8.
# If not, repeat the procedure until you get
# two "good numbers"

shipStartField = randint(0, 30)
shipEndField = randint(shipStartField, 30)
shipSize = shipEndField - shipStartField + 1 # +1 ker stevilo polj ni enako razliki med eno in drugo stevilko

while shipSize < 5 or shipSize > 8:
    shipStartField = randint(0, 30)
    shipEndField = randint(shipStartField, 30)
    shipSize = shipEndField - shipStartField + 1  # +1 ker stevilo polj ni enako razliki med eno in drugo stevilko
else:
    print "Battleship size is: " + str(shipSize)

print "Ship is between %d and %d" % (shipStartField, shipEndField)

# Set the boat in the boat list
#Battelship length is: 6
#Ship is between 24 and 30
#Traceback (most recent call last):
#
#    boatField[i] = True
#IndexError: list assignment index out of range"""
for i in range(shipStartField, shipEndField + 1):
	boatField[i] = True

gameRunning = True
shipPiecesLeft = 0
shootHistory = [] # tabela ki belezi prejsne uspesne zadetke, da nas opozori na primer, da ciljamo ze zadet del ladje

while gameRunning:
	# What to add?
	# target = raw_input - prompt player to pick a
	# number between 0 and 30, make sure that the
	# input is integer (number) before using it

	# BONUS: Check if the user picked the right
	# number (between 0 and 30, if he hasn't,
	# prompt him for the number again)

	# TODO: Uncomment this line and read user input ...




	while True:
		try:
			target = int(raw_input("Pick a number between 0 and 30: "))
			if target < 0 or target > 30:
				target = int(raw_input("Please pick a number between 0 and 30: "))
			break
		except ValueError:
			print "Please pick only numbers between 0 and 30"

	if boatField[target] == False:
		if target in shootHistory:
			print "You already hit that piece of ship!"
		else:
			print "Missed!"
	elif boatField[target] == True:
		shootHistory.append(target)
		# TODO: Set the target in boat field to False
		boatField[target] = False
		print "Boat hit!"




	# Check if we still have any ship pieces left
	# (was the boat sunk)
	for i in range(0, 30):
		if boatField[i] == True:
			shipPiecesLeft = shipPiecesLeft + 1
	if shipPiecesLeft == 0:
		gameRunning = False
	else:
		shipPiecesLeft = 0

print "You sank my battleship!"



