from googletrans import Translator
"""
Googletrans is a free and unlimited python library that implemented Google Translate API. 
This uses the Google Translate Ajax API to make calls to such methods as detect and translate. 

Used googletrans library, because it had AUTO LANGUAGE DETECTION option.

Make sure to install the version 3.1.0a0, by using the code "pip install googletrans==3.1.0a0 (CAN'T STRESS THIS ENOUGH)
"""
from gtts import gTTS
"""
gtts (stands for Google Text To Speech)
"""
from tkinter import *
"""
tkinter is GUI (Graphical User Interface) library for python.
Follow the URL for more about this library :
 https://www.tutorialspoint.com/python/python_gui_programming.htm#:~:text=Tkinter%20is%20the%20standard%20GUI,Tkinter%20is%20an%20easy%20task. 
"""
def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb
"""
Copied the rgb_hack function from this URL. It essentially helps to translate the RGB code to I think HEX (Not sure. Should ask in class)
Did this way to match the BG colour with Image
https://pythonguides.com/python-tkinter-colors/ 
"""
window = Tk() #This is how we make outer main window
window.title("Translator")
window.geometry('1200x760') #Window size
window.config(bg=rgb_hack((0,150,135))) #Background color of the main window, RGB Color code found using MS Paint
set_bg = PhotoImage(file="C:\\Users\\Fahad Engineering\\Desktop\\translate-3324171_1280.png") #set_bg is variable. PhotoImage function. To load the image.

label_1 = Label(window, image=set_bg) #This helps to specify where we want to place the loaded image
label_1.place(x=0,y=0) # This gives the coordinates where the image to be placed. I tried randomly on the coordinates.

e1 = Entry(window,width=35, bg='white',fg='black',font=('Arial',10,'bold')) #This is used to ENTER a single line of text bg: Background, fg: Font color, font: Font style
e1.place(x=170,y=225) # Here we position the Entry widget we created, on to the main window.

def convert_language():
    a1 = e1.get() #This extracts the text from e1 Entry widget. In e1 we enter the text to translate.
    t1 = Translator()
    t2 = click_option.get()

    if t2 == "English":
        convert = "en" #ISO 639-1 standard language codes are used. https://www.loc.gov/standards/iso639-2/php/code_list.php
    elif t2 == "Hindi":
        convert = "hi"
    elif t2 == "Tamil":
        convert = "ta"
    elif t2 == "Telugu":
        convert = "te"
    elif t2 == "Kannada":
        convert = "kn"
    elif t2 == "Gujarati":
        convert = "gu"
    elif t2 == "Malayalam":
        convert = "ml"
    elif t2 == "Urdu":
        convert = "ur"
    elif t2 == "Marathi":
        convert = "mr"

    trans_text = t1.translate(a1, dest= convert)
    trans_text = trans_text.text
    ob1 = gTTS(text= trans_text, slow= False, lang= convert)
    label_2.config(text= trans_text)
"""
How the translator library is used, is mentioned in the documentation in given URL.
https://py-googletrans.readthedocs.io/en/latest/
"""
choices = ["English",
           "Hindi",
           "Tamil",
           "Telugu",
           "Kannada",
           "Gujarati",
           "Malayalam",
           "Urdu",
           "Marathi"
]

click_option = StringVar() # Holds a string; the default value is an empty string
click_option.set("Select Language")

list_drop = OptionMenu(window, click_option, *choices) #OptionMenu provides drop down list, *choices for multiple args
list_drop.configure(background="cyan", foreground="black", font=('Arial',12,'bold'))
list_drop.place(x=210, y=310)

label_2 = Label(window, text="Translated text", fg='black', font=('Arial',14,'bold'), justify= "left", wraplength=260)
label_2.place(x=465, y=225)
label_2.config(bg=rgb_hack((176,235,241)))

#To see color names follow this link https://trinket.io/pygame/f5af3f7500

Button_1 = Button(window, text="Translate", bg="red", fg="white", font=('Arial',16,'bold'), command= convert_language)
Button_1.place(x=455, y=310)

window.state('zoomed') #This helps in running the window in fullscreen mode when opened.
window.mainloop() #This command is used to close the tk inter program. Kind of like closing the file when file handling

"""
പ്രിയങ്ക ഒരു മികച്ച അധ്യാപികയാണ് 
"""
