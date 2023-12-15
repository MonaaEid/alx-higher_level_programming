
db_connection= MySQLdb.connect(
    host= "localhost",
	user=username,
	passwd=password,
    db=database, port=3306)
#  for city in cities:
#         for row in table[:-1]:
#             for i in row:
#                 print(city, end=", " )
#         print(table[-1][0])