#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor
from pybricks.parameters import Port, Button, Color, ImageFile, SoundFile
from pybricks.tools import wait
from pybricks.robotics import DriveBase

# Play a sound.
brick.sound.beep(500,200)
brick.sound.beep(600,300)

# details
# The top of the letter is not by the little motor, to go away -, to come + 
# the next letter is 50 degree away
# the letters are 100 degree wide
# the paper goes - to the roll and + away

# A, B, C, D, E, F, G, H, I, J, L, M, N, O, P, Q, S, T, U,

# Initialize two motors with default settings on Port B and Port C.
left_motor = Motor(Port.A)
right_motor = Motor(Port.C)
little_motor = Motor(Port.B)

# Letter "A"
def printLetterA():
    little_motor.run_angle(100, 180)
    right_motor.run_angle(100, 90)
    little_motor.run_angle(-100, 360)
    left_motor.run_angle(-100, 100)
    little_motor.run_angle(100, 360)
    right_motor.run_angle(-100, 90)
    little_motor.run_angle(-100, 180)
    right_motor.run_angle(100, 90)
    left_motor.run_angle(100, 100)
    right_motor.run_angle(-100, 90)
    left_motor.run_angle(-200, 200)

# Letter "B"
def printLetterB():
   # the right motor turns the pencil down to write
   right_motor.run_angle(-100, 90)
   # the little motor turns the pencil to make the first line
   little_motor.run_angle(-100, 180)
   # the left motor turns the paper to make the line above
   left_motor.run_angle(-200, 100)
   # the little motor turns the pencil 
   little_motor.run_angle(100, 180)
   # the right motor turns the pencil up to not write
   right_motor.run_angle(100, 90)
   # the left motor turns the paper 
   left_motor.run_angle(200, 100)
   #the right motor turns the pencil down to write
   right_motor.run_angle(-100, 90)
   # the left motor turns the paper to continue the letter and to write the line in the middle
   left_motor.run_angle(-200, 100)
   # the little motor turns the pencil 
   little_motor.run_angle(100, 180)
   #the left motor turns the paper to continue the letter and to write the line under
   left_motor.run_angle(200, 100)
   # the little motor turns the pencil to finish the letter
   little_motor.run_angle(-100, 180)
   # the right motor turns the pencil up to not write
   right_motor.run_angle(100, 90)
   # the left motor turns the paper to make the paper continue
   left_motor.run_angle(-200, 150)


# Letter "C"
def printLetterC():
    #the left motor takes the paper to the start
    left_motor.run_angle(-200, 100)
    #little motor goes from his base to the top of the paper
    little_motor.run_angle(-100, 180)
    #the right motor turns the pencil down to write
    right_motor.run_angle(200,90)
    #the left motor takes the paper to the start
    left_motor.run_angle(200, 100)
    #the little motor makes a line to make the letter
    little_motor.run_angle(100, 360)
    #the left motor turns the paper to finish the letter
    left_motor.run_angle(-200, 70)
    #the right motor turns the pencil up to finish writing
    right_motor.run_angle(-200, 90)
    # the little motor takes the pencil to the base
    little_motor.run_angle(-100, 180)
    #the left motor turns the paper continue
    left_motor.run_angle(-200, 50)

# Letter "D"
def printLetterD():
   #the right motor turns the pencil down to write
   right_motor.run_angle(-100, 90)
   # the little motor turns the pencil to make the first line
   little_motor.run_angle(-100, 180)
   # the left motor turns the paper to make the line above
   left_motor.run_angle(-200, 100)
   # the little motor turns the pencil to make the secound line
   little_motor.run_angle(100, 360)
   # the left motor turns the paper to write the line under
   left_motor.run_angle(200, 100)
   # the little motor turns the pencil to make the last line to the middle
   little_motor.run_angle(-100, 180)
   # the right motor turns the pencil up
   right_motor.run_angle(100, 90)
   # the left motor makes the paper the paper continue
   left_motor.run_angle(-200, 150)
  
# Letter "E"
def printLetterE():
    #the little motor goes from his base to the top of the paper
    little_motor.run_angle(-100, 180)
    # the left motor turns the paper to start the letter
    left_motor.run_angle(-200, 100)
    # the right motor turns the pencil down to write
    right_motor.run_angle(-100, 90)
    # the left motor turns the paper to make the first horizontal line
    left_motor.run_angle(200, 100)
    #the little motor turns the pencil
    little_motor.run_angle(100, 180)
    # the right motor turns the pencil up to do not make a fat line
    right_motor.run_angle(100, 90)
    #the left motor turns the paper to go for the line
    left_motor.run_angle(-200, 100)
    #the right motor turns the pencil on the paper to write
    right_motor.run_angle(-100, 90)
    #the left motor turns the paper back to make the letter
    left_motor.run_angle(200, 100)
    #the little motor turns the pencil
    little_motor.run_angle(100, 180)
    #the left motor turns the paper to finish the letter
    left_motor.run_angle(-200, 100)
    #the right motor turns the pencil up to not write
    right_motor.run_angle(100, 90)
    # the little motor turns the pencil to his base
    little_motor.run_angle(-100, 180)
    #the left motor turns the paper continue
    left_motor.run_angle(-200, 50)

