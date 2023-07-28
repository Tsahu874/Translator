import tkinter as tk

# importing  ttk module from tkinter as it has the combobox class  
from tkinter import ttk  

# let's get the language list in this file  
import backend   

import googletrans
googletrans.Translator()



# let's create the language list
languages = backend.get_languages()  
abbreviation = backend.get_abbreviation()  

#  creating root gui 
# tk function is used to create main or root window  
root = tk.Tk() 

#  properties of root gui
root.geometry('700x400')    
root.resizable(width=False, height=False)    
root.title('Language Translator')  
root.config(bg='#f3e5f5')  

# Universal variables
px = 30 # padx (padding) not pixel
py = 10
bg_color= '#FF9999'      
fg_color = 'black'    
button_font = 'Helvetica'   
button_font_size= 12    


# adding widgets
welcome_label = tk.Label(root, text ='LANGUAGE TRANSLATOR', bg='#f3e5f5', font= ('Comic Sans MS ',27))  
welcome_label.pack(pady=20)  


# creating a frame to arrange my widgets in grid layout  
frame = tk.Frame(root, bg='#e7decc',width=500, height=100) 
frame.pack( padx=10,pady=10, fill='both') 

# source and target language label
source_label = tk.Label(frame, text='Source Language', bg = bg_color, fg = fg_color,font=('Comic Sans MS', 20))
source_label.grid(row=0, column=0,padx=px, pady=py)
target_label = tk.Label(frame, text='Target Language', bg = bg_color, fg = fg_color,font=('Comic Sans MS', 20))
target_label.grid(row=0, column=2,padx=px, pady=py) 

# tk.OptionMenu(root, value=[1,2,3,4], variable=tk.StringVar()).pack() <----option menu

# adding combobox 
source_cb = ttk.Combobox(frame, values=languages, width= 30)  
target_cb = ttk.Combobox(frame, values=languages, width= 30)  
source_cb.grid(row=1, column=0,padx=px, pady=py) 
target_cb.grid(row=1, column=2,padx=px, pady=py)   

# setting the default language
source_cb.current(21)
target_cb.current(38)

# Adding row 2 elements --> Input text area , translate button , output label
input_text = tk.Text(frame, width=25, height=5)
input_text.grid(row=2, column=0,padx=px, pady=py)

translate_button = tk.Button(frame, text='Translate',  bg = bg_color, fg = fg_color, font=(button_font, button_font_size))
translate_button.grid(row=2, column=1,padx=px, pady=py)

output_label = tk.Label(frame, text='No Translations Yet!',  bg = bg_color, fg = fg_color, width = 30, height=5)
output_label.grid(row=2,column=2,padx=px, pady=py)

# Adding row 3 elements ---> voice, celar, speak button
voice_button = tk.Button(frame, text='Say Something!',  bg = bg_color, fg = fg_color,font=(button_font, button_font_size))
voice_button.grid(row=3, column=0,padx=px, pady=py) 

clear_button = tk.Button(frame, text='Clear',  bg = bg_color, fg = fg_color,font=(button_font, button_font_size))
clear_button.grid(row=3, column=1,padx=px, pady=py)

speak_button = tk.Button(frame, text='Speak the translation',  bg = bg_color, fg = fg_color,font=(button_font, button_font_size))
speak_button.grid(row=3, column=2,padx=px, pady=py) 


root.mainloop()  