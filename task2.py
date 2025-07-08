import pandas as pd
# Read the CSV file
data = pd.read_csv('student_marks.csv')
# Convert Marks column to numbers
data['Marks'] = pd.to_numeric(data['Marks'],errors='coerce')
# Analysis
total_students = len(data)
average_marks = data['Marks'].mean()
highest_marks = data['Marks'].max()
lowest_marks = data['Marks'].min()
topper = data.loc[data['Marks'].idxmax()]
['Name']
weakest = data.loc[data['Marks'].idxmin()]
['Name']
# Print results to console
print("STUDENT MARKS ANALYSIS:")
print(f"Total Students:{total_students}")
print(f"Average Marks: {average_marks:.2f}")
print(f"Highest marks:{highest_marks}(by {topper})")
print(f"Lowest Marks:{lowest_marks}(by {weakest})")
from fpdf import FPDF
from datetime import datetime

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Student Marks Report", ln=True, align='C')
        self.set_font("Arial", "", 12)
        self.cell(0, 10, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True, align='C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align='C')

    def report_body(self):
        self.set_font("Arial", "", 12)
        self.cell(0, 10, f"Total Students: {total_students}", ln=True)
        self.cell(0, 10, f"Average Marks: {average_marks:.2f}", ln=True)
        self.cell(0, 10, f"Highest Marks: {highest_marks} (by {topper})", ln=True)
        self.cell(0, 10, f"Lowest Marks: {lowest_marks} (by {weakest})", ln=True)
        self.ln(5)

        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Detailed Data:", ln=True)
        self.set_font("Arial", "", 12)

        # Table header
        self.cell(60, 10, "Name", border=1)
        self.cell(60, 10, "Subject", border=1)
        self.cell(60, 10, "Marks", border=1)
        self.ln()

        # Table rows
        for index, row in data.iterrows():
            self.cell(60, 10, row['Name'], border=1)
            self.cell(60, 10, row['Subject'], border=1)
            self.cell(60, 10, str(row['Marks']), border=1)
            self.ln()

# Create and save the PDF
pdf = PDF()
pdf.add_page()
pdf.report_body()
pdf.output("Students_Marks_Report.pdf")
