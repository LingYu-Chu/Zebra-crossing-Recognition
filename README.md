# Zebra-crossing-Recognition
#Step1. 建立圖集
  – 498張斑馬線圖+121張無斑馬線圖
#Step2. 架構
  • dataset:包含了需要訓練的種類
  • examples:包含了我們將要用來測試CNN的圖
  • pyimagesearch模塊:包含了SmallerVGGNet模型
  • lb.pickle:LabelBinarizer序列化的目標文件
  • a.model:這是我們序列化的Keras卷積神經網絡的模型文件(即權值文件)
  • train.py:我們將用這個腳本來訓練我們的Keras CNN，劃分準確率/失敗率，然後將CNN和標籤二值序列化於磁碟上。
  • classify.py:測試腳本   
 #Step2. VGGNet
 「SmallerVGGNet」的 VGGNet類神經網絡， 它將被用於和Keras一 起訓練一個深度學習分類器。
• train.py – 80%training, 20%testing
• EPOCHS = 100將要訓練的網絡總epoch次數。
• INIT_LR:開始的學習率——1e-3是我們將用於訓練網絡的Adam優化器的初始值
