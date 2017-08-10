import turtle
import random
turtle.bgcolor("AntiqueWhite")
turtle.tracer(1,0)
SIZE_X=950
SIZE_Y=510
turtle.setup(SIZE_X+20,SIZE_Y+20)
#size of the game
edge=turtle.clone()
edge.penup()
edge.goto(SIZE_X/2,SIZE_Y/2)
edge.pendown()
edge.goto(SIZE_X/2,-SIZE_Y/2)
edge.goto(-SIZE_X/2,-SIZE_Y/2)
edge.goto(-SIZE_X/2,SIZE_Y/2)
edge.goto(SIZE_X/2,SIZE_Y/2)
edge.penup()
edge.hideturtle()
#the edge place

turtle.penup()
SQUARE_SIZE = 20
START_LENGTH = 3#snake size
TIME_STEP = 100
pos_list = []
stamp_list = []
food_pos = []
food_stamp = []
turtle.color("AntiqueWhite4")
snake = turtle.clone()

snake.shape("circle")
turtle.hideturtle()
########################  snake shape




########################
for i in range (START_LENGTH):
    x_pos=snake.pos()[0]
    y_pos=snake.pos()[1]
    x_pos = x_pos + SQUARE_SIZE

    new_pos=(x_pos,y_pos)

    snake.goto(x_pos,y_pos)
    pos_list.append(new_pos)
    
    stamp1 = snake.stamp()
    stamp_list.append(stamp1)
    
UP_ARROW="Up"

LEFT_ARROW="Left"
DOWN_ARROW="Down"
RIGHT_ARROW="Right"

SPACEBAR="space"
#the arrows

UP=0
LEFT=2
DOWN=1
RIGHT=3

direction = UP

UP_EDGE = SIZE_Y/2
DOWN_EDGE = -SIZE_Y/2
RIGHT_EDGE = SIZE_X/2
LEFT_EDGE = -SIZE_X/2

#size of the edge

def up():
    global direction
    if direction != DOWN :
        direction=UP    
    print("you pressed the up key")

def down():
    global direction
    if direction != UP :
        direction=DOWN
    print("you pressed the down key")

def left():
    global direction
    if direction != RIGHT :
        direction=LEFT
    print("you pressed the left key")

def right():
    global direction
    if direction != LEFT :
        direction=RIGHT
    print("you pressed the right key")
# how to work the arrow
turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
#change the placess
turtle.listen()
my_pos = snake.pos()
x_pos=my_pos[0]
y_pos=my_pos[1]

turtle.register_shape("trash.gif")
food = turtle.clone()
food.shape("trash.gif")
#the food
    






food_pos = [(100,100)]
for this_food_pos in food_pos:
    food.goto(this_food_pos)
    newstamp=food.stamp()
    food_stamp.append(newstamp)
food.hideturtle()


#food place


def make_food():
   


    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-1

    food_x=random.randint(min_x,max_x)*SQUARE_SIZE
    food_y=random.randint(min_y,max_y)*SQUARE_SIZE

    food.goto(food_x,food_y)
    food_turtle_pos=(food_x,food_y)
    food_pos.append(food_turtle_pos)
    newstamp1=food.stamp()
    
    food_stamp.append(newstamp1)
    food_stamp!=snake.pos()
    
#food appers randomly
    
score=turtle.clone()  
c=0
score.goto(-448,230)
score.color ("AntiqueWhite3")



def move_snake():
    my_pos = snake.pos()
    x_pos=my_pos[0]
    y_pos=my_pos[1]




    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("you moved right!")

    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("you moved left!")

    elif direction==UP:
        snake.goto(x_pos, SQUARE_SIZE + y_pos)
        print("you moved up!")

    elif direction==DOWN:
        snake.goto(x_pos ,y_pos - SQUARE_SIZE )
        print("you moved down!")
    #####################the move of the snake
    my_pos=snake.pos()
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    global c,food_stamp,food_pos
    ## how the snake stamps disapper
    
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos())
        food.clearstamp(food_stamp[food_ind])
        food_pos.pop(food_ind)
        food_stamp.pop(food_ind)
        print("you have eaten the food")
        make_food()
    ##how to eat food
        c = c + 1
        score.clear()
        score.write("score = "+ str (c))
        

        
        
    else :
        old_stamp = stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)
    
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
#clear stamp
    if new_x_pos >= RIGHT_EDGE:
        print("you hit the right edge! game over!")
        quit()
    
    elif new_x_pos <= LEFT_EDGE:
        print("you hit the left edge! game over!")
        quit()

    elif new_y_pos >= UP_EDGE:
        print("you hit the up edge! game over!")
        quit()

    elif new_y_pos <= DOWN_EDGE:
        print("you hit the down edge! game over!")
        quit()

    if pos_list[-1] in pos_list[0:-1]:
        
        print("you ate yourself")
        quit()
##when you hit edges you die
    turtle.ontimer(move_snake,TIME_STEP)

move_snake()




