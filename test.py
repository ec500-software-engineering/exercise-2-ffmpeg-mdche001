import subprocess
import json
from pathlib import Path
from pytest import approx

def ffprobe(file: Path) -> dict:
    meta_json = subprocess.check_output(['ffprobe', '-v', 'warning', '-print_format',
                                         'json', '-show_streams', '-show_format', file],
                                        universal_newlines = True)
    return json.loads(meta_json)

def test_duration():

    orig_meta = ffprobe('Makefile.mp4')
    meta_480 = ffprobe('transcoded_video_480p.mp4')
    meta_720 = ffprobe('transcoded_video_720p.mp4')
    video_duration = float(orig_meta['streams'][0]['duration'])
    video_480_duration = float(meta_480['streams'][0]['duration'])
    video_720_duration = float(meta_720['streams'][0]['duration'])
    assert video_duration == approx(video_480_duration)
    assert video_duration == approx(video_720_duration)