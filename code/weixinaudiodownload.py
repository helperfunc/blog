# Version20200415 下载音频
# Version20200620 下载视频，音乐
# validated in python3

url = 'https://mp.weixin.qq.com/s?...' # 微信页面地址
downloadDir = '/Users/yourname/Downloads' #本地文件夹地址

import requests
import re
import os
import json

if __name__ == '__main__':
	prefix = 'https://res.wx.qq.com/voice/getvoice?mediaid='
	voiceUrlpattern = r'(?<=voice_encode_fileid=")([\s\S]*?)(?=</mpvoice>)'
	titlepattern = r'(?<=rich_media_title")([\s\S]*?)(?=</h2>)'
	
	# get from network tab in devtools
	videoprefix = 'https://mp.weixin.qq.com/mp/videoplayer?action=get_mp_video_play_url&preview=0&__biz=&mid=&idx=1&vid='
	videosuffix = '&uin=&key=&pass_ticket=&wxtoken=777&devicetype=&enterid=&appmsg_token=&x5=0&f=json'
	videoidpattern = r'(?<=data-mpvid=")([\s\S]*?)(?=")'

	musicprefix = 'https://mp.weixin.qq.com/mp/qqmusic?action=get_song_info&song_mid='
	musicsuffix = '&uin=&key=&pass_ticket=&wxtoken=777&devicetype=&clientversion=&__biz=%3D%3D&appmsg_token=&x5=0&f=json'
	musicidpattern = r'(?<=musicid=")([\s\S]*?)(?=albumurl=)'

	session_requests = requests.session()
	html = session_requests.get(url).text

	voiceUrlresult = re.findall(voiceUrlpattern, html)
	videoids = re.findall(videoidpattern, html)
	musicids_raw = re.findall(musicidpattern, html)
	
	title = re.findall(titlepattern, html)
	if len(title) > 0:
		title = title[0]
		title = title.replace('\n', '').replace(' ','')
		title = title.split('">')
		if len(title) > 0:
			if len(title) > 1:
				title = title[1]
			else:
				title = title[0]
		else:
			title = url[-10:]
	else:
		title = url[-10:]
	

	print(title)
	

	for i, elem in enumerate(videoids):
		videoUrlPost = videoprefix+elem+videosuffix
		r = session_requests.post(videoUrlPost)
		resultdict = r.json()
		if 'title' not in resultdict:
			continue
		videotitle = resultdict['title']
		if 'url_info' not in resultdict:
			continue
		videourls = resultdict['url_info']
		videourl = ''
		if len(videourls) > 0:
			if 'url' not in videourls:
				continue
			videourl = videourls[0]['url']
			if videourl:
				print('Downloading video: ' + videourl)
				myfile = requests.get(videourl)
				if myfile.status_code == 200:
					target_path = os.path.join(downloadDir, title+'_'+videotitle+str(i)+'.mp4')
					with open(target_path, 'wb') as f:
						f.write(myfile.content)
					print('Saved video to ' + target_path)
				else:
					print(myfile.status_code)

	for i, elem in enumerate(voiceUrlresult):
		t = elem.split('" ')
		if len(t) > 0:
			target = prefix + t[0]
			print('Downloading audio: ' + target)
			myfile = requests.get(target)
			if myfile.status_code == 200:
				target_path = os.path.join(downloadDir, title+str(i)+'.mp3')
				with open(target_path, 'wb') as f:
					f.write(myfile.content)
				print('Saved audio to ' + target_path)
			else:
				print(myfile.status_code)


	for i, elem in enumerate(musicids_raw):
		elem = elem[elem.find('mid="')+5:]
		elem = elem[:elem.find('"')]
		
		musicUrlPost = musicprefix+elem+musicsuffix
		r = session_requests.get(musicUrlPost)
		resultdict = r.json()
		if 'resp_data' not in resultdict:
			continue
		resultdict = json.loads(resultdict['resp_data'])
		if 'songlist' not in resultdict:
			continue
		songs = resultdict['songlist']
		if len(songs) > 0:
			song = songs[0]
			if 'song_play_url_standard' not in song:
				continue
			if 'song_title' not in song:
				continue
			songurl = song['song_play_url_standard']
			songtitle = song['song_title']
			if songurl:
				print('Downloading music: ' + songurl)
				headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
				myfile = requests.get(songurl, headers=headers)
				if myfile.status_code == 200:
					target_path = os.path.join(downloadDir, title+'_'+songtitle+str(i)+'.mp3')
					with open(target_path, 'wb') as f:
						f.write(myfile.content)
					print('Saved music to ' + target_path)
				else:
					print(myfile.status_code)
