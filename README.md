<h1 align="center" >INVOICE GENERATOR</h1>

# Prerequisties: 
**1.** Required Libraries :

Install the following Python libraries :
    
**•** ```mysql-connector``` : To connect and interact with the MySQL database.

    pip install mysql-connector
**•** ```tabulate``` : To display data in table format.

    pip install tabulate
**•** ```qrcode``` : For generating QR codes.

    pip install qrcode
**•** ```pillow``` : Required for image processing (used by qrcode library).

    pip install pillow
**•** ```tkinter``` : For creating GUI

    pip install tk
**2.** MySQL Setup:

**•** Install [MySQL](https://dev.mysql.com/downloads/file/?id=534098) server on your system.

**•** Create a database named ```bill_generator_db```

    CREATE DATABASE bill_generator_db;
    
    USE bill_generator_db;
**•** Database Credentials:

Update the database credentials in the script (host, user, password, and database) based on your MySQL setup:

    db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0000",
    database="bill_generator_db"
    )
**3.** Internet Connection (optional):

**•** If QR code-based payment is enabled, you might need an internet connection to test or use UPI payment links.
