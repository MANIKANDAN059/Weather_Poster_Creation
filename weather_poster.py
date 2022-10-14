import json
import requests
from PIL import Image, ImageFont, ImageDraw
from datetime import datetime

api_key="Your API key"
city_list=["Coimbatore","Chennai","Cochin","Ooty","Madurai"]
position=[305,430,560,695,825]

my_image = Image.open("condition.jpeg")
draw = ImageDraw.Draw(my_image)
now = datetime.now()

fonts = ImageFont.truetype('winter.ttf', 100)
text = "Weather Condition"
color = (255,215,0)
draw.text((260,40), text, color, font=fonts)

fonts = ImageFont.truetype('winter.ttf', 50)
content = now.strftime("%A  - %B %d, %Y")
color = (255,255,255)
draw.text((330,150), content, color, font=fonts)

index=0
for city in city_list:
    my_url="http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(city,api_key)
    response=requests.get(my_url)
    data=json.loads(response.text)

    fonts = ImageFont.truetype('winter.ttf', 65)
    color = (0,0,205)
    draw.text((172,position[index]), city, color, font=fonts)

    fonts = ImageFont.truetype('winter.ttf', 55)
    content =(str(data["main"]["temp"])+'\u00b0')
    color = (255,255,255)
    draw.text((640,position[index]), content, color, font=fonts)

    fonts = ImageFont.truetype('winter.ttf', 55)
    content =(str(data["main"]["humidity"])+'%')
    color = (255,255,255)
    draw.text((837,position[index]), content, color, font=fonts)
    index=index+1

my_image.save("result.jpg")
image_pdf = my_image.convert('RGB')
image_pdf.save("result.pdf")