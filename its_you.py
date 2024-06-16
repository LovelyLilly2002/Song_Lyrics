import sys
from time import sleep
import time

def print_lyrics():
    # Lista de tuplas con las líneas y sus respectivos retrasos por carácter
    lines = [
        ("So please ", 0.09 ),
        ("Don't break my heart", 0.05),
        ("Don't tear me apart", 0.09),
        ("I know how it starts", 0.08),
        ("Trust me, I've been broken before", 0.05),
        ("Don't break me again", 0.08),
        ("I am delicate", 0.12),
        ("Please don't break my heart", 0.07),
        ("Trust me, I've been broken before", 0.05) 
        ]
    delays = [0.2,0.2, 0.4 ,0.2,0.4 , 0.5 ,      0.4 , 0.5 , 0.9  ]
    
    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()
           
