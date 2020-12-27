import tkinter as tk
import time

import system
import api


class Clock(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, bg='black')
        # 時計ラベルの初期化
        self.clock = ''
        self.clockLabel = tk.Label(self, font=(
            'Helvetica', 90), fg="white", bg="black")
        self.clockLabel.pack(side=tk.TOP, anchor=tk.E)
        # 曜日ラベルの初期化
        self.day_of_week = ''
        self.dayOfWeekLabel = tk.Label(self, text=self.day_of_week, font=(
            'Helvetica', 45), fg="white", bg="black")
        self.dayOfWeekLabel.pack(side=tk.TOP, anchor=tk.E)
        # 日付ラベルの初期化
        self.date = ''
        self.dateLabel = tk.Label(self, text=self.date, font=('Helvetica', 45), fg="white", bg="black")
        self.dateLabel.pack(side=tk.TOP, anchor=tk.E)

        self.tick()
    
    def tick(self):
        day = system.nowDate()
        if day[0] != self.date:
            self.day_of_week = system.nowDate()[0]
            self.dayOfWeekLabel.config(text=self.day_of_week)
            self.date = system.nowDate()[1]
            self.dateLabel.config(text=self.date)
        self.clock = system.nowTime()
        self.clockLabel.config(text=system.nowTime())
        self.clockLabel.after(200, self.tick)

class Weather(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, bg='black')
        self.weather = ''
        self.weatherLabel = tk.Label(self, text=self.weather, font=(
            'Helvetica', 45), fg="white", bg="black")
        self.weatherLabel.pack(side=tk.TOP, anchor=tk.W)

        self.weatherIcon = ''
        self.weatherIconLabel = tk.Label(self, fg="white", bg="black")
        self.weatherIconLabel.pack(side=tk.TOP, anchor=tk.N, padx=20)

        self.temp = ''
        self.tempLabel = tk.Label(self, text=self.temp, font=(
            'Helvetica', 45), fg="white", bg="black")
        self.tempLabel.pack(side=tk.LEFT, anchor=tk.W)
        self.setWeather()
    
    def setWeather(self):
        self.data = system.getWeather()
        self.weatherLabel.config(text=self.data[0])
        self.tempLabel.config(text=self.data[1])
        self.weatherIconLabel.config(image=self.data[2])
        self.weatherIconLabel.image = self.data[2]

        # およそ３時間おきに取得
        self.weatherLabel.after(10000000, self.setWeather)

class NhkNews(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, bg='black')
        self.length = api.getNHKNews[1]
        for i in self.length:
            self.title = ''
            self.titleLabel = tk.Label(self, font=('Helvetica', 16), fg="white", bg="black")
            self.titleLabel.pack(side=tk.LEFT, anchor=tk.W)
            self.description = ''
            self.descriptionLabel = tk.Label(self,font=('Helvetica', 16), fg="white", bg="black")
            self.titleLabel.pack(side=tk.LEFT, anchor=tk.W)
            self.setNews()
    def setNews(self):
        self.news_data = api.getNHKNews()
        self.titleLabel.config(text=self.news_data[0].get("title"))
        self.descriptionLabel.config(text=self.news_data[0].get("summary"))
        #およそ1時間お気に取得
        self.titleLabel.after(3600000, self.setNews)



class Window:
    def __init__(self):
        self.window = tk.Tk()
        self.window.configure(bg='#000000')
        self.window.attributes('-fullscreen', True)
        self.topFrame = tk.Frame(self.window, background= '#000000')
        self.topFrame.pack(side=tk.TOP, fill=tk.BOTH, expand= tk.YES)
        self.bottomFrame = tk.Frame(self.window, background= '#000000')
        self.bottomFrame.pack(side=tk.TOP, fill=tk.BOTH, expand= tk.YES)
        # self.fullScreenState = False
        self.window.bind("<F11>", self.toggleFullScreen)
        self.window.bind("<Escape>", self.quitFullScreen)
        #clock
        self.clock = Clock(self.topFrame)
        self.clock.pack(side=tk.RIGHT, anchor=tk.N, padx=100, pady=60)
        #weather
        self.weather = Weather(self.topFrame)
        self.weather.pack(side=tk.LEFT, anchor=tk.N, padx=100, pady=60)
        #news
        self.news = NhkNews(self.bottomFrame)
        self.news.pack(side=tk.LEFT, anchor=tk.N, padx=100, pady=60)

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.window.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)





if __name__ == '__main__':
    w = Window()
    w.window.systemloop()
