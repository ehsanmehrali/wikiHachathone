import random
import  os
import pygame


def get_music_list():
    """Returns a list of music tracks addresses,compatible with all operating systems"""
    music_list = [
        os.path.join("music", "game-arcade-236133.mp3"),
        os.path.join("music", "game-arcade-medium-236110.mp3"),
        os.path.join("music", "gaming-music-8-bit-console-play-background-intro-theme-278382.mp3"),
        os.path.join("music", "game-8-bit-on-278083.mp3"),
        os.path.join("music", "8-bit-arcade-138828.mp3"),
        os.path.join("music", "9th-loop-227009.mp3"),
        os.path.join("music", "modern-inspiring-beats-beatgenesis-213694.mp3")
    ]
    return music_list


def play_random_music():
    """Selects a random music track(shuffel)"""
    musics = get_music_list()
    random_music = random.choice(musics)
    play_music(random_music, repeat=-1)


def play_music(sound_file, repeat = 0):
    """
    Initializes the pygame module and plays the music track.
    :param sound_file: A music file name(address)
    :param repeat: 0 by default or -1(Which repeats the music playback.)
    """
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play(repeat)
    # It acts as a callback function and if music is playing,
    # it waits until it ends before playing the next song.
    if repeat == 0:
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
