import pygame
import pygame.midi
from time import sleep

import math
import sys
import time

import scrollphat

i = 0
buf = [0] * 11
scrollphat.set_brightness(20)


instrument = 0
note = 20
volume = 127



pygame.midi.init()

for id in range(pygame.midi.get_count()):
  print pygame.midi.get_device_info(id)

port = 0
midiOutput = pygame.midi.Output(port, 0)
midiOutput.set_instrument(instrument)
for note in range(0,127):
  midiOutput.note_on(note,volume)

while True:
    try:
        for x in range(0, 11):
            y = (math.sin((i + (x * note)) / 10.0) + 1) # Produces range from 0$
            y *= 2.5 # Scale to 0 to 5
            buf[x] = 1 << int(y)

        scrollphat.set_buffer(buf)
        scrollphat.update()

        time.sleep(0.005)

        i += 1
    except KeyboardInterrupt:
        scrollphat.clear()
        sys.exit(-1)
