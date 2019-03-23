import sys;

# Renvoie True si un mur est present a droite
def murPresentE (x,y,laby) :
	max =9;
	if (x+1 > max ) :
		return True;
	elif (laby[y][x+1] == 1 ) :
		return True;
	else :
		return False;
		
		
# Renvoie True si un mur est present en haut
def murPresentN (x,y,laby) :
	min = 0;
	if (y-1 < min ) :
		return True;
	elif (laby[y-1][x] == 1 ) :
		return True;
	else :
		return False;
		
		
# Renvoie True si un mur est present a gauche	
def murPresentO (x,y,laby) :
	min = 0;
	if (x-1 < min ) :
		return True;
	elif (laby[y][x-1] == 1 ) :
		return True;
	else :
		return False;
	

# Renvoie True si un mur est present en bas	
def murPresentS (x,y,laby) :
	max =9;
	if (y+1 > max ) :
		return True;
	elif (laby[y+1][x] == 1 ) :
		return True;
	else :
		return False;
		
		
# affichage console		
def show(laby) :
	for i in range (0,10):
		for j in range (0,10):
			# eau
			if ( laby[i][j] == 0 ) :
				sys.stdout.write("_ ");
			# rate
			elif ( laby[i][j] == 1 ) :
				sys.stdout.write("# ");
			elif (laby[i][j] == 2) :
				sys.stdout.write("o ");
		print '';		
	
# fonction d'initialisation
def init() :
	res = [   [0,0,0,0,1,1,1,1,0,0],
               [1,0,1,0,0,1,0,0,1,0],
               [1,0,1,1,0,1,1,0,1,0],
               [0,0,1,0,0,0,0,0,1,0],
               [0,1,1,0,1,0,1,0,0,0],
               [0,0,0,1,1,1,1,1,1,0],
               [1,1,0,1,0,0,0,0,0,1],
               [0,0,0,0,0,1,0,1,0,1],
               [1,1,1,0,1,0,0,1,0,1],
               [1,0,0,0,1,0,1,1,0,0]  ];
			   
	return res;

# met a jour la position du pointeur
def update(x,y):
	res = init();
	for i in xrange(0,10):
		for j in xrange(0,10):
			if (i == y and j == x):
				res[i][j] = 2;
	return res;

	
# initialisation du labyrinthe
laby = init();
# definition de la position initiale
current_pos_x = 0;
current_pos_y = 0;
min = 0;
max = 9;

# tant que la position du pointeur n'est pas en bas a droite...
while (current_pos_x != 9 or current_pos_y != 9):

	laby = update(current_pos_x, current_pos_y);
	show(laby);

	# input de l'utilisateur
	orientation = str(raw_input("Entrez une direction : (z q s d)"));

	
	if (orientation == "s"):
		# test si un mur est present au sud
		if (murPresentS(current_pos_x, current_pos_y, laby) == True):
			print("Impossible : mur en bas");
		# sinon on va en bas
		else :
			current_pos_y = current_pos_y+1;

	elif (orientation == "q") :
		if (murPresentO(current_pos_x, current_pos_y, laby) == True):
			print("Impossible : mur a gauche");
		else :
			current_pos_x = current_pos_x-1;

	elif (orientation == "z") :
		if (murPresentN(current_pos_x, current_pos_y, laby) == True):
			print("Impossible : mur en haut");
		else :
			current_pos_y = current_pos_y-1;

	elif (orientation == "d") :
		if (murPresentE(current_pos_x, current_pos_y, laby) == True):
			print("Impossible : mur a droite");
		else :
			current_pos_x = current_pos_x+1;

	else :
		print("Commande inconnue");

laby = update(current_pos_x, current_pos_y);
show(laby);	

	
