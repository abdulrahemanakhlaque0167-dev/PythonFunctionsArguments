from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import csv
import os

# Try importing reportlab for PDF generation
try:
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas
    REPORTLAB_AVAILABLE = True
except ImportError:
    REPORTLAB_AVAILABLE = False


def generate_pdf_report(student_name, roll_no, marks_dict, total, percentage, parent_window):
    """Generates a professional PDF report for a student using ReportLab."""
    if not REPORTLAB_AVAILABLE:
        messagebox.showerror(
            "Missing Library",
            "The 'reportlab' library is required to export PDFs.\nPlease install it using: pip install reportlab",
            parent=parent_window
        )
        return

    # Ask user where to save the PDF file
    file_path = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")],
        initialfile=f"Result_Roll_{roll_no}.pdf",
        parent=parent_window
    )

    if not file_path:
        return  # User cancelled the save dialog

    try:
        # Create PDF document
        c = canvas.Canvas(file_path, pagesize=letter)
        width, height = letter  # 612 x 792 points

        # Draw decorative header banner
        c.setFillColorRGB(0.07, 0.23, 0.36)  # #123B5D
        c.rect(40, height - 100, width - 80, 70, fill=1, stroke=0)

        c.setFillColorRGB(1, 1, 1)
        c.setFont("Helvetica-Bold", 20)
        c.drawString(60, height - 60, "STUDENT ACADEMIC REPORT")

        # Student Details Section
        c.setFillColorRGB(0.09, 0.49, 0.60)  # #167D9A
        c.setFont("Helvetica-Bold", 14)
        c.drawString(40, height - 140, f"Student Name: {student_name}")
        c.drawString(40, height - 165, f"Roll Number: {roll_no}")

        # Draw Table Headers
        c.setFillColorRGB(0.75, 0.89, 0.95)  # #BFE3F2
        c.rect(40, height - 215, width - 80, 25, fill=1, stroke=0)

        c.setFillColorRGB(0.07, 0.23, 0.36)
        c.setFont("Helvetica-Bold", 12)
        c.drawString(60, height - 207, "SUBJECT")
        c.drawString(400, height - 207, "MARKS OBTAINED / 100")

        # Draw Individual Subject Marks
        y_pos = height - 245
        c.setFont("Helvetica", 11)
        c.setFillColorRGB(0.09, 0.13, 0.16)

        for subject, mark in marks_dict.items():
            c.drawString(60, y_pos, subject)
            c.drawString(400, y_pos, f"{mark:g} / 100")
            
            # Light separator line
            c.setStrokeColorRGB(0.85, 0.85, 0.85)
            c.setLineWidth(0.5)
            c.line(40, y_pos - 8, width - 40, y_pos - 8)
            
            y_pos -= 30

        # Total and Percentage Summary Box
        y_pos -= 15
        c.setFillColorRGB(0.75, 0.89, 0.95)
        c.rect(40, y_pos - 45, width - 80, 45, fill=1, stroke=0)

        c.setFillColorRGB(0.07, 0.23, 0.36)
        c.setFont("Helvetica-Bold", 13)
        c.drawString(60, y_pos - 28, f"TOTAL MARKS: {total:g} / 600")

        c.setFont("Helvetica-Bold", 15)
        c.drawRightString(width - 60, y_pos - 30, f"Percentage: {percentage:.2f}%")

        # Footer note
        c.setFont("Helvetica-Oblique", 9)
        c.setFillColorRGB(0.36, 0.43, 0.49)
        c.drawCentredString(width / 2.0, 40, "Student Information Management System — Generated Automatically")

        c.showPage()
        c.save()

        messagebox.showinfo(
            "Success",
            f"PDF successfully generated and saved to:\n{file_path}",
            parent=parent_window
        )

    except Exception as e:
        messagebox.showerror(
            "PDF Generation Error",
            f"An error occurred while creating the PDF:\n{str(e)}",
            parent=parent_window
        )


