from pydub import AudioSegment
import os

files_path = r'D:/dirname'
file_name = r'filename'
splitInMin = 0.92

splitInMiliSec = int(splitInMin * 60 * 1000) #55 seconds

'''
startMin = 9
startSec = 50

endMin = 13
endSec = 30


# Time to miliseconds
startTime = startMin*60*1000+startSec*1000
endTime = endMin*60*1000+endSec*1000
'''

# Opening file and extracting segment
song = AudioSegment.from_mp3(os.path.join(files_path,file_name)+'.mp3' )
total_milis = len(song)

print(total_milis)

buffer = 0
if total_milis % splitInMiliSec != 0:
    buffer = 1
total_segs = total_milis // splitInMiliSec + buffer
print(buffer)
print(total_segs)
offset = 10
for i in range(total_segs):
    startTime = i * splitInMiliSec
    if startTime != 0:
        startTime -= offset
    endTime = (i + 1) * splitInMiliSec
    print((startTime, endTime))
    if endTime > total_milis - 1:
        endTime = total_milis - 1
    extract = song[startTime:endTime]
    print(i)
    print('extracting ' + str(startTime) + ': ' + str(endTime))
    # Saving
    extract.export( os.path.join(files_path, file_name + str(i) +'-extract.mp3'), format="mp3")
    #break
