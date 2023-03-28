import os 
import sys
from Connection import Conn


# Display SGCadaster Table
def all_students():
    qu= "SELECT [PK_ID], [DESCRIPTION] FROM [SGCadasterSystem].[dbo].[LK_SGOfficeCodes]"
    students = crs.execute(qu)
    students_data = []
    for row in students:
        student= {"ID":row[0], "Description":row[2]}
        students_data.append(student)

    final_data["students_info"] = students_data
    return final_data