from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from pastpaper import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(517, 801)
        MainWindow.setMinimumSize(QtCore.QSize(517,801))
        MainWindow.setMaximumSize(QtCore.QSize(517,801))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.layoutWidget = QtWidgets.QWidget(MainWindow)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 481, 771))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setMouseTracking(True)
        self.label.setTabletTracking(False)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label)
        self.splitter = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.exam_office = QtWidgets.QToolButton(self.splitter)
        self.exam_office.setObjectName("exam_office")
        self.grade = QtWidgets.QToolButton(self.splitter)
        self.grade.setObjectName("grade")
        self.subject = QtWidgets.QToolButton(self.splitter)
        self.subject.setObjectName("subject")
        self.year = QtWidgets.QToolButton(self.splitter)
        self.year.setObjectName("year")
        self.month = QtWidgets.QToolButton(self.splitter)
        self.month.setObjectName("month")
        self.component = QtWidgets.QToolButton(self.splitter)
        self.component.setObjectName("component")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.splitter)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.start_search = QtWidgets.QPushButton(self.layoutWidget)
        self.start_search.setObjectName("start_search")
        self.gridLayout_2.addWidget(self.start_search, 0, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.toolButton = QtWidgets.QToolButton(self.layoutWidget)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout_2.addWidget(self.toolButton, 0, 2, 1, 1)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.SpanningRole, self.gridLayout_2)
        self.progressBar = QtWidgets.QProgressBar(self.layoutWidget)
        self.progressBar.setProperty("value", 100)
        self.progressBar.setObjectName("progressBar")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.progressBar)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.info = QtWidgets.QTableView(self.layoutWidget)
        self.model = QStandardItemModel()
        
        self.info.setEnabled(True)
        self.info.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.info.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)#纵向滚轮
        self.info.setObjectName("info")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.info.setFont(font)
        self.horizontalLayout.addWidget(self.info)
        self.info.horizontalHeader().setVisible(False)#横向表头无
        self.info.verticalHeader().setVisible(False)#纵向表头无

        self.formLayout.setLayout(3, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout)
        self.download = QtWidgets.QPushButton(self.layoutWidget)
        self.download.setObjectName("download")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.download)
        self.store_place = QtWidgets.QPushButton(self.layoutWidget)
        self.store_place.setObjectName("store_place")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.store_place)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Pastpaper 下载器"))
        self.exam_office.setText(_translate("MainWindow", "考试局"))
        self.grade.setText(_translate("MainWindow", "年级"))
        self.subject.setText(_translate("MainWindow", "科目"))
        self.year.setText(_translate("MainWindow", "年份"))
        self.month.setText(_translate("MainWindow", "月份"))
        self.component.setText(_translate("MainWindow", "卷号"))
        self.start_search.setText(_translate("MainWindow", "GO"))
        self.lineEdit.setText(_translate("MainWindow", "Search component"))
        self.toolButton.setText(_translate("MainWindow", "多选功能"))
        self.download.setText(_translate("MainWindow", "下载所选文件、文件夹"))
        self.store_place.setText(_translate("MainWindow", "文件储存位置"))