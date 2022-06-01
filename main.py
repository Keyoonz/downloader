import tkinter as tk
from tkinter import filedialog as fd
import youtubesearchpython as ysp
import youtube_dl as ydl


searchResult = None

def download(videoUrl) : 
    ydl.YoutubeDL(ydl_opts).download([videoUrl])

def changeColor() :
    global bgColor, fgColor, widgets, widgetsText
    bgColor, fgColor = fgColor, bgColor
    for widget in widgets :
        widget["bg"]= bgColor
    for widget in widgetsText :
        widget["fg"]= fgColor

def changeFrame(removed, added) :
    global ydl_opts
    if added == directoryFrame :
        searchMusic(query.get())
    elif added == downloadFrame :
        path.set(fd.askdirectory() + "/" + searchResultTitle.get() + ".mp3")
        if path.get() == ("/" + searchResultTitle.get() + ".mp3") :
            path.set("defaultpath/" + searchResultTitle.get() + ".mp3")

        ydl_opts['outtmpl'] = path.get()
    elif removed == downloadFrame :
        download(searchResult['link'])
    removed.pack_forget()
    added.pack(side=tk.LEFT, expand=tk.YES)
    


def searchMusic(query) :
    global searchResult
    searchResult = ysp.VideosSearch(query, limit=1)
    searchResult = searchResult.result()['result'][0]
    searchResultTitle.set(searchResult['title'])

bgColor = "#333"
fgColor = "#eee"

            #root
root = tk.Tk()
root.title("Music Downloader")
root.geometry('1080x720')
root.configure(background=bgColor)
root.resizable(height=False, width=False)
root.iconbitmap('flavicon.ico')

            #stringVar
query = tk.StringVar()
searchResultTitle = tk.StringVar()
path = tk.StringVar()


            #frames
colorModeFrame = tk.Frame(root,bg=bgColor)
homeFrame = tk.Frame(root, bg=bgColor)
explainationFrame = tk.Frame(root, bg=bgColor)
explainationButtonsFrame = tk.Frame(explainationFrame, bg=bgColor)
chooseMusicFrame = tk.Frame(root, bg=bgColor)
chooseMusicButtonsFrame = tk.Frame(chooseMusicFrame, bg=bgColor)
directoryFrame = tk.Frame(root, bg=bgColor)
directoryButtonsFrame = tk.Frame(directoryFrame, bg=bgColor)
downloadFrame = tk.Frame(root, bg=bgColor)
    #pack
colorModeFrame.pack(side= tk.RIGHT)
homeFrame.pack(side=tk.LEFT, expand=tk.YES)
explainationButtonsFrame.pack(side=tk.BOTTOM)
chooseMusicButtonsFrame.pack(side=tk.BOTTOM)
directoryButtonsFrame.pack(side=tk.BOTTOM)

            #labels
welcomeLabel = tk.Label(homeFrame, text="Bienvenue sur notre téléchargeur.", bg=bgColor, fg=fgColor, font=('Times', 20, "bold"))
explainationLabel = tk.Label(explainationFrame, width=720, text="Rentrez le nom de la musique à télécharger,\n séléctionnez la musique,\n lorsque vous arriverez sur la page de séléction de destination,\n choisissez la destination du fichier.", bg=bgColor, fg=fgColor, font=('Times', 15, "bold"))
chooseMusicLabel = tk.Label(chooseMusicFrame, text="Choisissez la musique à télécharger", bg=bgColor, fg=fgColor, font=('Times', 20, "bold"))
directoryLabel = tk.Label(directoryFrame, text="Nous allons télécharger :", bg=bgColor, fg=fgColor, font=('Times', 20, "bold"))
searchResultLabel = tk.Label(directoryFrame, textvariable=searchResultTitle, bg=bgColor, fg=fgColor, font=('Times', 15, "bold"))
downloadLabel = tk.Label(downloadFrame, text="Pour commencer le téléchargement,\n cliquez sur le bouton ci-dessous \net attendez de revenir à la page d'accueuil\n pour télécharger une autre musique.", bg=bgColor, fg=fgColor, font=('Times', 20, "bold"))
    #pack
welcomeLabel.pack(side=tk.TOP)
explainationLabel.pack(side=tk.TOP)
chooseMusicLabel.pack(side=tk.TOP)
directoryLabel.pack(side=tk.TOP)
searchResultLabel.pack(side=tk.TOP)
downloadLabel.pack(side=tk.TOP)

            #buttons
