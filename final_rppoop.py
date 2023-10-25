import pandas as pd
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from PIL import ImageTk, Image
from tkinter import Toplevel, Label, Frame
import mysql.connector
import os
import re
from tkinter import filedialog
import csv

# Create the main tkinter window
root = tk.Tk()
root.geometry("2000x2000")
root.title("Academic Search Engine")
root.configure()
bgimg = PhotoImage(file="coep.png")
bg_label = Label(root, image=bgimg)
bg_label.place(x=0, y=0, relheight=1, relwidth=1)


# Create a frame for the main content
frame = tk.Frame(root)
frame.pack(pady=20)

# Add a label for the heading
heading_label = tk.Label(frame, text="WELCOME TO COEP'S STUDENT MANAGEMENT SYSTEM", font=("Arial", 16, "bold")) #bg='orange')
heading_label.pack(pady=10)

# Create an entry field and a submit button
entry_frame = tk.Frame(frame, bg="pink")
entry_frame.pack()


def window1():
    window1 = Toplevel(root)
    window1.geometry("850x478")
    window1.configure(bg='light blue')
    w1 = Label(window1, text='Student Portal', font="headlabelfont", bg='light green', height='5')
    w1.pack(side=TOP, fill=X)
    
    # Get the path to the image file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(script_dir, "abc.jpg")  # Replace "image_file.jpg" with the actual image file name

    # Load and display the background image
    background_image = Image.open(image_path)
    background_image = background_image.resize((850, 478))  # Resize the image to fit the window
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = Label(window1, image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    # Keep a reference to the background_photo to prevent it from being garbage collected
    background_label.image = background_photo


    # Create a frame for the widgets
    #widget_frame = Frame(window1, )
    #widget_frame.pack(pady=20)
    
    def fetch_data():
        # Retrieve user input
        user_input = entry.get()

        # Connect to MySQL database
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Sainath@2521",
            database="fy22"
        )
        cursor = db.cursor()

        # Query the database
        query = "SELECT * FROM fydata WHERE MIS = %s"
        cursor.execute(query, (user_input,))
        row = cursor.fetchone()

        # Close database connection
        cursor.close()
        db.close()

        if row:
            # Create a new tkinter window
            window = tk.Toplevel(root)
            window.geometry("2000x2000")
            window.title("Student Information")
            window.configure(bg="lightblue")

            # Display the row data in the new window
            labels = ["MIS:", "Student Name:", "Division:", "Batches:", "Branch:", "Coep mailid:", "Mobile No:"]

            for i in range(len(labels)):
                label = tk.Label(window, text=f"{labels[i]}", font=("Arial", 12, "bold"), bg="lightblue")
                label.grid(row=i, column=0, sticky=tk.W, padx=10, pady=5)

                value_label = tk.Label(window, text=f"{row[i]}", font=("Arial", 12), bg="lightblue")
                value_label.grid(row=i, column=1, sticky=tk.W, padx=10, pady=5)
        else:
            # If no matching row is found, show an error message
            messagebox.showerror("Error", "MIS data is not available")

    def back_to_root():
        window1.destroy()

    
    mis_label = tk.Label(window1, text="MIS:", bg="pink", font=("Arial", 12, "bold"), width=5, height=2)
    mis_label.place(x=250, y=90)

    entry = tk.Entry(window1, font=("Arial", 12,), width=20)
    entry.place(x=350, y=100)  # Adjust the coordinates to position the entry widget correctly

    submit_button = tk.Button(window1,  text="Submit",  command=fetch_data, bg="#FFFF8C", font=("Arial", 12, "bold"), width=10, height=2)
    submit_button.place(x=380, y=160) 


    # Create a button to clear the entry field
    clear_button = tk.Button(window1,  text="Clear", command=lambda: entry.delete(0, tk.END), bg="#FFFF8C",
                             font=("Arial", 12, "bold"), width=10, height=2)
    clear_button.place(x=380, y=220) 

    back_button = tk.Button( window1, text="Back", command=back_to_root, bg="#FFFF8C", font=("Arial", 12, "bold"), width=10, height=2)
    back_button.place(x=380, y=280) 

