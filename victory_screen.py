from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1200, 960)
        self.design_stripe = QtWidgets.QLabel(Form)
        self.design_stripe.setGeometry(QtCore.QRect(0, 240, 1200, 480))
        self.design_stripe.setAutoFillBackground(False)
        self.design_stripe.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.505273, y1:0.506, x2:0.5, y2:1, stop:0.630682 rgba(0, 55, 255, 244), stop:1 rgba(255, 255, 255, 0));")
        self.design_stripe.setText("")
        self.design_stripe.setObjectName("design_stripe")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1200, 960))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("background-color: rgba(0, 0, 0, 180);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.victory_label = QtWidgets.QLabel(Form)
        self.victory_label.setGeometry(QtCore.QRect(390, 140, 420, 140))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(72)
        font.setBold(False)
        font.setWeight(50)
        self.victory_label.setFont(font)
        self.victory_label.setStyleSheet("color: rgb(250, 203, 17);")
        self.victory_label.setTextFormat(QtCore.Qt.PlainText)
        self.victory_label.setScaledContents(False)
        self.victory_label.setAlignment(QtCore.Qt.AlignCenter)
        self.victory_label.setObjectName("victory_label")
        self.kills_label = QtWidgets.QLabel(Form)
        self.kills_label.setGeometry(QtCore.QRect(250, 350, 140, 60))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(28)
        self.kills_label.setFont(font)
        self.kills_label.setStyleSheet("color: rgb(250, 203, 17);")
        self.kills_label.setObjectName("kills_label")
        self.time_label = QtWidgets.QLabel(Form)
        self.time_label.setGeometry(QtCore.QRect(250, 420, 320, 60))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(28)
        self.time_label.setFont(font)
        self.time_label.setStyleSheet("color: rgb(250, 203, 17);")
        self.time_label.setObjectName("time_label")
        self.points_label = QtWidgets.QLabel(Form)
        self.points_label.setGeometry(QtCore.QRect(250, 490, 160, 60))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(28)
        self.points_label.setFont(font)
        self.points_label.setStyleSheet("color: rgb(250, 203, 17);")
        self.points_label.setObjectName("points_label")
        self.kills_score = QtWidgets.QLabel(Form)
        self.kills_score.setGeometry(QtCore.QRect(710, 350, 200, 60))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(28)
        self.kills_score.setFont(font)
        self.kills_score.setStyleSheet("color: rgb(250, 203, 17);")
        self.kills_score.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.kills_score.setObjectName("kills_score")
        self.time_score = QtWidgets.QLabel(Form)
        self.time_score.setGeometry(QtCore.QRect(710, 420, 200, 60))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(28)
        self.time_score.setFont(font)
        self.time_score.setStyleSheet("color: rgb(250, 203, 17);")
        self.time_score.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.time_score.setObjectName("time_score")
        self.points_score = QtWidgets.QLabel(Form)
        self.points_score.setGeometry(QtCore.QRect(710, 490, 200, 60))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(28)
        self.points_score.setFont(font)
        self.points_score.setStyleSheet("color: rgb(250, 203, 17);")
        self.points_score.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.points_score.setObjectName("points_score")
        self.retry_button = QtWidgets.QPushButton(Form)
        self.retry_button.setGeometry(QtCore.QRect(680, 620, 180, 60))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(28)
        self.retry_button.setFont(font)
        self.retry_button.setStyleSheet("background-color: rgb(18, 16, 156);\n"
"color: rgb(250, 203, 17);")
        self.retry_button.setObjectName("retry_button")
        self.quit_button = QtWidgets.QPushButton(Form)
        self.quit_button.setGeometry(QtCore.QRect(340, 620, 180, 60))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(28)
        self.quit_button.setFont(font)
        self.quit_button.setStyleSheet("background-color: rgb(18, 16, 156);\n"
"color: rgb(250, 203, 17);")
        self.quit_button.setObjectName("quit_button")
        self.label_2.raise_()
        self.design_stripe.raise_()
        self.victory_label.raise_()
        self.kills_label.raise_()
        self.time_label.raise_()
        self.points_label.raise_()
        self.kills_score.raise_()
        self.time_score.raise_()
        self.points_score.raise_()
        self.retry_button.raise_()
        self.quit_button.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.victory_label.setText(_translate("Form", "Victory"))
        self.kills_label.setText(_translate("Form", "Kills:"))
        self.time_label.setText(_translate("Form", "Time survived:"))
        self.points_label.setText(_translate("Form", "Points:"))
        self.kills_score.setText(_translate("Form", "0"))
        self.time_score.setText(_translate("Form", "0"))
        self.points_score.setText(_translate("Form", "0"))
        self.retry_button.setText(_translate("Form", "Retry"))
        self.quit_button.setText(_translate("Form", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())