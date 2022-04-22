#John Brent David
import turtle
import os
import math
import random

#Choose the level difficulty IMPLEMENTATION OF NESTED HASH TABLE
difficulty = {'easy':{'speed':.2,'enemies':5},'medium':{'speed':2,'enemies':6},'hard':{'speed':4,'enemies':5}}
level = input("What level would you like to play?\nEasy\nMedium\nHard\nDecision : ")

if level.lower() == "easy":
    enemyspeed = difficulty['easy']['speed']
    number_of_enemies = difficulty['easy']['enemies']
elif level.lower() == "medium":
    enemyspeed = difficulty['medium']['speed']
    number_of_enemies = difficulty['medium']['enemies']
elif level.lower() == "hard":
    enemyspeed = difficulty['hard']['speed']
    number_of_enemies = difficulty['hard']['enemies']

#setup screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("bg.gif")

#Register the shapes
turtle.register_shape("kirby.gif")
turtle.register_shape("enemy.gif")
#Create the border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Set the score to 0
score = 0
#Draw the score
score_pen = turtle.Turtle()
score_pen.speed
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290,280)
scorestring= "Score: %s" %score
score_pen.write(scorestring,False,align="left",font = ("Arial",14,"normal"))
score_pen.hideturtle()

#Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("kirby.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

#Create an empty list of enemies
enemies = []

#Add enemy to the list
for i in range (number_of_enemies):
    enemies.append(turtle.Turtle())
enemy = turtle.Turtle()
for enemy in enemies:
    #Create the invader
    enemy.color("red")
    enemy.shape("enemy.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200,200)
    y = random.randint(100,250)
    enemy.setposition(x,y)



#Create Player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.hideturtle()
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(.5,.5)


bulletspeed = 40

#DEF bullet state
#ready - ready to fire
#fire - bullet is firing
bulletstate = "ready"
#movement of the player
playerspeed = 20

def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate ="fire"
        x = player.xcor()
        y = player.ycor()+10
        bullet.setposition(x,y)
        bullet.showturtle()

def isCollision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    return False

#Create keyboard bindings
turtle.listen()
turtle.onkeypress(move_left,"Left")
turtle.onkeypress(move_right,"Right")
turtle.onkeypress(fire_bullet,"space")


#MAIN GAME LOOP
while True:
    wn.update()
    for enemy in enemies:
        #Move the enemy
        x = enemy.xcor()
        x+= enemyspeed
        enemy.setx(x)

        #Move the enemy back and forth
        if enemy.xcor()>280:
            #Move all the enemies down
            for e in enemies:
                y = e.ycor()
                y-= 40
                e.sety(y)
            enemyspeed *= -1

        if enemy.xcor()<-280:
            for e in enemies:
                y = e.ycor()
                y-= 40
                e.sety(y)
            enemyspeed *= -1

        #Check for a collision 
        if isCollision(bullet,enemy):
            #Reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0,-400)
            #Reset the enemy
            x = random.randint(-200,200)
            y = random.randint(100,250)
            enemy.setposition(x,y)
            #Update the score
            score+= 10
            scorestring= "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring,False,align="left",font = ("Arial",14,"normal"))

        if isCollision(player,enemy):
            player.setposition(1500,1500)
            player.hideturtle()
            enemy.hideturtle()
            print ("Game Over\nFinal Score : ", score)
            break

    #Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    if bullet.ycor()>275:
        bullet.hideturtle()
        bulletstate = "ready"
