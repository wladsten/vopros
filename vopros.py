from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
app = QApplication([])

window = QWidget()
window.setWindowTitle("Анкета")
window.resize(400,600)

name=QLabel("ім'я")
name_w=QLineEdit()

s=QLabel("Стать")
s1=QRadioButton('ч')
s2=QRadioButton('ж')

c=QLabel("ти віриш в бога ")
c1=QCheckBox('да')
c2=QCheckBox('Ніііііііі')
c3=QCheckBox('50 на 50')

alo=QLabel("чя мама найкраща")
alo1=QComboBox()
alo1.addItems(['моя мама','мама нолана','мама ігоря','папа'])

button=QPushButton('ok')

laoyth_v=QVBoxLayout()
laoyth_h1=QHBoxLayout()

laoyth_h3=QHBoxLayout()
laoyth_h4=QHBoxLayout()
laoyth_h5=QHBoxLayout()
laoyth_h6=QHBoxLayout()

laoyth_h1.addWidget(name)
laoyth_h1.addWidget(name_w)

laoyth_h3.addWidget(s)
laoyth_h3.addWidget(s1)
laoyth_h3.addWidget(s2)
laoyth_h4.addWidget(c)
laoyth_h4.addWidget(c1)
laoyth_h4.addWidget(c2)
laoyth_h4.addWidget(c3)

laoyth_h5.addWidget(alo)
laoyth_h5.addWidget(alo1)
laoyth_h6.addWidget(button)

laoyth_v.addLayout(laoyth_h1)
laoyth_v.addLayout(laoyth_h3)
laoyth_v.addLayout(laoyth_h4)
laoyth_v.addLayout(laoyth_h5)
laoyth_v.addLayout(laoyth_h6)
window.setLayout(laoyth_v)
def hello():
    info_win=QMessageBox()
    info_win.setWindowTitle('Результат')
    info_win.setText('Дякуємо ваша анкета заповнена'+name_w.text())
    info_win.exec_()

button.clicked.connect(hello)
window.show()
app.exec_()