# Letter "F"
def printLetterF():
   # little motor goes from the his base to the bottom of the paper
   little_motor.run_angle(100, 180)
   # right motor goes down
   right_motor.run_angle(-100, 90)
   #right motor goes to the middle
   little_motor.run_angle(-100, 360)
   #left motor goes 100 degries left
   left_motor.run_angle(-200, 100)
   #right motor pull up the pencil
   right_motor.run_angle(100, 90)
   #left motor bring the pencil to the middle of the paper
   little_motor.run_angle(100, 180)
   left_motor.run_angle(200, 25)
   #right motor bring the pencil down
   right_motor.run_angle(-100, 90)
   #left motor 
   left_motor.run_angle(200, 75)
   right_motor.run_angle(200, 90)
   left_motor.run_angle(-200, 100)

# Letter "G"
def printLetterG():
   #left motor go 100 degres left 
   left_motor.run_angle(-200, 150)
   #pencil go to the top of the paper
   little_motor.run_angle(-100, 180)
   #pencil go down
   right_motor.run_angle(100, 90)
   #pencil write a line left
   left_motor.run_angle(200, 150)
   #pencil make a wertikal line
   little_motor.run_angle(100, 360)
   #pencil go to the right
   left_motor.run_angle(-200, 150)
   #pencil go in the middle
   little_motor.run_angle(-100, 180)
   #pencil make the G complet
   left_motor.run_angle(200, 50)
   #pencil go up
   right_motor.run_angle(-100, 90)
   #pencil go to the next leter
   left_motor.run_angle(-200, 150)

# Letter "H"
def printLetterH():
   # the little motor goes from his base in the middle to the top of the paper
   little_motor.run_angle(-100, 180)
   #the right motor takes the pencil down to write
   right_motor.run_angle(-100, 90)
   # the little motor makes the first line
   little_motor.run_angle(100, 360)
   # the right motor takes the pencil up
   right_motor.run_angle(100, 90)
   # the little motor goes in the middle to write the horizontal line
   little_motor.run_angle(-100, 180)
   # the right motor turns the pencil down to write
   right_motor.run_angle(-100, 90)
   # the left motor turns the paper to make the horizontal line
   left_motor.run_angle(-200, 100)
   # the right motor turns the pencil down to write
   right_motor.run_angle(100, 90)
   # the little motor turns the pencil to the top of the paper to make a line
   little_motor.run_angle(-100, 180)
   # the right motor turns the pencil up to not write
   right_motor.run_angle(-100, 90)
   # the little motor turns the pencil to the top of the paper to make the last line
   little_motor.run_angle(100, 360)
   # the right motor turns the pencil down 
   right_motor.run_angle(100, 90)
   #the little motor makes the last line
   little_motor.run_angle(-100, 180)
   # the left motor makes the paper continue#
   left_motor.run_angle(-200, 50)

# Letter "I"
def printLetterI():
   #little motor goes from his base to the top of the paper
   little_motor.run_angle(-100, 180)
   # the right motor turns the pencil down to write
   right_motor.run_angle(-100, 90)
   # the little motor turns the pencil from one headend to the other
   little_motor.run_angle(100, 360)
   # the right motor turns the pencil up to not write while going to the base
   right_motor.run_angle(100, 90)
   # the little motor turns the pencil to the base
   little_motor.run_angle(100, 180)
   # the left motor turns the paper continue
   left_motor.run_angle(-200, 50)

# Letter "J"
def printLetterJ():
   #go to the topp of the letter
   little_motor.run_angle(-100, 180)
   #rhe right motor turns the pencil down
   right_motor.run_angle(-100, 100)
   #make the topline of the "J" 
   left_motor.run_angle(-200, 100)
   #go down to the ground
   little_motor.run_angle(100, 360)
   #make the groundline
   left_motor.run_angle(200, 100)
   #make the last line
   little_motor.run_angle(-100, 130)
   #put the pencil up
   right_motor.run_angle(100, 100)
   #go a littlebit up to the middle
   little_motor.run_angle(-100, 50)
   #go to the next letter
   left_motor.run_angle(-200, 150)

