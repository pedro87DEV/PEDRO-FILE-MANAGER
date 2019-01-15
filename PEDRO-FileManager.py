#!/usr/bin/env python

#########################################################
# Autore    : Mattia Pedroncelli
# Date      : Gennaio 2019 
# COPYRIGHT : Pedro Software
#########################################################

from sys import version_info
if version_info.major == 2:
    # Python 2.x
    from Tkinter import *
    from Tkinter.ttk import *
elif version_info.major == 3:
    # Python 3.x
    from tkinter import *
    from tkinter.ttk import *
    from tkinter import messagebox
    from tkinter import filedialog
    from PIL import ImageTk, Image
    import filecmp
    import hashlib
    import os
    import pkgutil

class Page(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

###############################################################################
# PAGINA HOME PAGE
###############################################################################

class HomePage(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
    
       self.label = Label(self, text = " SUPER FILE MANAGER ", font=("Courier", 30))
       self.label.place(x = 100,y = 50)

       self.img = ImageTk.PhotoImage(Image.open("GUI_Pedro.png"))
       panel = Label(self, image = self.img)
       panel.place(x = 100,y = 100)

###############################################################################
# PAGINA VERIFICA LUNGHEZZA RECORD DEL FILE
###############################################################################

class PageVerificaLunghezza(Page):
   def __init__(self, *args, **kwargs):
    Page.__init__(self, *args, **kwargs)

    self.filename_lung = "INPUT VUOTO"

    def KOFileInputMessage():
        msg = messagebox.showerror( "ERRORE", "Malandrino!!! Devi selezionare il file di input")

    def KOLengthMessage():
        msg = messagebox.showerror( "ERRORE", "Malandrino!!! Devi inserire la lunghezza record da verificare")
    
    def choose_path_filelung():
        self.filename_lung = filedialog.askopenfilename(filetypes=[("File txt","*.txt")])
        pathlabel_file_lunghezza.config(text=self.filename_lung)

    def verify_record():

      if self.filename_lung == "INPUT VUOTO":
         KOFileInputMessage()
      elif entry_lenght.get() == "INSERT RECORD LENGHT": 
         KOLengthMessage()
      else: 
        name_file_OK = self.filename_lung + "_recordOK"
        name_file_fallati = self.filename_lung + "_record_fallati"
       
        in_file = open(self.filename_lung,"r")
        out_file_OK = open(name_file_OK,"w")
        out_file_fallati = open(name_file_fallati,"w")
        counter_fallati = 0
        lunghezza_record = entry_lenght.get()
        lunghezza_record = int(lunghezza_record)
          
        rigaletta = in_file.readlines()
        for i in rigaletta:  
          if len(i) > lunghezza_record:
             out_file_fallati.write(i)
             counter_fallati = counter_fallati + 1
          else:
             out_file_OK.write(i)

        in_file.close()
        out_file_OK.close()
        out_file_fallati.close()
       
        file_creati = "FILE DI INPUT CONTROLLATO : "+ str(self.filename_lung) + "\n\nFILE DI OUTPUT CREATI :\n"+ name_file_OK + "\n" + name_file_fallati + "\n\nN° righe con lunghezza record maggiore di " + str(lunghezza_record) + " ---> " + str(counter_fallati)
        msgOK = messagebox.showinfo( "OPERAZIONE ESEGUITA", str(file_creati))
        

    label_sel = Label(self, text = "1)Verifica lunghezza record del file", font=("Courier", 20))
    label_sel.place(x = 50,y = 50)

    label_sel = Label(self, text = "File di input da controllare", background='#dff4be')
    label_sel.place(x = 50,y = 130)

    button_seleziona_file = Button(self, text = "Seleziona file", command = choose_path_filelung)
    button_seleziona_file.place(x = 384,y = 150)
    
    pathlabel_file_lunghezza = Label(self, background='#FFFFFF', width=55)
    pathlabel_file_lunghezza.place(x = 50,y = 150)
    
    label_lenght = Label(self, text = "Lunghezza record maggiore di ", background='#dff4be')
    label_lenght.place(x = 50,y = 200)
     
    entry_lenght = Entry(self, width=26)
    entry_lenght.insert(END, 'INSERT RECORD LENGHT')
    entry_lenght.place(x = 220,y = 200)
      
    button_verifica = Button(self, text = "VERIFICA", command = verify_record)
    button_verifica.place(x = 50,y = 250)

###############################################################################
# PAGINA CONFRONTA CONTENUTO DUE FILE
###############################################################################

class PageConfrontaFile(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

       self.filename1_confronta = "INPUT1 VUOTO"
       self.filename2_confronta = "INPUT2 VUOTO"

       def KOFile1InputMessage():
        msg = messagebox.showerror( "ERRORE", "Malandrino!!! Devi selezionare il file di input 1")

       def KOFile2InputMessage():
        msg = messagebox.showerror( "ERRORE", "Malandrino!!! Devi selezionare il file di input 2")

 
       def confronta_file():
           
        if self.filename1_confronta == "INPUT1 VUOTO":
           KOFile1InputMessage()
        elif self.filename2_confronta == "INPUT2 VUOTO": 
           KOFile2InputMessage()
        else:
           compare_file = filecmp.cmp(self.filename1_confronta,self.filename2_confronta,shallow=True)
           if compare_file:
               messaggio = "FILE 1 : "+ str(self.filename1_confronta) + "\n""FILE 2 : "+ str(self.filename2_confronta) + "\n\nIl contenuto dei due file risulta identico."
               msg = messagebox.showinfo( "CONFRONTO FILE OK", str(messaggio))
           else:
               messaggio = "FILE 1 : "+ str(self.filename1_confronta) + "\n""FILE 2 : "+ str(self.filename2_confronta) + "\n\nIl contenuto dei due file risulta DIVERSO!!!"
               msg = messagebox.showerror( "CONFRONTO FILE ERROR", str(messaggio))
        filecmp.clear_cache()
         
 
       def choose_path_confronta1():
        self.filename1_confronta = filedialog.askopenfilename(filetypes=[("File txt","*.txt")])
        pathlabel_file_lunghezza1.config(text=self.filename1_confronta)

       def choose_path_confronta2():
        self.filename2_confronta = filedialog.askopenfilename(filetypes=[("File txt","*.txt")])
        pathlabel_file_lunghezza2.config(text=self.filename2_confronta)

       label_sel = Label(self, text = "2)Confronta contenuto file", font=("Courier", 20))
       label_sel.place(x = 50,y = 50)

       label_sel1 = Label(self, text = "File input 1", background='#dff4be')
       label_sel1.place(x = 50,y = 130)

       button_seleziona_file1 = Button(self, text = "Seleziona file", command = choose_path_confronta1)
       button_seleziona_file1.place(x = 384,y = 150)
    
       pathlabel_file_lunghezza1 = Label(self, background='#FFFFFF', width=55)
       pathlabel_file_lunghezza1.place(x = 50,y = 150)

       label_sel2 = Label(self, text = "File input 2", background='#dff4be')
       label_sel2.place(x = 50,y = 200)

       button_seleziona_file2 = Button(self, text = "Seleziona file", command = choose_path_confronta2)
       button_seleziona_file2.place(x = 384,y = 220)
    
       pathlabel_file_lunghezza2 = Label(self, background='#FFFFFF', width=55)
       pathlabel_file_lunghezza2.place(x = 50,y = 220)

       button_confronta = Button(self, text = "CONFRONTA", command = confronta_file)
       button_confronta.place(x = 50,y = 250)



###############################################################################
# PAGINA ESEGUI HASHING CONTENUTO FILE
###############################################################################

class PageHash(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

          
       def choose_pathfile_hash():
        self.filename_hash = filedialog.askopenfilename(filetypes=[("All file types","*.*")])
        pathlabel_file_hash.config(text=self.filename_hash)

       def crea_hash():
        sha256_hash = hashlib.sha256()   
        with open(self.filename_hash,"rb") as f:
            
          # Read and update hash string value in blocks of 4K
          for byte_block in iter(lambda: f.read(4096),b""):
              sha256_hash.update(byte_block)

          entry_stringa_hash.insert(END, sha256_hash.hexdigest())
          
        

       label_hash1 = Label(self, text = "3)Crea stringa hash del contenuto file", font=("Courier", 20))
       label_hash1.place(x = 50,y = 50)

       label_hash2 = Label(self, text = "SHA256 is a secure hash algorithm which creates a fixed length one way string from any input data.\nCalculating a hash for a file is always useful when you need to check if two files are identical, or to make sure \nthat the contents of a file were not changed, and to check the integrity of a file when it is transmitted over a network.")
       label_hash2.place(x = 50,y = 90)

       label_hash3 = Label(self, text = "Seleziona il file di input da trasformare", background='#dff4be')
       label_hash3.place(x = 50,y = 180)

       button_seleziona_filehash = Button(self, text = "Seleziona file", command = choose_pathfile_hash)
       button_seleziona_filehash.place(x = 384,y = 200)
    
       pathlabel_file_hash = Label(self, background='#FFFFFF', width=55)
       pathlabel_file_hash.place(x = 50,y = 200)

       button_crea_hash = Button(self, text = "CREA HASH", command = crea_hash)
       button_crea_hash.place(x = 50,y = 230)

       label_hash4 = Label(self, text = "Stringa hash generata :")
       label_hash4.place(x = 40, y = 320)
       
       entry_stringa_hash = Text(self, width=65, height=1)
       entry_stringa_hash.place(x = 170,y = 320)


       

class MainView(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        p1 = HomePage(self)
        p2 = PageVerificaLunghezza(self)
        p3 = PageConfrontaFile(self)
        p4 = PageHash(self)

        s = Style()
        s.configure('My.TFrame', background='red',relief="ridge")
 
        buttonframe = Frame(self,style='My.TFrame')
        container = Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b0 = Label (buttonframe, text="Menù funzioni :", background='red', foreground='white')
        b1 = Button(buttonframe, text="HOME PAGE", command=p1.lift)
        b2 = Button(buttonframe, text="1)Record lenght", command=p2.lift)
        b3 = Button(buttonframe, text="2)Confronta file", command=p3.lift)
        b4 = Button(buttonframe, text="3)Hashing file", command=p4.lift)

        b0.pack(side="left")
        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        b4.pack(side="left")

        p1.show()

if __name__ == "__main__":
    root = Tk()
 
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)

    author = Label(root, text="Author : Mattia Pedroncelli - Copyright 'PEDRO Software©' ")
    author.pack(side="bottom")

    root.title("GUI PEDRO - SUPER FILE MANAGER")
    root.minsize(width=700, height=500)
    root.maxsize(width=700, height=500)
    
    root.mainloop()
