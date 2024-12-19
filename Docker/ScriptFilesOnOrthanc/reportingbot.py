This is the original (reportingbot.py) file that is adding data to the bot db on orthanc container production : - Himanshu
============================================================================================================================
aman.gupta@ip-10-12-1-83:~/Scripts$ cat reportingbot.py
import sys
import psycopg2
from psycopg2 import sql


#Orthanc generated study id obtained from system variable
study_id = sys.argv[1]

#patientName variable obtained from system variable
patientName = sys.argv[2]

#patientAge variable obtained from system variable
patientAge = sys.argv[3]

#patientGender variable obtained from system variable
patientGender = sys.argv[4]

#patientId variable obtained from system variable
patientId = sys.argv[5]

#studyDesc variable obtained from system variable
studyDesc = sys.argv[6]

#address variable obtained from system variable
address = sys.argv[7]

#studyDate variable obtained from system variable
studyDate = sys.argv[8]

#bodyParts variable obtained from system variable
bodyParts = sys.argv[9]




# Create a tuple of all the data to insert into the PostgreSQL database
data_to_insert = (patientName, patientId, patientAge, patientGender, studyDate, study_id, studyDesc, False, False, '', address, bodyParts)

# Connect to PostgreSQL database
conn = psycopg2.connect(
    dbname='botdb',
    user='postgres',
    password='postgres',
    host='10.12.0.92',
    port='5432'
)

# Create a cursor object
cursor = conn.cursor()

# Insert the data into the users_dicomdata table
insert_query = """
    INSERT INTO users_dicomdata (
        patient_name, patient_id, age, gender, study_date, study_id, study_description, "isDone", "NonReportable", notes, location, body_part_examined
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""
cursor.execute(insert_query, data_to_insert)

# Commit the transaction
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
aman.gupta@ip-10-12-1-83:~/Scripts$
 