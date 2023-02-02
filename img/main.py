import glob
import os
import subprocess

path = './source/before/*.jpg'
i = 1

flist = glob.glob(path)

cmd = R"C:\Users\tsune\OneDrive\ドキュメント\ffmpeg\bin\ffmpeg.exe"

for file in flist:
    filename = file.replace('./source/before\\', "")
    filename = filename.replace('.jpg', "")
    subprocess.run(cmd + " -i " + file + " -crf 18 ./source/after/" + filename + ".webp" ,shell=True)
    i += 1
