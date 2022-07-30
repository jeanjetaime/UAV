# from PyQt5 import QtWidgets, uic
# import sys
# import os
from PyQt5.QtWidgets import QMainWindow, QApplication

# 导入pyUIC转化出来的.py文件,Ui_Form就是转化出的.py文件的类名
from uav2 import Ui_MainWindow
from ImageBox import ImageBox

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
# from PyQt5.QtCore import Qt, QRect, QEvent, QPoint
# from PyQt5.Qt import QCursor, QPropertyAnimation
# from qt_material import apply_stylesheet
from Algorithm import *
from lxml import etree
import time
from draw_line import draw_line
from shutil import copyfile
# SCREEN_WEIGHT = 1920
# SCREEN_HEIGHT = 1080

X1 = 0
Y1 = 0
X2 = 0
Y2 = 0
class Ui(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        self.moved = False
        super(Ui, self).__init__(parent)
        self.setupUi(self)
        self.resize(449, 763)
        self.actionsss.setShortcut('Alt+E')
        self.action_R.setShortcut('Alt+R')
        self.actionsss.triggered.connect(self.readFans)
        self.action_R.triggered.connect(self.generate_XML)
        self.groupBox = ImageBox()
        self.groupBox.setObjectName("groupBox")
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)
        self.pushButton_2.clicked.connect(self.large_click)
        self.pushButton_3.clicked.connect(self.small_click)

    """贴边"""
    # def enterEvent(self, event):
    #     self.hide_or_show('show', event)
    # def leaveEvent(self, event):
    #     self.hide_or_show('hide', event)
    # def mousePressEvent(self, event):
    #     if event.button() == Qt.LeftButton:
    #         self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
    #     QApplication.postEvent(self, QEvent(174))
    #     event.accept()
    # def mouseMoveEvent(self, event):
    #     if event.buttons() == Qt.LeftButton:
    #         try:
    #             self.move(event.globalPos() - self.dragPosition)
    #             event.accept()
    #         except:pass
    # def mouseReleaseEvent(self, event):
    #     self.moved = True
    #     self.hide_or_show('show', event)
    """贴边"""
    # def open_image(self):
    #     """
    #     select image file and open it
    #     :return:
    #     """
    #     # img_name, _ = QFileDialog.getOpenFileName(self, "打开图片", "", "All Files(*);;*.jpg;;*.png")
    #     img_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open Image File","","All Files(*);;*.jpg;;*.png;;*.jpeg")
    #     self.groupBox.set_image(img_name)

    def large_click(self):
        """
        used to enlarge image
        :return:
        """
        if self.groupBox.scale < 2:
            self.groupBox.scale += 0.1
            self.groupBox.adjustSize()
            self.update()

    def small_click(self):
        """
        used to reduce image
        :return:
        """
        if self.groupBox.scale > 0.3:
            self.groupBox.scale -= 0.2
            self.groupBox.adjustSize()
            self.update()

    def resizeEvent(self, event):
        self.tableWidget.setGeometry(self.frame.geometry())

    """贴边"""
    # def hide_or_show(self, mode, event):
    #     WINDOW_WEIGHT = self.size().width()
    #     WINDOW_HEIGHT = self.size().height()
    #     pos = self.frameGeometry().topLeft()
    #     if mode == 'show' and self.moved:
    #         if pos.x() + WINDOW_WEIGHT >= SCREEN_WEIGHT: # 右侧显示
    #             self.startAnimation(SCREEN_WEIGHT - WINDOW_WEIGHT + 2, pos.y())
    #             event.accept()
    #             self.moved = False
    #         elif pos.x() <= 0: # 左侧显示
    #             self.startAnimation(0,pos.y())
    #             event.accept()
    #             self.moved = False
    #         elif pos.y() <= 0: # 顶层显示
    #             self.startAnimation(pos.x(),0)
    #             event.accept()
    #             self.moved = False
    #     elif mode == 'hide':
    #         if pos.x() + WINDOW_WEIGHT >= SCREEN_WEIGHT: # 右侧隐藏
    #             self.startAnimation(SCREEN_WEIGHT - 2,pos.y())
    #             event.accept()
    #             self.moved = True
    #         elif pos.x() <= 2: # 左侧隐藏
    #             self.startAnimation(2 - WINDOW_WEIGHT,pos.y())
    #             event.accept()
    #             self.moved = True
    #         elif pos.y() <= 2: # 顶层隐藏
    #             self.startAnimation(pos.x(),2 - WINDOW_HEIGHT)
    #             event.accept()
    #             self.moved = True
    # def startAnimation(self,width,height):
    #     animation = QPropertyAnimation(self,b"geometry",self)
    #     startpos = self.geometry()
    #     animation.setDuration(200)
    #     newpos = QRect(width,height,startpos.width(),startpos.height())
    #     animation.setEndValue(newpos)
    #     animation.start()
    """贴边"""
    def readFans(self):
        lon = []
        lat = []
        height = []
        speed = []
        task = []
        taskParam = []
        flymode = []
        flymodeParam = []
        surround = []
        radius = []
        ID = []
        result = []
        fname, ftype = QtWidgets.QFileDialog.getOpenFileName(self, "打开风场信息文件：.txt", "./", "Txt (*.txt)")
        # 打开文件 返回一个字符串第一个是路径， 第二个是要打开文件的类型
        # 如果用户主动关闭文件对话框，则返回值为空
        if fname:  # 判断路径非空
            # open()会自动返回一个文件对象
            with open(fname, "r", encoding='utf-8') as f:  # 打开路径所对应的文件， "r"以只读的方式 也是默认的方式
                for line in f:
                    result.append(line.strip('\n'))
                length = int((len(result) - 4) / 11)
                global X1
                X1 = result[0]
                global Y1
                Y1 = result[1]
                global X2
                X2 = result[2]
                global Y2
                Y2 = result[3]
                global len_blade
                len_blade = result[4]
                for i in range(length):
                    lon.append(result[i * 11 + 5])
                    lat.append(result[i * 11 + 6])
                    height.append(result[i * 11 + 7])
                    speed.append(result[i * 11 + 8])
                    task.append(result[i * 11 + 9])
                    taskParam.append(result[i * 11 + 10])
                    flymode.append(result[i * 11 + 11])
                    flymodeParam.append(result[i * 11 + 12])
                    surround.append(result[i * 11 + 13])
                    radius.append(result[i * 11 + 14])
                    ID.append(result[i * 11 + 15])
                for i in range(len(lon)):
                    self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(ID[i]))
                    self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(lon[i]))
                    self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(lat[i]))
                    self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(height[i]))
                    self.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(speed[i]))
                    self.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(task[i]))
                    self.tableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(taskParam[i]))
                    self.tableWidget.setItem(i, 7, QtWidgets.QTableWidgetItem(flymode[i]))
                    self.tableWidget.setItem(i, 8, QtWidgets.QTableWidgetItem(flymodeParam[i]))
                    self.tableWidget.setItem(i, 9, QtWidgets.QTableWidgetItem(surround[i]))
                    self.tableWidget.setItem(i, 10, QtWidgets.QTableWidgetItem(radius[i]))
        # img_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open Image File", "",
        #                                                     "All Files(*);;*.jpg;;*.png;;*.jpeg")
            copyfile('./map/' + self.tableWidget.item(0, 0).text(), './th.png')
            img_name = self.tableWidget.item(0, 0).text()
            self.groupBox.set_image(img_name)

    def generate_XML(self):
        copyfile('./map/' + self.tableWidget.item(0, 0).text(), './th.png')
        """
        生成XML文件
        :param coordinate:
        :return:
        """
        coordinate = []
        lonList1 = []
        latList1 = []
        num = 0
        while self.tableWidget.item(num, 1) != None:
            num = num + 1
        for i in range(num):
            temp_value1 = float(self.tableWidget.item(i, 1).text())
            temp_value2 = float(self.tableWidget.item(i, 2).text())
            coordinate.append([temp_value1, temp_value2])
            lonList1.append(temp_value1)
            latList1.append(temp_value2)
        new_coordinate = lonlat2meter(coordinate)
        best_solution = main(coordinate)


        def func(list):
            index = list.index(0)
            new_list = []
            for i in range(index, len(list)):
                new_list.append(list[i])
            for i in range(index):
                new_list.append(list[i])
            return new_list

        def angle(v1, v2):
            dx1 = v1[2] - v1[0]
            dy1 = v1[3] - v1[1]
            dx2 = v2[2] - v2[0]
            dy2 = v2[3] - v2[1]
            angle1 = math.atan2(dy1, dx1)
            angle1 = int(angle1 * 180 / math.pi)
            # print(angle1)
            angle2 = math.atan2(dy2, dx2)
            angle2 = int(angle2 * 180 / math.pi)
            included_angle = angle2 - angle1
            return included_angle

        best_solution = func(best_solution)
        lonList = []
        latList = []
        for i in range(len(best_solution)):
            lonList.append(lonList1[best_solution[i]])
            latList.append(latList1[best_solution[i]])
        lonList.append(lonList1[best_solution[0]])
        latList.append(latList1[best_solution[0]])
        best_solution.append(best_solution[0])

        angle_list = []
        for m in range(1, len(best_solution) - 1):
            v1 = [lonList[m - 1], latList[m - 1], lonList[m], latList[m]]
            v2 = [lonList[m], latList[m], lonList[m + 1], latList[m + 1]]
            if angle(v1, v2) > 0:
                angle_list.append(-1)
            else:
                angle_list.append(1)
        print(angle_list)
        print(best_solution)
        print(lonList)
        print(latList)
        global X1, Y1, X2, Y2
        X1 = float(X1)
        Y1 = float(Y1)
        X2 = float(X2)
        Y2 = float(Y2)
        draw_line(lonList, latList, self.tableWidget.item(0, 0).text(), X1, Y1, X2, Y2)
        self.groupBox.set_image(self.tableWidget.item(0, 0).text())


        listLon1 = []
        listLat1 = []

        listLon2 = []
        listLat2 = []

        for i in range(3):
            listLon1.append(lonList[i])
            listLat1.append(latList[i])
        listLon1.append(lonList[0])
        listLat1.append(latList[0])
        if len(lonList) > 4:
            for i in range(len(lonList) - 4):
                listLon2.append(lonList[i + 3])
                listLat2.append(latList[i + 3])
            listLon2.append(lonList[3])
            listLat2.append(latList[3])

        # F = MyFigure(4, 4, 100)
        # axes = F.fig.add_subplot(111)
        # axes.plot(listLon1, listLat1)
        # axes.scatter(listLon1, listLat1)
        # if len(lonList) > 4:
        #     axes.plot(listLon2, listLat2)
        #     axes.scatter(listLon2, listLat2)
        # QtWidgets.QGridLayout(self.groupBox).addWidget(F)

        # lon = 'lon = ['
        # lat = 'lat = ['
        # for i in range(len(lonList)):
        #     if i < len(lonList) - 1:
        #         lon = lon + str(lonList[i]) + ','
        #     else:
        #         lon = lon + str(lonList[i]) + '];'
        # for i in range(len(latList)):
        #     if i < len(latList) - 1:
        #         lat = lat + str(latList[i]) + ','
        #     else:
        #         lat = lat + str(latList[i]) + '];'
        # daima = "num = " + str(num) + ";"
        # self.graphicsView.page().runJavaScript(daima)
        # self.graphicsView.page().runJavaScript(lon)
        # self.graphicsView.page().runJavaScript(lat)
        # self.graphicsView.page().runJavaScript('plot();')

        root = etree.Element('Root')
        ItemNode = etree.SubElement(root, 'Item')
        skyNode = etree.SubElement(ItemNode, 'SkywayNo')
        skyNode.text = '0'
        idAllNumNode = etree.SubElement(ItemNode, 'IdAllNum')
        idAllNumNode.text = str(num + 1)
        timeNode = etree.SubElement(ItemNode, 'CreateTimer')
        timeNode.text = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        global len_blade
        len_blade = float(len_blade)

        for i in range(num + 1):
            # 寻找当前点顺序是初始顺序的第几个
            if (i == num):
                ItemINode = etree.SubElement(root, 'Item' + str(eval('i+1')))
                lonNode = etree.SubElement(ItemINode, 'Longitude')
                lonNode.text = self.tableWidget.item(best_solution[0], 1).text()
                latNode = etree.SubElement(ItemINode, 'Latitude')
                latNode.text = self.tableWidget.item(best_solution[0], 2).text()
                altiNode = etree.SubElement(ItemINode, 'Altitude')
                # altiNode.text = self.tableWidget.item(best_solution[0], 3).text()
                altitude_fan = float(self.tableWidget.item(best_solution[0], 3).text())
                altitude_uav = altitude_fan + float(len_blade)
                altitude_uav = str(altitude_uav)
                altiNode.text = altitude_uav
                altitude_uav = float(altitude_uav)
                speedNode = etree.SubElement(ItemINode, 'Speed')
                speedNode.text = self.tableWidget.item(best_solution[0], 4).text()
                modelNode = etree.SubElement(ItemINode, 'WaypointModel')
                if (self.tableWidget.item(best_solution[0], 7).text() == '水平环绕'):
                    modelNode.text = '6'
                if (self.tableWidget.item(best_solution[0], 7).text() == '悬停'):
                    modelNode.text = '2'
                if (self.tableWidget.item(best_solution[0], 7).text() == '协调转弯'):
                    modelNode.text = '1'
                modelNameNode = etree.SubElement(ItemINode, 'WaypointModelName')
                modelNameNode.text = self.tableWidget.item(best_solution[0], 7).text()
                modelParamsNode = etree.SubElement(ItemINode, 'WaypointModelTimer')
                if (self.tableWidget.item(best_solution[0], 7).text() == '协调转弯'):
                    modelParamsNode.text = self.tableWidget.item(best_solution[0], 8).text()
                else:
                    modelParamsNode.text = self.tableWidget.item(best_solution[0], 8).text()
                taskNode = etree.SubElement(ItemINode, 'WaypointTask')
                if (self.tableWidget.item(best_solution[0], 5).text() == '无任务'):
                    taskNode.text = '1'
                if (self.tableWidget.item(best_solution[0], 5).text() == '定距拍照'):
                    taskNode.text = '2'
                if (self.tableWidget.item(best_solution[0], 5).text() == '定时拍照'):
                    taskNode.text = '3'
                taskNameNode = etree.SubElement(ItemINode, 'WaypointTaskName')
                taskNameNode.text = self.tableWidget.item(best_solution[0], 5).text()
                taskParamsNode = etree.SubElement(ItemINode, 'WaypointTaskTimer')
                if (self.tableWidget.item(best_solution[0], 5).text() == '无任务'):
                    taskParamsNode.text = self.tableWidget.item(best_solution[0], 6).text()
                else:
                    taskParamsNode.text = self.tableWidget.item(best_solution[0], 6).text()
                levelNode = etree.SubElement(ItemINode, 'LevelAltitude')
                levelNode.text = '0'
                wptNode = etree.SubElement(ItemINode, 'WptHeading')
                if (modelNode.text == '6'):
                    wptNode.text = self.tableWidget.item(best_solution[0], 9).text()
                else:
                    wptNode.text = '0'
                altTypeNode = etree.SubElement(ItemINode, 'AltType')
                altTypeNode.text = '0'
                circleRNode = etree.SubElement(ItemINode, 'CircleR')
                circleRNode.text = self.tableWidget.item(best_solution[0], 10).text()
                targetYawNode = etree.SubElement(ItemINode, 'TargetYaw')
                targetYawNode.text = '0'
                targetPitchNode = etree.SubElement(ItemINode, 'TargetPitch')
                if modelNode.text == '6':
                    targetPitchNode.text = str(cal_gradient(altitude_uav, altitude_fan,
                                                            int(self.tableWidget.item(best_solution[0], 10).text())))
                else:
                    targetPitchNode.text = '0'
            else:
                ItemINode = etree.SubElement(root, 'Item' + str(eval('i+1')))
                lonNode = etree.SubElement(ItemINode, 'Longitude')
                lonNode.text = self.tableWidget.item(best_solution[i], 1).text()
                latNode = etree.SubElement(ItemINode, 'Latitude')
                latNode.text = self.tableWidget.item(best_solution[i], 2).text()
                altiNode = etree.SubElement(ItemINode, 'Altitude')
                altitude_fan = float(self.tableWidget.item(best_solution[0], 3).text())
                altitude_uav = altitude_fan + float(len_blade)
                altitude_uav = str(altitude_uav)
                altiNode.text = altitude_uav
                altitude_uav = float(altitude_uav)
                # altiNode.text = self.tableWidget.item(best_solution[i], 3).text()
                speedNode = etree.SubElement(ItemINode, 'Speed')
                speedNode.text = self.tableWidget.item(best_solution[i], 4).text()
                modelNode = etree.SubElement(ItemINode, 'WaypointModel')
                if (self.tableWidget.item(best_solution[i], 7).text() == '水平环绕'):
                    modelNode.text = '6'
                if (self.tableWidget.item(best_solution[i], 7).text() == '悬停'):
                    modelNode.text = '2'
                if (self.tableWidget.item(best_solution[i], 7).text() == '协调转弯'):
                    modelNode.text = '1'
                modelNameNode = etree.SubElement(ItemINode, 'WaypointModelName')
                modelNameNode.text = self.tableWidget.item(best_solution[i], 7).text()
                modelParamsNode = etree.SubElement(ItemINode, 'WaypointModelTimer')
                if (self.tableWidget.item(best_solution[i], 7).text() == '协调转弯'):
                    modelParamsNode.text = self.tableWidget.item(best_solution[i], 8).text()
                else:
                    modelParamsNode.text = self.tableWidget.item(best_solution[i], 8).text()
                taskNode = etree.SubElement(ItemINode, 'WaypointTask')
                if (self.tableWidget.item(best_solution[i], 5).text() == '无任务'):
                    taskNode.text = '1'
                if (self.tableWidget.item(best_solution[i], 5).text() == '定距拍照'):
                    taskNode.text = '2'
                if (self.tableWidget.item(best_solution[i], 5).text() == '定时拍照'):
                    taskNode.text = '3'
                taskNameNode = etree.SubElement(ItemINode, 'WaypointTaskName')
                taskNameNode.text = self.tableWidget.item(best_solution[i], 5).text()
                taskParamsNode = etree.SubElement(ItemINode, 'WaypointTaskTimer')
                if (self.tableWidget.item(best_solution[i], 5).text() == '无任务'):
                    taskParamsNode.text = self.tableWidget.item(best_solution[i], 6).text()
                else:
                    taskParamsNode.text = self.tableWidget.item(best_solution[i], 6).text()
                levelNode = etree.SubElement(ItemINode, 'LevelAltitude')
                levelNode.text = '0'
                wptNode = etree.SubElement(ItemINode, 'WptHeading')
                if (modelNode.text == '6'):
                    wptNode.text = self.tableWidget.item(best_solution[i], 9).text()
                else:
                    wptNode.text = '0'
                altTypeNode = etree.SubElement(ItemINode, 'AltType')
                altTypeNode.text = '0'
                circleRNode = etree.SubElement(ItemINode, 'CircleR')
                if (i == 0):
                    circleRNode.text = self.tableWidget.item(best_solution[i], 10).text()
                else:
                    circleRNode.text = str(angle_list[i - 1] * int(self.tableWidget.item(best_solution[i], 10).text()))
                targetYawNode = etree.SubElement(ItemINode, 'TargetYaw')
                targetYawNode.text = '0'
                targetPitchNode = etree.SubElement(ItemINode, 'TargetPitch')
                if modelNode.text == '6':
                    targetPitchNode.text = str(cal_gradient(altitude_uav, altitude_fan,
                                                            int(self.tableWidget.item(best_solution[i],
                                                                                   10).text())))
                else:
                    targetPitchNode.text = '0'
        tree = etree.ElementTree(root)
        fxml1, ftype1 = QtWidgets.QFileDialog.getSaveFileName(self, "Write File", "./", "All (*.*)")
        if fxml1:
            tree.write(fxml1, pretty_print=True, xml_declaration=True, encoding='utf-8')
        if num > 3:
            fxml2, ftype2 = QtWidgets.QFileDialog.getSaveFileName(self, "Write File", "./", "All (*.*)")
            if fxml2:
                tree.write(fxml2, pretty_print=True, xml_declaration=True, encoding='utf-8')
        # fxml3, ftype3 = QtWidgets.QFileDialog.getSaveFileName(self.page1, "Write File", "./", "All (*.*)")
        # if fxml3:
        #     tree.write(fxml3, pretty_print=True, xml_declaration=True, encoding='utf-8')

        fw = open('serial_num.txt', 'w')
        for i in range(num):
            fw.write(str(i + 1))
            fw.write(' ')
        fw.write('\n')
        for i in range(num):
            fw.write(self.tableWidget.item(i, 1).text())
            fw.write(' ')
            fw.write(self.tableWidget.item(i, 2).text())
            fw.write(' ')

# class MyFigure(FigureCanvas):
#     def __init__(self, width=5, height=4, dpi=100):
#         # 第一步：创建一个创建Figure
#         self.fig = Figure(figsize=(width, height), dpi=dpi)
#         # 第二步：在父类中激活Figure窗口
#         super(MyFigure, self).__init__(self.fig)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    # apply_stylesheet(app, theme='dark_teal.xml')
    window.show()
    sys.exit(app.exec_())