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
				client_full_name    TEXT UNIQUE,
                client_birth_date   INTEGER NOT NULL
			);
			
			CREATE TABLE DOCTORS (
				id    INTEGER PRIMARY KEY AUTOINCREMENT,
				doctor_full_name    TEXT UNIQUE
			);

			CREATE TABLE SCHEDULE (
				booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
				client_id INTEGER NOT NULL,
				doctor_id INTEGER NOT NULL,
				consultancy_start_time INTEGER NOT NULL,
				consultancy_end_time INTEGER NOT NULL,
				type_of_consultation TEXT NOT NULL UNIQUE,
				consultancy_duration INTEGER NOT NULL,
				actual_consultancy_start_time INTEGER,
				FOREIGN KEY (client_id) REFERENCES CLIENTS(id),
				FOREIGN KEY (doctor_id) REFERENCES DOCTORS(id)
			); 
			COMMIT;
		""")
		conn.commit()

		cursor.executescript("""
			BEGIN TRANSACTION;
			INSERT INTO DOCTORS (doctor_full_name) VALUES 
      			('Голикова Ирина Васильевна'),('Женгурова Елена Александровна'),
				('Зюзева Надежда Валерьевна'),('Руднева Наталья Петровна'),
				('Садигова Оксана Александровна'); 
			COMMIT;
		""")
		conn.commit()
            
	except sqlite3.Error as e:            
		print('Ошибка БД: ' + str(e))

'''
SELECT * FROM CLIENTS;
SELECT id FROM CLIENTS where client_full_name = 'Иванов Иван Иванович';
SELECT * FROM DOCTORS;
SELECT id FROM DOCTORS where doctor_full_name = 'Голикова Ирина Васильевна';
SELECT * FROM SCHEDULE;
 /* Comments */
SELECT sql FROM sqlite_master WHERE name = 'SCHEDULE';


INSERT OR IGNORE INTO DOCTORS (doctor_full_name) VALUES 
      			('Голикова Ирина Васильевна'),('Женгурова Елена Александровна'),
				('Зюзева Надежда Валерьевна'),('Руднева Наталья Петровна'),
				('Садигова Оксана Александровна'); 

INSERT OR IGNORE INTO CLIENTS (client_full_name, client_birth_date) VALUES 
      			('Иванов Иван Иванович','739569600'),('Хамидуллин Динар Маратович','771105600'),
				('Зуев Акбар Ахматович','708033600'),('Кадыров Руден Ирекович','644875200'); 

INSERT OR IGNORE INTO SCHEDULE (client_id,doctor_id, consultancy_start_time, consultancy_end_time, consultancy_duration, type_of_consultation) VALUES 
      			('4','1','1567278000','1567281600','60','Test1 Consultation'),
				('4','2','1567278000','1567285600','60','Test2 Consultation'),
				('4','2','1567227600','1567234800','120','Test3 Consultation'); 


SELECT CLIENTS.client_full_name AS client_name, 
	DOCTORS.doctor_full_name  AS doctor_name,
	strftime('%H:%M', DATETIME(SCHEDULE.consultancy_start_time, 'unixepoch','localtime')) AS consultancy_start,
	strftime('%H:%M', DATETIME(SCHEDULE.consultancy_end_time, 'unixepoch','localtime')) AS consultancy_finish,
	strftime('%d/%m/%Y', DATETIME(SCHEDULE.consultancy_start_time, 'unixepoch','localtime')) AS date_of_consultancy,
	SCHEDULE.consultancy_start_time AS unix_epoch_time_start,
	SCHEDULE.consultancy_end_time AS unix_epoch_time_finish,
	SCHEDULE.type_of_consultation AS consultancy_type,
	SCHEDULE.consultancy_duration  AS duration
	FROM SCHEDULE
	INNER JOIN CLIENTS ON SCHEDULE.client_id=CLIENTS.id INNER JOIN DOCTORS ON SCHEDULE.doctor_id=DOCTORS.id
	WHERE SCHEDULE.consultancy_start_time >= '1567198800' AND SCHEDULE.consultancy_start_time <= '1567285200'
	ORDER BY SCHEDULE.consultancy_start_time;
'''