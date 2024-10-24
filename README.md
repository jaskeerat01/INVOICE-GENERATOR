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
**•** ```datetime``` : Returns the current local date and time

    pip install datetime
**2.** MySQL Setup:

**•** Install [MySQL](https://dev.mysql.com/downloads/file/?id=534098) server on your system.

**•** Create a database named ```bill_generator_db```

    CREATE DATABASE bill_generator_db;
    
    USE bill_generator_db;
**•** Create table named ```products``` under database ```bill_generator_db``` :

    CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    price INT
    );
**•** Enter the names of products in the table based on your choice:

Example:

    INSERT INTO products (id, name, price) VALUES
    (1, 'PRODUCT A', 50),
    (2, 'PRODUCT B', 20),
    (3, 'PRODUCT C', 35),
    (4, 'PRODUCT D', 25),
    (5, 'PRODUCT E', 65);

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

## Working:
This project is a Billing System for a store, with features for invoice generation, QR code-based payment, and a graphical user interface (GUI) to interact with the user. Here's a breakdown of how the project works based on the script:

**1.** User Interface (GUI)
The GUI is created using Tkinter, which welcomes the user to "B.B.S Mega Mart."
The interface displays buttons and labels such as "WELCOME TO B.B.S. MEGA MART" and the developers' names.
There's a NEXT button that, when clicked, proceeds to the main billing system by invoking the proceed() function.

**2.** Database Setup (MySQL)
Upon clicking the "NEXT" button, the program connects to a MySQL database (bill_generator_db) using mysql-connector.
If tables for Invoices and InvoiceItems do not exist, they are created automatically:
Invoices Table: Stores each invoice's total amount and the date it was generated.
InvoiceItems Table: Stores the details of each item in an invoice, including the product name, quantity, rate, and amount.

**3.** Product Selection
The program queries the products table in the database to retrieve a list of available products. These products are displayed to the user in a list format.
The user is prompted to select a product by entering its number and can continue selecting products until they are done (entering '0' finishes the selection).

**4.** Cart and Invoice Generation
For each product selected, it is added to a cart.
After the product selection is completed, the program:
Calculates the total amount for each item in the cart (based on the quantity selected).
Adds two types of taxes: CGST (9%) and SGST (9%).
Calculates the final total amount including taxes.
Inserts the total amount and current date into the Invoices table.
For each item in the invoice, inserts its details (product name, quantity, rate, and amount) into the InvoiceItems table, linking it to the corresponding invoice.

**5.** Invoice Display
The generated invoice is displayed in the console using the tabulate library, which presents the data in a neatly formatted table.
The table includes:
Product name, quantity, rate, and amount.
CGST and SGST amounts.
Total amount before tax and after tax.
The invoice is printed with the store's name and the current date and time.

**6.** QR Code for Payment
After the invoice is generated, the user is asked if they want to pay via a QR code.
If they agree (Y), a QR code is generated using the qrcode library with the total amount embedded in a UPI payment link (example provided is for amarpreet.sidman@okaxis).
The QR code is displayed as an image for the user to scan and make the payment.

**7.** Program Exit
Once the invoice is displayed and payment (if chosen) is processed, the program thanks the user for shopping and exits.

**Summary of Workflow:**
GUI: User clicks "Next" to proceed to the billing system.
Product Selection: User selects products from a list.
Invoice Generation:
Cart is processed.
Invoice is created with taxes and stored in the database.
Display: The invoice is displayed in a tabulated format.
QR Payment: Optional QR code is generated for UPI payment.
End: The user is thanked, and the program exits.
This project is a well-rounded billing system suitable for small stores, combining GUI, database management, and advanced features like QR code-based payments.
