# NOTE: pydub might have a simpler interface than using ffmpeg directly

import json
import os

import ffmpeg


OUTPUT_DIR = 'split_audio_out'
# INPUT_AUDIO_FILE = os.path.join('data', 'cadiz_ch_1_audio.mp3')
INPUT_AUDIO_FILE = os.path.join('data', 'cadiz_ch_1_audio_small.mp3')


if not os.path.isdir(OUTPUT_DIR):
    os.mkdir(OUTPUT_DIR)

# with open('syncmap_web.json', 'r') as fp:
with open('syncmap.json', 'r') as fp:
    syncmap = json.load(fp)

mp3 = ffmpeg.input(INPUT_AUDIO_FILE)

for fragment in syncmap['fragments']:
    start = float(fragment['begin'])
    end = float(fragment['end'])
    id_ = fragment['id']
    lines = fragment['lines']

    output_file = os.path.join(OUTPUT_DIR, f'{id_}.mp3')

    mp3.audio.filter('atrim', start=start, end=end).output(output_file).run(overwrite_output=True)