# Letter "K"
def printLetterK():
   #go to the top
   little_motor.run_angle(-100, 180)
   #put the pencil down
   right_motor.run_angle(-100, 100)
   #go to the bottom
   little_motor.run_angle(100, 360)
   #put the pencil up
   right_motor.run_angle(100, 100)
   #go to the middle
   little_motor.run_angle(-100, 180)
   #put the pencil down
   right_motor.run_angle(-100, 100)
   #make the slanted line
   little_motor.run_angle(-100, 180, wait=False)
   left_motor.run_angle(-100, 180)
   #wait 300 ms
   wait(300)
   #put the pencil up
   right_motor.run_angle(100, 100)
   #return the pencil to the middle
   little_motor.run_angle(100, 180, wait=False)
   left_motor.run_angle(100, 180)
   #wait 300 ms
   wait(300)
   #put the pencil down
   right_motor.run_angle(-100, 100)
   #make the slanted line
   little_motor.run_angle(100, 180, wait=False)
   left_motor.run_angle(-100, 180)
   #wait 300 ms
   wait(300)
   #put the pencil up
   right_motor.run_angle(100, 100)
   #return the pencil to the middle
   little_motor.run_angle(-100, 180, wait=False)
   left_motor.run_angle(100, 180)
   #wait 300 ms
   wait(300)
   left_motor.run_angle(-100, 200)

# Letter "L"
def printLetterL():
   #little motor goes from his base in the middle to the top of the paper
   little_motor.run_angle(-100, 180)
   # the right motor turns the pencil down to write
   right_motor.run_angle(100, 90)
   # the little motor turns the pencil from one headend to the other
   little_motor.run_angle(100, 360)
   # the left motor makes the L complete
   left_motor.run_angle(-100, 100)
   # the right motor turns the pencil up to not write while going to the base
   right_motor.run_angle(-100, 90)
   # the little motor turns the pencil to the base
   little_motor.run_angle(-100, 180)
   # the left motor turns the paper continue
   left_motor.run_angle(-200, 50)
 
# Letter "M"
def printLetterM():
   # the little motor goes from his base to the bottom of the paper
   little_motor.run_angle(100, 180)
   # the right motor turns the pencil down
   right_motor.run_angle(-100, 90)
   # the little motor turns the pencil to the other side of the paper
   little_motor.run_angle(-100, 360)
   # the left motor turns the pencil to make the frist horizontal line
   left_motor.run_angle(-100, 100)
   # the little motor turns the pencil to make the middel line
   little_motor.run_angle(100, 180)
   # the right motor turns the pencil up
   right_motor.run_angle(100, 90)
   # the little motor returns the pencil to the top
   little_motor.run_angle(-100, 180)
   # the right motor turns the pencil down
   right_motor.run_angle(-100, 90)
   #the left motor turns the paper to make the secound horizontal line
   left_motor.run_angle(-100, 100)
   # the little motor turns the pencil to make the last line
   little_motor.run_angle(100, 360)
   # the right motor turns the pencil up
   right_motor.run_angle(100, 90)
   # the little motor returns to his base
   little_motor.run_angle(-100, 180)
   # the left motor makes the paper continue
   left_motor.run_angle(-100, 50)

# Letter "N"
def printLetterN():
   # the little motor goes from his base to the bottom of the paper
   little_motor.run_angle(100, 180)
   # the right motor turns the pencil down 
   right_motor.run_angle(-100, 90)
   # the little motor turns the pencil to make the first line
   little_motor.run_angle(100, 360)
   # the left motor turns the paper to make the line under
   left_motor.run_angle(-100, 100)
   # the little motor turns the pencil to make the last line
   little_motor.run_angle(-100, 360)
   # the right motor turns the pencil up
   right_motor.run_angle(100, 90)
   # the left motor makes the paper continue
   left_motor.run_angle(-200, 50)

# Letter "O"
def printLetterO():
   # the right motor turns the pencil down to write
   right_motor.run_angle(-100, 90)
   # the little motor turns the pencil to the top of the paper
   little_motor.run_angle(-100, 120)
   # the left motor turns the paper to make the line above
   left_motor.run_angle(-100, 120)
   # the little motor turns the pencil to make a line
   little_motor.run_angle(100, 240)
   # the left motor turns the paper to make the line under
   left_motor.run_angle(100, 120)
   # the little motor turns the pencil to make the last line
   little_motor.run_angle(-100, 120)
   # the right motor turns the pencil up
   right_motor.run_angle(100, 90)
   # the left motor makes the paper contiue
   left_motor.run_angle(-200, 150)

