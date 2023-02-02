import glob
import subprocess

path = './source/before/*.mp4'
i = 1

flist = glob.glob(path)

cmd = R"C:\Users\tsune\OneDrive\ドキュメント\ffmpeg\bin\ffmpeg.exe"

for file in flist:
    filename = file.replace('./source/before\\', "")
    filename = filename.replace('.mp4', "")
    # ファイル名
    subprocess.run(cmd + " -i " + file + " ./source/after/" + filename + ".webm" ,shell=True)
    i += 1
