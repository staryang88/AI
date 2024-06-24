import cv2
from PyQt5.QtWidgets import QApplication,QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *

from PyQt5 import QtCore, QtGui, QtWidgets
import waste_category
from PIL import Image

from yolo import YOLO
class Ui_MainWindow(QWidget):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(1065, 663)
                MainWindow.setStyleSheet("background-color: rgb(67, 152, 255)")
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(230, 20, 661, 101))
                self.label.setStyleSheet("font: 30pt \"微软雅黑\";\n"
                                         "color: rgb(255, 255, 255);")
                self.label.setObjectName("label")
                self.label_5 = QtWidgets.QLabel(self.centralwidget)
                self.label_5.setGeometry(QtCore.QRect(30, 70, 41, 51))
                self.label_5.setStyleSheet("font: 22pt \"微软雅黑\";\n"
                                           "color: rgb(255, 255, 255);")
                self.label_5.setObjectName("label_5")
                self.label_7 = QtWidgets.QLabel(self.centralwidget)
                self.label_7.setGeometry(QtCore.QRect(30, 20, 121, 31))
                self.label_7.setStyleSheet("font: 20pt \"微软雅黑\";\n"
                                           "color: rgb(255, 255, 255);")
                self.label_7.setObjectName("label_7")
                self.label_8 = QtWidgets.QLabel(self.centralwidget)
                self.label_8.setGeometry(QtCore.QRect(90, 100, 51, 21))
                self.label_8.setStyleSheet("font: 8pt \"微软雅黑\";\n"
                                           "color: rgb(255, 255, 255);")
                self.label_8.setObjectName("label_8")
                self.label_11 = QtWidgets.QLabel(self.centralwidget)
                self.label_11.setGeometry(QtCore.QRect(560, 170, 511, 431))
                self.label_11.setStyleSheet("image:url(1/白框区域.png);")
                self.label_11.setText("")
                self.label_11.setObjectName("label_11")
                self.label_25 = QtWidgets.QLabel(self.centralwidget)
                self.label_25.setGeometry(QtCore.QRect(10, 180, 591, 411))
                self.label_25.setStyleSheet("color: rgb(255, 255, 255);\n"
                                            "font: 36pt \"微软雅黑\";\n"
                                            "image: url(1/显示背景.png);\n"
                                            "")
                self.label_25.setText("")
                self.label_25.setAlignment(QtCore.Qt.AlignCenter)
                self.label_25.setObjectName("label_25")
                self.label_13 = QtWidgets.QLabel(self.centralwidget)
                self.label_13.setGeometry(QtCore.QRect(80, 220, 451, 331))
                self.label_13.setStyleSheet("background-color: transparent;\n"
                                            "background-color: teansparent;")
                self.label_13.setText("")
                self.label_13.setObjectName("label_13")
                self.file = QtWidgets.QPushButton(self.centralwidget)
                self.file.setGeometry(QtCore.QRect(10, 590, 61, 51))
                self.file.setStyleSheet("image: url(1/文件夹.png);\n"
                                        "background-color: transparent;")
                self.file.setText("")
                self.file.setObjectName("file")
                self.label_15 = QtWidgets.QLabel(self.centralwidget)
                self.label_15.setGeometry(QtCore.QRect(810, 360, 71, 31))
                self.label_15.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "font: 75 18pt \"Arial\";")
                self.label_15.setObjectName("label_15")
                self.label_16 = QtWidgets.QLabel(self.centralwidget)
                self.label_16.setGeometry(QtCore.QRect(810, 430, 71, 31))
                self.label_16.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "font: 75 18pt \"Arial\";")
                self.label_16.setObjectName("label_16")
                self.label_name = QtWidgets.QLabel(self.centralwidget)
                self.label_name.setGeometry(QtCore.QRect(890, 360, 91, 31))
                self.label_name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                              "font: 16pt \"Arial\";")
                self.label_name.setAlignment(QtCore.Qt.AlignCenter)
                self.label_name.setObjectName("label_name")
                self.label_type = QtWidgets.QLabel(self.centralwidget)
                self.label_type.setGeometry(QtCore.QRect(880, 430, 121, 31))
                self.label_type.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                              "font: 16pt \"Arial\";")
                self.label_type.setAlignment(QtCore.Qt.AlignCenter)
                self.label_type.setObjectName("label_type")
                self.label_type_2 = QtWidgets.QLabel(self.centralwidget)
                self.label_type_2.setGeometry(QtCore.QRect(760, 210, 131, 41))
                self.label_type_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                "font: 75 18pt \"Arial\";")
                self.label_type_2.setObjectName("label_type_2")
                self.line = QtWidgets.QFrame(self.centralwidget)
                self.line.setGeometry(QtCore.QRect(620, 280, 401, 3))
                self.line.setFrameShape(QtWidgets.QFrame.HLine)
                self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.line.setObjectName("line")
                self.line_2 = QtWidgets.QFrame(self.centralwidget)
                self.line_2.setGeometry(QtCore.QRect(620, 550, 401, 3))
                self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
                self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.line_2.setObjectName("line_2")
                self.small_pic = QtWidgets.QLabel(self.centralwidget)
                self.small_pic.setGeometry(QtCore.QRect(620, 340, 161, 141))
                self.small_pic.setStyleSheet("background-color: transparent;")
                self.small_pic.setText("")
                self.small_pic.setObjectName("small_pic")
                self.shutdown = QtWidgets.QPushButton(self.centralwidget)
                self.shutdown.setGeometry(QtCore.QRect(970, 610, 61, 51))
                self.shutdown.setStyleSheet("image: url(1/识别.png);\n"
                                            "background-color: transparent;")
                self.shutdown.setText("")
                self.shutdown.setObjectName("shutdown")
                self.camera = QtWidgets.QPushButton(self.centralwidget)
                self.camera.setGeometry(QtCore.QRect(890, 610, 61, 51))
                self.camera.setStyleSheet("image: url(1/相机 (2).png);\n"
                                          "background-color: transparent;")
                self.camera.setText("")
                self.camera.setObjectName("camera")
                self.label_11.raise_()
                self.label.raise_()
                self.label_5.raise_()
                self.label_7.raise_()
                self.label_8.raise_()
                self.label_25.raise_()
                self.label_13.raise_()
                self.file.raise_()
                self.small_pic.raise_()
                self.line.raise_()
                self.label_type.raise_()
                self.camera.raise_()
                self.shutdown.raise_()
                self.label_type_2.raise_()
                self.label_name.raise_()
                self.label_16.raise_()
                self.label_15.raise_()
                self.line_2.raise_()
                MainWindow.setCentralWidget(self.centralwidget)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)
                self.name_dict={
                        'xie':'废旧鞋子','jidanke':'鸡蛋壳',
                'shuibei':'水杯','xia':'虾壳','qingcai':'青菜','canjinzhi':'餐巾纸',
                'dao':'刀','wanou':'毛绒玩偶','xiguapi':'西瓜皮','chongdianbao':'充电宝','suliaodai':'塑料袋','qiaokeli':'巧克力',
                'wenduji':'温度计','naicha':'奶茶','zhiniaoku':'纸尿裤','diliao':'火锅底料','guo':'铁锅','baozhi':'报纸杂志',
                'jidankedddaa':'鸡蛋壳',
                'mifan':'米饭',
                'kouxiangtang':'口香糖',
                'zhibei':'纸杯',
                'dengpao':'灯泡',
                'yantou':'烟头',
                'yao':'药片',
                'chazuo':'插座',
                'baoxianmo':'保鲜膜',
                'bao':'包',
                'jiuping':'酒瓶',
                'neizang':'内脏',
                'yilaguan':'易拉罐',
                'wazi':'袜子',
                'huoji':'打火机',
                'dingzi':'铁钉',
                'xiangjiaopi':'香蕉皮',
                'mianbao':'面包',
                'yaqian':'牙签',
                'kouzhao':'口罩'
                }
                # 图像识别
                self.yolo = YOLO() #初始化网络
                self.timer_camera = QtCore.QTimer()  # 定义定时器，用于控制显示视频的帧率 循环倒计时
                self.cap = cv2.VideoCapture()  # 视频流
                self.CAM_NUM = 0  # 为0时表示视频流来自笔记本内置摄像头
                self.camera.clicked.connect(self.button_open_camera_clicked)  # 摄像头开启,倒计时6秒
                self.timer_camera.timeout.connect(self.show_camera)  # 若定时器结束，则调用show_camera()
                self.shutdown.clicked.connect(self.get_picture)  # 图像检测
                self.file.clicked.connect(self.loadImage)
                self.file_name=''

        #打开摄像头
        def button_open_camera_clicked(self):
            self.label_13.setStyleSheet("background: transparent;")
            if self.timer_camera.isActive() == False:  # 若定时器未启动
                    flag = self.cap.open(self.CAM_NUM)  # 参数是0，表示打开笔记本的内置摄像头，参数是视频文件路径则打开视频
                    if flag == False:  # flag表示open()成不成功
                            msg = QtWidgets.QMessageBox.warning(self, 'warning', "请检查相机于电脑是否连接正确",
                                                                buttons=QtWidgets.QMessageBox.Ok)
                    else:
                            self.timer_camera.start(30)  # 定时器开始计时30ms，结果是每过30ms从摄像头中取一帧显示

            else:
                    self.timer_camera.stop()  # 关闭定时器
                    self.cap.release()  # 释放视频流
                    self.label_13.clear()  # 清空视频显示区域

        #调用摄像头检测
        def show_camera(self):
            flag, self.image = self.cap.read()  # 从视频流中读取
            show = cv2.resize(self.image, (640, 480))  # 把读到的帧的大小重新设置为 640x480
            cv2.imwrite('camera.jpg',show)
            image = Image.open('camera.jpg')
            r_image = self.yolo.detect_image(image, crop=False, count=False)
            r_image.save('res.jpg')

            self.label_13.setPixmap(QPixmap('res.jpg'))
            with open('res.txt','r')as fb:
                rubbish_name=fb.read()
            print(rubbish_name)


            if rubbish_name != ' ':
                    inf_res = waste_category.main(rubbish_name)
                    self.display(inf_res)
            else:
                    self.label_name.setText('未知')
                    self.label_type.setText('未知垃圾')
                    self.small_pic.setPixmap(QPixmap('icon/unknow.png'))
        #图像检测
        def get_picture(self):
            # 模型调用
            image = Image.open(self.file_name)
            r_image = self.yolo.detect_image(image, crop=False, count=False)
            r_image.save('res.jpg')

            self.label_13.setPixmap(QPixmap('res.jpg'))

            with open('res.txt','r')as fb:
                rubbish_name=fb.read()
            print(rubbish_name)


            if rubbish_name != ' ':
                    inf_res = waste_category.main(rubbish_name)
                    self.display(inf_res)
            else:
                    self.label_name.setText('未知')
                    self.label_type.setText('未知垃圾')
                    self.small_pic.setPixmap(QPixmap('icon/unknow.png'))

        #把相关信息显示到界面上
        def display(self, inf):
                self.small_pic.setStyleSheet("")
                if inf == None:
                        self.label_name.setText('未知')
                        self.label_type.setText('未知垃圾')

                else:
                        if inf[1] == '其他垃圾':
                            self.small_pic.setPixmap(QPixmap('icon/qita.jpg'))
                        if inf[1] == '有害垃圾':
                            self.small_pic.setPixmap(QPixmap('icon/youhai.jpg'))
                        if inf[1] == '可回收物':
                            self.small_pic.setPixmap(QPixmap('icon/kehuishou.jpg'))
                        if inf[1] == '厨余垃圾':
                            self.small_pic.setPixmap(QPixmap('icon/chuyu.jpg'))



                        self.label_name.setText(self.name_dict[inf[0]])
                        self.label_type.setText(inf[1])

        # 加载图片
        def loadImage(self):
            # QtCore.QFileDialog.getOpenFileName()
            self.timer_camera.stop()  # 关闭定时器
            self.cap.release()  # 释放视频流
            self.label_13.clear()  # 清空视频显示区域
            self.file_name, _ = QFileDialog.getOpenFileName(self, '打开文件', '.', '图像文件(*.jpg *.png)')
            # self.label_13.setPixmap(QPixmap(fname))
            print(self.file_name)
            self.label_13.clear()
            self.label_13.setPixmap(QPixmap(self.file_name))
            # api方式
            # rubbish_name = img_recognition.main(fname)
            # self.category(rubbish_name)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.label.setText(_translate("MainWindow", "垃圾图像分类识别系统"))
                self.label_5.setText(_translate("MainWindow", "8"))
                self.label_7.setText(_translate("MainWindow", "2024/6"))
                self.label_8.setText(_translate("MainWindow", "星期六"))
                self.label_15.setText(_translate("MainWindow", "名称："))
                self.label_16.setText(_translate("MainWindow", "类别："))
                self.label_name.setText(_translate("MainWindow", ""))
                self.label_type.setText(_translate("MainWindow", ""))
                self.label_type_2.setText(_translate("MainWindow", "识别信息"))
if __name__ == '__main__':
        import sys

        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())

