import json
import os
import time

from pydub import AudioSegment
from pydub.playback import play


OUTPUT_DIR = 'split_audio_out'


#with open('syncmap_web.json', 'r') as fp:
with open('syncmap.json', 'r') as fp:
    syncmap = json.load(fp)

for fragment in syncmap['fragments']:
    id_ = fragment['id']
    lines = fragment['lines']
    text = '\n'.join(lines)

    audio_file = os.path.join(OUTPUT_DIR, f'{id_}.mp3')

    print(text)

    # FIXME: Having trouble getting audio to play in ubuntu - wsl.
    #        For now, just printing file name and manually playing audio.
    print(audio_file)

    # audio = AudioSegment.from_mp3(audio_file)
    # play(audio)

    # time.sleep(0.2)
    print()
