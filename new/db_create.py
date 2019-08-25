import sqlite3
import os

name_db = 'timetable.db'
cur_dir = os.getcwd()
path_db = os.path.join(cur_dir, name_db)

if not os.path.exists(path_db):
	try:
		conn = sqlite3.connect(path_db)
		cursor = conn.cursor()

		#создание таблиц + наполнение
		cursor.executescript("""
			BEGIN TRANSACTION;
			CREATE TABLE CLIENTS (
				id    INTEGER PRIMARY KEY AUTOINCREMENT,
				client_full_name    TEXT,
                client_birth_date   INTEGER NOT NULL
			);
			
			CREATE TABLE DOCTORS (
				id    INTEGER PRIMARY KEY AUTOINCREMENT,
				doctor_full_name    TEXT
			);

			CREATE TABLE SCHEDULE (
				booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
				client_id INTEGER NOT NULL,
				doctor_id INTEGER NOT NULL,
				consultancy_start_time INTEGER NOT NULL,
				consultancy_end_time INTEGER NOT NULL,
				type_of_consultation TEXT NOT NULL,
				consultancy_duration INTEGER NOT NULL,
				FOREIGN KEY (client_id) REFERENCES CLIENTS(id),
				FOREIGN KEY (doctor_id) REFERENCES DOCTORS(id)
			); 
			COMMIT;
		""")
		conn.commit()
            
	except sqlite3.Error as e:            
		print('Ошибка БД: ' + str(e))
