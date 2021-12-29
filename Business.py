 
from PyQt5 import QtCore, QtGui, QtWidgets
1
#DATABASE IMPORT
import pyodbc

#IMPORT MAIL FUNCTION
import win32com.client as win32
from win32com.client.selecttlb import SelectTlb

#IMPORT SMS FUNCTION
from twilio.rest import Client 

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=FELIPE-ALMEIDA\SQLEXPRESS;'
                      'Database=Bancodedados;'
                      'Trusted_Connection=yes;')            
                                                    
cursor = conn.cursor()
cursor.execute('SELECT * FROM bank1$')

outlook = win32.Dispatch('outlook.application')
email = outlook.CreateItem(0)

   
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(844, 700)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("window_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(550, 700))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.bg_topbar = QtWidgets.QFrame(self.centralwidget)
        self.bg_topbar.setMaximumSize(QtCore.QSize(16777215, 50))
        self.bg_topbar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bg_topbar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bg_topbar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bg_topbar.setObjectName("bg_topbar")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.bg_topbar)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.error_status = QtWidgets.QFrame(self.bg_topbar)
        self.error_status.setMinimumSize(QtCore.QSize(0, 25))
        self.error_status.setMaximumSize(QtCore.QSize(450, 30))
        self.error_status.setStyleSheet("background-color: rgb(0, 58, 112);\n"
"border-radius:0px;")
        self.error_status.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.error_status.setFrameShadow(QtWidgets.QFrame.Raised)
        self.error_status.setObjectName("error_status")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.error_status)
        self.horizontalLayout_6.setContentsMargins(10, 3, 10, 3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_error = QtWidgets.QLabel(self.error_status)
        self.label_error.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 10pt \"Caros Soft Bold\";\n"
"")
        self.label_error.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error.setObjectName("label_error")
        self.horizontalLayout_6.addWidget(self.label_error)
        self.close_bttn = QtWidgets.QPushButton(self.error_status)
        self.close_bttn.setMaximumSize(QtCore.QSize(20, 20))
        self.close_bttn.setAutoFillBackground(False)
        self.close_bttn.setStyleSheet("QPushButton{\n"
"background-image: url(:/logo/x_unclicked_1.png);\n"
"background-repeat:no-repeat;\n"
"background-position:center;\n"
"}\n"
"QPushButton:hover{\n"
"background-image: url(:/logo/x_hover_1.png);\n"
"background-repeat:no-repeat;\n"
"background-position:center;\n"
"}\n"
"QPushButton:pressed{\n"
"background-image: url(:/logo/x_hover_1.png);\n"
"background-repeat:no-repeat;\n"
"background-position:center;\n"
"}")
        self.close_bttn.setText("")
        self.close_bttn.setObjectName("close_bttn")
        self.horizontalLayout_6.addWidget(self.close_bttn)
        self.horizontalLayout_5.addWidget(self.error_status)
        self.verticalLayout.addWidget(self.bg_topbar)
        self.bg_search = QtWidgets.QFrame(self.centralwidget)
        self.bg_search.setMaximumSize(QtCore.QSize(16777215, 80))
        self.bg_search.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bg_search.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bg_search.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bg_search.setObjectName("bg_search")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.bg_search)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bg_search_frame = QtWidgets.QFrame(self.bg_search)
        self.bg_search_frame.setMinimumSize(QtCore.QSize(0, 80))
        self.bg_search_frame.setMaximumSize(QtCore.QSize(500, 80))
        self.bg_search_frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bg_search_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bg_search_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bg_search_frame.setObjectName("bg_search_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.bg_search_frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.search_bar_back = QtWidgets.QFrame(self.bg_search_frame)
        self.search_bar_back.setMaximumSize(QtCore.QSize(370, 50))
        self.search_bar_back.setStyleSheet("background-color: rgb(229, 241, 248);\n"
"border-radius:0px;")
        self.search_bar_back.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.search_bar_back.setFrameShadow(QtWidgets.QFrame.Raised)
        self.search_bar_back.setObjectName("search_bar_back")
        self.search_bttn = QtWidgets.QPushButton(self.search_bar_back, clicked = lambda: self.press_it(self.search_bar_2.text()))
        self.search_bttn.setGeometry(QtCore.QRect(330, 10, 30, 31))
        self.search_bttn.setMaximumSize(QtCore.QSize(30, 40))
        self.search_bttn.setStyleSheet("QPushButton{\n"
"background-image: url(:/logo/search_unclicked_2.png);\n"
"background-repeat:no-repeat;\n"
"background-position:center;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/logo/search_hover.png);\n"
"background-repeat:no-repeat;\n"
"background-position:center;\n"
"}\n"
"QPushButton:pressed{\n"
"background-image: url(:/logo/search_hover.png);\n"
"background-repeat:no-repeat;\n"
"background-position:center;\n"
"}")
        self.search_bttn.setText("")
        self.search_bttn.setObjectName("search_bttn")
        self.search_bar_2 = QtWidgets.QLineEdit(self.search_bar_back)
        self.search_bar_2.setGeometry(QtCore.QRect(10, 10, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Caros Soft Bold")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.search_bar_2.setFont(font)
        self.search_bar_2.setStyleSheet("font: 63 9pt \"Caros Soft Bold\";\n"
"QLineEdit{\n"
"\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(214, 228, 234);\n"
"}\n"
"")
        self.search_bar_2.setMaxLength(15)
        self.search_bar_2.setAlignment(QtCore.Qt.AlignCenter)
        self.search_bar_2.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.search_bar_2.setObjectName("search_bar_2")
        self.horizontalLayout_3.addWidget(self.search_bar_back)
        self.image_logo = QtWidgets.QFrame(self.bg_search_frame)
        self.image_logo.setMaximumSize(QtCore.QSize(50, 50))
        self.image_logo.setStyleSheet("image: url(:/logo/main_logo.png);")
        self.image_logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.image_logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.image_logo.setObjectName("image_logo")
        self.horizontalLayout_3.addWidget(self.image_logo)
        self.horizontalLayout.addWidget(self.bg_search_frame)
        self.verticalLayout.addWidget(self.bg_search)
        self.whole_bg = QtWidgets.QFrame(self.centralwidget)
        self.whole_bg.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.whole_bg.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.whole_bg.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.whole_bg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.whole_bg.setObjectName("whole_bg")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.whole_bg)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.info_bg = QtWidgets.QFrame(self.whole_bg)
        self.info_bg.setMaximumSize(QtCore.QSize(600, 480))
        self.info_bg.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.info_bg.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.info_bg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.info_bg.setObjectName("info_bg")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.info_bg)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.info_bg_2 = QtWidgets.QWidget(self.info_bg)
        self.info_bg_2.setMinimumSize(QtCore.QSize(0, 0))
        self.info_bg_2.setMaximumSize(QtCore.QSize(440, 500))
        self.info_bg_2.setStyleSheet("background-color: rgb(229, 241, 248);\n"
"border-radius:0px;")
        self.info_bg_2.setObjectName("info_bg_2")
        self.tag_fullname = QtWidgets.QLabel(self.info_bg_2)
        self.tag_fullname.setGeometry(QtCore.QRect(20, 30, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Caros Soft Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.tag_fullname.setFont(font)
        self.tag_fullname.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color: rgb(0, 116, 189);\n"
"border-radius:0px;")
        self.tag_fullname.setAlignment(QtCore.Qt.AlignCenter)
        self.tag_fullname.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.tag_fullname.setObjectName("tag_fullname")
        self.tag_dtnascimento = QtWidgets.QLabel(self.info_bg_2)
        self.tag_dtnascimento.setGeometry(QtCore.QRect(270, 30, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Caros Soft Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.tag_dtnascimento.setFont(font)
        self.tag_dtnascimento.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color: rgb(0, 116, 189);\n"
"border-radius:0px;")
        self.tag_dtnascimento.setAlignment(QtCore.Qt.AlignCenter)
        self.tag_dtnascimento.setObjectName("tag_dtnascimento")
        self.tag_cpf = QtWidgets.QLabel(self.info_bg_2)
        self.tag_cpf.setGeometry(QtCore.QRect(20, 90, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Caros Soft Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.tag_cpf.setFont(font)
        self.tag_cpf.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color: rgb(0, 116, 189);\n"
"border-radius:0px;")
        self.tag_cpf.setAlignment(QtCore.Qt.AlignCenter)
        self.tag_cpf.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.tag_cpf.setObjectName("tag_cpf")
        self.tag_celular = QtWidgets.QLabel(self.info_bg_2)
        self.tag_celular.setGeometry(QtCore.QRect(230, 90, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Caros Soft Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.tag_celular.setFont(font)
        self.tag_celular.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color: rgb(0, 116, 189);\n"
"border-radius:0px;")
        self.tag_celular.setAlignment(QtCore.Qt.AlignCenter)
        self.tag_celular.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.tag_celular.setObjectName("tag_celular")
        self.tag_email = QtWidgets.QLabel(self.info_bg_2)
        self.tag_email.setGeometry(QtCore.QRect(20, 150, 401, 31))
        font = QtGui.QFont()
        font.setFamily("Caros Soft Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.tag_email.setFont(font)
        self.tag_email.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color: rgb(0, 116, 189);\n"
"border-radius:0px;")
        self.tag_email.setAlignment(QtCore.Qt.AlignCenter)
        self.tag_email.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.tag_email.setObjectName("tag_email")
        self.tag_unidade = QtWidgets.QLabel(self.info_bg_2)
        self.tag_unidade.setGeometry(QtCore.QRect(230, 210, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Caros Soft Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.tag_unidade.setFont(font)
        self.tag_unidade.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color: rgb(0, 116, 189);\n"
"border-radius:0px;")
        self.tag_unidade.setAlignment(QtCore.Qt.AlignCenter)
        self.tag_unidade.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.tag_unidade.setObjectName("tag_unidade")
        self.tag_cargo = QtWidgets.QLabel(self.info_bg_2)
        self.tag_cargo.setGeometry(QtCore.QRect(20, 210, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Caros Soft Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.tag_cargo.setFont(font)
        self.tag_cargo.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color: rgb(0, 116, 189);\n"
"border-radius:0px;")
        self.tag_cargo.setAlignment(QtCore.Qt.AlignCenter)
        self.tag_cargo.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.tag_cargo.setObjectName("tag_cargo")
        self.tag_dtperiodoco = QtWidgets.QLabel(self.info_bg_2)
        self.tag_dtperiodoco.setGeometry(QtCore.QRect(20, 270, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Caros Soft Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.tag_dtperiodoco.setFont(font)
        self.tag_dtperiodoco.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color: rgb(0, 116, 189);\n"
"border-radius:0px;")
        self.tag_dtperiodoco.setAlignment(QtCore.Qt.AlignCenter)
        self.tag_dtperiodoco.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.tag_dtperiodoco.setObjectName("tag_dtperiodoco")
        self.tag_clinica = QtWidgets.QLabel(self.info_bg_2)
        self.tag_clinica.setGeometry(QtCore.QRect(200, 270, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Caros Soft Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.tag_clinica.setFont(font)
        self.tag_clinica.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color: rgb(0, 116, 189);\n"
"border-radius:0px;")
        self.tag_clinica.setAlignment(QtCore.Qt.AlignCenter)
        self.tag_clinica.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.tag_clinica.setObjectName("tag_clinica")
        self.tag_endereco = QtWidgets.QLabel(self.info_bg_2)
        self.tag_endereco.setGeometry(QtCore.QRect(20, 330, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Caros Soft Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.tag_endereco.setFont(font)
        self.tag_endereco.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color: rgb(0, 116, 189);\n"
"border-radius:0px;")
        self.tag_endereco.setAlignment(QtCore.Qt.AlignCenter)
        self.tag_endereco.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.tag_endereco.setObjectName("tag_endereco")
        self.tag_contato = QtWidgets.QLabel(self.info_bg_2)
        self.tag_contato.setGeometry(QtCore.QRect(270, 330, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Caros Soft Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.tag_contato.setFont(font)
        self.tag_contato.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color: rgb(0, 116, 189);\n"
"border-radius:0px;")
        self.tag_contato.setAlignment(QtCore.Qt.AlignCenter)
        self.tag_contato.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.tag_contato.setObjectName("tag_contato")
        self.bttn_clear = QtWidgets.QPushButton(self.info_bg_2, clicked = lambda: self.clear_it(self.clear_it))
        self.bttn_clear.setGeometry(QtCore.QRect(20, 420, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Caros Soft Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.bttn_clear.setFont(font)
        self.bttn_clear.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color: rgb(0, 58, 112);\n"
"border-radius: 0px;\n"
"\n"
"\n"
"    \n"
"    \n"
"")
        self.bttn_clear.setObjectName("bttn_clear")
        self.frame = QtWidgets.QFrame(self.info_bg_2)
        self.frame.setGeometry(QtCore.QRect(189, 419, 111, 41))
        self.frame.setStyleSheet("background-color: rgb(0, 116, 189);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.bttn_send_mail = QtWidgets.QPushButton(self.frame, clicked = lambda: self.press_it2(self.search_bar_2.text()))
        self.bttn_send_mail.setGeometry(QtCore.QRect(0, 0, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Caros Soft Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.bttn_send_mail.setFont(font)
        self.bttn_send_mail.setAutoFillBackground(False)
        self.bttn_send_mail.setStyleSheet("QPushButton{\n"
"background-image: url(:/logo/mail_unclicked_4.png);\n"
"background-repeat:no-repeat;\n"
"background-position:center;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/logo/mail_clicked_3.png);\n"
"background-repeat:no-repeat;\n"
"background-position:center;\n"
"}\n"
"QPushButton:pressed{\n"
"background-image: url(:/logo/mail_clicked_3.png);\n"
"background-repeat:no-repeat;\n"
"background-position:center;\n"
"}")
        self.bttn_send_mail.setText("")
        self.bttn_send_mail.setAutoDefault(False)
        self.bttn_send_mail.setFlat(False)
        self.bttn_send_mail.setObjectName("bttn_send_mail")
        self.frame_2 = QtWidgets.QFrame(self.info_bg_2)
        self.frame_2.setGeometry(QtCore.QRect(319, 420, 101, 41))
        self.frame_2.setStyleSheet("background-color: rgb(0, 116, 189);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.bttn_send_text = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.press_it3(self.search_bar_2.text()))
        self.bttn_send_text.setGeometry(QtCore.QRect(0, 0, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Caros Soft Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.bttn_send_text.setFont(font)
        self.bttn_send_text.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.bttn_send_text.setStyleSheet("QPushButton{\n"
"background-image: url(:/logo/sms_unclicked_2.png);\n"
"background-repeat:no-repeat;\n"
"background-position:center;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/logo/smsclicked_1.png);\n"
"background-repeat:no-repeat;\n"
"background-position:center;\n"
"}\n"
"QPushButton:pressed{\n"
"background-image: url(:/logo/smsclicked_1.png);\n"
"background-repeat:no-repeat;\n"
"background-position:center;\n"
"}")
        self.bttn_send_text.setText("")
        self.bttn_send_text.setObjectName("bttn_send_text")
        self.frame_3 = QtWidgets.QFrame(self.info_bg_2)
        self.frame_3.setGeometry(QtCore.QRect(20, 420, 111, 41))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.tag_fullname.raise_()
        self.tag_dtnascimento.raise_()
        self.tag_cpf.raise_()
        self.tag_celular.raise_()
        self.tag_email.raise_()
        self.tag_unidade.raise_()
        self.tag_cargo.raise_()
        self.tag_dtperiodoco.raise_()
        self.tag_clinica.raise_()
        self.tag_endereco.raise_()
        self.tag_contato.raise_()
        self.frame.raise_()
        self.frame_2.raise_()
        self.frame_3.raise_()
        self.bttn_clear.raise_()
        self.horizontalLayout_4.addWidget(self.info_bg_2)
        self.horizontalLayout_2.addWidget(self.info_bg)
        self.verticalLayout.addWidget(self.whole_bg)
        self.bottom_bar = QtWidgets.QFrame(self.centralwidget)
        self.bottom_bar.setMaximumSize(QtCore.QSize(16777215, 30))
        self.bottom_bar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bottom_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bottom_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom_bar.setObjectName("bottom_bar")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.bottom_bar)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label = QtWidgets.QLabel(self.bottom_bar)
        self.label.setStyleSheet("QLabel{\n"
"font: 75 8pt \"Century Gothic\";\n"
"color: rgb(141, 141, 141);\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_7.addWidget(self.label)
        self.verticalLayout.addWidget(self.bottom_bar)
        MainWindow.setCentralWidget(self.centralwidget)

         #CLOSE ERROR BOX WITH BUTTON
        self.close_bttn.clicked.connect(lambda: self.error_status.hide())
        
        #CLOSE ERROR POPOUT
        self.error_status.hide()
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    
    
        
          
    def press_it(self, pressed):
        
        self.search_bar_2.setText(pressed)      
        
        cursor.execute('SELECT * FROM bank1$ WHERE [Cod Funcionário] = %s' % (self.search_bar_2.text()))
        
        for row in cursor:
            
            self.tag_fullname.setText(row[4])
            self.tag_dtnascimento.setText(row[5])
            self.tag_cpf.setText(row[8])
            self.tag_celular.setText(row[11])
            self.tag_email.setText(row[10])
            self.tag_cargo.setText(row[3])
            self.tag_unidade.setText(row[1])
            self.tag_dtperiodoco.setText(row[13])
            self.tag_clinica.setText(row[14])
            self.tag_endereco.setText(row[16])
            self.tag_contato.setText(row[12])
          
        

   
      
    def press_it2(self, pressed):
        
        self.search_bar_2.setText(pressed)
        
        cursor.execute('SELECT * FROM bank1$ WHERE [Cod Funcionário] = %s' % (self.search_bar_2.text()))

        
        for row in cursor:
            
            email.To = row[10]
            email.Subject = f"VENCIMENTO EXAME PERÍODICO - {row[4]}"	
            email.HTMLBody = f"""
            <h1 style="color:#006CAF;font-size:15px"> Olá, {row[4]}  </h1>
            <p style="color:#006CAF;font-size:15px"> O seu exame períodico vence em {row[17]} dias. </p>
            <p style="color:#006CAF;font-size:15px"> Entre em contato com seu Coordenador/RH para que possa agendar seus exames. </p>
            
            <p style="color:#006CAF;font-size:15px"> Kind regards, </p>
            <p style="color:#006CAF;font-size:15px"> Felipe Almeida. </p>
            """
        email.Send()
        print("EMAIL ENVIADO COM SUCESSO!")  
        
        
        self.error_status.show()
        self.label_error.setText("Email enviado com sucesso!")
     
     
    def press_it3(self, pressed):
        
        self.search_bar_2.setText(pressed)
        
        cursor.execute('SELECT * FROM bank1$ WHERE [Cod Funcionário] = %s' % (self.search_bar_2.text()))

        for row in cursor:
            
            account_sid = 'AC5da20764511523ea6d32e07696056b3e' 
            auth_token = '01473d72f04d9a46af73d6ddd03d66e8' 
            client = Client(account_sid, auth_token) 
 
            message = client.messages.create(  
                              messaging_service_sid='MG503044e4bf12a33527b1937c894c8fe1', 
                              body= f'Olá, {row[4]} \nO seu exame períodico vence em {row[17]} dias.\nEntre em contato com seu Coordenador para que possa agendar seus exames\nKind regards,\nFelipe Almeida.',    
                              to= row[11],
                          ) 
 
            print(message.sid)
                
        self.error_status.show()
        self.label_error.setText("SMS enviado com sucesso!")          
   
   
#CLEAR ALL FIELDS 
    def clear_it(self,pressed):

        self.tag_fullname.setText("NOME COMPLETO")
        self.tag_dtnascimento.setText("DATA DE NASCIMENTO")
        self.tag_cpf.setText("CPF")
        self.tag_celular.setText("CELULAR")
        self.tag_email.setText("E-MAIL")
        self.tag_cargo.setText("CARGO")
        self.tag_unidade.setText("UNIDADE")
        self.tag_dtperiodoco.setText("DT. ÚLTIMO PERÍODICO")
        self.tag_clinica.setText("CLÍNICA RESPONSÁVEL")
        self.tag_endereco.setText("ENDEREÇO")
        self.tag_contato.setText("CONTATO")
       
        self.search_bar_2.setText("")
        self.error_status.hide()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BUSINESS CASE"))
        self.label_error.setText(_translate("MainWindow", "ID NÃO ENCONTRADO!"))
        self.search_bttn.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.search_bar_2.setPlaceholderText(_translate("MainWindow", "INSIRA O ID DO COLABORADOR"))
        self.tag_fullname.setText(_translate("MainWindow", "NOME COMPLETO"))
        self.tag_dtnascimento.setText(_translate("MainWindow", "DATA DE NASCIMENTO"))
        self.tag_cpf.setText(_translate("MainWindow", "CPF"))
        self.tag_celular.setText(_translate("MainWindow", "CELULAR"))
        self.tag_email.setText(_translate("MainWindow", "E-MAIL"))
        self.tag_unidade.setText(_translate("MainWindow", "UNIDADE"))
        self.tag_cargo.setText(_translate("MainWindow", "CARGO"))
        self.tag_dtperiodoco.setText(_translate("MainWindow", "DT. ÚLTIMO PERIÓDICO"))
        self.tag_clinica.setText(_translate("MainWindow", "CLÍNICA RESPONSÁVEL"))
        self.tag_endereco.setText(_translate("MainWindow", "ENDEREÇO"))
        self.tag_contato.setText(_translate("MainWindow", "CONTATO"))
        self.bttn_clear.setText(_translate("MainWindow", "CLEAR"))
        self.label.setText(_translate("MainWindow", "Business Case: Felipe Almeida"))
import files_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
