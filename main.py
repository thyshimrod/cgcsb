import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

prevx=0
prevy=0
prevchkx=-1
prevchkx=-1
prevdistance=0
turn=10
first = True
boost = 1
# game loop
while True:
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]
    bX = next_checkpoint_x
    bY = next_checkpoint_y

    if prevx != 0:
        reachX = (x - prevx)
        reachY = (y - prevy)
        length = math.sqrt(reachX * reachX + reachY * reachY)
        if length != 0:
            targetX = x +int(reachX / length * next_checkpoint_dist)
            targetY = y+ int(reachY/ length * next_checkpoint_dist)
            bX = int(next_checkpoint_x + 0.5*( next_checkpoint_x - targetX))
            bY = int(next_checkpoint_y + 0.5*( next_checkpoint_y - targetY))

    vitesse = 100
    if next_checkpoint_x == prevchkx:
        if next_checkpoint_angle > 110 or next_checkpoint_angle < -110 and next_checkpoint_dist > 2000:
            vitesse = 0
            turn += 1
        else:
            if boost == 1 and next_checkpoint_dist > 6000 and next_checkpoint_angle <10 and next_checkpoint_angle > -10:
                vitesse = "BOOST"
                boost-=1
            elif next_checkpoint_dist < 1000:
                vitesse = 80


    prevx = x
    prevy = y

    prevchkx = next_checkpoint_x
    prevchky = next_checkpoint_y
    print(str(bX) + " " + str(bY) + " " + str(vitesse))
    #print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " " + str(vitesse))