def display_data():

    window1 = Toplevel(table)
    window1.title("Student Data")
    window1.geometry("1450x650")
    window1.configure(bg="#EAF4F8")

    title_frame = Frame(
        window1,
        bg="#123B5D",
        height=80
    )
    title_frame.pack(fill=X, padx=15, pady=(15, 10))
    title_frame.pack_propagate(False)

    Label(
        title_frame,
        text="STUDENT DATA",
        font=("Calibri", 25, "bold"),
        bg="#123B5D",
        fg="white"
    ).pack(side=LEFT, padx=25)

    # ================= SEARCH =================

    search_frame = Frame(window1, bg="#EAF4F8")
    search_frame.pack(fill=X, padx=20, pady=5)

    Label(
        search_frame,
        text="Search:",
        font=("Calibri", 14, "bold"),
        bg="#EAF4F8",
        fg="#123B5D"
    ).pack(side=LEFT, padx=(0, 8))

    search_var = StringVar()

    search_entry = Entry(
        search_frame,
        textvariable=search_var,
        font=("Calibri", 13),
        width=35,
        relief="solid",
        bd=1
    )
    search_entry.pack(side=LEFT, ipady=5)

    # ================= TABLE FRAME =================

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

    # ================= SCROLLBARS =================

    scrollbar_y = ttk.Scrollbar(
        table_frame,
        orient=VERTICAL
    )
    scrollbar_y.pack(side=RIGHT, fill=Y)

    scrollbar_x = ttk.Scrollbar(
        window1,
        orient=HORIZONTAL
    )
    scrollbar_x.pack(fill=X, padx=20)

    # ================= TREEVIEW =================

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
        "Hindi",
        "Result"
    ]

    tree = ttk.Treeview(
        table_frame,
        columns=headers,
        displaycolumns=headers,
        show="headings",
        style="Student.Treeview"
    )

    tree.pack(side=LEFT, fill=BOTH, expand=True)

    tree.configure(
        yscrollcommand=scrollbar_y.set,
        xscrollcommand=scrollbar_x.set
    )

    scrollbar_y.configure(command=tree.yview)
    scrollbar_x.configure(command=tree.xview)

    column_widths = {
        "Roll No": 80,
        "First Name": 120,
        "Last Name": 120,
        "Class": 65,
        "Division": 85,
        "ID Number": 110,
        "English": 80,
        "Urdu": 80,
        "Maths": 80,
        "Science": 80,
        "SST": 80,
        "Hindi": 80,
        "Result": 100
    }

    for column in headers:
        tree.heading(column, text=column)
        tree.column(
            column,
            width=column_widths[column],
            minwidth=60,
            anchor=CENTER,
            stretch=(column == "Result")
        )

    # ================= READ CSV FILE =================

    try:
        with open("student_data.csv", "r", newline="") as f:
            csvReader = csv.reader(f)
            next(csvReader, None)
            data = list(csvReader)

    except FileNotFoundError:
        messagebox.showerror(
            "File Error",
            "student_data.csv was not found!",
            parent=window1
        )
        window1.destroy()
        return

    # ================= INSERT STUDENTS =================

    student_rows = {}

    for index, row in enumerate(data):

        if len(row) < 12:
            continue

        item_id = tree.insert(
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
                row[11],
                "VIEW RESULT"
            ),
            tags=("evenrow" if index % 2 == 0 else "oddrow",)
        )

        student_rows[item_id] = row[:12]

    tree.tag_configure("evenrow", background="#F4FAFC")
    tree.tag_configure("oddrow", background="white")

    # ================= STUDENT RESULT WINDOW =================

    def open_student_result(row):

        result_window = Toplevel(window1)
        result_window.title("Student Result")
        result_window.geometry("500x670")
        result_window.resizable(False, False)
        result_window.configure(bg="#EAF4F8")

        Label(
            result_window,
            text="STUDENT RESULT",
            font=("Calibri", 23, "bold"),
            bg="#123B5D",
            fg="white",
            pady=18
        ).pack(fill=X, padx=12, pady=12)

        first_name = row[1]
        last_name = row[2]
        roll_no = row[0]
        student_full_name = f"{first_name} {last_name}"

        Label(
            result_window,
            text=student_full_name,
            font=("Calibri", 20, "bold"),
            bg="#EAF4F8",
            fg="#167D9A"
        ).pack(pady=(10, 4))

        Label(
            result_window,
            text=f"Roll Number: {roll_no}",
            font=("Calibri", 13),
            bg="#EAF4F8",
            fg="#123B5D"
        ).pack(pady=4)

        try:
            subject_names = [
                "English",
                "Urdu",
                "Maths",
                "Science",
                "SST",
                "Hindi"
            ]

            marks_values = [float(row[i]) for i in range(6, 12)]

            if any(mark < 0 or mark > 100 for mark in marks_values):
                raise ValueError

            total = sum(marks_values)
            percentage = (total / 600) * 100
            marks_dict = dict(zip(subject_names, marks_values))

        except ValueError:
            messagebox.showerror(
                "Invalid Marks",
                "Marks must be numbers between 0 and 100.",
                parent=result_window
            )
            result_window.destroy()
            return

        # Subject marks table frame
        marks_frame = Frame(
            result_window,
            bg="white",
            bd=1,
            relief="solid"
        )
        marks_frame.pack(fill=X, padx=30, pady=10)

        Label(
            marks_frame,
            text="SUBJECT MARKS",
            font=("Calibri", 14, "bold"),
            bg="#BFE3F2",
            fg="#123B5D",
            pady=6
        ).pack(fill=X)

        for subject, mark in zip(subject_names, marks_values):

            subject_frame = Frame(marks_frame, bg="white")
            subject_frame.pack(fill=X, padx=20, pady=3)

            Label(
                subject_frame,
                text=subject,
                font=("Calibri", 11),
                bg="white",
                fg="#17202A"
            ).pack(side=LEFT)

            Label(
                subject_frame,
                text=f"{mark:g} / 100",
                font=("Calibri", 11, "bold"),
                bg="white",
                fg="#123B5D"
            ).pack(side=RIGHT)

        # Show obtained marks, maximum total marks, and percentage separately
        Label(
            result_window,
            text=(
                f"OBTAINED MARKS: {total:g}\n"
                f"TOTAL MARKS: 600\n"
                f"PERCENTAGE: {percentage:.2f}%"
            ),
            font=("Calibri", 13, "bold"),
            bg="#BFE3F2",
            fg="#123B5D",
            padx=15,
            pady=8,
            justify=CENTER
        ).pack(pady=6)

        # PDF Download Button
        Button(
            result_window,
            text="DOWNLOAD PDF REPORT",
            font=("Calibri", 12, "bold"),
            bg="#167D9A",
            fg="white",
            activebackground="#0B5D73",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=7,
            command=lambda: generate_pdf_report(
                student_full_name, roll_no, marks_dict, total, percentage, result_window
            )
        ).pack(pady=4)

        Button(
            result_window,
            text="CLOSE",
            font=("Calibri", 11, "bold"),
            bg="#123B5D",
            fg="white",
            activebackground="#0B5D73",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            padx=30,
            pady=6,
            command=result_window.destroy
        ).pack(pady=6)

    # ================= CLICK RESULT CELL =================

    def on_tree_click(event):
        region = tree.identify_region(event.x, event.y)
        if region != "cell":
            return
        column = tree.identify_column(event.x)
        item_id = tree.identify_row(event.y)

        if column == "#13" and item_id in student_rows:
            open_student_result(student_rows[item_id])

    tree.bind("<ButtonRelease-1>", on_tree_click)

    # ================= SEARCH FUNCTION =================

    all_items = list(student_rows.keys())

    def search_data(*args):
        search_text = search_var.get().strip().lower()
        for item_id in all_items:
            values = tree.item(item_id, "values")
            found = any(search_text in str(value).lower() for value in values)
            if found:
                tree.reattach(item_id, "", "end")
            else:
                tree.detach(item_id)

    def reset_search():
        search_var.set("")

    search_var.trace_add("write", search_data)

    Button(
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
    ).pack(side=LEFT, padx=10)

    # ================= CLOSE BUTTON =================

    Button(
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
    ).pack(pady=12)


