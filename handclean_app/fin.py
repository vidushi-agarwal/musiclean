from PIL import Image, ImageFont, ImageDraw
import re
import json
import requests
from django.conf import settings
import os


class lyric_class:
    def __init__(self, artist,song_title):
        self.artist = artist
        self.song_title=song_title

    def text_wrap(self,text, font, max_width):
	    lines = []
	    # If the width of the text is smaller than image width
	    # we don't need to split it, just add it to the lines array
	    # and return
	    if font.getsize(text)[0] <= max_width:
	        lines.append(text) 
	    else:
	        # split the line by spaces to get words
	        words = text.split(' ')  
	        i = 0
	        # append every word to a line while its width is shorter than image width
	        while i < len(words):
	            line = ''         
	            while i < len(words) and font.getsize(line + words[i])[0] <= max_width:                
	                line = line + words[i] + " "
	                i += 1
	            if not line:
	                line = words[i]
	                i += 1
	            # when the line gets longer than the max width do not append the word, 
	            # add the line to the lines array
	            lines.append(line)    
	    return lines

    def img_wrt(self, text_arr, song_title, artist):
        font_hin = ImageFont.truetype(settings.BASE_DIR + '/handclean_app/static/handclean_app/fonts/Gargi.ttf',12) #absolute path
        font_eng_bd=ImageFont.truetype(settings.BASE_DIR + '/handclean_app/static/handclean_app/fonts/DejaVuSans-Bold.ttf',10) #absolute path
        font_eng_bd_title=ImageFont.truetype(settings.BASE_DIR + '/handclean_app/static/handclean_app/fonts/DejaVuSans-Bold.ttf',25) #absolute path
        font_eng=ImageFont.truetype(settings.BASE_DIR + '/handclean_app/static/handclean_app/fonts/DejaVuSans.ttf',12) #absolute path
        text_hin = "नित्य"
        source_img = Image.open(settings.BASE_DIR + '/handclean_app/static/handclean_app/images/handwash.png') #absolute path
        draw = ImageDraw.Draw(source_img)
        x = 30
        y = 320
        ctr = 0
        box_x = 200
        line_height = font_eng.getsize('hg')[1]
        for i in range(4):
            for j in range(3):
                print(text_arr[ctr])
                lines = self.text_wrap(text_arr[ctr], font_eng, box_x - 10)
                y1 = y
                for line in lines:
                    draw.text((x, y1), line, fill=(0, 0, 0), font=font_eng)
                    y1 = y1 + line_height
                x += box_x + 30
                ctr += 1
            x = 30
            y = y + 170

        y = 20
        text = "Wash your hands with '" + self.song_title.title() + "'";
        lines = self.text_wrap(text, font_eng_bd_title, box_x * 2+50)
        for line in lines:
            draw.text((x, y), line, fill=(0, 0, 0), font=font_eng_bd_title)
            y += line_height + 30
        source_img.save(settings.BASE_DIR + '/handclean_app/static/handclean_app/images/a.png') #absolute path



    def parse_sen(self,str1):
        str_txt="";
        i=0
        while(i<len(str1)):
            if(str1[i]==' '):
                while(i<len(str1) and str1[i]==' '):
                    i+=1
                if(i<len(str1)):
                    str_txt+='-'
            if(i<len(str1)):
                str_txt=str_txt+str1[i];
                i+=1
        return(str_txt)

    def get_lyrics(self):
        artist = self.artist.lower()
        song_title = self.song_title.lower()
        artist=self.parse_sen(artist)
        song_title = self.parse_sen(song_title)# with open(os.path.join(settings.BASE_DIR, 'handwash_app/myauth.json')) as json_file: #absolute path
        with open(settings.BASE_DIR + '/handclean_app/static/handclean_app/myauth.json') as json_file:
            data = json.load(json_file)
            apikey = data["authkey"]
        r=requests.get("https://api.musixmatch.com/ws/1.1/matcher.lyrics.get?q_track="+song_title+"&q_artist="+artist+"&apikey="+apikey)
        
        try:
            # r is of type response            
            packages_json = r.json()  # converts into json  
            if (packages_json['message']['header']['status_code'] == 404):
                return packages_json['message']['header']['status_code']
                       
            text = packages_json['message']['body']['lyrics']['lyrics_body']
                
            
            str1=""
            text_arr=[]
            c=0
            i=0
            while( i <len(text)):
            	while(text[i]=='\n'):
            		i+=1
            	str1+=text[i]
            	i+=1
            	if(text[i]=='\n'):
            		text_arr.append(str1)
            		str1=""
            		c+=1
            	if(c==12):
            		break
            print(text_arr)
            self.img_wrt(text_arr,song_title,artist)
            return text_arr
        except Exception as e:
            return "Exception occurred \t" +str(e)


