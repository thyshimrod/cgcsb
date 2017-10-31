import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

prevx=-1
prevy=0
prevdistance=0
turn=10
first = True
boost = 1
# game loop
while True:
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]
   
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    a = x-next_checkpoint_x
    a=a*a
    b = y-next_checkpoint_y
    b=b*b
    distance = math.sqrt(a+b)
    print("Debug messages..." + str(distance) + "//" + str(next_checkpoint_dist) + "//" + str(next_checkpoint_angle) , file=sys.stderr)
    vitesse = 100
    if next_checkpoint_x == prevx:
        #if distance > prevdistance and turn < 5:
        if next_checkpoint_angle > 100 or next_checkpoint_angle < -100:
            vitesse = 0
            turn += 1
        else:
            if boost == 1 and next_checkpoint_dist > 6000 and next_checkpoint_angle <10 and next_checkpoint_angle > -10:
                vitesse = "BOOST"
                boost-=1
            elif next_checkpoint_dist < 1000:
                vitesse = 80
    
        
    print(str(next_checkpoint_x) + "//" + str(next_checkpoint_y),file=sys.stderr)
    prevdistance=distance
    prevx = next_checkpoint_x
    prevy = next_checkpoint_y
    # You have to output the target position
    # followed by the power (0 <= thrust <= 100)
    # i.e.: "x y thrust"
    print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " " + str(vitesse))