def show_result():

    result_window = Toplevel(table)
    result_window.title("Student Result")
    result_window.geometry("650x740")
    result_window.configure(bg="#EAF4F8")
    result_window.resizable(False, False)

    result_header = Label(
        result_window,
        text="STUDENT RESULT",
        font=("Calibri", 25, "bold"),
        bg="#123B5D",
        fg="white",
        padx=30,
        pady=18
    )
    result_header.pack(fill=X, padx=15, pady=15)

    roll_frame = Frame(result_window, bg="#EAF4F8")
    roll_frame.pack(pady=5)

    Label(
        roll_frame,
        text="Enter Roll Number:",
        font=("Calibri", 14, "bold"),
        bg="#EAF4F8",
        fg="#123B5D"
    ).pack(side=LEFT, padx=10)

    roll_entry = Entry(
        roll_frame,
        font=("Calibri", 14),
        width=18,
        relief="solid",
        bd=1
    )
    roll_entry.pack(side=LEFT, ipady=5)

    result_area = Frame(result_window, bg="#EAF4F8")
    result_area.pack(fill=BOTH, expand=True, padx=25, pady=5)

    def calculate_result():
        roll_no = roll_entry.get().strip()

        if roll_no == "":
            messagebox.showwarning("Warning", "Please enter a Roll Number!")
            return

        for widget in result_area.winfo_children():
            widget.destroy()

        try:
            with open("student_data.csv", "r") as f:
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
                            student_full_name = f"{first_name} {last_name}"

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

                            percentage = (total_marks / 600) * 100

                            subject_names = [
                                "English",
                                "Urdu",
                                "Maths",
                                "Science",
                                "SST",
                                "Hindi"
                            ]
                            marks_values = [
                                english_marks,
                                urdu_marks,
                                maths_marks,
                                science_marks,
                                sst_marks,
                                hindi_marks
                            ]
                            marks_dict = dict(zip(subject_names, marks_values))

                            Label(
                                result_area,
                                text="Student Name",
                                font=("Calibri", 13, "bold"),
                                bg="#EAF4F8",
                                fg="#123B5D"
                            ).pack(pady=(2, 0))

                            Label(
                                result_area,
                                text=student_full_name,
                                font=("Calibri", 16, "bold"),
                                bg="#EAF4F8",
                                fg="#167D9A"
                            ).pack(pady=(0, 4))

                            Label(
                                result_area,
                                text=f"Roll Number: {student_roll}",
                                font=("Calibri", 12),
                                bg="#EAF4F8",
                                fg="#17202A"
                            ).pack(pady=2)

                            marks_frame = Frame(
                                result_area,
                                bg="white",
                                bd=1,
                                relief="solid"
                            )
                            marks_frame.pack(fill=X, pady=8)

                            Label(
                                marks_frame,
                                text="SUBJECT MARKS",
                                font=("Calibri", 13, "bold"),
                                bg="#BFE3F2",
                                fg="#123B5D",
                                pady=5
                            ).pack(fill=X)

                            Label(
                                marks_frame,
                                text=(
                                    f"English     : {english_marks:g}/100\n"
                                    f"Urdu        : {urdu_marks:g}/100\n"
                                    f"Maths       : {maths_marks:g}/100\n"
                                    f"Science     : {science_marks:g}/100\n"
                                    f"SST         : {sst_marks:g}/100\n"
                                    f"Hindi       : {hindi_marks:g}/100"
                                ),
                                font=("Calibri", 11),
                                bg="white",
                                fg="#17202A",
                                justify=LEFT,
                                padx=25,
                                pady=6
                            ).pack(anchor="w")

                            # Show obtained marks, maximum total marks, and percentage separately
                            Label(
                                result_area,
                                text=(
                                    f"OBTAINED MARKS: {total_marks:g}\n"
                                    f"TOTAL MARKS: 600\n"
                                    f"PERCENTAGE: {percentage:.2f}%"
                                ),
                                font=("Calibri", 13, "bold"),
                                bg="#BFE3F2",
                                fg="#123B5D",
                                padx=20,
                                pady=6,
                                justify=CENTER
                            ).pack(pady=4)

                            # PDF Download Button inside Roll Number search result
                            Button(
                                result_area,
                                text="DOWNLOAD PDF REPORT",
                                font=("Calibri", 12, "bold"),
                                bg="#167D9A",
                                fg="white",
                                activebackground="#0B5D73",
                                activeforeground="white",
                                relief="flat",
                                cursor="hand2",
                                padx=25,
                                pady=6,
                                command=lambda: generate_pdf_report(
                                    student_full_name, student_roll, marks_dict, total_marks, percentage, result_window
                                )
                            ).pack(pady=4)

                            return

                if not student_found:
                    Label(
                        result_area,
                        text="Student Not Found",
                        font=("Calibri", 16, "bold"),
                        bg="#EAF4F8",
                        fg="#C0392B"
                    ).pack(pady=20)

                    Label(
                        result_area,
                        text=f"No student was found with Roll Number: {roll_no}",
                        font=("Calibri", 11),
                        bg="#EAF4F8",
                        fg="#17202A"
                    ).pack()

        except FileNotFoundError:
            messagebox.showerror("File Error", "student_data.csv was not found!")
        except ValueError:
            messagebox.showerror("Invalid Marks", "The marks in the CSV file must be numbers.")

    Button(
        result_window,
        text="SHOW RESULT",
        font=("Calibri", 13, "bold"),
        bg="#167D9A",
        fg="white",
        activebackground="#0B5D73",
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        padx=25,
        pady=7,
        command=calculate_result
    ).pack(pady=6)

    Button(
        result_window,
        text="CLOSE",
        font=("Calibri", 11, "bold"),
        bg="#123B5D",
        fg="white",
        activebackground="#0B5D73",
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        padx=30,
        pady=6,
        command=result_window.destroy
    ).pack(pady=(2, 10))

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
button_hover = "#011A20"

