# medicalSurveyGUI
cd ./new
pyinstaller --onefile ./mainApp.py --noconsole --icon ./med.ico --add-data="checkmark.png;." --add-data="leftArrow.png;." --add-data="rightArrow.png;."