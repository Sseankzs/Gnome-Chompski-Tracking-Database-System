db = mysql.connector.connect(
    host= "localhost",
    user= "root",
    passwd = "password",
    database = "testdatabase"
)

mycursor = db.cursor()