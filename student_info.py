

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv


def display_data():

    window1 = Toplevel(table)
    window1.title("Student Data")
    window1.geometry("1350x650")
    window1.configure(bg="#EAF4F8")

    title_frame = Frame(
        window1,
        bg="#123B5D",
        height=80
    )

    title_frame.pack(
        fill=X,
        padx=15,
        pady=(15, 10)
    )

    title_frame.pack_propagate(False)

    title = Label(
        title_frame,
        text="STUDENT DATA",
        font=("Calibri", 25, "bold"),
        bg="#123B5D",
        fg="white"
    )

    title.pack(
        side=LEFT,
        padx=25
    )

    search_frame = Frame(
        window1,
        bg="#EAF4F8"
    )

    search_frame.pack(
        fill=X,
        padx=20,
        pady=5
    )

    Label(
        search_frame,
        text="Search:",
        font=("Calibri", 14, "bold"),
        bg="#EAF4F8",
        fg="#123B5D"
    ).pack(
        side=LEFT,
        padx=(0, 8)
    )

    search_var = StringVar()

    search_entry = Entry(
        search_frame,
        textvariable=search_var,
        font=("Calibri", 13),
        width=35,
        relief="solid",
        bd=1
    )

    search_entry.pack(
        side=LEFT,
        ipady=5
    )

    def reset_search():

        search_var.set("")

        for item in all_items:

            tree.reattach(
                item,
                "",
                "end"
            )

    reset_button = Button(
        search_frame,
        text="RESET",
        font=("Calibri", 12, "bold"),
        bg="#167D9A",
        fg="white",
        activebackground="#0B5D73",
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        padx=20,
        pady=5,
        command=reset_search
    )

    reset_button.pack(
        side=LEFT,
        padx=10
    )

    table_frame = Frame(
        window1,
        bg="white",
        bd=1,
        relief="solid"
    )

    table_frame.pack(
        fill=BOTH,
        expand=True,
        padx=20,
        pady=10
    )

    style = ttk.Style()

    style.theme_use("clam")

    style.configure(
        "Student.Treeview",
        background="white",
        foreground="#17202A",
        rowheight=35,
        fieldbackground="white",
        font=("Calibri", 11)
    )

    style.configure(
        "Student.Treeview.Heading",
        background="#167D9A",
        foreground="white",
        font=("Calibri", 12, "bold"),
        relief="flat"
    )

    style.map(
        "Student.Treeview",
        background=[("selected", "#BFE3F2")],
        foreground=[("selected", "#123B5D")]
    )

    tree = ttk.Treeview(
        table_frame,
        style="Student.Treeview",
        show="headings"
    )

    tree.pack(
        side=LEFT,
        fill=BOTH,
        expand=True
    )

    scrollbar_y = ttk.Scrollbar(
        table_frame,
        orient=VERTICAL,
        command=tree.yview
    )

    scrollbar_y.pack(
        side=RIGHT,
        fill=Y
    )

    scrollbar_x = ttk.Scrollbar(
        window1,
        orient=HORIZONTAL,
        command=tree.xview
    )

    scrollbar_x.pack(
        fill=X,
        padx=20
    )

    tree.configure(
        yscrollcommand=scrollbar_y.set,
        xscrollcommand=scrollbar_x.set
    )

    try:

        with open(
            "student_data.csv",
            "r"
        ) as f:

            csvReader = csv.reader(f)

            next(csvReader)

            data = list(csvReader)

    except FileNotFoundError:

        messagebox.showerror(
            "File Error",
            "student_data.csv was not found!"
        )

        window1.destroy()
        return

    if len(data) == 0:

        messagebox.showinfo(
            "No Data",
            "There is no data in the CSV file."
        )

        window1.destroy()
        return

    headers = [
        "Roll No",
        "First Name",
        "Last Name",
        "Class",
        "Division",
        "ID Number",
        "English",
        "Urdu",
        "Maths",
        "Science",
        "SST",
        "Hindi"
    ]

    tree["columns"] = headers

    column_widths = {
        "Roll No": 90,
        "First Name": 130,
        "Last Name": 130,
        "Class": 80,
        "Division": 100,
        "ID Number": 130,
        "English": 100,
        "Urdu": 100,
        "Maths": 100,
        "Science": 100,
        "SST": 100,
        "Hindi": 100
    }

    for column in headers:

        tree.heading(
            column,
            text=column
        )

        tree.column(
            column,
            width=column_widths[column],
            anchor=CENTER
        )

    for row in data:

        if len(row) >= 12:

            tree.insert(
                "",
                END,
                values=(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6],
                    row[7],
                    row[8],
                    row[9],
                    row[10],
                    row[11]
                )
            )

    all_items = tree.get_children()

    tree.tag_configure(
        "evenrow",
        background="#F4FAFC"
    )

    tree.tag_configure(
        "oddrow",
        background="white"
    )

    for index, item in enumerate(all_items):

        if index % 2 == 0:

            tree.item(
                item,
                tags=("evenrow",)
            )

        else:

            tree.item(
                item,
                tags=("oddrow",)
            )

    def search_data(*args):

        search_text = search_var.get().lower()

        for item in all_items:

            values = tree.item(
                item,
                "values"
            )

            found = False

            for value in values:

                if search_text in str(value).lower():

                    found = True
                    break

            if found:

                tree.reattach(
                    item,
                    "",
                    "end"
                )

            else:

                tree.detach(item)

    search_var.trace_add(
        "write",
        search_data
    )

    close_button = Button(
        window1,
        text="CLOSE",
        font=("Calibri", 13, "bold"),
        bg="#167D9A",
        fg="white",
        activebackground="#0B5D73",
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        padx=30,
        pady=8,
        command=window1.destroy
    )

    close_button.pack(
        pady=12
    )



