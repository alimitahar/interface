#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter.filedialog
import tkinter as tk
from tkinter import ttk
from tkinter import * 
import tkinter.font as font
from tkinter.filedialog import askopenfilename
import os
import webbrowser
from tkinter.messagebox import showinfo

def onSave():
    print(filedialog.asksaveasfilename(initialdir = "/",title = "Save as",filetypes = (("Python files","*.py;*.pyw"),("All files","*.*"))))

def onOpen():
    #print(filedialog.askopenfilename(initialdir = "/",title = "Open file",filetypes = (("Python files","*.py;*.pyw"),("All files","*.*")))) 
    rep = filedialog.askopenfilenames(
    	parent=fp,
    	initialdir='/',
    	initialfile='tmp',
    	filetypes=[
    		("Python", ["*.py","*.ipynb"]),
      		("Pdf", "*.pdf"),
    		("Text", "*.txt"),
    		("All files", "*")])
    print(rep)
    try:
	    os.startfile(rep[0])
    except IndexError:
        print("No file selected")


def openAlgo1():
    webbrowser.open_new(r"Mobile_Price_Prediction.pdf")
    
def openAlgo2():
    webbrowser.open_new(r"Covid-19 Data Analysis and Predcitions.pdf")
    
def openAlgo3():
    webbrowser.open_new(r"KNN-abalone-with-panda-module.pdf")
    
def openAlgo4():
    webbrowser.open_new(r"logistic Regression_infidelity_menage.pdf")
    
def openAlgo5():
    webbrowser.open_new(r"k-Means_Mall_Customers_View_Clusters.pdf")
    
def openAlgo6()    :
    webbrowser.open_new(r"vader_sentiment_analysis.pdf")
    
def openAlgo7()    :
    webbrowser.open_new(r"IRIS.pdf")
    

fp =Tk()


fz1 = font.Font(size=40,family='Times New Roman',weight="bold")
fz2 = font.Font(size=15,family='Times New Roman',weight="bold")

p = PanedWindow(fp, orient=HORIZONTAL)

F1 = Frame(fp, bg='gold', bd=5,relief = RAISED)
Label(F1,text='Machine Learning : Liste des Algorithmes',font=("Courier", 20,"bold")).pack(padx = 10, pady = 10)
F1.pack(padx =10, pady = 10)




Frame3 = Frame(fp,borderwidth=1,relief=GROOVE)
Label(Frame3).pack(fill=tk.BOTH)
Frame3.pack(side=LEFT)
Frame3.pack(fill=tk.BOTH, expand=True)

Frame4 = Frame(fp,borderwidth=1,relief=GROOVE)
tkinter.Label (Frame4, text = "Projet : Fouille de données",fg='DodgerBlue2',bg="light yellow",font=("Courier", 20,"bold")).pack(pady=20, side= TOP, anchor="w")
#l1.pack (side=TOP) # positionne l à l'intérieur de Frame4

tkinter.Label (Frame4, text = "Présenté par : Tahar ALIMI",bg="light yellow",fg='DodgerBlue2',font=("Courier", 20,"bold")).pack(pady=20, side= TOP, anchor="w")
#l3.pack (side=TOP) # positionne l à l'intérieur de Frame4

tkinter.Label (Frame4, text = "Classe : Master de Recherche SINT (M1)",bg="light yellow",fg='DodgerBlue2',font=("Courier", 18,"bold")).pack(pady=20, side= TOP, anchor="w")
#l2.pack (side=TOP) # positionne l à l'intérieur de Frame4

tkinter.Label (Frame4, text = "Proposé par : Prof. Lamia Belguith",bg="light yellow",fg='DodgerBlue2',font=("Courier", 18,"bold")).pack(pady=20, side= TOP, anchor="w")
#l4.pack (side=TOP) # positionne l à l'intérieur de Frame4

tkinter.Label (Frame4, text = "Année Académique : 2020/2021",bg="light yellow",fg='DodgerBlue2',font=("Courier", 10,"bold")).pack(pady=20, side= BOTTOM, anchor="c")
Frame4.pack(side=RIGHT)
Frame4.pack(fill=tk.BOTH, expand=True)

Alg1=Button(Frame3,text="Mobile_Price_Prediction",borderwidth = 5,font=("Courier", 15,"bold"),
             fg='PaleVioletRed',bg="lightblue1",command = openAlgo1).pack(side=TOP,fill=tk.BOTH)

Alg2=Button(Frame3,text="Covid-19 Predcitions",borderwidth = 5,font=("Courier", 15,"bold"),fg='PaleVioletRed',bg="lightblue1",command = openAlgo2).pack(side=TOP,fill=tk.BOTH)

Alg3=Button(Frame3,text="KNN-abalone : Panda-module",borderwidth = 5,font=("Courier", 15,"bold"),fg='PaleVioletRed',bg="lightblue1",command = openAlgo3).pack(side=TOP,fill=tk.BOTH)

Alg4=Button(Frame3,text="logistic Regression_infidelity_menage",borderwidth = 5,font=("Courier", 15,"bold"),fg='PaleVioletRed',bg="lightblue1",command = openAlgo4).pack(side=TOP,fill=tk.BOTH)

Alg5=Button(Frame3,text="k-Means_Mall_Customers_View_Clusters",borderwidth = 5,font=("Courier", 15,"bold"),fg='PaleVioletRed',bg="lightblue1",command = openAlgo5).pack(side=TOP,fill=tk.BOTH)

Alg6=Button(Frame3,text="Vader_sentiment_analysis",borderwidth = 5,font=("Courier", 15,"bold"),fg='PaleVioletRed',bg="lightblue1",command = openAlgo6).pack(side=TOP,fill=tk.BOTH)

Alg7=Button(Frame3,text="Iris",borderwidth = 5,font=("Courier", 15,"bold"),fg='PaleVioletRed',bg="lightblue1",command = openAlgo7).pack(side=TOP,fill=tk.BOTH)




fp.title('Machine Learning') # Ajout d'un titre
fp.resizable(True, True) # autoriser le redimensionnement vertical et horizontal
fp.geometry("1072x800+80+50")#dimensionner et positionner la fnêtre

menubar = Menu(fp)
menufile = Menu(menubar,tearoff=0)
menufile.add_command(label="Open ",command=onOpen)
menufile.add_separator()

menufile.add_command(label="Save",command=onSave)
menufile.add_separator()


menufile.add_command(label="Save as")
menufile.add_separator()


menufile.add_command(label="Quit", command=fp.destroy) 
menufile.add_separator()

menubar.add_cascade(label="File", menu=menufile)

menuedition = Menu(menubar,tearoff=0)

def alert():
    showinfo("alerte", "Thank You!")


menuedition.add_command(label="Cut")
menuedition.add_separator()

menuedition.add_command(label="Copy")
menuedition.add_separator()

menuedition.add_command(label="Past")
menuedition.add_separator()

menuedition.add_cascade(label="Edit")
menuedition.add_separator()

menubar.add_cascade(label="Edit", menu=menuedition)

menuhelp = Menu(menubar, tearoff=0)
menuhelp.add_command(label="About !", command=alert)
menubar.add_cascade(label="Help", menu=menuhelp)


fp.config(menu=menubar)

p.pack()
fp.mainloop()


# In[ ]:




