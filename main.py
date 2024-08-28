#Snake Game
#author: Sehaj

import pygame
import random

#initialise pygame module
pygame.init()

#creating a pygame window
display = pygame.display.set_mode((500,400))

#set the title on pygame window
pygame.display.set_caption("Snake Game")

timer = pygame.time.Clock()

#defining colors
blue = (0,0,255)
red = (255,0,0)
black = (0,0,0)
white = (255, 255, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)

#define speed of the snake
snakespeed = 15

#choose the progression of size of snakespeed
snakeadd = 10

#fruit positions
fruit_positions = [random.randrange(1, (500//10)) * 10,
random.randrange(1, (400//10)) * 10]

#choosing displaying fonts and their sizes
font_style = pygame.font.SysFont("Aerial", 25)
score_font = pygame.font.SysFont("Comicsansms", 40)

#define a function to create the snake 
def snake(snakeadd, snake_list):
  for x in snake_list:
    pygame.draw.rect(display, blue, [x[0], x[1], snakeadd, snakeadd])

#define a function to display user score
def your_score(score):
  value = score_font.render("Your Score: " + str(score), True, white)
  display.blit(value, [0, 0])

#define a function to use whenever displaing a message
def message(msg, color):
  mesg = font_style.render(msg, True, color)
  display.blit(mesg, [500 / 6, 400 / 3])

#define a function to start the steps of the game whenever the function is called 
def gameloop():
  game_over = False
  game_close = False
 
#assign the coordinated for snake to start
  x = 500 / 2
  y = 400 / 2
 
 #predefine the change in snake movements to be zero until redefined
  change_in_x = 0
  change_in_y = 0
 
 #make an empty list for all snake positions
  snake_list = []
  length_of_snake = 1

#assign the range of random positions for food to appear
  foodx = round(random.randrange(0, 500 - snakeadd) / 10.0) * 10.0
  foody = round(random.randrange(0, 400 - snakeadd) / 10.0) * 10.0

#create a while loop to continue the game 
  while not game_over:

#create a while loop for whenever the user wants to close the game
    while game_close == True:
      display.fill(green)
      message("You Lost! Press P-Play Again or Q-Quit", black)
      your_score(length_of_snake - 1)
      pygame.display.update()
 
#nest a for loop for every action taken/event happening during the game
      for event in pygame.event.get():

#nest an if statement for any key pressed on the keyboard
        if event.type == pygame.KEYDOWN:

#if the key pressed is 'q' game is closed
          if event.key == pygame.K_q:
            game_over = True
            game_close = False

#if the key pressed is 'p' call out the function to start the game loop again
          if event.key == pygame.K_p:
            gameloop()

#
    for event in pygame.event.get():

#if the user wants to quit the game, game_over becomes true and pygame library is deactivated
      if event.type == pygame.QUIT:
        game_over = True

#define the movements of the snake for every key that is pressed- up/down/right/left and redefine the changes in x and y coordinates
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          change_in_x = -snakeadd
          change_in_y = 0
        elif event.key == pygame.K_RIGHT:
          change_in_x = snakeadd
          change_in_y = 0
        elif event.key == pygame.K_UP:
          change_in_x = 0
          change_in_y = -snakeadd
        elif event.key == pygame.K_DOWN:
          change_in_x = 0
          change_in_y = snakeadd

#if the coordinates of the snake are equal to greater than the dimensions of the pygame window, game does not continue
    if x >= 500 or x < 0 or y >= 400 or y < 0:
      game_close = True

#add the changes in both x and y, and redefine them to the new value at the same time 
    x += change_in_x
    y += change_in_y

#specify the aspects of rectangle(food)
    display.fill(green)
    pygame.draw.rect(display, red, [foodx, foody, snakeadd, snakeadd])

#define the coordinates for the head of snake that change with the changes in x and y defined earlier
    snake_head = []
    snake_head.append(x)
    snake_head.append(y)

#make a list of snake body that is where ever the head has gone
    snake_list.append(snake_head)

#make the list to omit the first item after the items in list become equal to the length of snake so that the list only has the positions of the snake body in current time
    if len(snake_list) > length_of_snake:
      del snake_list[0]

#for part of snake to touch the snake head, the game is over
    for a in snake_list[:-1]:
      if a == snake_head:
        game_close = True

#call out the score function to display score
    snake(snakeadd, snake_list)
    your_score(length_of_snake - 1)

    pygame.display.update()

#when the position of the snake head is the same as the food move on to display some other position of food and increase the length of snake by one
    if x == foodx and y == foody:
      foodx = round(random.randrange(0, 500 - snakeadd) / 10.0) * 10.0
      foody = round(random.randrange(0, 400 - snakeadd) / 10.0) * 10.0
      length_of_snake += 1

    timer.tick(snakespeed)

#end the pygame module
  pygame.quit()
  quit()

#call out the game loop function to start the game
gameloop()