def show_result():

    result_window = Toplevel(table)

    result_window.title(
        "Student Result"
    )

    result_window.geometry(
        "650x700"
    )

    result_window.configure(
        bg="#EAF4F8"
    )

    result_window.resizable(
        False,
        False
    )

    result_header = Label(
        result_window,
        text="STUDENT RESULT",
        font=("Calibri", 25, "bold"),
        bg="#123B5D",
        fg="white",
        padx=30,
        pady=18
    )

    result_header.pack(
        fill=X,
        padx=15,
        pady=15
    )

    roll_frame = Frame(
        result_window,
        bg="#EAF4F8"
    )

    roll_frame.pack(
        pady=10
    )

    Label(
        roll_frame,
        text="Enter Roll Number:",
        font=("Calibri", 14, "bold"),
        bg="#EAF4F8",
        fg="#123B5D"
    ).pack(
        side=LEFT,
        padx=10
    )

    roll_entry = Entry(
        roll_frame,
        font=("Calibri", 14),
        width=18,
        relief="solid",
        bd=1
    )

    roll_entry.pack(
        side=LEFT,
        ipady=5
    )

    result_area = Frame(
        result_window,
        bg="#EAF4F8"
    )

    result_area.pack(
        fill=BOTH,
        expand=True,
        padx=25,
        pady=10
    )

    def calculate_result():

        roll_no = roll_entry.get().strip()

        if roll_no == "":

            messagebox.showwarning(
                "Warning",
                "Please enter a Roll Number!"
            )

            return

        for widget in result_area.winfo_children():

            widget.destroy()

        try:

            with open(
                "student_data.csv",
                "r"
            ) as f:

                csvReader = csv.reader(f)

                
                next(csvReader)

                student_found = False

                for row in csvReader:

                    if len(row) >= 12:

                        
                        if row[0].strip() == roll_no:

                            student_found = True

                            

                            student_roll = row[0]
                            first_name = row[1]
                            last_name = row[2]

                            

                            english_marks = float(row[6])
                            urdu_marks = float(row[7])
                            maths_marks = float(row[8])
                            science_marks = float(row[9])
                            sst_marks = float(row[10])
                            hindi_marks = float(row[11])

                            

                            total_marks = (
                                english_marks +
                                urdu_marks +
                                maths_marks +
                                science_marks +
                                sst_marks +
                                hindi_marks
                            )

                            

                            percentage = (
                                total_marks / 600
                            ) * 100

                            Label(
                                result_area,
                                text="Student Name",
                                font=("Calibri", 14, "bold"),
                                bg="#EAF4F8",
                                fg="#123B5D"
                            ).pack(
                                pady=(5, 2)
                            )

                            Label(
                                result_area,
                                text=first_name + " " + last_name,
                                font=("Calibri", 18, "bold"),
                                bg="#EAF4F8",
                                fg="#167D9A"
                            ).pack(
                                pady=(0, 8)
                            )

                            
                            Label(
                                result_area,
                                text="Roll Number: " + student_roll,
                                font=("Calibri", 13),
                                bg="#EAF4F8",
                                fg="#17202A"
                            ).pack(
                                pady=4
                            )

                            marks_frame = Frame(
                                result_area,
                                bg="white",
                                bd=1,
                                relief="solid"
                            )

                            marks_frame.pack(
                                fill=X,
                                pady=12
                            )

                            Label(
                                marks_frame,
                                text="SUBJECT MARKS",
                                font=("Calibri", 14, "bold"),
                                bg="#BFE3F2",
                                fg="#123B5D",
                                pady=7
                            ).pack(
                                fill=X
                            )

                            Label(
                                marks_frame,
                                text=(
                                    f"English     : {english_marks:g}\n"
                                    f"Urdu        : {urdu_marks:g}\n"
                                    f"Maths       : {maths_marks:g}\n"
                                    f"Science     : {science_marks:g}\n"
                                    f"SST         : {sst_marks:g}\n"
                                    f"Hindi       : {hindi_marks:g}"
                                ),
                                font=("Calibri", 12),
                                bg="white",
                                fg="#17202A",
                                justify=LEFT,
                                padx=25,
                                pady=10
                            ).pack(
                                anchor="w"
                            )

                            Label(
                                result_area,
                                text="TOTAL MARKS",
                                font=("Calibri", 14, "bold"),
                                bg="#EAF4F8",
                                fg="#123B5D"
                            ).pack(
                                pady=(5, 2)
                            )

                            Label(
                                result_area,
                                text=f"{total_marks:g} / 600",
                                font=("Calibri", 18, "bold"),
                                bg="#BFE3F2",
                                fg="#123B5D",
                                padx=25,
                                pady=7
                            ).pack()

                            Label(
                                result_area,
                                text="PERCENTAGE",
                                font=("Calibri", 15, "bold"),
                                bg="#EAF4F8",
                                fg="#123B5D"
                            ).pack(
                                pady=(12, 3)
                            )

                            Label(
                                result_area,
                                text=f"{percentage:.2f}%",
                                font=("Calibri", 28, "bold"),
                                bg="#167D9A",
                                fg="white",
                                padx=35,
                                pady=10
                            ).pack()

                            return

                
                if not student_found:

                    Label(
                        result_area,
                        text="Student Not Found",
                        font=("Calibri", 18, "bold"),
                        bg="#EAF4F8",
                        fg="#C0392B"
                    ).pack(
                        pady=30
                    )

                    Label(
                        result_area,
                        text="No student was found with Roll Number: "
                             + roll_no,
                        font=("Calibri", 12),
                        bg="#EAF4F8",
                        fg="#17202A"
                    ).pack()

        except FileNotFoundError:

            messagebox.showerror(
                "File Error",
                "student_data.csv was not found!"
            )

        except ValueError:

            messagebox.showerror(
                "Invalid Marks",
                "The marks in the CSV file must be numbers."
            )

    Button(
        result_window,
        text="SHOW RESULT",
        font=("Calibri", 14, "bold"),
        bg="#167D9A",
        fg="white",
        activebackground="#0B5D73",
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        padx=30,
        pady=8,
        command=calculate_result
    ).pack(
        pady=8
    )

    Button(
        result_window,
        text="CLOSE",
        font=("Calibri", 12, "bold"),
        bg="#123B5D",
        fg="white",
        activebackground="#0B5D73",
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        padx=35,
        pady=7,
        command=result_window.destroy
    ).pack(
        pady=(2, 15)
    )

    
    roll_entry.focus()