table.configure(bg=bg_color)

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
header.grid(row=0, column=0, columnspan=4, sticky="ew", padx=15, pady=(15, 20))


def create_label(text, row, column):
    label = Label(
        table,
        text=text,
        font=("Calibri", 14, "bold"),
        bg=bg_color,
        fg=label_color
    )
    label.grid(row=row, column=column, padx=18, pady=9, sticky="w")
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
    entry.grid(row=row, column=column, padx=18, pady=9, ipady=5)
    return entry


create_label("First Name", 1, 0)
e1 = create_entry(fname, 1, 1)

create_label("Last Name", 1, 2)
e2 = create_entry(lname, 1, 3)

create_label("Class", 2, 0)
e3 = create_entry(sclass, 2, 1)

create_label("Class Division", 2, 2)
e4 = create_entry(division, 2, 3)

create_label("Roll Number", 3, 0)
e11 = create_entry(rnumber, 3, 1)

create_label("Student ID Number", 3, 2)
e12 = create_entry(idnumber, 3, 3)

marks_title = Label(
    table,
    text="SUBJECT MARKS",
    font=("Calibri", 19, "bold"),
    bg="#BFE3F2",
    fg="#123B5D",
    padx=15,
    pady=10
)
marks_title.grid(row=4, column=0, columnspan=4, sticky="ew", padx=15, pady=(15, 8))

