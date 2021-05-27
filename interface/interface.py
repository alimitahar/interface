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
    #print(filedialog.askopenfilename(initialdir = "/",title = "Open file",filetypes = (("Python files","*.py;*.pyw"),("All files","*.*")))) 
    webbrowser.open_new(r"Covid-19 Data Analysis and Predcitions.ipynb")

def openbtn1():    
    webbrowser.open_new(r"Mobile_Price_Prediction.pdf")
def openbtn2():    
    webbrowser.open_new(r"DataSet Presentation.pdf")
def openbtn3():    
    webbrowser.open_new(r"Data Analysis.pdf")
def openbtn4():    
    webbrowser.open_new(r"Correlation Map.pdf")
def openbtn5():    
    webbrowser.open_new(r"preprocessing.pdf")
def openbtn6():    
    webbrowser.open_new(r"Logistic regression.pdf")
def openbtn7():    
    webbrowser.open_new(r"Linear Discriminant Analysis.pdf")
def openbtn8():    
    webbrowser.open_new(r"Grid Search - Cross Validation.pdf")
def openbtn9():    
    webbrowser.open_new(r"Ensemble Learning.pdf")
def openbtn10():    
    webbrowser.open_new(r"Best Estimator.pdf")
def openbtn11():    
    webbrowser.open_new(r"Test _ Data Preparation.pdf")
def openbtn12():    
    webbrowser.open_new(r"Test _ Baseline Model.pdf")
def openbtn13():    
    webbrowser.open_new(r"Test _ Linear Regression model.pdf")
def openbtn14():    
    webbrowser.open_new(r"Test _ Logistic Regression.pdf")
def openbtn15():    
    webbrowser.open_new(r"Test _ Creating & Training KNN Model.pdf")
def openbtn16():    
    webbrowser.open_new(r"Les Algos\Les Algos.exe")
        

fp =Tk()


fz1 = font.Font(size=40,family='Times New Roman',weight="bold")
fz2 = font.Font(size=15,family='Times New Roman',weight="bold")

p = PanedWindow(fp, orient=HORIZONTAL)

F1 = Frame(fp, bg='gold', bd=5,relief = RAISED)
Label(F1,text='',borderwidth = 5,font=("Courier", 20,"bold")).pack(side=LEFT)
Label(F1,text="Faculté des Sciences Economiques et de Gestion de Sfax (FSEGS)",fg="red",borderwidth = 5,font=("Courier", 20,"bold")).pack(side=TOP)
F1.pack(side=TOP)
F1.pack(fill=tk.BOTH, expand=False)



F2 = Frame(fp, bg='gold', bd=5,relief = RAISED)
Label(F2,text='Mobile_Price_Prediction',borderwidth = 5,font=("Courier", 20,"bold")).pack(side=TOP)
F2.pack(side=TOP)
F2.pack(fill=tk.BOTH, expand=True)


Frame3 = Frame(fp,borderwidth=1,relief=GROOVE)
Label(Frame3).pack(fill=tk.BOTH)
Frame3.pack(side=LEFT)
Frame3.pack(fill=tk.BOTH, expand=True)

Frame4 = Frame(fp,borderwidth=2,relief=GROOVE)
Label(Frame4,text="",font=("Courier", 20,"bold")).pack(fill=tk.BOTH)
Frame4.pack(side=RIGHT)
Frame4.pack(fill=tk.BOTH, expand=True)

tkinter.Label (Frame4, text = "Projet : Fouille de données",bg="light yellow",fg='DodgerBlue2',font=("Courier", 20,"bold")).pack(pady=20, side= TOP, anchor="w")
#l1.pack (side=TOP) # positionne l à l'intérieur de Frame4

tkinter.Label (Frame4, text = "Présenté par : Tahar ALIMI",bg="light yellow",fg='DodgerBlue2',font=("Courier", 20,"bold")).pack(pady=20, side= TOP, anchor="w")
#l3.pack (side=TOP) # positionne l à l'intérieur de Frame4

tkinter.Label (Frame4, text = "Classe : Master de Recherche SINT (M1)",bg="light yellow",fg='DodgerBlue2',font=("Courier", 18,"bold")).pack(pady=20, side= TOP, anchor="w")
#l2.pack (side=TOP) # positionne l à l'intérieur de Frame4