def save_data():

    if (
        fname.get() == "" or
        lname.get() == "" or
        sclass.get() == "" or
        division.get() == "" or
        rnumber.get() == "" or
        idnumber.get() == "" or
        english.get() == "" or
        urdu.get() == "" or
        maths.get() == "" or
        science.get() == "" or
        sst.get() == "" or
        hindi.get() == ""
    ):

        messagebox.showerror(
            "Alert!",
            "All Fields must be filled!"
        )

    else:

        with open(
            "student_data.csv",
            "a",
            newline=""
        ) as f1:

            csvWriter = csv.writer(f1)

            csvWriter.writerow([
                rnumber.get(),
                fname.get(),
                lname.get(),
                sclass.get(),
                division.get(),
                idnumber.get(),
                english.get(),
                urdu.get(),
                maths.get(),
                science.get(),
                sst.get(),
                hindi.get()
            ])

        messagebox.showinfo(
            "Success!",
            "Data Stored Successfully!"
        )


        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
        e7.delete(0, END)
        e8.delete(0, END)
        e9.delete(0, END)
        e10.delete(0, END)
        e11.delete(0, END)
        e12.delete(0, END)



table = Tk()

table.title("Student Information System")
table.geometry("850x720")
table.resizable(False, False)



bg_color = "#EAF4F8"
header_color = "#123B5D"
label_color = "#173F5F"
entry_bg = "#FFFFFF"
button_color = "#167D9A"
button_hover = "#0B5D73"

