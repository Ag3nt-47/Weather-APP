from tkinter import *
from tkinter.ttk import Progressbar
from tkinter.ttk import Combobox
from tkinter.ttk import Notebook
from tkinter.ttk import Treeview
from PIL import Image, ImageTk
import tkinter.font
import requests
from bs4 import BeautifulSoup

derece_label = None
durum_label = None

image_req = requests.get("https://www.webtekno.com/images/editor/default/0003/28/2c0e3b703a9d620ee9cec146ada63b7e081e5501.jpeg")
if image_req.status_code == 200:
    with open("image.jpeg", 'wb') as file:
        file.write(image_req.content)


class WeatherMap():
    global derece_label, durum_label
    def __init__(self, parent):
        self.gui(parent)


    def gui(self, parent):
        global derece_label, durum_label

        if parent == 0:
            self.w1 = Tk()
            self.w1.title("Weather App")
            self.w1.geometry('440x400')
            self.w1.iconbitmap("weather.ico")
        else:
            self.w1 = Frame(parent)
            self.w1.place(x = 0, y = 0, width = 440, height = 390)
        self.label2 = Label(self.w1, text = "Enter city name:", anchor='w', font = tkinter.font.Font(family = "Britannic", size = 11), cursor = "arrow", state = "normal")
        self.label2.place(x = 60, y = 260, width = 110, height = 22)
        self.button1 = Button(self.w1, text = "Find", font = tkinter.font.Font(family = "Tw Cen MT Condensed Extra Bold", size = 11), cursor = "arrow", state = "normal", command=make_req)
        self.button1.place(x = 220, y = 290, width = 100, height = 32)
        self.image1 = Canvas(self.w1, bg = 'white')
        self.image1.place(x = 0, y = 0, width = 439, height = 246)
        self.image1i = Image.open("C:/Users/akbas/Downloads/2c0e3b703a9d620ee9cec146ada63b7e081e5501.jpeg")
        self.image1img = ImageTk.PhotoImage(self.image1i.resize((439, 246)))
        self.image1.create_image(0, 0, image = self.image1img, anchor=NW)
        self.ltext2 = Entry(self.w1, font = tkinter.font.Font(family = "Calibri", size = 9), state = "normal")
        self.ltext2.place(x = 180, y = 260, width = 180, height = 22)
        self.derece_label = Label(self.w1, text ="", anchor='w', font = tkinter.font.Font(family ="Bodoni MT", size = 14), cursor ="arrow", state ="normal")
        self.derece_label.place(x = 10, y = 330, width = 440, height = 22)
        self.durum_label = Label(self.w1, text ="", anchor='w', font = tkinter.font.Font(family ="Impact", size = 11), cursor ="arrow", state ="normal")
        self.durum_label.place(x = 350, y = 350, width = 400, height = 42)

def make_req():

    try:
        city = a.ltext2.get()
        response = requests.get(f"https://www.google.com/search?q=weather+{city}")
        soup = BeautifulSoup(response.content, 'html.parser')

        derece_element = soup.find('div', class_='BNeawe iBp4i AP7Wnd')
        if derece_element:
            degree = derece_element.get_text(strip=True)
            a.derece_label.config(text=f'{city[0].upper()+city[1:]} {degree[:-2]}°C')

        durum_element = soup.find('div', class_='BNeawe tAd8D AP7Wnd')
        if durum_element:
            durum = durum_element.get_text(strip=True)
            a.durum_label.config(text=durum)

    except:
        a.durum_label.config(text="Error, try again.")


if __name__ == '__main__':
    a = WeatherMap(0)
    a.w1.mainloop()

