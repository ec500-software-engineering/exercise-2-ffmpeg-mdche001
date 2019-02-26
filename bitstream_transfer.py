import os
import subprocess
import queue
import asyncio
import pytest
import time

async def transfer_bit480(queue_name):
    "Convert vedio"
    transfer_file = queue_name.get()
    # print(transfer_file)
    # os.chdir('C:/Users/synox/mini_project1/') change to dirctionary including images
    # oppo = ['ffmpeg -i' + transfer_file + '-r 30 -s hd480 -b:v 1024k -loglevel quiet' + t./transcoded_video.mp4]
    subprocess.Popen('ffmpeg -i ./' + transfer_file + ' -r 30 -s hd480 -b:v 1024k ./transcoded_video_480p.mp4')
    # subprocess.Popen("ffmpeg -i ./" + transfer_file + " -vcodec h264 -b:v 1048576 -s 720*480 -r 30 ./transcoded_video.mp4")
    print("--------------480p All done")
    return "transcoded_video_480p"


async def transfer_bit720(queue_name):
    "Convert vedio"
    transfer_file = queue_name.get()
    # print(transfer_file)

    subprocess.Popen('ffmpeg -i ./' + transfer_file + ' -r 30 -s hd720 -b:v 1024k ./transcoded_video_720p.mp4')
    print("-------------720p All done")
    return "transcoded_video_720p"


async def put_in_queue(queue_name,file_name):
    format_name = file_name + ".mp4"
    if (queue_name.full()== True):
        queue_name.get()
        queue_name.put(format_name)
    else:
        queue_name.put(format_name)


if __name__ == "__main__":
    start_time = time.clock()
    q = queue.Queue()

    file_name = input("Plz input your the name of your media files:\n")
    if (file_name):
        loop = asyncio.get_event_loop()
        task = [asyncio.ensure_future(put_in_queue(q, file_name)),asyncio.ensure_future(transfer_bit480(q)), asyncio.ensure_future(transfer_bit720(q))]
        loop.run_until_complete(asyncio.wait(task))

    files = os.listdir()
    for file in files:
        if(os.path.basename(os.path.realpath(__file__)) == "ranscoded_video_480p.mp4"):
            file_name1 == os.path.basename(os.path.realpath(__file__))
        elif(os.path.basename(os.path.realpath(__file__)) == "ranscoded_video_720p.mp4"):
            file_name2 == os.path.basename(os.path.realpath(__file__))


    assert filename1 == pytest.approx("ranscoded_video_480p.mp4")
    assert filename2 == pytest.approx("ranscoded_video_720p.mp4")
    print("---transfermation successful!--------")
    duration = time.clock() - start_time
    print("Total_running time is:", duration)