colorModeButton = tk.Button(colorModeFrame, cursor="hand2", text="C", bg=bgColor, fg=fgColor, height=1080, command=changeColor)
continueButton = tk.Button(homeFrame, cursor="hand2", text="Continuer", bg=bgColor, fg=fgColor, font=("Times", 20), command=lambda: changeFrame(homeFrame, explainationFrame))
explainationHomeButton = tk.Button(explainationButtonsFrame, cursor="hand2", text="Accueil", bg=bgColor, fg=fgColor, font=("Times", 15), command=lambda: changeFrame(explainationFrame, homeFrame))
explainationContinueButton = tk.Button(explainationButtonsFrame, cursor="hand2", text="Suivant", bg=bgColor, fg=fgColor, font=("Times", 15), command=lambda: changeFrame(explainationFrame, chooseMusicFrame))
chooseMusicHomeButton = tk.Button(chooseMusicButtonsFrame, cursor="hand2", text="Accueil", bg=bgColor, fg=fgColor, font=("Times", 15), command=lambda: changeFrame(chooseMusicFrame, homeFrame))
chooseMusicContinueButton = tk.Button(chooseMusicButtonsFrame, cursor="hand2", text="Suivant", bg=bgColor, fg=fgColor, font=("Times", 15), command=lambda: changeFrame(chooseMusicFrame, directoryFrame))
directoryHomeButton = tk.Button(directoryButtonsFrame, cursor="hand2", text="Accueil", bg=bgColor, fg=fgColor, font=("Times", 15), command=lambda: changeFrame(directoryFrame, homeFrame))
directoryPreviousButton = tk.Button(directoryButtonsFrame, cursor="hand2", text="Précédent", bg=bgColor, fg=fgColor, font=("Times", 15), command=lambda: changeFrame(directoryFrame, chooseMusicFrame))
directoryContinueButton = tk.Button(directoryButtonsFrame, cursor="hand2", text="Choisir la destination", bg=bgColor, fg=fgColor, font=("Times", 15), command=lambda: changeFrame(directoryFrame, downloadFrame))
downloadButton = tk.Button(downloadFrame, cursor="hand2", text="Commencer le téléchargement", bg=bgColor, fg=fgColor, font=("Times", 20), command=lambda: changeFrame(downloadFrame, homeFrame))

    #pack
colorModeButton.pack(side=tk.LEFT)
continueButton.pack(side=tk.BOTTOM)
explainationHomeButton.pack(side=tk.LEFT)
explainationContinueButton.pack(side=tk.RIGHT)
chooseMusicHomeButton.pack(side=tk.LEFT)
chooseMusicContinueButton.pack(side=tk.RIGHT)
directoryHomeButton.pack(side=tk.LEFT)
directoryContinueButton.pack(side=tk.RIGHT)
directoryPreviousButton.pack(side=tk.RIGHT)
downloadButton.pack(side=tk.BOTTOM)


ydl_opts = {
    'format': "bestaudio/best",
    'outtmpl': "%(title)s.%(ext)s",
    "postprocessors" : [{
        "key" : 'FFmpegExtractAudio',
        "preferredcodec" : 'mp3',
        "preferredquality" : '320'
    }]
}


            #entry
musicEntry = tk.Entry(chooseMusicFrame, textvariable=query, width=50, bg=bgColor, fg=fgColor, font=("Times", 15))
    #pack
musicEntry.pack(side=tk.TOP)



widgets = [root, colorModeFrame, homeFrame, explainationFrame, chooseMusicFrame, directoryFrame, downloadFrame, welcomeLabel, explainationLabel, chooseMusicLabel, directoryLabel, searchResultLabel, downloadLabel, colorModeButton, continueButton, explainationHomeButton, explainationContinueButton, chooseMusicHomeButton, chooseMusicContinueButton, directoryHomeButton, directoryPreviousButton, directoryContinueButton, downloadButton, musicEntry]
widgetsText = [welcomeLabel, explainationLabel, chooseMusicLabel, directoryLabel, searchResultLabel, downloadLabel, colorModeButton, continueButton, explainationHomeButton, explainationContinueButton, chooseMusicHomeButton, chooseMusicContinueButton, directoryHomeButton, directoryPreviousButton, directoryContinueButton, downloadButton, musicEntry]


root.mainloop()