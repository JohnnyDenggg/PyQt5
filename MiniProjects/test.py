#文件名 unix_time.py

from PyQt5.QtCore import QDateTime, Qt

now = QDateTime.currentDateTime() #当前日期与时间

unix_time = now.toSecsSinceEpoch() #获取Unix时间
print(unix_time)

d = QDateTime.fromSecsSinceEpoch(unix_time) #Unix时间转换为QDate
print(d.toString(Qt.ISODate))