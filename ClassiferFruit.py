import os
import pickle
from tkinter import *
import numpy as np
from PIL import ImageTk, Image
from tkinter import filedialog, messagebox
import cv2
import Data_Classifer as svm

root = Tk()
root.geometry("500x500")
root.resizable(width=True, height=True)

def openfn():
    filename = filedialog.askopenfilename(title='open')
    return filename

def open_img():
    x = openfn()
    img = Image.open(x)
    img = img.resize((200, 200), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.place(x = 120, y = 150) # vị trí ảnh
    return x  # trả về đường dẫn

def prepare(filepath):
    img_array = cv2.imread(filepath, 0)  # đọc ảnh, chuyển thành ảnh xám
    img_array = cv2.resize(img_array, (50, 50))  # thay đổi kích thước hình ảnh để phù hợp với kích thước ảnh cu mô hình
    return np.array(img_array).flatten()

def Evaluate():
    if (os.path.isfile(svm.location_data(1))):
        # đọc mô hình huấn luyện
        pick = open('.\\File\\model.sav', 'rb')
        model = pickle.load(pick)
        pick.close()

        prediction = model.predict([prepare(open_img())])

        error1 = Label(root, background='Orange', width=20, font=('Time New Roman', 10), text=svm.categories[prediction[0]])
        error1.place(x=170, y=430)
    else:
        messagebox.showerror('Thông báo', 'Mô hình chưa được tạo!')

label = Label(root, width= 32, font=('Time New Roman', 20), fg= 'red', text='PHÂN LOẠI TRÁI CÂY', bg='yellow')
label.place(y=1)

label1 = Label(root, width= 40, font=('Time New Roman', 12), fg= 'black', text='Hãy chọn ảnh một loại trái cây bạn muốn biết tên')
label1.place(x = 70, y=60)

btn6 = Button(root, text = 'Mở ảnh', width= 10, font=('Time New Roman', 10), activebackground='Light Blue',command=Evaluate)
btn6.place(x = 200, y = 100)

root.mainloop()