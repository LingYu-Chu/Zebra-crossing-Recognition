# USAGE
# python classify.py --model pokedex.model --labelbin lb.pickle --image examples/charmander_counter.png

# import the necessary packages
from PIL import Image, ImageTk # 導入圖像處理函數庫
import matplotlib.pyplot as plt # 繪圖庫
import numpy as np
import tkinter as tk           # 介面
import tkinter.filedialog
import os.path
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import imutils
import pickle
import cv2
import os

# 設定窗口大小命名
window = tk.Tk()
window.title('AIP 60847017S')
window.geometry('1000x700')
global img_png, image, nim, show_hist            # 定義img_png
var = tk.StringVar()    
width = 300
'''
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model",  type=str, default="a.model",
	help="path to trained model model")
ap.add_argument("-l", "--labelbin", type=str, default="lb.pickle",
	help="path to label binarizer")
ap.add_argument("-i", "--image", type=str, default = "",
	help="path to input image")

args = vars(ap.parse_args())
'''
# 打開圖像 顯示圖像
def Open_Img():
    global img_png, img, img_name, filename
    filename = tkinter.filedialog.askopenfilename(filetypes = [("Image files",("*.jpg","*.jpeg","*.ppm","*.bmp"))])
    img_name = os.path.basename(filename)
    print('檔名：' + os.path.basename(filename))
    img = Image.open(filename)
	#args["image"] = filename

    ratio = float(width)/img.size[0] # 寬300 
    height = int(img.size[1]*ratio) # 以原始比率調整整張大小
    nim = img.resize( (width, height), Image.BILINEAR ) #得到新的尺寸圖片
    img_png = ImageTk.PhotoImage(nim)
    label_Img = tk.Label(window, image = img_png)
    label_Img.place(x = 100, y = 120) # 第一張圖的位置

def load_image():
	global show_zebra, filename, recognition_img
	# load the image
	image = cv2.imread(filename)
	output = image.copy()
	
	# pre-process the image for classification
	image = cv2.resize(image, (96, 96))
	image = image.astype("float") / 255.0
	image = img_to_array(image)
	image = np.expand_dims(image, axis=0)

	# load the trained convolutional neural network and the label
	# binarizer
	print("[INFO] loading network...")
	model = load_model("a.model")
	lb = pickle.loads(open("lb.pickle", "rb").read())

	# classify the input image
	print("[INFO] classifying image...")
	proba = model.predict(image)[0]
	idx = np.argmax(proba)
	label = lb.classes_[idx]

	# we'll mark our prediction as "correct" of the input image filename
	# contains the predicted label text (obviously this makes the
	# assumption that you have named your testing image files this way)
	filenames = filename[filename.rfind(os.path.sep) + 1:]
	#correct = "correct" if filename.rfind(label) != -1 else "incorrect"

	correct = "correct" if filenames.rfind(label) != -1 else "incorrect"



	# build the label and draw the label on the image
	#label = "{}: {:.2f}% ({})".format(label, proba[idx] * 100, correct)

	label = "{}: {:.2f}% ".format(label, proba[idx] * 100)
	output = imutils.resize(output, width=400)
	cv2.putText(output, label, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,
		0.7, (0, 255, 0), 2)

	# show the output image
	print("[INFO] {}".format(label))
	
	#cv2.imshow("Output", output)
	#cv2.waitKey(0)
	cv2.imwrite("./outpute.jpg", output)	
	recognition_img = Image.open('outpute.jpg')

	ratio = float(400) / recognition_img.size[0] # 寬300 
	height = int(recognition_img.size[1]*ratio) # 以原始比率調整整張大小 
	recognition_img_im = recognition_img.resize( (width, height), Image.BILINEAR ) # 得到新的尺寸圖片
	
	show_zebra= ImageTk.PhotoImage(recognition_img)
	label_Img3= tk.Label(window, image = show_zebra)
	label_Img3.place(x = 450, y = 100) #第二張圖的位置

# 創建打開影像按鈕 
btn_Open = tk.Button(window,
    text = '選擇圖像',      
    width = 13, height = 2,
    command = Open_Img)     # 執行open img
btn_Open.place(x = 100, y = 20)    # 按鈕位置

# 創建按鈕
btn_Open = tk.Button(window,
    text = '斑馬線辨識',      
    width = 13, height = 2,
    command = load_image)     # 執行open img
btn_Open.place(x = 250, y = 20)    # 按鈕位置

# 運行整體窗口
window.mainloop()