tkinter.Label (Frame4, text = "Proposé par : Prof. Lamia Belguith",bg="light yellow",fg='DodgerBlue2',font=("Courier", 18,"bold")).pack(pady=20, side= TOP, anchor="w")
#l4.pack (side=TOP) # positionne l à l'intérieur de Frame4

tkinter.Label (Frame4, text = "Année Académique : 2020/2021",bg="light yellow",fg='DodgerBlue2',font=("Courier", 10,"bold")).pack(pady=20, side= BOTTOM, anchor="c")

btn1=Button(Frame3,text="Mobile_Price_Prediction (Alg. Complet)",borderwidth = 5,font=("Courier", 15,"bold"),fg='tomato',bg="lightblue1",command = openbtn1).pack(side=TOP,fill=tk.BOTH)
#Algo1.pack()

btn2=Button(Frame3,text="Train : DataSet Presentation",borderwidth = 3,font=("Courier", 15,"bold"),fg='tomato',bg="lightblue1",command = openbtn2).pack(side=TOP,fill=tk.BOTH)

btn3=Button(Frame3,text="Train : Data Analysis",borderwidth = 3,font=("Courier", 15,"bold"),fg='tomato',bg="lightblue1",command = openbtn3).pack(side=TOP,fill=tk.BOTH)

btn4=Button(Frame3,text="Train : Correlation Map",borderwidth = 3,font=("Courier", 15,"bold"),fg='tomato',bg="lightblue1",command = openbtn4).pack(side=TOP,fill=tk.BOTH)

btn5=Button(Frame3,text="Train : Preprocessing",borderwidth = 3,font=("Courier", 15,"bold"),fg='tomato',bg="lightblue1",command = openbtn5).pack(side=TOP,fill=tk.BOTH)

btn6=Button(Frame3,text="Train : Logistic Regression",borderwidth = 3,font=("Courier", 15,"bold"),fg='tomato',bg="lightblue1",command = openbtn6).pack(side=TOP,fill=tk.BOTH)

btn7=Button(Frame3,text="Train : Linear Discriminant Analysis",borderwidth = 3,font=("Courier", 15,"bold"),fg='tomato',bg="lightblue1",command = openbtn7).pack(side=TOP,fill=tk.BOTH)

btn8=Button(Frame3,text="Train : Grid Search - Cross Validation",borderwidth = 3,font=("Courier", 15,"bold"),fg='tomato',bg="lightblue1",command = openbtn8).pack(side=TOP,fill=tk.BOTH)

btn9=Button(Frame3,text="Train : Ensemble Learning",borderwidth = 3,font=("Courier", 15,"bold"),fg='tomato',bg="lightblue1",command = openbtn9).pack(side=TOP,fill=tk.BOTH)

btn10=Button(Frame3,text="Train : Best Estimator",borderwidth = 3,font=("Courier", 15,"bold"),fg='tomato',bg="lightblue1",command = openbtn10).pack(side=TOP,fill=tk.BOTH)

btn11=Button(Frame3,text="Train : Test : Data Preparation",borderwidth = 3,font=("Courier", 15,"bold"),fg='tomato',bg="lightblue1",command = openbtn11).pack(side=TOP,fill=tk.BOTH)

btn12=Button(Frame3,text="Test : Baseline Model",borderwidth = 3,font=("Courier", 15,"bold"),fg='tomato',bg="lightblue1",command = openbtn12).pack(side=TOP,fill=tk.BOTH)

btn13=Button(Frame3,text="Test : Linear Regression model",borderwidth = 3,font=("Courier", 15,"bold"),fg='tomato',bg="lightblue1",command = openbtn13).pack(side=TOP,fill=tk.BOTH)

btn14=Button(Frame3,text="Test : Logistic Regression",borderwidth = 3,font=("Courier", 15,"bold"),fg='tomato',bg="lightblue1",command = openbtn14).pack(side=TOP,fill=tk.BOTH)

btn15=Button(Frame3,text="Test : Creating & Training KNN Model",borderwidth = 3,font=("Courier", 15,"bold"),fg='tomato',bg="lightblue1",command = openbtn15).pack(side=TOP,fill=tk.BOTH)

btn16=Button(Frame4,text="Voir Plus d'Algorithmes --> ",height=6,borderwidth = 6,font=("Courier", 15,"bold"),fg='tomato',bg="lightblue1",command = openbtn16).pack(side=BOTTOM,fill=tk.BOTH)

fp.title('Fouille de données') # Ajout d'un titre
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





# In[ ]:




