import os
import time
import qrcode
import pyimgur
import requests

##################################################################

Client_ID = "3a8ab8e3953a1a8"
img_folder_path = "./mars/utils/imgs/"

API_KEY = '0417ca6acced31fdcbf4525ccf8302862893a'
Base_URL = 'https://cutt.ly/api/api.php'


##################################################################
def upload_imgur(path, name):
    im = pyimgur.Imgur(Client_ID)
    upload_img = im.upload_image(path, title=name)
    
    return upload_img.link
    
def generate_qr(url, name="default"):
    Path = f"{img_folder_path}qr_temporal_{str(name)}.png"
    qr = qrcode.QRCode(
	version=2,
	box_size=10,
	border=2)

    data = url
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(f'{Path}')
    
    link = upload_imgur(Path, name)
    
    time.sleep(1)
    os.remove(f"{img_folder_path}/qr_temporal_{str(name)}.png")
    return link

def short_url(url):
    payload = {'key': API_KEY, 'short': url}
    request = requests.get(Base_URL, params=payload)
    data = request.json()
    shortlink = data['url']['shortLink']
    
    return shortlink


