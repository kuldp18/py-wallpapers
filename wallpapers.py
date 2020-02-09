import requests
import os
import wget
import ctypes
# Get the wallpaper from the internet(unsplash api)
# save it to a  directory
# set the wallpaper


def get_wallpaper():
    accesskey = 'use your api key here, get it from unsplash'
    url = 'https://api.unsplash.com/photos/random/?client_id='+accesskey
    params = {
        "query": "cars",
        "orientation": "landscape",
    }
    response = requests.get(url,params).json()
    image_url = response['urls']['full']
    download_path = getDownloadPath()
    wallpaper = wget.download(image_url,download_path)
    return wallpaper

def main():
    get_wallpaper()
    downloaded = getDownloadPath()
    SPI_SETDESKWALLPAPER = 20 
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, downloaded, 0)

def getDownloadPath():
    download_path = r'C:\Users\Lenovo\Desktop\Kuldeep\auto_wallpapers\wallpaper.jpg'
    return download_path

if __name__ == '__main__':
    main()