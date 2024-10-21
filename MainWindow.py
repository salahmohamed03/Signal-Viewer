# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt, QMimeData
from PySide6.QtWidgets import QListWidget, QHBoxLayout, QWidget, QPushButton ,QMainWindow
from Graph import Graph
from styleSheet import styleSheet

class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1514, 899)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 0))
        styleSheet(MainWindow)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.sidePar = QtWidgets.QVBoxLayout()
        self.sidePar.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.sidePar.setObjectName("sidePar")
        self.Channals = QtWidgets.QTabWidget(self.centralwidget)
        self.Channals.setMinimumSize(QtCore.QSize(350, 450))
        self.Channals.setMaximumSize(QtCore.QSize(400, 10000))
        self.Channals.setObjectName("Channals")
        self.C1_tap = QtWidgets.QWidget()
        self.C1_tap.setObjectName("C1_tap")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.C1_tap)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.playc1 = QtWidgets.QPushButton(self.C1_tap)
        self.playc1.setObjectName("playc1")
        self.verticalLayout_2.addWidget(self.playc1)
        self.stopc1 = QtWidgets.QPushButton(self.C1_tap)
        self.stopc1.setObjectName("stopc1")
        self.verticalLayout_2.addWidget(self.stopc1)
        self.replayc1 = QtWidgets.QPushButton(self.C1_tap)
        self.replayc1.setObjectName("replayc1")
        self.verticalLayout_2.addWidget(self.replayc1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 30)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.addsignal_c1 = QtWidgets.QPushButton(self.C1_tap)
        self.addsignal_c1.setObjectName("addsignal_c1")
        self.horizontalLayout_3.addWidget(self.addsignal_c1)
        self.addsignalc1_combo = QtWidgets.QComboBox(self.C1_tap)
        self.addsignalc1_combo.setObjectName("addsignalc1_combo")
        self.horizontalLayout_3.addWidget(self.addsignalc1_combo)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.checkBox_c1 = QtWidgets.QCheckBox(self.C1_tap)
        self.checkBox_c1.setCheckable(True)
        self.checkBox_c1.setObjectName("checkBox_c1")
        self.verticalLayout_2.addWidget(self.checkBox_c1)
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.label_5 = QtWidgets.QLabel(self.C1_tap)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_30.addWidget(self.label_5)
        self.choosesignalc1_combo = QtWidgets.QComboBox(self.C1_tap)
        self.choosesignalc1_combo.setEnabled(True)
        self.choosesignalc1_combo.setDuplicatesEnabled(False)
        self.choosesignalc1_combo.setObjectName("choosesignalc1_combo")
        self.horizontalLayout_30.addWidget(self.choosesignalc1_combo)
        self.verticalLayout_2.addLayout(self.horizontalLayout_30)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 10, -1, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_9 = QtWidgets.QLabel(self.C1_tap)
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.dial_slide_c1 = QtWidgets.QDial(self.C1_tap)
        self.dial_slide_c1.setObjectName("dial_slide_c1")
        self.verticalLayout_5.addWidget(self.dial_slide_c1)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_10 = QtWidgets.QLabel(self.C1_tap)
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_6.addWidget(self.label_10)
        self.dial_speed_c1 = QtWidgets.QDial(self.C1_tap)
        self.dial_speed_c1.setObjectName("dial_speed_c1")
        self.verticalLayout_6.addWidget(self.dial_speed_c1)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.Channals.addTab(self.C1_tap, "")
        self.C2_tap = QtWidgets.QWidget()
        self.C2_tap.setObjectName("C2_tap")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.C2_tap)
        self.verticalLayout.setObjectName("verticalLayout")
        self.playc2 = QtWidgets.QPushButton(self.C2_tap)
        self.playc2.setObjectName("playc2")
        self.verticalLayout.addWidget(self.playc2)
        self.stopc2 = QtWidgets.QPushButton(self.C2_tap)
        self.stopc2.setObjectName("stopc2")
        self.verticalLayout.addWidget(self.stopc2)
        self.replayc2 = QtWidgets.QPushButton(self.C2_tap)
        self.replayc2.setObjectName("replayc2")
        self.verticalLayout.addWidget(self.replayc2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 30)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.addsignalc2_btn = QtWidgets.QPushButton(self.C2_tap)
        self.addsignalc2_btn.setObjectName("addsignalc2_btn")
        self.horizontalLayout_4.addWidget(self.addsignalc2_btn)
        self.addsignalc2_combo = QtWidgets.QComboBox(self.C2_tap)
        self.addsignalc2_combo.setObjectName("addsignalc2_combo")
        self.horizontalLayout_4.addWidget(self.addsignalc2_combo)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.checkBox_c2 = QtWidgets.QCheckBox(self.C2_tap)
        self.checkBox_c2.setCheckable(True)
        self.checkBox_c2.setObjectName("checkBox_c2")
        self.verticalLayout.addWidget(self.checkBox_c2)
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.label_6 = QtWidgets.QLabel(self.C2_tap)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_31.addWidget(self.label_6)
        self.choosesignalc2_combo = QtWidgets.QComboBox(self.C2_tap)
        self.choosesignalc2_combo.setEnabled(True)
        self.choosesignalc2_combo.setDuplicatesEnabled(False)
        self.choosesignalc2_combo.setObjectName("choosesignalc2_combo")
        self.horizontalLayout_31.addWidget(self.choosesignalc2_combo)
        self.verticalLayout.addLayout(self.horizontalLayout_31)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 10, -1, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_11 = QtWidgets.QLabel(self.C2_tap)
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_7.addWidget(self.label_11)
        self.dial_slide_c2 = QtWidgets.QDial(self.C2_tap)
        self.dial_slide_c2.setObjectName("dial_slide_c2")
        self.verticalLayout_7.addWidget(self.dial_slide_c2)
        self.horizontalLayout_6.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_12 = QtWidgets.QLabel(self.C2_tap)
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_8.addWidget(self.label_12)
        self.dial_speed_c2 = QtWidgets.QDial(self.C2_tap)
        self.dial_speed_c2.setObjectName("dial_speed_c2")
        self.verticalLayout_8.addWidget(self.dial_speed_c2)
        self.horizontalLayout_6.addLayout(self.verticalLayout_8)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.Channals.addTab(self.C2_tap, "")
        self.C3_tap = QtWidgets.QWidget()
        self.C3_tap.setObjectName("C3_tap")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.C3_tap)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.play_c3 = QtWidgets.QPushButton(self.C3_tap)
        self.play_c3.setObjectName("play_c3")
        self.verticalLayout_3.addWidget(self.play_c3)
        self.stop_c3 = QtWidgets.QPushButton(self.C3_tap)
        self.stop_c3.setObjectName("stop_c3")
        self.verticalLayout_3.addWidget(self.stop_c3)
        self.replay_c3 = QtWidgets.QPushButton(self.C3_tap)
        self.replay_c3.setObjectName("replay_c3")
        self.verticalLayout_3.addWidget(self.replay_c3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, 30)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.addsignal_c3 = QtWidgets.QPushButton(self.C3_tap)
        self.addsignal_c3.setObjectName("addsignal_c3")
        self.horizontalLayout_7.addWidget(self.addsignal_c3)
        self.addsignalc3_combo = QtWidgets.QComboBox(self.C3_tap)
        self.addsignalc3_combo.setObjectName("addsignalc3_combo")
        self.horizontalLayout_7.addWidget(self.addsignalc3_combo)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.checkBox_c3 = QtWidgets.QCheckBox(self.C3_tap)
        self.checkBox_c3.setCheckable(True)
        self.checkBox_c3.setObjectName("checkBox_c3")
        self.verticalLayout_3.addWidget(self.checkBox_c3)
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.label_7 = QtWidgets.QLabel(self.C3_tap)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_32.addWidget(self.label_7)
        self.choosesignalc3_combo = QtWidgets.QComboBox(self.C3_tap)
        self.choosesignalc3_combo.setEnabled(True)
        self.choosesignalc3_combo.setDuplicatesEnabled(False)
        self.choosesignalc3_combo.setObjectName("choosesignalc3_combo")
        self.horizontalLayout_32.addWidget(self.choosesignalc3_combo)
        self.verticalLayout_3.addLayout(self.horizontalLayout_32)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(-1, 10, -1, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_13 = QtWidgets.QLabel(self.C3_tap)
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_13.setLineWidth(8)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_9.addWidget(self.label_13)
        self.dial_slide_c3 = QtWidgets.QDial(self.C3_tap)
        self.dial_slide_c3.setObjectName("dial_slide_c3")
        self.verticalLayout_9.addWidget(self.dial_slide_c3)
        self.horizontalLayout_8.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_14 = QtWidgets.QLabel(self.C3_tap)
        self.label_14.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_10.addWidget(self.label_14)
        self.dial_speed_c3 = QtWidgets.QDial(self.C3_tap)
        self.dial_speed_c3.setObjectName("dial_speed_c3")
        self.verticalLayout_10.addWidget(self.dial_speed_c3)
        self.horizontalLayout_8.addLayout(self.verticalLayout_10)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.Channals.addTab(self.C3_tap, "")
        self.C4_tap = QtWidgets.QWidget()
        self.C4_tap.setObjectName("C4_tap")
        self.verticalLayout_31 = QtWidgets.QVBoxLayout(self.C4_tap)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.play_c4 = QtWidgets.QPushButton(self.C4_tap)
        self.play_c4.setObjectName("play_c4")
        self.verticalLayout_31.addWidget(self.play_c4)
        self.stop_c4 = QtWidgets.QPushButton(self.C4_tap)
        self.stop_c4.setObjectName("stop_c4")
        self.verticalLayout_31.addWidget(self.stop_c4)
        self.replay_c4 = QtWidgets.QPushButton(self.C4_tap)
        self.replay_c4.setObjectName("replay_c4")
        self.verticalLayout_31.addWidget(self.replay_c4)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setContentsMargins(-1, 0, -1, 30)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.addsignal_c4 = QtWidgets.QPushButton(self.C4_tap)
        self.addsignal_c4.setObjectName("addsignal_c4")
        self.horizontalLayout_19.addWidget(self.addsignal_c4)
        self.addsignalc4_combo = QtWidgets.QComboBox(self.C4_tap)
        self.addsignalc4_combo.setObjectName("addsignalc4_combo")
        self.horizontalLayout_19.addWidget(self.addsignalc4_combo)
        self.verticalLayout_31.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setContentsMargins(-1, 0, -1, 50)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout()
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.label_39 = QtWidgets.QLabel(self.C4_tap)
        self.label_39.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_39.setAlignment(QtCore.Qt.AlignCenter)
        self.label_39.setObjectName("label_39")
        self.verticalLayout_29.addWidget(self.label_39)
        self.dial_slide_c4 = QtWidgets.QDial(self.C4_tap)
        self.dial_slide_c4.setObjectName("dial_slide_c4")
        self.verticalLayout_29.addWidget(self.dial_slide_c4)
        self.horizontalLayout_20.addLayout(self.verticalLayout_29)
        self.verticalLayout_30 = QtWidgets.QVBoxLayout()
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.label_40 = QtWidgets.QLabel(self.C4_tap)
        self.label_40.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_40.setObjectName("label_40")
        self.verticalLayout_30.addWidget(self.label_40)
        self.dial_speed_c4 = QtWidgets.QDial(self.C4_tap)
        self.dial_speed_c4.setObjectName("dial_speed_c4")
        self.verticalLayout_30.addWidget(self.dial_speed_c4)
        self.horizontalLayout_20.addLayout(self.verticalLayout_30)
        self.verticalLayout_31.addLayout(self.horizontalLayout_20)
        self.Channals.addTab(self.C4_tap, "")
        self.all_Channals = QtWidgets.QWidget()
        self.all_Channals.setObjectName("all_Channals")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.all_Channals)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.play_all_btn = QtWidgets.QPushButton(self.all_Channals)
        self.play_all_btn.setObjectName("play_all_btn")
        self.verticalLayout_4.addWidget(self.play_all_btn)
        self.stop_all_btn = QtWidgets.QPushButton(self.all_Channals)
        self.stop_all_btn.setObjectName("stop_all_btn")
        self.verticalLayout_4.addWidget(self.stop_all_btn)
        self.replay_all_btn = QtWidgets.QPushButton(self.all_Channals)
        self.replay_all_btn.setObjectName("replay_all_btn")
        self.verticalLayout_4.addWidget(self.replay_all_btn)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_15 = QtWidgets.QLabel(self.all_Channals)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_11.addWidget(self.label_15)
        self.dial_slide_btn = QtWidgets.QDial(self.all_Channals)
        self.dial_slide_btn.setObjectName("dial_slide_btn")
        self.verticalLayout_11.addWidget(self.dial_slide_btn)
        self.horizontalLayout_10.addLayout(self.verticalLayout_11)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_16 = QtWidgets.QLabel(self.all_Channals)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_12.addWidget(self.label_16)
        self.dial_speed_btn = QtWidgets.QDial(self.all_Channals)
        self.dial_speed_btn.setMinimumSize(QtCore.QSize(0, 100))
        self.dial_speed_btn.setObjectName("dial_speed_btn")
        self.verticalLayout_12.addWidget(self.dial_speed_btn)
        self.horizontalLayout_10.addLayout(self.verticalLayout_12)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.line = QtWidgets.QFrame(self.all_Channals)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.all_Channals)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.all_Channals)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.all_Channals)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.verticalLayout_13.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        # self.horizontalLayout.setObjectName("horizontalLayout")
        self.C1_list :DragDropList= None
        # self.C1_list.setObjectName("C1_list")
        # self.horizontalLayout.addWidget(self.C1_list)
        self.C2_list:DragDropList = None
        # self.C2_list.setObjectName("C2_list")
        # self.horizontalLayout.addWidget(self.C2_list)
        self.C3_list:DragDropList = None
        # self.C3_list.setObjectName("C3_list")
        # self.horizontalLayout.addWidget(self.C3_list)
        # self.verticalLayout_13.addLayout(self.horizontalLayout)
        # self.verticalLayout_4.addLayout(self.verticalLayout_13)
        self.Channals.addTab(self.all_Channals, "")
        self.General_tap = QtWidgets.QWidget()
        self.General_tap.setObjectName("General_tap")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.General_tap)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        # self.crop_label = QtWidgets.QLabel(self.General_tap)
        # self.crop_label.setMinimumSize(QtCore.QSize(0, 10))
        # self.crop_label.setObjectName("crop_label")
        # self.verticalLayout_14.addWidget(self.crop_label)
        # self.horizontalLayout_33 = QtWidgets.QHBoxLayout()
        # self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        # self.crop_Choose_label = QtWidgets.QLabel(self.General_tap)
        # self.crop_Choose_label.setObjectName("crop_Choose_label")
        # self.horizontalLayout_33.addWidget(self.crop_Choose_label)
        # self.crop_combo = QtWidgets.QComboBox(self.General_tap)
        # self.crop_combo.addItem("")
        # self.crop_combo.addItem("")
        # self.crop_combo.addItem("")
        # self.crop_combo.setEnabled(True)
        # self.crop_combo.setDuplicatesEnabled(False)
        # self.crop_combo.setObjectName("crop_combo")
        # self.horizontalLayout_33.addWidget(self.crop_combo)
        # self.verticalLayout_14.addLayout(self.horizontalLayout_33)
        # self.crop_btn = QtWidgets.QPushButton(self.General_tap)
        # self.crop_btn.setObjectName("crop_btn")
        # self.verticalLayout_14.addWidget(self.crop_btn)
        # self.line_2 = QtWidgets.QFrame(self.General_tap)
        # self.line_2.setMinimumSize(QtCore.QSize(0, 20))
        # self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        # self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        # self.line_2.setObjectName("line_2")
        # self.verticalLayout_14.addWidget(self.line_2)
        # self.glue_label = QtWidgets.QLabel(self.General_tap)
        # self.glue_label.setMinimumSize(QtCore.QSize(0, 10))
        # self.glue_label.setObjectName("glue_label")
        # self.verticalLayout_14.addWidget(self.glue_label)
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.glue_signal1_label = QtWidgets.QLabel(self.General_tap)
        self.glue_signal1_label.setObjectName("glue_signal1_label")
        self.horizontalLayout_34.addWidget(self.glue_signal1_label)
        self.glue_signal1_combo = QtWidgets.QComboBox(self.General_tap)
        self.glue_signal1_combo.setEnabled(True)
        self.glue_signal1_combo.setDuplicatesEnabled(False)
        self.glue_signal1_combo.setObjectName("glue_signal1_combo")
        self.horizontalLayout_34.addWidget(self.glue_signal1_combo)
        self.verticalLayout_14.addLayout(self.horizontalLayout_34)
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.glue_signal2_label = QtWidgets.QLabel(self.General_tap)
        self.glue_signal2_label.setObjectName("glue_signal2_label")
        self.horizontalLayout_35.addWidget(self.glue_signal2_label)
        self.glue_singal2_combo = QtWidgets.QComboBox(self.General_tap)
        self.glue_singal2_combo.setEnabled(True)
        self.glue_singal2_combo.setDuplicatesEnabled(False)
        self.glue_singal2_combo.setObjectName("glue_singal2_combo")
        self.horizontalLayout_35.addWidget(self.glue_singal2_combo)
        self.verticalLayout_14.addLayout(self.horizontalLayout_35)
        self.glue_combo_Channal = QtWidgets.QComboBox(self.General_tap)
        self.glue_combo_Channal.setObjectName("glue_combo_Channal")
        self.glue_combo_Channal.addItem("")
        self.glue_combo_Channal.addItem("")
        self.glue_combo_Channal.addItem("")
        # self.verticalLayout_14.addWidget(self.glue_combo_Channal)
        self.horizontalLayoutglue = QtWidgets.QHBoxLayout()
        self.horizontalLayoutglue.setObjectName("horizontalLayoutglue")
        self.glue_btn = QtWidgets.QPushButton(self.General_tap)
        self.glue_btn.setObjectName("glue_btn")
        self.horizontalLayoutglue.addWidget(self.glue_btn)
        self.horizontalLayoutglue.addWidget(self.glue_combo_Channal)
        self.verticalLayout_14.addLayout(self.horizontalLayoutglue)
        # self.verticalLayout_14.addWidget(self.glue_btn)
        self.line_3 = QtWidgets.QFrame(self.General_tap)
        self.line_3.setMinimumSize(QtCore.QSize(0, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_14.addWidget(self.line_3)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.real_time_btn = QtWidgets.QPushButton(self.General_tap)
        self.real_time_btn.setObjectName("real_time_btn")
        self.horizontalLayout_9.addWidget(self.real_time_btn)
        self.real_time_combo = QtWidgets.QComboBox(self.General_tap)
        self.real_time_combo.setObjectName("real_time_combo")
        self.real_time_combo.addItem("")
        self.real_time_combo.addItem("")
        self.real_time_combo.addItem("")
        self.horizontalLayout_9.addWidget(self.real_time_combo)
        self.verticalLayout_14.addLayout(self.horizontalLayout_9)
        self.line_7 = QtWidgets.QFrame(self.General_tap)
        self.line_7.setMinimumSize(QtCore.QSize(0, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayout_14.addWidget(self.line_7)
        self.report_btn = QtWidgets.QPushButton(self.General_tap)
        self.report_btn.setObjectName("report_btn")
        self.verticalLayout_14.addWidget(self.report_btn)
        self.Channals.addTab(self.General_tap, "")
        self.sidePar.addWidget(self.Channals)
        self.nonRect_widget = QtWidgets.QWidget(self.centralwidget)
        self.nonRect_widget.setMinimumSize(QtCore.QSize(350, 350))
        self.nonRect_widget.setMaximumSize(QtCore.QSize(400, 351))
        self.nonRect_widget.setObjectName("nonRect_widget")
        self.sidePar.addWidget(self.nonRect_widget)
        self.horizontalLayout_11.addLayout(self.sidePar)
        self.graphs_layout = QtWidgets.QVBoxLayout()
        self.graphs_layout.setObjectName("graphs_layout")
        self.C1_widget = QtWidgets.QWidget(self.centralwidget)
        self.C1_widget.setMinimumSize(QtCore.QSize(800, 0))
        self.C1_widget.setObjectName("C1_widget")
        self.verticalLayout_34 = QtWidgets.QVBoxLayout(self.C1_widget)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.C1_graph_label = QtWidgets.QLabel(self.C1_widget)
        self.C1_graph_label.setObjectName("C1_graph_label")
        self.verticalLayout_34.addWidget(self.C1_graph_label)
        self.graphs_layout.addWidget(self.C1_widget)
        self.C2_widget = QtWidgets.QWidget(self.centralwidget)
        self.C2_widget.setMinimumSize(QtCore.QSize(800, 0))
        self.C2_widget.setObjectName("C2_widget")
        self.verticalLayout_35 = QtWidgets.QVBoxLayout(self.C2_widget)
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        self.C2_graph_label = QtWidgets.QLabel(self.C2_widget)
        self.C2_graph_label.setObjectName("C2_graph_label")
        self.verticalLayout_35.addWidget(self.C2_graph_label)
        self.graphs_layout.addWidget(self.C2_widget)
        self.C3_widget = QtWidgets.QWidget(self.centralwidget)
        self.C3_widget.setMinimumSize(QtCore.QSize(800, 0))
        self.C3_widget.setObjectName("C3_widget")
        self.verticalLayout_36 = QtWidgets.QVBoxLayout(self.C3_widget)
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        self.C3_graph_label = QtWidgets.QLabel(self.C3_widget)
        self.C3_graph_label.setObjectName("C3_graph_label")
        self.verticalLayout_36.addWidget(self.C3_graph_label)
        self.graphs_layout.addWidget(self.C3_widget)
        self.horizontalLayout_11.addLayout(self.graphs_layout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1514, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Channals.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.playc1.setText(_translate("MainWindow", "Play"))
        self.stopc1.setText(_translate("MainWindow", "Stop"))
        self.replayc1.setText(_translate("MainWindow", "replay"))
        self.addsignal_c1.setText(_translate("MainWindow", "Add signal"))
        self.checkBox_c1.setText(_translate("MainWindow", "Control one signal"))
        self.label_5.setText(_translate("MainWindow", "Choose Signal"))
        self.label_9.setText(_translate("MainWindow", "Slide"))
        self.label_10.setText(_translate("MainWindow", "Speed"))
        self.Channals.setTabText(self.Channals.indexOf(self.C1_tap), _translate("MainWindow", "C1"))
        self.playc2.setText(_translate("MainWindow", "Play"))
        self.stopc2.setText(_translate("MainWindow", "Stop"))
        self.replayc2.setText(_translate("MainWindow", "replay"))
        self.addsignalc2_btn.setText(_translate("MainWindow", "Add signal"))
        self.checkBox_c2.setText(_translate("MainWindow", "Control one signal"))
        self.label_6.setText(_translate("MainWindow", "Choose Signal"))
        self.label_11.setText(_translate("MainWindow", "Slide"))
        self.label_12.setText(_translate("MainWindow", "Speed"))
        self.Channals.setTabText(self.Channals.indexOf(self.C2_tap), _translate("MainWindow", "C2"))
        self.play_c3.setText(_translate("MainWindow", "Play"))
        self.stop_c3.setText(_translate("MainWindow", "Stop"))
        self.replay_c3.setText(_translate("MainWindow", "replay"))
        self.addsignal_c3.setText(_translate("MainWindow", "Add signal"))
        self.checkBox_c3.setText(_translate("MainWindow", "Control one signal"))
        self.label_7.setText(_translate("MainWindow", "Choose Signal"))
        self.label_13.setText(_translate("MainWindow", "Slide"))
        self.label_14.setText(_translate("MainWindow", "Speed"))
        self.Channals.setTabText(self.Channals.indexOf(self.C3_tap), _translate("MainWindow", "C3"))
        self.play_c4.setText(_translate("MainWindow", "Play"))
        self.stop_c4.setText(_translate("MainWindow", "Stop"))
        self.replay_c4.setText(_translate("MainWindow", "replay"))
        self.addsignal_c4.setText(_translate("MainWindow", "Add signal"))
        self.label_39.setText(_translate("MainWindow", "Slide"))
        self.label_40.setText(_translate("MainWindow", "Speed"))
        self.Channals.setTabText(self.Channals.indexOf(self.C4_tap), _translate("MainWindow", "C4"))
        self.play_all_btn.setText(_translate("MainWindow", "Play"))
        self.stop_all_btn.setText(_translate("MainWindow", "Stop"))
        self.replay_all_btn.setText(_translate("MainWindow", "replay"))
        self.label_15.setText(_translate("MainWindow", "Slide"))
        self.label_16.setText(_translate("MainWindow", "Speed"))
        self.label.setText(_translate("MainWindow", "C1"))
        self.label_2.setText(_translate("MainWindow", "C2"))
        self.label_3.setText(_translate("MainWindow", "C3"))
        # __sortingEnabled = self.C1_list.isSortingEnabled()
        # self.C1_list.setSortingEnabled(False)
        # item = self.C1_list.item(0)
        # item.setText(_translate("MainWindow", "signal1"))
        # self.C1_list.setSortingEnabled(__sortingEnabled)
        self.Channals.setTabText(self.Channals.indexOf(self.all_Channals), _translate("MainWindow", "All"))
        # self.crop_label.setText(_translate("MainWindow", "Crop"))
        # self.crop_Choose_label.setText(_translate("MainWindow", "Channal"))
        # self.crop_combo.setItemText(0, _translate("MainWindow", "C1"))
        # self.crop_combo.setItemText(1, _translate("MainWindow", "C2"))
        # self.crop_combo.setItemText(2, _translate("MainWindow", "C3"))
        # self.crop_btn.setText(_translate("MainWindow", "add"))
        # self.glue_label.setText(_translate("MainWindow", "Glue"))
        self.glue_signal1_label.setText(_translate("MainWindow", "Signal 1"))
        self.glue_signal2_label.setText(_translate("MainWindow", "Signal 2"))
        self.glue_btn.setText(_translate("MainWindow", "Glue"))
        self.glue_combo_Channal.setItemText(0, _translate("MainWindow", "C1"))
        self.glue_combo_Channal.setItemText(1, _translate("MainWindow", "C2"))
        self.glue_combo_Channal.setItemText(2, _translate("MainWindow", "C3"))
        self.real_time_btn.setText(_translate("MainWindow", "Plot real time"))
        self.real_time_combo.setItemText(0, _translate("MainWindow", "C1"))
        self.real_time_combo.setItemText(1, _translate("MainWindow", "C2"))
        self.real_time_combo.setItemText(2, _translate("MainWindow", "C3"))
        self.report_btn.setText(_translate("MainWindow", "Make a Report"))
        self.Channals.setTabText(self.Channals.indexOf(self.General_tap), _translate("MainWindow", "General"))
        self.C1_graph_label.setText(_translate("MainWindow", "Channal 1"))
        self.C2_graph_label.setText(_translate("MainWindow", "Channal 2"))
        self.C3_graph_label.setText(_translate("MainWindow", "Channal 3"))

class DragDropList(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.setDropIndicatorShown(True)
        self.objects = []
        self.graph1 = None
        self.graph2 = None
        self.graph3 = None
        self.ui = None
        self.AllSignals = None


    def setupParameters(self, ui, graph1, graph2, graph3,AllSignals):
        self.ui = ui
        self.graph1 = graph1
        self.graph2 = graph2
        self.graph3 = graph3
        self.AllSignals = AllSignals
    
    def addItems(self, items):
        for item in items:
            self.addItem(item)

    def mimeData(self, items):
        mime_data = QMimeData()
        text = "\n".join(item.text() for item in items)
        mime_data.setText(text)
        return mime_data

    def dropEvent(self, event):
        # Accept the event
        if event.mimeData().hasText():
            items = event.mimeData().text().split("\n")
            self.addItems(items)
            event.accept()

            # Remove the items from the source list
            source = event.source()
            for item in items:
                matching_items = source.findItems(item, Qt.MatchExactly)
                if matching_items:
                    source.takeItem(source.row(matching_items[0]))
        else:
            event.ignore()
        self.swap_signals(self.ui,self.graph1,self.graph2,self.graph3,self.AllSignals)

    def swap_signals(self, ui: Ui_MainWindow, graph1: Graph, graph2: Graph, graph3: Graph, AllSignals):
        items1 = ui.C1_list.get_items()
        items2 = ui.C2_list.get_items()
        items3 = ui.C3_list.get_items()
        # remove duplicates from each dragdrop list
        ui.C1_list.clear()
        ui.C2_list.clear()
        ui.C3_list.clear()
        ui.C1_list.addItems(list(set(items1)))
        ui.C2_list.addItems(list(set(items2)))
        ui.C3_list.addItems(list(set(items3)))

        # get plots for each graph corresponding to the signals
        allplots1 = graph1.plots + graph2.plots + graph3.plots

        plots1 = [plot for plot in allplots1 if plot.signal.label in items1]
        plots2 = [plot for plot in allplots1 if plot.signal.label in items2]
        plots3 = [plot for plot in allplots1 if plot.signal.label in items3]
        # print(plots1)
        # print(plots2)
        # print(plots3)
        for plot in plots1:
            last_point = int((plot.last_point ) / len(plot.signal.data_pnts))
            if plot.isRealTime:
                graph1.plot_real_time(label="Real Time")
            else:
                graph1.plot_signal(plot.signal)
        for plot in plots2:
            last_point = int((plot.last_point ) / len(plot.signal.data_pnts))
            if plot.isRealTime:
                graph2.plot_real_time(label="Real Time")
            else:
                graph2.plot_signal(plot.signal)
        for plot in plots3:
            last_point = int((plot.last_point ) / len(plot.signal.data_pnts))
            if plot.isRealTime:
                graph3.plot_real_time(label="Real Time")
            else:
                graph3.plot_signal(plot.signal)

        for plot in graph1.plots:
            if plot.signal.label not in items1:
                graph1.delete_signal(plot.signal)
        for plot in graph2.plots:
            if plot.signal.label not in items2:
                graph2.delete_signal(plot.signal)
        for plot in graph3.plots:
            if plot.signal.label not in items3:
                graph3.delete_signal(plot.signal)
        # delete signals from combobox that not in the list
        for i in range(ui.choosesignalc1_combo.count()):
            if ui.choosesignalc1_combo.itemText(i) not in items1:
                ui.choosesignalc1_combo.removeItem(i)
        for i in range(ui.choosesignalc2_combo.count()):
            if ui.choosesignalc2_combo.itemText(i) not in items2:
                ui.choosesignalc2_combo.removeItem(i)
        for i in range(ui.choosesignalc3_combo.count()):
            if ui.choosesignalc3_combo.itemText(i) not in items3:
                ui.choosesignalc3_combo.removeItem(i)
        # add signals to combobox that not in the list
        for plot in plots1:
            if ui.choosesignalc1_combo.findText(plot.signal.label) == -1:
                ui.choosesignalc1_combo.addItem(plot.signal.label)
        for plot in plots2:
            if ui.choosesignalc2_combo.findText(plot.signal.label) == -1:
                ui.choosesignalc2_combo.addItem(plot.signal.label)
        for plot in plots3:
            if ui.choosesignalc3_combo.findText(plot.signal.label) == -1:
                ui.choosesignalc3_combo.addItem(plot.signal.label)






    def dragMoveEvent(self, event):
        # Accept the drag if it's a text item
        if event.mimeData().hasText():
            event.accept()
        else:
            event.ignore()

    def dragEnterEvent(self, event):
        # Accept the drag if it's a text item
        if event.mimeData().hasText():
            event.accept()
        else:
            event.ignore()

    def get_items(self):
        return [self.item(i).text() for i in range(self.count())]
    def mouseDoubleClickEvent(self, event):
        item = self.itemAt(event.pos())
        if item:
            self.takeItem(self.row(item))
        self.swap_signals(self.ui,self.graph1,self.graph2,self.graph3,self.AllSignals)
        super().mouseDoubleClickEvent(event)
        
