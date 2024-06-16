import sys
from time import sleep
import time

def print_lyrics():
    # Lista de tuplas con las líneas y sus respectivos retrasos por carácter
    lines = [
        ("Got the music in you, baby", 0.09),
         ("Tell me why", 0.08),
         ("Got the music in you, baby", 0.09),
         ("Tell me why", 0.08),
         ("You've been locked in here forever", 0.08),
         ("And you just can't say goodbye", 0.08),
         
         ("your lips , my lips ", 0.08),
         ("apocalypse", 0.08),
         ("your lips , my lips ", 0.08),
         ("apocalypse", 0.08),
          
       
    ]
    delays = [0.1, 1.2, 0.4, 2.1, 0.2, 6.5 , 1.1,  6.5 , 1.1 , 3 ]
    
    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()
           