create_label("English Marks", 5, 0)
e5 = create_entry(english, 5, 1)

create_label("Urdu Marks", 5, 2)
e6 = create_entry(urdu, 5, 3)

create_label("Maths Marks", 6, 0)
e7 = create_entry(maths, 6, 1)

create_label("Science Marks", 6, 2)
e8 = create_entry(science, 6, 3)

create_label("SST Marks", 7, 0)
e9 = create_entry(sst, 7, 1)

create_label("Hindi Marks", 7, 2)
e10 = create_entry(hindi, 7, 3)

button_frame = Frame(table, bg=bg_color)
button_frame.grid(row=8, column=0, columnspan=4, pady=(25, 20))

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
l9.grid(row=0, column=0, padx=15)

l10 = Button(
    button_frame,
    text="DISPLAY DATA",
    padx=15,
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
l10.grid(row=0, column=1, padx=15)

result_button = Button(
    button_frame,
    text="RESULT BY ROLL",
    padx=20,
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
result_button.grid(row=0, column=2, padx=15)

footer = Label(
    table,
    text="Student Information Management System",
    font=("Calibri", 10, "italic"),
    bg=bg_color,
    fg="#5D6D7E"
)
footer.grid(row=9, column=0, columnspan=4, pady=(0, 15))

table.mainloop()