table.configure(
    bg=bg_color
)


fname = StringVar()
lname = StringVar()
sclass = StringVar()
division = StringVar()
rnumber = StringVar()
idnumber = StringVar()
english = StringVar()
urdu = StringVar()
maths = StringVar()
science = StringVar()
sst = StringVar()
hindi = StringVar()



header = Label(
    table,
    text="STUDENT INFORMATION FORM",
    font=("Calibri", 26, "bold"),
    bg=header_color,
    fg="white",
    padx=30,
    pady=20
)

header.grid(
    row=0,
    column=0,
    columnspan=4,
    sticky="ew",
    padx=15,
    pady=(15, 20)
)



def create_label(text, row, column):

    label = Label(
        table,
        text=text,
        font=("Calibri", 14, "bold"),
        bg=bg_color,
        fg=label_color
    )

    label.grid(
        row=row,
        column=column,
        padx=18,
        pady=9,
        sticky="w"
    )

    return label


def create_entry(variable, row, column):

    entry = Entry(
        table,
        font=("Calibri", 14),
        textvariable=variable,
        bg=entry_bg,
        fg="#17202A",
        insertbackground=button_color,
        relief="solid",
        bd=1,
        width=18
    )

    entry.grid(
        row=row,
        column=column,
        padx=18,
        pady=9,
        ipady=5
    )

    return entry


create_label(
    "First Name",
    1,
    0
)

e1 = create_entry(
    fname,
    1,
    1
)


create_label(
    "Last Name",
    1,
    2
)

e2 = create_entry(
    lname,
    1,
    3
)


create_label(
    "Class",
    2,
    0
)

e3 = create_entry(
    sclass,
    2,
    1
)


create_label(
    "Class Division",
    2,
    2
)

