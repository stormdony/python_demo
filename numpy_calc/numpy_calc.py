# -*- coding: utf-8 -*-
#
# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Author: Don Lex
# 微信公众号:Python绿洲
# 欢迎交流讨论
# 引用代码请注明出处,谢谢
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 编译环境:
# python       3.5.4
# numpy        1.14.2
# PyQt5        5.10.1
# PyInstaller  3.3.1
# PyQt5-sip    4.19.12
# pyqt5-tools  5.9.0
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication
import numpy as np
from numpy.linalg import det, inv, solve


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMaximumSize(QtCore.QSize(800, 635))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 140, 431, 381))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_row1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_row1.setObjectName("lineEdit_row1")
        self.gridLayout.addWidget(self.lineEdit_row1, 1, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.gridLayout.addWidget(self.lineEdit_1, 0, 1, 1, 1)
        self.lineEdit_row2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_row2.setObjectName("lineEdit_row2")
        self.gridLayout.addWidget(self.lineEdit_row2, 3, 1, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(520, 140, 221, 381))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_inv = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_inv.setObjectName("btn_inv")
        self.gridLayout_2.addWidget(self.btn_inv, 2, 0, 1, 1)
        self.btn_clear = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_clear.setObjectName("btn_clear")
        self.gridLayout_2.addWidget(self.btn_clear, 0, 0, 1, 1)
        self.btn_dot = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_dot.setObjectName("btn_dot")
        self.gridLayout_2.addWidget(self.btn_dot, 4, 0, 1, 1)
        self.btn_solve = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_solve.setObjectName("btn_solve")
        self.gridLayout_2.addWidget(self.btn_solve, 5, 0, 1, 1)
        self.btn_det = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_det.setObjectName("btn_det")
        self.gridLayout_2.addWidget(self.btn_det, 1, 0, 1, 1)
        self.btn_t = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_t.setObjectName("btn_t")
        self.gridLayout_2.addWidget(self.btn_t, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 480, 351, 61))
        self.label_5.setObjectName("label_5")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(60, 10, 681, 131))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit_result1 = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.textEdit_result1.setObjectName("textEdit_result1")
        self.horizontalLayout.addWidget(self.textEdit_result1)
        self.textEdit_result2 = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.textEdit_result2.setObjectName("textEdit_result2")
        self.horizontalLayout.addWidget(self.textEdit_result2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 31))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "行,列"))
        self.label_2.setText(_translate("MainWindow", "行,列"))
        self.label.setText(_translate("MainWindow", "矩阵一"))
        self.label_3.setText(_translate("MainWindow", "矩阵二"))
        self.btn_inv.setText(_translate("MainWindow", "矩阵的逆"))
        self.btn_clear.setText(_translate("MainWindow", "归零"))
        self.btn_dot.setText(_translate("MainWindow", "矩阵乘法"))
        self.btn_solve.setText(_translate("MainWindow", "解矩阵方程"))
        self.btn_det.setText(_translate("MainWindow", "行列式"))
        self.btn_t.setText(_translate("MainWindow", "转置"))
        self.label_5.setText(_translate("MainWindow", "矩阵：从左到右依次输入,用逗号隔开\n"
                                                      "行列：用逗号隔开,例如:3行4列->3,4"))
        self.textEdit_result1.setHtml(_translate("MainWindow",
                                                 "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                 "p, li { white-space: pre-wrap; }\n"
                                                 "</style></head><body style=\" font-family:\'SimSun\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
                                                 "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">矩阵一的结果</p></body></html>"))
        self.textEdit_result2.setHtml(_translate("MainWindow",
                                                 "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                 "p, li { white-space: pre-wrap; }\n"
                                                 "</style></head><body style=\" font-family:\'SimSun\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
                                                 "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">矩阵二的结果</p></body></html>"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        #
        # 以上为UI文件转换内容
        # 以下为添加内容
        #
        self.actionAbout.triggered.connect(self.show_my_window)  # 绑定事件

    def show_my_window(self):
        '''
        帮助弹出页面
        :return:
        '''
        QMessageBox.about(self, "About", '''<html>
    <style>
    h3{
    margin:20px;
    font-size:18px;
    font-weight:800
    }
    p{
    margin:20px;
    font-size:12px;
    font-weight:500
    }
    </style>
    <body>
    <h3>矩阵计算器</h3>
    <p>简介:  一个基于Numpy和PyQt编写的轻量级矩阵计算器,可以快速的计算出矩阵的结果</p>
    <p>版本:  1.0.0</p>
    <p>作者:   <a href="https://github.com/stormdony">Don Lex </a></p>
    <p>反馈邮箱: stormdony@foxmail.com</p>
    <p>项目地址:  <a href="https://github.com/stormdony/python_demo">https://github.com/stormdony/python_demo/numpy_demo</a></p>
    </body>
    </html>

    ''')


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.btn_dot.clicked.connect(self.dot_func)  # 矩阵乘积按钮绑定事件
        self.btn_solve.clicked.connect(self.solve_func)  # 解矩阵方程按钮绑定事件
        self.btn_t.clicked.connect(self.t_func)  # 矩阵转置按钮绑定事件
        self.btn_inv.clicked.connect(self.inv_func)  # 矩阵的逆按钮绑定事件
        self.btn_det.clicked.connect(self.det_func)  # 矩阵的行列式按钮绑定事件
        self.btn_clear.clicked.connect(self.clear_func)  # 归零按钮绑定事件

    def dot_func(self):
        ''''
        矩阵的乘积
        '''
        line1 = self.lineEdit_1.text()
        line2 = self.lineEdit_2.text()
        row1 = self.lineEdit_row1.text()
        row2 = self.lineEdit_row2.text()
        try:
            linelist1, rowlist1 = to_array(line1, row1)
            linelist2, rowlist2 = to_array(line2, row2)
            # 修正错误的输入
            self.lineEdit_1.setText(str(linelist1)[1:-1])
            self.lineEdit_row1.setText(str(rowlist1)[1:-1])
            self.lineEdit_2.setText(str(linelist2)[1:-1])
            self.lineEdit_row2.setText(str(rowlist2)[1:-1])

            A = np.array(linelist1).reshape(rowlist1)
            B = np.array(linelist2).reshape(rowlist2)
            txt = '矩阵的乘积:\n' + str(A.dot(B))
            self.textEdit_result1.setText(txt)
        except:
            A_text = '请检查矩阵'
            self.textEdit_result1.setText(A_text)
            self.textEdit_result2.setText(A_text)

    def solve_func(self):
        ''''
        解矩阵方程
        '''
        line1 = self.lineEdit_1.text()
        line2 = self.lineEdit_2.text()
        row1 = self.lineEdit_row1.text()
        row2 = self.lineEdit_row2.text()
        try:
            linelist1, rowlist1 = to_array(line1, row1)
            linelist2, rowlist2 = to_array(line2, row2)
            # 修正错误的输入
            self.lineEdit_1.setText(str(linelist1)[1:-1])
            self.lineEdit_row1.setText(str(rowlist1)[1:-1])
            self.lineEdit_2.setText(str(linelist2)[1:-1])
            self.lineEdit_row2.setText(str(rowlist2)[1:-1])

            A = np.array(linelist1).reshape(rowlist1)
            B = np.array(linelist2).reshape(rowlist2)
            txt = '矩阵的解:\n' + str(solve(A, B))
            self.textEdit_result1.setText(txt)
        except:
            A_text = '矩阵错误或无解'
            self.textEdit_result1.setText(A_text)
            self.textEdit_result2.setText(A_text)

    def t_func(self):
        '''
        矩阵转置
        '''
        line1 = self.lineEdit_1.text()
        line2 = self.lineEdit_2.text()
        row1 = self.lineEdit_row1.text()
        row2 = self.lineEdit_row2.text()
        try:
            linelist1, rowlist1 = to_array(line1, row1)
            # 修正错误
            self.lineEdit_1.setText(str(linelist1)[1:-1])
            self.lineEdit_row1.setText(str(rowlist1)[1:-1])

            A = np.array(linelist1).reshape(rowlist1)
            txt = '矩阵一的转置:\n' + str(A.T)
            self.textEdit_result1.setText(txt)
        except:
            A_text = '请检查矩阵一'
            self.textEdit_result1.setText(A_text)
        try:
            linelist2, rowlist2 = to_array(line2, row2)
            # 修正错误
            self.lineEdit_2.setText(str(linelist2)[1:-1])
            self.lineEdit_row2.setText(str(rowlist2)[1:-1])
            B = np.array(linelist2).reshape(rowlist2)
            txt = '矩阵二的转置:\n' + str(B.T)
            self.textEdit_result2.setText(txt)
        except:
            self.textEdit_result2.setText("请检查矩阵二")

    def inv_func(self):
        '''
        矩阵的逆
        '''
        line1 = self.lineEdit_1.text()
        line2 = self.lineEdit_2.text()
        row1 = self.lineEdit_row1.text()
        row2 = self.lineEdit_row2.text()
        try:
            linelist1, rowlist1 = to_array(line1, row1)
            # 修正错误
            self.lineEdit_1.setText(str(linelist1)[1:-1])
            self.lineEdit_row1.setText(str(rowlist1)[1:-1])
            A = np.array(linelist1).reshape(rowlist1)
            txt = '矩阵一的逆:\n' + str(inv(A))
            self.textEdit_result1.setText(txt)
        except:
            A_text = '矩阵一错误或无解'
            self.textEdit_result1.setText(A_text)
        try:
            linelist2, rowlist2 = to_array(line2, row2)
            # 修正错误
            self.lineEdit_2.setText(str(linelist2)[1:-1])
            self.lineEdit_row2.setText(str(rowlist2)[1:-1])
            B = np.array(linelist2).reshape(rowlist2)
            txt = '矩阵二的逆:\n' + str(inv(B))
            self.textEdit_result2.setText(txt)
        except:
            self.textEdit_result2.setText("矩阵二错误或无解")

    def det_func(self):
        '''
        矩阵的行列式
        '''
        line1 = self.lineEdit_1.text()
        line2 = self.lineEdit_2.text()
        row1 = self.lineEdit_row1.text()
        row2 = self.lineEdit_row2.text()
        try:
            linelist1, rowlist1 = to_array(line1, row1)
            # 修正错误
            self.lineEdit_1.setText(str(linelist1)[1:-1])
            self.lineEdit_row1.setText(str(rowlist1)[1:-1])

            A = np.array(linelist1).reshape(rowlist1)
            txt = '矩阵一的行列式:\n' + str(det(A))[:4]
            self.textEdit_result1.setText(txt)
        except:
            A_text = '矩阵一错误或无解'
            self.textEdit_result1.setText(A_text)
        try:
            linelist2, rowlist2 = to_array(line2, row2)
            # 修正错误
            self.lineEdit_2.setText(str(linelist2)[1:-1])
            self.lineEdit_row2.setText(str(rowlist2)[1:-1])
            B = np.array(linelist2).reshape(rowlist2)
            txt = '矩阵二的行列式:\n' + str(det(B))[:4]
            self.textEdit_result2.setText(txt)
        except:
            self.textEdit_result2.setText("矩阵二错误或无解")

    def clear_func(self):
        '''
        归零,清除文本内容
        '''
        self.lineEdit_1.clear()
        self.lineEdit_2.clear()
        self.lineEdit_row1.clear()
        self.lineEdit_row2.clear()


def to_array(text, row):
    '''
    将输入的数字转为矩阵
    :param text: 矩阵元素字符串
    :param row: 矩阵形态字符串
    :return: 元素列表,形态列表
    '''
    # 将中文逗号替换为英文逗号
    text = text.replace('，', ',')
    row = row.replace('，', ',')

    # 切除矩阵元素前后的逗号
    if text[-1] == ',':
        text = text[:-1]
    if text[0] == ',':
        text = text[1:]

    # 切除矩阵形态前后的逗号
    if row[-1] == ',':
        row = row[:-1]
    if row[0] == ',':
        row = row[1:]

    new = []
    rowlis = []
    numlist = text.split(',')
    # 将字符串转换为列表
    for i in range(len(numlist)):
        new.append(int(numlist[i]))
    rowlist = row.split(',')
    for i in range(len(rowlist)):
        rowlis.append(int(rowlist[i]))
    return new, rowlis


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