def window2():
    window2 = Toplevel(root)
    window2.geometry("1500x1003")
    window2.configure(bg='light blue')
    #w2 = Label(window2, text='Admin Portal', font="headlabelfont", bg='light green', height='5')
    #w2.pack(side=TOP, fill=X)
    
    # Get the path to the image file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(script_dir, "admin2.jpg")  # Replace "image_file.jpg" with the actual image file name

    # Load and display the background image
    background_image = Image.open(image_path)
    background_image = background_image.resize((1500,1003))  # Resize the image to fit the window
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = Label(window2, image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    # Keep a reference to the background_photo to prevent it from being garbage collected
    background_label.image = background_photo

    #w2.lift()

    def download_excel():
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Sainath@2521",
            database="fy22"
        )

        # Create a cursor to interact with the database
        cursor = connection.cursor()

        # Execute the query to fetch data
        cursor.execute("SELECT * FROM fydata")

        # Fetch all the rows
        rows = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        # Create a DataFrame from the fetched data
        df = pd.DataFrame(rows, columns=["MIS:", "Student Name:", "Division:", "Batches:", "Branch:", "Coep mailid:", "Mobile No:"])

        # Save the DataFrame as an Excel file
        df.to_excel("student_data.xlsx", index=False)
        messagebox.showinfo("Success", "Excel file downloaded successfully and stored in the folder where the Source Code file is located.")

    def window4():
        window4 = tk.Toplevel(window2)
        window4.geometry("1400x867")
        window4.configure(bg='light blue')
        window4.deiconify()
        
         # Get the path to the image file
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, "101.jpg")  # Replace "image_file.jpg" with the actual image file name

        # Load and display the background image
        background_image = Image.open(image_path)
        background_image = background_image.resize((1400, 867))  # Resize the image to fit the window
        background_photo = ImageTk.PhotoImage(background_image)
        background_label = Label(window4, image=background_photo)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Keep a reference to the background_photo to prevent it from being garbage collected
        background_label.image = background_photo

        def fetch_data():
            # Connect to the MySQL database
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Sainath@2521",
                database="fy22"
            )

            # Create a cursor to interact with the database
            cursor = connection.cursor()

            # Execute the query to fetch data
            cursor.execute("SELECT * FROM fydata")

            # Fetch all the rows
            rows = cursor.fetchall()

            # Close the cursor and connection
            cursor.close()
            connection.close()

            # Create a new window to display the data
            data_window = tk.Toplevel(window4)
            data_window.title("Student Data")
            data_window.geometry("2000x2000")
            data_window.configure(bg='light blue')
            
             # Get the path to the image file
            script_dir = os.path.dirname(os.path.abspath(__file__))
            image_path = os.path.join(script_dir, "102.jpg")  # Replace "image_file.jpg" with the actual image file name

            # Load and display the background image
            background_image = Image.open(image_path)
            background_image = background_image.resize((1400, 867))  # Resize the image to fit the window
            background_photo = ImageTk.PhotoImage(background_image)
            background_label = Label(data_window, image=background_photo)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)
            
            # Keep a reference to the background_photo to prevent it from being garbage collected
            background_label.image = background_photo

            # Create a Treeview widget to display the data
            treeview = ttk.Treeview(data_window)
            treeview.pack()

            # Define the columns
            columns = ["MIS:", "Student Name:", "Division:", "Batches:", "Branch:", "Coep mailid:", "Mobile No:"]

            # Configure the Treeview columns
            treeview['columns'] = columns
            treeview.heading('#0', text='Row')
            for col in columns:
                treeview.heading(col, text=col)

            # Insert the fetched data into the Treeview widget
            for i, row in enumerate(rows):
                treeview.insert('', 'end', text=str(i + 1), values=row)

            # Adjust column widths
            for col in columns:
                treeview.column(col, width=100)  # Adjust the width as needed

            download_button = Button(data_window, text='Download Excel', font=("headlabelfont", 12, "bold"), height='3', width=30, bg='#FFC125',
                                     command=download_excel)
            download_button.place(x=570, y=300)
            

        def upload_data():
                file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

                if not file_path:
                    return  # User canceled the file dialog

                # Connect to the MySQL database
                db_connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Sainath@2521",
                    database="fy22"
                )

                # Create a cursor object to execute SQL queries
                cursor = db_connection.cursor()

                try:
                    with open(file_path, 'r') as csv_file:
                        csv_reader = csv.reader(csv_file)

                        for row in csv_reader:
                            if len(row) != 7:
                                messagebox.showerror("Error", "Invalid CSV format. Each row should have 7 columns.")
                                return

                            mis, student_name, division, batches, branch, coep_mail, mob_no = row
                            mob_no = mob_no.strip()

                            # Data validation (similar to your insert_data function)
                            if (not mis.isdigit() or
                                len(mob_no) != 10 or not mob_no.isdigit() or
                                not re.match(r"^[A-Za-z ]+$", student_name) or
                                not re.match(r".+@coeptech.ac.in$", coep_mail)):
                                messagebox.showerror("Error", "Invalid data in the CSV file.")
                                return

                            # Prepare the INSERT statement
                            insert_query = "INSERT INTO fydata (MIS, Student_Name, Division, Batches, Branch, Coep_Mail, mob_no) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                            values = (mis, student_name, division, batches, branch, coep_mail, mob_no)

                            # Execute the INSERT statement
                            cursor.execute(insert_query, values)

                    # Commit the changes to the database
                    db_connection.commit()

                    # Display a success message
                    messagebox.showinfo("Success", "Data uploaded successfully.")
                except Exception as error:
                    # Display an error message
                    messagebox.showerror("Error", str(error))
                finally:
                    # Close the cursor and database connection
                    cursor.close()
                    db_connection.close()
        
        def window6():
            window6 = Toplevel(window4)
            window6.geometry("2000x2000")
            window6.configure(bg='light blue')
            
             # Get the path to the image file
            script_dir = os.path.dirname(os.path.abspath(__file__))
            image_path = os.path.join(script_dir, "102.jpg")  # Replace "image_file.jpg" with the actual image file name

            # Load and display the background image
            background_image = Image.open(image_path)
            background_image = background_image.resize((1400, 867))  # Resize the image to fit the window
            background_photo = ImageTk.PhotoImage(background_image)
            background_label = Label(window6, image=background_photo)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)
            
            # Keep a reference to the background_photo to prevent it from being garbage collected
            background_label.image = background_photo
            labels = [
                ("MIS:", ""),
                ("Student_Name:", ""),
                ("Division:", ""),
                ("Batches:", ""),
                ("Branch:", ""),
                ("Coep_Mail:", ""),
                ("Mob_No:", "")
            ]

            entries = []

            def clear_entries():
                for entry in entries:
                    entry.delete(0, tk.END)

            def insert_data():
                # Access the values entered by the user
                data = [entry.get() for entry in entries]

                # Check if any fields are empty
                if any(not value for value in data):
                    messagebox.showerror("Error", "Please fill in all fields.")
                    return

                # Validate MIS entry
                mis_value = mis_entry.get()
                if not mis_value.isdigit():
                    messagebox.showerror("Error", "Invalid MIS. Must be an integer.")
                    return
                
                mobile_value = entries[-1].get()
                if len(mobile_value) != 10 or not mobile_value.isdigit():
                    messagebox.showerror("Error", "Invalid mobile number. Must be a 10-digit number.")
                    return
                
                student_name = data[1]
                if not re.match(r"^[A-Za-z ]+$", student_name):
                    messagebox.showerror("Error", "Invalid student name. Should contain alphabetic characters only.")
                    return
                
                coep_mail = data[5]
                if not re.match(r".+@coeptech.ac.in$", coep_mail):
                        messagebox.showerror("Error", "Invalid Coep_Mail. Should end with @coeptech.ac.in.")
                        return

                # Connect to the MySQL database
                db_connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Sainath@2521",
                    database="fy22"
                )

                # Create a cursor object to execute SQL queries
                cursor = db_connection.cursor()

                # Prepare the INSERT statement
                insert_query = "INSERT INTO fydata (MIS, Student_Name, Division, Batches, Branch, Coep_Mail, mob_no) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                values = tuple(data)  # Convert the data list into a tuple

                try:
                    # Execute the INSERT statement
                    cursor.execute(insert_query, values)

                    # Commit the changes to the database
                    db_connection.commit()

                    # Clear the entries
                    clear_entries()

                    # Display a success message
                    messagebox.showinfo("Success", "Data submitted successfully.")
                except mysql.connector.Error as error:
                    # Display an error message
                    messagebox.showerror("Error", str(error))

                # Close the cursor and database connection
                cursor.close()
                db_connection.close()

            # Create a frame to hold labels and entries
            frame = tk.Frame(window6, bg='#009ACD')
            frame.pack(pady=10)

            # Create labels and entries using the grid layout manager
            for row, (label_text, placeholder_text) in enumerate(labels):
                label = tk.Label(frame, text=label_text)
                label.grid(row=row, column=0, sticky="e", padx=10, pady=5)

                entry = tk.Entry(frame)
                entry.grid(row=row, column=1, padx=10, pady=5)

                # Add entry to the list
                entries.append(entry)

                # Validate MIS entry
                if label_text == "MIS:":
                    mis_entry = entry

            # Create buttons and place them in the next row
            submit_button = tk.Button(window6, text="Submit", command=insert_data, bg="orange", fg="white", relief=tk.RAISED, padx=10, pady=5)
            submit_button.pack(pady=10)

            clear_button = tk.Button(window6, text="Clear", command=clear_entries, bg="gray", fg="white", relief=tk.RAISED, padx=10, pady=5)
            clear_button.pack()
            
            
            upload_button = tk.Button(window6, text="Upload Data", command=upload_data, bg="green", fg="white", relief=tk.RAISED, padx=10, pady=5)
            upload_button.pack(pady=50)



        def window7():
            window7 = Toplevel(window4)
            window7.geometry("2000x2000")
            window7.configure(bg='light blue')
            
            # Get the path to the image file
            script_dir = os.path.dirname(os.path.abspath(__file__))
            image_path = os.path.join(script_dir, "102.jpg")  # Replace "image_file.jpg" with the actual image file name

            # Load and display the background image
            background_image = Image.open(image_path)
            background_image = background_image.resize((1400, 867))  # Resize the image to fit the window
            background_photo = ImageTk.PhotoImage(background_image)
            background_label = Label(window7, image=background_photo)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)
            
            # Keep a reference to the background_photo to prevent it from being garbage collected
            background_label.image = background_photo
            
    
            # Establish a connection to the MySQL database
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Sainath@2521",
                database="fy22"
            )

            def delete_data():
                # Retrieve the value from the entry field
                MIS = MIS_entry.get()

                # Create a cursor object to execute SQL queries
                cursor = conn.cursor()

                # Check if the MIS exists in the database
                select_sql = "SELECT * FROM fydata WHERE MIS = %s"
                select_values = (MIS,)
                cursor.execute(select_sql, select_values)
                result = cursor.fetchone()

                if result:
                    # MIS exists, proceed with deletion
                    # Delete the row from the database
                    delete_sql = "DELETE FROM fydata WHERE MIS = %s"
                    delete_values = (MIS,)
                    cursor.execute(delete_sql, delete_values)

                    # Commit the changes to the database
                    conn.commit()

                    # Display a success message
                    result_label.config(text="MIS exist in database and Data deleted successfully.")
                else:
                    # MIS does not exist, display an error message
                    result_label.config(text="MIS does not exist in the database.")

                # Close the cursor and the database connection
                cursor.close()
                conn.close()

            frame = tk.Frame(window7, bg="#009ACD")
            frame.pack(padx=10, pady=10)

            MIS_label = tk.Label(frame, text="MIS:", fg="red", font=("Arial", 12, "bold"))
            MIS_label.pack(padx=10, pady=10)
            
            MIS_entry = tk.Entry(frame)
            MIS_entry.pack(padx=10, pady=10)

            

            submit_button = tk.Button(frame, text="Submit", fg="green", command=delete_data, font=("Arial", 12, "bold"))
            submit_button.pack(padx=30, pady=10)

            result_label = tk.Label(frame,)
            result_label.pack()




        def close():
            window2.destroy()

        view = Button(window4, text='View Data', font=("headlabelfont", 16, "bold"), height='3', width=30, bg='#FF8C00',
                      command=fetch_data)
        insert = Button(window4, text='Insert Data', font=("headlabelfont", 16, "bold"), height='3', width=30, bg='#FF8C00',
                        command=window6)
        delete = Button(window4, text='Delete Data', font=("headlabelfont", 16, "bold"), height='3', width=30, bg='#FF8C00',
                        command=window7)
        exit = Button(window4, text='Exit', font=("headlabelfont", 16, "bold"), height='3', width=30, bg='#EE0000', command=close)
        view.place(x=570, y=200)
        insert.place(x=570, y=300)
        delete.place(x=570, y=400)
        exit.place(x=570, y=500)

    def submit_password():
        password = password_entry.get()
        if password == "1854":                  # establish year of coep
            window4()
        else:
            messagebox.showerror("Invalid Password", "The password is incorrect.")

    password_label = tk.Label(window2, text="Password:", bg="#FFFF8C", font=("headlabelfont", 14, "bold"), height='2', width='10').place(x=520,
                                                                                                            y=95)
    password_entry =tk.Entry(window2, show="*", width='20')
    password_entry.pack()
    password_entry.place(x=670, y=110)
    
    
    submit = Button(window2, text="Submit", command=submit_password,  font=("headlabelfont", 12, "bold"), bg="#FFFF8C", height='2', width='6')
    submit.place(x=700, y=160)


# Load the image
image_student = Image.open("student_portal.png")
image_student = image_student.resize((250, 100), Image.LANCZOS)  # Resize the image if needed
image_student = ImageTk.PhotoImage(image_student)

student = Button(root,image=image_student, compound=tk.LEFT,
                 font=("headlabelfont", 12, "bold"), bg='#EEEEDF', command=window1)
student.pack()
student.place(x=580, y=200)




# Load the image
admin_image = Image.open("admin_portal1.png")
admin_image = admin_image.resize((250, 100), Image.LANCZOS)  # Resize the image if needed
admin_image = ImageTk.PhotoImage(admin_image)

# Create the button with the image
admin = Button(root, image=admin_image, compound=tk.LEFT, font=("headlabelfont", 12, "bold"),  command=window2)
admin.pack()
admin.place(x=580, y=350)



def close():
    if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
        root.destroy()

# Load the image
image = PhotoImage(file="exit1.png")


# Create the exit button with the image
exit_button = Button(root, text="Exit", command=close, image=image, bg="red", font=("Arial", 12))
        
# Place the button in the window
exit_button.place(x=670, y=480)

# Start the tkinter event loop
root.mainloop()