# Letter "P"
def printLetterP(): 
   #pencil go to the botton
   little_motor.run_angle(100, 180)
   #pencil go down
   right_motor.run_angle(200, 90)
   #the pencil mke a lin to the top
   little_motor.run_angle(-100, 360)
   #the pencil go right
   left_motor.run_angle(-100, 100)
   #pencil go to th middle
   little_motor.run_angle(100, 180)
   #pencil run left
   left_motor.run_angle(100, 100)
   #pencil go up
   right_motor.run_angle(-200, 90)
   #pencil go to the next letter
   left_motor.run_angle(100, 150)
   
# Letter "Q"
def printLetterQ():
   #the right motor turns the pencil down to write
   right_motor.run_angle(-100, 90)
   # the little motor turns the pencil to make the first line
   little_motor.run_angle(-100, 180)
   # the left motor turns the paper to make the line above
   left_motor.run_angle(-100, 90)
   # the little motor turns the pencil to make the secound line
   little_motor.run_angle(100, 300)
   #the right motor turns the pencil up
   right_motor.run_angle(100, 90)
   # the left motor turns the paper 
   left_motor.run_angle(-200, 50)
   # the right motor turns the pencil down to write
   right_motor.run_angle(-100, 90)
   # the left motor turns the paper to write the little line
   left_motor.run_angle(200, 75)
   # the right motor turns the pencil up
   right_motor.run_angle(100, 90)
   # the left motor turns the paper forwards to contiue
   left_motor.run_angle(-200, 90)
   # the right motor turns the pencil down to write
   right_motor.run_angle(-100, 90)
   # the little motor turns the pencil to go to the bottom
   little_motor.run_angle(100, 50)
   # the left motor turns the paper to write the line under
   left_motor.run_angle(100, 90)
   # the little motor turns the pencil to make the last line to the middle
   little_motor.run_angle(-100, 180)
   # the right motor turns the pencil up
   right_motor.run_angle(100, 90)
   # the left motor makes the paper the paper continue
   left_motor.run_angle(-200, 150)
  
# Letter "S"
def printLetterS():
   #the little motor goes from his base in the middle to the top of the paper
   little_motor.run_angle(-100, 180)
   #the left motor turns the paper forwards to the start
   left_motor.run_angle(-200, 100)
   # the right motor turns the pencil down to write
   right_motor.run_angle(-100, 90)
   # the left motor turns the paper to make the first horizontal line
   left_motor.run_angle(200, 100)
   # the little motor turns the pencil to write the first  line
   little_motor.run_angle(100, 180)
   # the left motor turns the paper to make the secound horizontal line
   left_motor.run_angle(-200, 100)
   # the little motor turns the pencil to make the secound line 
   little_motor.run_angle(100, 180)
   # the left motor turns the paper to make the last line
   left_motor.run_angle(200, 100)
   # the right motor turns the pencil up to not write
   right_motor.run_angle(100, 90)
   # the little motor returns to his base in the middle
   little_motor.run_angle(-100, 180)
   # the left motor makes the paper continue 
   left_motor.run_angle(-200, 150)

# Letter "T"
def printLetterT():
   # the little motor goes from his base in the middle to the top of the paper
   little_motor.run_angle(-100, 180)
   # the right motor turns the pencil down to write
   right_motor.run_angle(-100, 90)
   # the left motor turns the paper to write the line above
   left_motor.run_angle(-200, 100)
   # the right motor turns the pencil up to not write
   right_motor.run_angle(100, 90)
   # the left motor turns the paper to come to the middle of the letter
   left_motor.run_angle(200, 50)
   # the right motor turns the pencil down to write
   right_motor.run_angle(-100, 90)
   # the little motor turns the pencil to the other side of the page to write the middle-line
   little_motor.run_angle(100, 360)
   # the right motor turns the pencil up to not write
   right_motor.run_angle(100, 90)
   # the little motor returns to his base in the middle
   little_motor.run_angle(-100, 180)
   # the left motor makes the paper continue
   left_motor.run_angle(-200, 100)

# Letter "U"
def printLetterU():
   # the little motor goes from his base to the top of the paper
   little_motor.run_angle(-100, 180)
   # the right motor turns the pencil down to write
   right_motor.run_angle(-100, 90)
   # the little motor turns the pencil to the other side of the paper to write the one line
   little_motor.run_angle(100, 360)
   # the left motor turns the paper to make the horizontal line
   left_motor.run_angle(-200, 100)
   # the little motor turns the pencil to the other side of the paper to write the secound line
   little_motor.run_angle(-100, 360)
   # the right motor turns the pencil up
   right_motor.run_angle(100, 90)
   # the little motor turns to his base
   little_motor.run_angle(100, 180)
   # the left motor makes the paper continue
   left_motor.run_angle(-200, 50)  

#


# Insert your Letters here:
printLetterT()
printLetterE()
printLetterS()
printLetterT()

# now you have the word "HASE"

brick.sound.beep(400,200)
brick.sound.beep(300,300)