"""The run script"""

from sequence_controller import *
from motor import *
from sequence import *

motor_x = Motor('xMotor', 31, 33, 10000)
motor_y = Motor('yMotor', 35, 37, 10000)
motor_z = Motor('zMotor', 28, 30, 80000)
SCONTROLLER = SequenceController(Sequence(), motor, 0)
SEQUENCE_READY = False


DURATION = input('Please define sleep duration in seconds:')

print('Ok, great. Next we will define a movement sequence made up of commands')

while not SEQUENCE_READY:
    COMMAND = input('Enter a command ( the amount of steps to be taken )')
    SCONTROLLER.sequence.enqueue(int(COMMAND))
    print('Queue now is: ', SCONTROLLER.sequence.listAll())
    DONE = input('Done with input phase? y/n     ')

    if DONE == 'y':
        SEQUENCE_READY = True

print('Starting moving through the sequence')
SCONTROLLER.work_sequence()
print('Done with Sequence')
