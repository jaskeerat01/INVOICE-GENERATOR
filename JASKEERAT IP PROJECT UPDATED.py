import mysql.connector
from tabulate import tabulate
import qrcode
from PIL import Image
import datetime
from tkinter import  *
from tkinter import ttk
from tkinter import font
def proceed():
    root.destroy()
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="0000",
        database="bill_generator_db"
    )
    cursor = db.cursor()
    
    # Create new tables for invoices and invoice items if they don't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Invoices (
        InvoiceID INT AUTO_INCREMENT PRIMARY KEY,
        TotalAmount INTEGER,
        InvoiceDate DATETIME
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS InvoiceItems (
        ItemID INT AUTO_INCREMENT PRIMARY KEY,
        InvoiceID INT,
        ProductName VARCHAR(255),
        Quantity INT,
        Rate INTEGER,
        Amount INTEGER,
        FOREIGN KEY (InvoiceID) REFERENCES Invoices(InvoiceID)
    )
    """)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    query='SELECT name from products;'
    cursor.execute(query)
    result=[item[0] for item in cursor.fetchall()]
    l=len(result)+1

    print('\t\t\tINVOICE GENERATOR')
    print('Available Products:')
    cart=[ ]
    invoice=[ ]
    total=[ ]
    ratel=[ ]

    while True:
        for i in range(1, l):
            print(i, '.', result[i - 1])
        
        choice = int(input('Enter the product number (0 to finish):'))
        
        if choice == 0:
            
            if not cart:
                print('Cart is empty. Nothing to invoice.')
                break
            
            print('Cart:')
            uni_cart=set(cart)
            
            for i in uni_cart:
                quantity=cart.count(i)
                print(i,'x',quantity)
                
                query1='SELECT PRICE from products WHERE NAME=%s;'
                cursor.execute(query1,(i,))
                result1=[items[0] for items in cursor.fetchall()]
                
                rate = result1[0]
                ratel.append(rate)
                amount = rate * quantity
                total.append(amount)
                invoice.append([i,quantity,rate,amount])
            
            # Calculate the tax amount
            cgst_rate = sgst_rate = 9 / 100  # Change this to your actual tax rate
            cgst_amount = sgst_amount = sum(total) * cgst_rate
            total_amount=round(sum(total) + cgst_amount + sgst_amount,0)
            # Insert the invoice into the Invoices table after calculating the total amount and tax amount
            cursor.execute("""
            INSERT INTO Invoices (TotalAmount, InvoiceDate)
            VALUES (%s, NOW())
            """, (total_amount,))
            db.commit()

            # Get the ID of the invoice we just inserted
            invoice_id = cursor.lastrowid

            # Convert uni_cart to a list
            uni_cart_list = list(uni_cart)

            for i in range(len(uni_cart_list)):
                # Insert the invoice item into the InvoiceItems table
                cursor.execute("""
                INSERT INTO InvoiceItems (InvoiceID, ProductName, Quantity, Rate, Amount)
                VALUES (%s, %s, %s, %s, %s)
                """, (invoice_id, uni_cart_list[i], cart.count(uni_cart_list[i]), ratel[i], total[i]))
                db.commit()
            
            header=['PRODUCT NAME','QUANTITY','RATE','AMOUNT']
            print('\t\tB.B.S MEGA MART')
            
            now = datetime.datetime.now()
            print(now.strftime("%d-%m-%Y"),'\t\tINVOICE',now.strftime("\t%H:%M:%S"))
            
            invoice.append(['CGST (9%)', '', '', cgst_amount])
            invoice.append(['SGST (9%)', '', '', sgst_amount])
            
            print(tabulate(invoice,headers=header,tablefmt="fancy_grid"))
            
            print('\tTOTAL AMOUNT BEFORE TAX:','₹',sum(total))
            print('\tTOTAL AMOUNT AFTER TAX:','₹',total_amount)

            
            qc=input('DO YOU WANT TO PAY BY QR CODE(Y/N)')
            if qc=='Y':
                upi_linktest='upi://pay?pa=amarpreet.sidman@okaxis&pn=Amarpreet%20Kaur&am={}&cu=INR&aid=uGICAgIC1oJ-TQ'
                upi_link=upi_linktest.format(total_amount)
                qr.add_data(upi_link)
                qr.make(fit=True)
                
                img = qr.make_image(fill_color="black", back_color="white")
                img.show()
            
            print('THANK YOU FOR SHOPPING :)')
            break
        elif 1 <= choice < l:
            cart.append(result[choice - 1])
            print(result[choice - 1],'added to cart')
        else:
            print('Invalid product number.')

    cursor.close()
    db.close()
root=Tk()
root.title("WELCOME TO B.B.S. MEGA MART")
root.geometry("550x750")
root.configure(bg='yellow')
customFont=font.Font(family="algerian", size=40, underline=True)
label1=Label(text="WELCOME TO B.B.S. MEGA MART",font=customFont,fg='green',bg='yellow')
label1.place(x=375, y=30)
label2=Label(root,text="DEVELOPED BY:",font="algerian 40",fg='green',bg='yellow')
label2.place(x=100,y=100)
label3=Label(root,text="1. JASKEERAT SINGH",font="algerian 40",fg='green',bg='yellow')
label3.place(x=30,y=175)
label4=Label(root,text="2. KARTIKEY VARSHNEY",font="algerian 40",fg='green',bg='yellow')
label4.place(x=30,y=250)
b1=Button(root, text="NEXT =>",font="arial 20 bold",bg='red',fg='yellow',command=proceed)
b1.place(x=700,y=440)
root.mainloop()
