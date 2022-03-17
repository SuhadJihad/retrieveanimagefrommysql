import mysql.connector
import tkinter as tk
from PIL import Image, ImageTk
import io
window = tk.Tk()
window.title(' MySQL أستخراج صورة من جدول')
window.option_add('*Font', 'Times 20')
def get():
   global img
   try:
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mydatabase"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT IMAGE FROM customers WHERE name='%s'"%edit.get())
    myresult = mycursor.fetchone()
    img = Image.open(io.BytesIO(myresult[0]))
    img=img.resize((100, 100))
    img = ImageTk.PhotoImage(img)
    label = tk.Label(master=frame, image=img,width=100,height=100)
    label.grid(row=0, column=3, padx=5, pady=5)
   except mysql.connector.Error as error:
    print("Failed to get from customer table {}".format(error))

   finally:
     if mydb.is_connected():
        mycursor.close()
        mydb.close()
        print("MySQL connection is closed")
    
frame = tk.Frame(master=window,relief=tk.SUNKEN,borderwidth=3)
labeln = tk.Label(master=frame,text='Student Name')
labeln.grid(row=0, column=0, padx=5, pady=5)
frame.grid(row=0, column=0, padx=5, pady=5)
edit=tk.Entry(master=frame,width=20)
edit.grid(row=0, column=1, padx=5, pady=5)
buttonl=tk.Button(master=frame,text='Get', command=get)
buttonl.grid(row=1, column=1, padx=5, pady=5)
window.geometry("600x200")
window.iconbitmap('D:\\Python\\student.ico')
window.mainloop()

