import pygame.mixer
import time

pygame.mixer.init()
pygame.mixer.music.load('kassen2.mp3')
pygame.mixer.music.play(2)

#pygame.mixer.music.pause()
#pygame.mixer.music.unpause
#pygame.mixer.music.set_volume(0.8)
#pygame.mixer.music.queue('test2.mp3')


time.sleep(200)
pygame.mixer.music.stop()
