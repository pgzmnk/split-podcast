from pydub import AudioSegment
from pydub.playback import play


import logging

# Set up logging
l = logging.getLogger("pydub.converter")
l.setLevel(logging.DEBUG)
l.addHandler(logging.StreamHandler())

# Function to convert hours, minutes, seconds to milliseconds
hms_to_ms = lambda hours, min, sec: int(3600000 * hours + 60000 * min + 1000 * sec)

# Path to audio file
mp3_file_path = 'data/28_vacunas.mp3'

# Create audio object
song = AudioSegment.from_mp3(mp3_file_path)

# Create clip
clip = song[hms_to_ms(0,0,5):hms_to_ms(0,0,8)]

# Play last 10 seconds
last_5_seconds = song[-5000:]
play(last_5_seconds)

# boost volume by 6dB
play(song[:1000] + 6)

# Splice intro music
INTRO_MUSIC_START = hms_to_ms(0,0,42)
INTRO_MUSIC_END =  hms_to_ms(0,0,50)
intro_music = song[INTRO_MUSIC_START:INTRO_MUSIC_END]

# Splice section of audio
SECTION_1_START = hms_to_ms(0,3,30)
SECTION_1_END = hms_to_ms(0,4,2)
section_1 = song[SECTION_1_START:SECTION_1_END]
play(section_1)

# How long is this?
section_1.duration_seconds

# Play in reverse
play(section_1.reverse())


# Crossfade
clip_1 = intro_music.append(section_1, crossfade=1500)
clip_1_v2 = (intro_music + section_1)
play(clip_1_v2)

# Overlay
play((AudioSegment.silent(duration=1000) + section_1).overlay(intro_music.fade(to_gain=-100, start=1000, duration=6000)))


# Export
file_handle = clip_1.export("data/clip_1.mp3",
                           format="mp3",
                           bitrate="192k",
                           tags={"episode": "28", "artist": "JP, Bea"})