e4 = create_entry(
    division,
    2,
    3
)


create_label(
    "Roll Number",
    3,
    0
)

e11 = create_entry(
    rnumber,
    3,
    1
)


create_label(
    "Student ID Number",
    3,
    2
)

e12 = create_entry(
    idnumber,
    3,
    3
)


marks_title = Label(
    table,
    text="SUBJECT MARKS",
    font=("Calibri", 19, "bold"),
    bg="#BFE3F2",
    fg="#123B5D",
    padx=15,
    pady=10
)

marks_title.grid(
    row=4,
    column=0,
    columnspan=4,
    sticky="ew",
    padx=15,
    pady=(15, 8)
)


create_label(
    "English Marks",
    5,
    0
)

e5 = create_entry(
    english,
    5,
    1
)


create_label(
    "Urdu Marks",
    5,
    2
)

e6 = create_entry(
    urdu,
    5,
    3
)


create_label(
    "Maths Marks",
    6,
    0
)

e7 = create_entry(
    maths,
    6,
    1
)


create_label(
    "Science Marks",
    6,
    2
)

e8 = create_entry(
    science,
    6,
    3
)


create_label(
    "SST Marks",
    7,
    0
)

e9 = create_entry(
    sst,
    7,
    1
)


create_label(
    "Hindi Marks",
    7,
    2
)

e10 = create_entry(
    hindi,
    7,
    3
)

button_frame = Frame(
    table,
    bg=bg_color
)

button_frame.grid(
    row=8,
    column=0,
    columnspan=4,
    pady=(25, 20)
)


l9 = Button(
    button_frame,
    text="STORE DATA",
    padx=25,
    pady=10,
    font=("Calibri", 15, "bold"),
    bg=button_color,
    fg="white",
    activebackground=button_hover,
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=save_data
)

l9.grid(
    row=0,
    column=0,
    padx=15
)


l10 = Button(
    button_frame,
    text="DISPLAY DATA",
    padx=25,
    pady=10,
    font=("Calibri", 15, "bold"),
    bg=button_color,
    fg="white",
    activebackground=button_hover,
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=display_data
)

l10.grid(
    row=0,
    column=1,
    padx=15
)


result_button = Button(
    button_frame,
    text="RESULT",
    padx=40,
    pady=10,
    font=("Calibri", 15, "bold"),
    bg=button_color,
    fg="white",
    activebackground=button_hover,
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=show_result
)

result_button.grid(
    row=0,
    column=2,
    padx=15
)


footer = Label(
    table,
    text="Student Information Management System",
    font=("Calibri", 10, "italic"),
    bg=bg_color,
    fg="#5D6D7E"
)

footer.grid(
    row=9,
    column=0,
    columnspan=4,
    pady=(0, 15)
)


table.mainloop()

'''
# ============================================================
# BUTTONS
# ============================================================

l9 = Button(
    table,
    text="STORE DATA",
    padx=25,
    pady=10,
    font=("Calibri", 15, "bold"),
    bg=button_color,
    fg="white",
    activebackground=button_hover,
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=save_data
)

l9.grid(
    row=8,
    column=0,
    padx=8,
    pady=(25, 20)
)


l10 = Button(
    table,
    text="DISPLAY DATA",
    padx=25,
    pady=10,
    font=("Calibri", 15, "bold"),
    bg=button_color,
    fg="white",
    activebackground=button_hover,
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=display_data
)

l10.grid(
    row=8,
    column=1,
    padx=8,
    pady=(25, 20)
)


# ============================================================
# RESULT BUTTON
# ============================================================

result_button = Button(
    table,
    text="RESULT",
    padx=40,
    pady=10,
    font=("Calibri", 15, "bold"),
    bg=button_color,
    fg="white",
    activebackground=button_hover,
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=show_result
)

result_button.grid(
    row=8,
    column=2,
    columnspan=2,
    padx=8,
    pady=(25, 20)
)

'''