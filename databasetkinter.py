import mysql.connector
from tkinter import *

# Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Malick@123",
    auth_plugin='mysql_native_password'
)
crsr = mydb.cursor()
# crsr.execute("create database newdata")  # Uncomment if you need to create the database
crsr.execute("use newdata")
crsr.execute("""
    create table if not exists login (
        first_name varchar(50),
        last_name varchar(50),
        email_id varchar(50),
        phone_no bigint,
        user_id varchar(50) primary key,
        password varchar(10)
    )
""")

app = Tk()
app.title("Login page")
app.geometry("500x1000")

# Function to clear registration fields
def clear():
    en1.delete(0, END)
    en2.delete(0, END)
    en3.delete(0, END)
    en4.delete(0, END)
    en5.delete(0, END)
    en6.delete(0, END)

# Function to register
def register():
    first_name = en1.get()
    last_name = en2.get()
    email_id = en3.get()
    phone_no = en4.get()
    user_id = en5.get()
    password = en6.get()
    try:
        crsr.execute("""
            INSERT INTO login (first_name, last_name, email_id, phone_no, user_id, password)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (first_name, last_name, email_id, phone_no, user_id, password))
        mydb.commit()
        clear()
    except mysql.connector.IntegrityError:
        print("User ID already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to login
def show():
    user_id = en9.get()
    password = en10.get()
    crsr.execute("SELECT * FROM login WHERE user_id = %s AND password = %s", (user_id, password))
    user = crsr.fetchone()
    en9.delete(0, END)
    en10.delete(0, END)


    if user:
        print("Login successful!")
        display_user_info(user)

    else:
        print("Invalid information.")

# Function to display user information after login
def display_user_info(user):
    en11.delete(0, END)
    en11.insert(0, user[0])  # first_name
    en12.delete(0, END)
    en12.insert(0, user[1])  # last_name
    en13.delete(0, END)
    en13.insert(0, user[2])  # email_id
    en14.delete(0, END)
    en14.insert(0, user[3])  # phone_no
    en15.delete(0, END)
    en15.insert(0, user[4])  # user_id
    en16.delete(0, END)
    en16.insert(0, user[5])  # password

# Function to update user information
def update_user():
    first_name = en11.get()
    last_name = en12.get()
    email_id = en13.get()
    phone_no = en14.get()
    user_id = en15.get()
    password = en16.get()

    try:
        crsr.execute("""
            UPDATE login
            SET first_name = %s, last_name = %s, email_id = %s, phone_no = %s, password = %s
            WHERE user_id = %s
        """, (first_name, last_name, email_id, phone_no, password, user_id))
        mydb.commit()
        print("User information updated successfully.")
    except Exception as e:
        print(f"An error occurred while updating: {e}")

# Function to delete user information
def delete_user():
    user_id = en15.get()
    
    try:
        crsr.execute("DELETE FROM login WHERE user_id = %s", (user_id,))
        mydb.commit()
        clear()
        print("User deleted successfully.")
    except Exception as e:
        print(f"An error occurred while deleting: {e}")

def clear_out():
    en11.delete(0, END)
    en12.delete(0, END)
    en13.delete(0, END)
    en14.delete(0, END)
    en15.delete(0, END)
    en16.delete(0, END)



# Registration section
lb1 = Label(app, text="Registration page", font=('times new roman', 15, "bold"))
lb1.grid(pady=20, padx=10, row=0, column=1)

d1 = Label(app, text="First name:")
d1.grid(pady=3, row=1, column=1)
en1 = Entry(app)
en1.grid(pady=3, row=1, column=2)

d2 = Label(app, text="Last name:")
d2.grid(pady=3, row=2, column=1)
en2 = Entry(app)
en2.grid(pady=3, row=2, column=2)

d3 = Label(app, text="Email id:")
d3.grid(pady=3, row=3, column=1)
en3 = Entry(app)
en3.grid(pady=3, row=3, column=2)

d4 = Label(app, text="Phone no:")
d4.grid(pady=3, row=4, column=1)
en4 = Entry(app)
en4.grid(pady=3, row=4, column=2)

d5 = Label(app, text="User id:")
d5.grid(pady=3, row=5, column=1)
en5 = Entry(app)
en5.grid(pady=3, row=5, column=2)

d6 = Label(app, text="Password:")
d6.grid(pady=3, row=6, column=1)
en6 = Entry(app, show="*")
en6.grid(pady=3, row=6, column=2)

btn = Button(app, text="Submit", command=register,fg="white",bg="blue",activeforeground="black",activebackground="grey")
btn.grid(pady=20, row=7, column=2)

# Login section
d8 = Label(app, text="To view", font=("times new roman", 15, "bold"))
d8.grid(pady=3, row=9, column=1)

d9 = Label(app, text="User id:")
d9.grid(pady=3, row=10, column=1)
en9 = Entry(app)
en9.grid(pady=3, row=10, column=2)

d10 = Label(app, text="Password:")
d10.grid(pady=3, row=11, column=1)
en10 = Entry(app, show="*")
en10.grid(pady=3, row=11, column=2)

btn1 = Button(app, text="Submit", command=show,fg="white",bg="blue",activeforeground="black",activebackground="grey")
btn1.grid(pady=20, row=12, column=2)

# Display section
d11 = Label(app, text="First name:")
d11.grid(pady=3, row=13, column=1)
en11 = Entry(app)
en11.grid(pady=3, row=13, column=2)

d12 = Label(app, text="Last name:")
d12.grid(pady=3, row=14, column=1)
en12 = Entry(app)
en12.grid(pady=3, row=14, column=2)

d13 = Label(app, text="Email id:")
d13.grid(pady=3, row=15, column=1)
en13 = Entry(app)
en13.grid(pady=3, row=15, column=2)

d14 = Label(app, text="Phone no:")
d14.grid(pady=3, row=16, column=1)
en14 = Entry(app)
en14.grid(pady=3, row=16, column=2)

d15 = Label(app, text="User id:")
d15.grid(pady=3, row=17, column=1)
en15 = Entry(app)
en15.grid(pady=3, row=17, column=2)

d16 = Label(app, text="Password:")
d16.grid(pady=3, row=18, column=1)
en16 = Entry(app)
en16.grid(pady=3, row=18, column=2)

btn2 = Button(app, text="Update", command=update_user,fg="white",bg="blue",activeforeground="black",activebackground="grey")
btn2.grid(pady=3, row=19, column=2)

btn3 = Button(app, text="Delete", command=delete_user,fg="white",bg="red",activeforeground="black",activebackground="grey")
btn3.grid(pady=3, row=20, column=2)

btn4 = Button(app, text="Clear", command=clear_out,fg="white",bg="blue",activeforeground="black",activebackground="grey")
btn4.grid(pady=3, row=21, column=2)

app.mainloop()
