import ffmpy
import os
import subprocess
import queue
import  threading

def transfer_bit(queue_name):
    "Convert vedio"
    transfer_file = queue_name.get()
    print(transfer_file)
    try:
        # os.chdir('C:/Users/synox/mini_project1/') change to dirctionary including images
        subprocess.Popen("ffmpeg -i ./" + transfer_file + " -vcodec h264 -b:v 1048576 -s 720*480 -r 30 ./transcoded_video.mp4")
        # subprocess.call(["ffmpeg -y -i" +"/Makefile.mp4" + "- vcodec h264 - b:v 1048576 - s 720*480 - r 30" + "/transcoded_video.mp4"])
        print("All done")
    except:
        print('error')

def put_in_queue(queue_name,file_name):
    format_name = file_name + ".mp4"
    if (queue_name.full()== True):
        queue_name.get()
        queue_name.put(format_name)
    else:
        queue_name.put(format_name)

def ffmpeg_combine(queue_name):
    while (True):
        file_name = input("Plz input your the name of your media files:\n")
        put_in_queue(queue_name, file_name)
        transfer_bit(queue_name)

if __name__ == "__main__":
    q = queue.Queue()
    for i in range(5):
        t= threading.Thread(target=ffmpeg_combine(q))
        t.start()
    t.join()