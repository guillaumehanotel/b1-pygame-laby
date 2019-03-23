#Importation des bibliotheques necessaires
import pygame
from pygame.locals import *

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
		
	
# fonction d'initialisation
def initial() :
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

	
# affichage graphique
def show(laby) :
	for i in range (0,10):
		for j in range (0,10):
			# 
			if ( laby[i][j] == 0 ) :
				pass;
			elif ( laby[i][j] == 1 ) :
				fenetre.blit(bush,(50*j,50*i ));
			elif (laby[i][j] == 2) :
				fenetre.blit(tofu,(50*j,50*i  ));
		

# met a jour la position du pointeur
def update(x,y):
	res = initial();
	for i in xrange(0,10):
		for j in xrange(0,10):
			if (i == y and j == x):
				res[i][j] = 2;
	return res;
	
	

#Initialisation de la bibliotheque Pygame
pygame.init();
# initialisation du labyrinthe
laby = initial();
# definition de la position initiale
current_pos_x = 0;
current_pos_y = 0;
min = 0;
max = 9;


#Creation de la fenetre
fenetre = pygame.display.set_mode((500, 500));
# Creation des images
grass = pygame.image.load("img/grass.jpg").convert();
bush = pygame.image.load("img/bush.png").convert_alpha();
tofu = pygame.image.load("img/tofu.png").convert_alpha();


fenetre.blit(grass,(0,0));
laby = update(current_pos_x, current_pos_y);
show(laby);
pygame.display.flip();


continuer = 1;

# tant que la position du pointeur n'est pas en bas a droite 
while continuer and (current_pos_x != 9 or current_pos_y != 9) :

	# pour tous les evenements :
	for event in pygame.event.get():
		
		# si l'evenement est une touche
		if event.type == KEYDOWN :
			
			# si la touche est 's' ou fleche bas :
			if event.key == K_s or event.key == K_DOWN :
				# si il n'y a pas de mur, on bouge 
				if (murPresentS(current_pos_x, current_pos_y, laby) == False):
					current_pos_y = current_pos_y+1;
	
			elif event.key == K_a or event.key == K_LEFT :# a correspond a q en qwerty
				if (murPresentO(current_pos_x, current_pos_y, laby) == False):
					current_pos_x = current_pos_x-1;
	
			elif event.key == K_w or event.key == K_UP : # w correspond a z en qwerty
				if (murPresentN(current_pos_x, current_pos_y, laby) == False):
					current_pos_y = current_pos_y-1;
					
			elif event.key == K_d or event.key == K_RIGHT :
				if (murPresentE(current_pos_x, current_pos_y, laby) == False):
					current_pos_x = current_pos_x+1;
			else :
				pass;
	
		elif event.type == pygame.QUIT:
			continuer = 0

	# on met a jour l'affichage
	fenetre.blit(grass,(0,0));
	laby = update(current_pos_x, current_pos_y);
	show(laby);
	pygame.display.flip();


