# medicalSurveyGUI
cd ./new

pyuic5 shell_ui.ui -o shell_ui.py

pyinstaller --onefile ./mainApp.py --noconsole --icon ./med.ico --add-data="checkmark.png;." --add-data="leftArrow.png;." --add-data="rightArrow.png;."





<!-- import os, sys


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


 icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("checkmark.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
  -->



<!-- 
"SELECT CLIENTS.client_full_name AS client_name, "
            "DOCTORS.doctor_full_name  AS doctor_name,"
            "strftime('%H:%M', DATETIME(SCHEDULE.consultancy_start_time, 'unixepoch','localtime')) AS consultancy_start,"
            "strftime('%H:%M', DATETIME(SCHEDULE.consultancy_end_time, 'unixepoch','localtime')) AS consultancy_finish,"
            "strftime('%m/%Y', DATETIME(SCHEDULE.consultancy_start_time, 'unixepoch','localtime')) AS date_of_consultancy,"
            "SCHEDULE.consultancy_start_time AS unix_epoch_time_start,"
            "SCHEDULE.consultancy_end_time AS unix_epoch_time_finish,"
            "SCHEDULE.type_of_consultation AS consultancy_type,"
            "SCHEDULE.consultancy_duration  AS duration"
            "FROM SCHEDULE"
            )
            # "INNER JOIN CLIENTS ON SCHEDULE.client_id=CLIENTS.id INNER JOIN DOCTORS ON SCHEDULE.doctor_id=DOCTORS.id"
            # "ORDER BY SCHEDULE.consultancy_start_time"
            # "WHERE SCHEDULE.consultancy_start_time >= ?  AND SCHEDULE.consultancy_start_time <= ?"



" SELECT CLIENTS.client_full_name AS client_name, "
" DOCTORS.doctor_full_name AS doctor_name, "
" strftime('%H:%M', DATETIME(consultancy_start_time, 'unixepoch','localtime')) AS 'start', "
" strftime('%H:%M', DATETIME(consultancy_end_time, 'unixepoch','localtime')) AS 'finish', "
" strftime('%m/%Y', DATETIME(consultancy_start_time, 'unixepoch','localtime')) AS 'date', "
" consultancy_start_time AS unix_epoch_time_start, "
" consultancy_end_time AS unix_epoch_time_finish, "
" type_of_consultation AS consultancy_type, "
" consultancy_duration  AS duration "
" FROM SCHEDULE "
" INNER JOIN CLIENTS ON SCHEDULE.client_id=CLIENTS.id INNER JOIN DOCTORS ON SCHEDULE.doctor_id=DOCTORS.id "
" WHERE SCHEDULE.consultancy_start_time >= ? AND SCHEDULE.consultancy_start_time <= ? "
" ORDER BY SCHEDULE.consultancy_start_time;"
-->