import json
import sys

from PIL import Image
import os
import io
from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication

ui = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>317</width>
    <height>297</height>
   </rect>
  </property>
  <property name="sizePolicy">
   <sizepolicy hsizetype="MinimumExpanding" vsizetype="MinimumExpanding">
    <horstretch>0</horstretch>
    <verstretch>0</verstretch>
   </sizepolicy>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <layout class="QVBoxLayout" name="verticalLayout_2">
   <item>
    <widget class="QLabel" name="label">
     <property name="text">
      <string>\</string>
     </property>
    </widget>
   </item>
   <item>
    <layout class="QHBoxLayout" name="horizontalLayout">
     <item>
      <widget class="QPushButton" name="pushButton_2">
       <property name="text">
        <string>Лайк</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="pushButton">
       <property name="text">
        <string>Скип</string>
       </property>
      </widget>
     </item>
    </layout>
   </item>
  </layout>
 </widget>
 <resources/>
 <connections/>
</ui>

"""


class Task(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(io.StringIO(ui), self)
        self.dirs = sorted(os.listdir('memes'), key=lambda x: int(x.split('.')[0]))
        self.count = 0
        pixmap = QtGui.QPixmap(f"memes/{self.dirs[self.count]}")
        self.label.setPixmap(pixmap)
        if not os.path.exists('data.json'):
            with open("data.json", 'w+') as data:
                data.write('{}')
        self.pushButton.clicked.connect(self.skip)

    def skip(self):
        self.count += 1; self.count %= len(self.dirs)
        pixmap = QtGui.QPixmap(f"memes/{self.dirs[self.count]}")
        self.label.setPixmap(pixmap)
        self.updateGeometry()


def main():
    dirs = sorted(os.listdir('memes'), key=lambda x: int(x.split('.')[0]))
    if not os.path.exists('data.json'):
        with open("data.json", 'w+') as data:
            data.write('{}')
    for path in dirs:
        with open("data.json", 'r') as data:
            dic = json.load(data)
        image = Image.open(f"memes/{path}")
        image.show()
        answer = input("Вам нравится пикча? (д/н) : ")
        if answer.lower() in ('д', 'y'):
            if path not in dic.keys():
                dic[path] = 1
            else:
                dic[path] += 1
        image.close()
        with open("data.json", 'w') as data:
            json.dump(dic, data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Task()
    ex.show()
    sys.exit(app.exec_())