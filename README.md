<div align="center">

# 🎓 Smart College Placement Analytics Dashboard


### 📊 Zero-Code Placement Analytics for College Placement Cells

An interactive data analytics dashboard built with **Python, Streamlit, Pandas, and Plotly** to help colleges analyze placement performance, companies, departments, packages, students, and year-wise placement trends.

<br>

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)](https://pandas.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-Visualization-3F4F75?logo=plotly)](https://plotly.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

</div>

---

## 📌 Table of Contents

- [Project Overview](#-project-overview)
- [What is this Project About?](#-what-is-this-project-about)
- [Key Features](#-key-features)
- [How is it Useful?](#-how-is-it-useful)
- [Who Can Use This?](#-who-can-use-this)
- [Why Use This Project?](#-why-use-this-project)
- [Prerequisites](#-prerequisites)
- [Software Setup Guide](#-software-setup-guide)
- [Installation](#-installation)
- [Project Structure](#-project-structure)
- [Input File Format](#-input-file-format)
- [How to Run the Project](#-how-to-run-the-project)
- [Dashboard Analytics](#-dashboard-analytics)
- [UI Screenshots](#-ui-screenshots)
- [Future Upgrades](#-future-upgrades)
- [Privacy and Data Safety](#-privacy-and-data-safety)
- [Contributing](#-contributing)
- [Thanks and Support](#-thanks-and-support)

---

## 🚀 Project Overview

**Smart College Placement Analytics Dashboard** is a web-based analytics application designed for college placement cells.

The application allows users to upload placement data in **CSV or XLSX format** and automatically generates interactive analytics.

No advanced programming or data-analysis knowledge is required to use the dashboard.

The system converts raw placement records into meaningful insights such as:

- Total students
- Placed students
- Placement rate
- Highest package
- Lowest package
- Average package
- Median package
- Department-wise placements
- Company-wise hiring
- Year-wise placement trends
- Year × Department analysis
- Highest-paying companies
- Top package holders
- Student-level placement records
- Package distribution
- Filtered report generation

---

## 💡 What is this Project About?

Placement data is often maintained in spreadsheets containing hundreds or thousands of student records.

Manually analyzing this data can be time-consuming.

This project provides a simple solution:

```text
Raw CSV / Excel Data
        ↓
   Data Validation
        ↓
    Data Filtering
        ↓
   Data Processing
        ↓
Interactive Visualizations
        ↓
Placement Insights
        ↓
Downloadable Report
```

---

## ✨ Key Features
### 📁 Multiple File Formats

Supports:

-CSV
-XLSX / Excel

Only supported file formats can be uploaded.

---

## 🔐 Data Validation

The application validates:

-Required columns
-Numeric package values
-Placement year
-File format
-Supported language characters

The application is designed to accept English-language data.

If non-English text is detected in the uploaded dataset, an appropriate error message is displayed.

---

## 🔎 Interactive Filters

Users can filter placement records by:

-📅 Placement Year
-🏫 Department / Branch
-🏢 Company
-📍 Job Location
-✅ Placement Status

All dashboard analytics update automatically according to the selected filters.

---

## 📊 Placement KPIs

The dashboard displays:

-Total Students
-Placed Students
-Placement Rate
-Total Companies
-Highest Package
-Lowest Package
-Average Package
-Median Package

---

## 🏫 Department Analytics

Analyze:

-Department-wise placement count
-Department-wise average package
-Department-wise highest package
-Year × Department placement performance

---

## 🏢 Company Analytics

Analyze:

-Companies hiring the most students
-Highest-paying companies
-Company-wise highest package
-Company-wise lowest package
-Company-wise average package
-Number of students hired by each company

---

## 🏆 Student-Level Analytics

Identify:

-Highest package student
-Lowest package student
-Top package holders
-Student's department
-Student's company
-Student's placement year
-Student's job location

---

## v💰 Package Analytics

Visualize package distribution across students and departments.

This helps identify the most common salary/package range.

---

## 📥 Report Generation

Filtered placement data can be downloaded as an Excel report.

This allows placement teams to generate customized reports based on selected filters.

---

## 📋 Prerequisites

Before running this project, install the following software.

<details> <summary><b>🐍 Python</b></summary> <br>

### Python 3.9 or above is recommended.

Download Python from:

```python
https://www.python.org/downloads/
```
After installation, verify it using:

```code
python --version
```

or:

```python
python3 --version
```

Make sure Python is added to your system PATH during installation.

</details> <details> <summary><b>💻 Visual Studio Code</b></summary> <br>

## Visual Studio Code is recommended for editing and running the project.

Download:

```python
https://code.visualstudio.com/download
```

After installation:

1. Open VS Code.
2. Open the project folder.
3. Open the integrated terminal.
4. Run the installation commands mentioned below.

Recommended VS Code extensions:

-Python
-Pylance
-Python Debugger

</details> <details> <summary><b>🌐 Git</b></summary> <br>

## Git is recommended for version control and pushing the project to GitHub.

Download:

```python
https://git-scm.com/downloads
```

Verify installation:

```python
git --version
```

</details>

---

## 🛠️ Software Setup Guide

<details> <summary><b>Step 1 — Install Python</b></summary> <br>

### Download and install Python from:

```code
https://www.python.org/downloads/
```

During installation, enable:

```python
Add Python to PATH
```

Verify:

```python
python --version
```

</details> <details> <summary><b>Step 2 — Install Visual Studio Code</b></summary> <br>

## Download:

```python
https://code.visualstudio.com/download
```

Open VS Code after installation.

</details> <details> <summary><b>Step 3 — Install Git</b></summary> <br>

Download:

```python
https://git-scm.com/downloads
```

Verify:

```python
git --version
```

</details> <details> <summary><b>Step 4 — Clone the Repository</b></summary> <br>

## Open a terminal and run:

```python

git clone https://github.com/alok-kumar8765/smart-college-placement-analytics.git
```

Then:

```python
cd smart-college-placement-analytics
```

</details>

---

## 📦 Installation

Required Python Packages

The project uses the following Python libraries:

```
Package |	Purpose
streamlit |	Web dashboard
pandas |	Data processing
plotly |	Interactive charts
openpyxl |	Excel file handling
io |	Built-in Python module
```

io is included with Python and does not need to be installed separately.


---

## Install All Packages

Run:

```python
pip install streamlit pandas plotly openpyxl
```

Or:

```python
python -m pip install streamlit pandas plotly openpyxl
```

### Using requirements.txt

Create a file named:

```code
requirements.txt
```

Add:

```python
streamlit
pandas
plotly
openpyxl
```

Then install everything using:

```python
pip install -r requirements.txt
```

---

## 📄 Input File Format

The dashboard accepts:

```code
.csv
.xlsx
```

Your file should contain the following columns:

```
Column	Description	Example
Student_ID	Unique student identifier	STU001
Student_Name	Student name	Aarav Sharma
Year	Placement year	2025
Branch	Department	CSE
Company	Recruiting company	Microsoft
Package	Package in LPA	18.5
Placement_Status	Placement status	Placed
Location	Job location	Bangalore
```

---

## ▶️ How to Run the Project

Open the project folder in VS Code.

Open the terminal and run:

```python
streamlit run app.py
```

The application will start locally.

Streamlit will provide a local URL such as:

```python
http://localhost:8501
```

Open that address in your browser.


---

## 📊 Dashboard Analytics

The dashboard provides several levels of placement analysis.

### 📅 Year-wise Analysis

Understand how placement performance changes over different years.

Example:

```code
2023 → 280 students placed
2024 → 340 students placed
2025 → 410 students placed

```

## 🏫 Department-wise Analysis

Compare departments such as:

```code
CSE
IT
ECE
ME
CE

```

The dashboard can show:

-Number of students placed
-Average package
-Highest package
-Company distribution


---

## 🔥 Year × Department Analysis

The heatmap helps identify:

> Which department performed better or worse in each placement year?

---

## 🏢 Company-wise Hiring

Identify which companies hired the highest number of students.

Example:

```
TCS          → 86 students
Infosys      → 72 students
Accenture    → 54 students
Wipro        → 48 students
Amazon       → 18 students
Microsoft    → 12 students

```

---

## 💰 Highest Paying Companies

Compare companies based on their offered packages.

Example:

```
Microsoft → ₹28 LPA
Amazon    → ₹24 LPA
Adobe     → ₹20 LPA
Google    → ₹18 LPA
```

---

## 🏆 Highest Package Student

The dashboard automatically identifies:

-Student
-Department
-Company
-Package
-Placement year
-Location

---

## 📉 Lowest Package Student

The dashboard also identifies the lowest package holder and the company that offered the package.

---

##🖥️ UI Screenshots

Main Dashboard


<img src="https://github.com/alok-kumar8765/smart-college-placement-analytics/blob/main/banner.jpg" alt="banner">

---

## 🎯 How is it Useful?

This project can help placement teams:

-Analyze placement performance quickly.
-Compare departments.
-Compare placement years.
-Identify top recruiting companies.
-Identify highest-paying companies.
-Find highest and lowest packages.
-Analyze package distribution.
-Search student placement records.
-Generate filtered placement reports.
-Reduce manual spreadsheet analysis.

---

## 👥 Who Can Use This?

This project can be useful for:

-🎓 College Placement Cells
-🏫 Universities
-👨‍💼 Training & Placement Officers
-📊 Placement Coordinators
-👨‍🏫 Faculty Coordinators
-👨‍🎓 Students
-📈 Data Analytics Students
-💼 Career Services Teams
-🧑‍💻 Academic Institutions

---

## ❓ Why Use This Project?

Traditional placement analysis often requires manually creating:

-Excel filters
-Pivot tables
-Charts
-Reports
-Package comparisons

This dashboard automates much of that process.

Instead of manually analyzing spreadsheets:

```python

Upload File
    ↓
Select Filters
    ↓
Dashboard Updates Automatically
    ↓
Analyze Placement Insights
    ↓
Download Report


```

This makes placement analysis faster and easier for users who may not have programming or advanced data-analysis skills.


---

## 🚀 Future Upgrades

Several improvements can be added in future versions.

### 🔐 Authentication

Add secure login for:

-Placement officers
-Faculty
-Students
-Administrators

---

## ☁️ Cloud Database

Move from file-based storage to databases such as:

-PostgreSQL
-MySQL
-MongoDB

---

## 📊 Advanced Analytics

Add:

-Placement prediction
-Salary prediction
-Branch performance forecasting
-Company hiring prediction
-Year-wise growth percentage
-Package growth trends

---

## 🤖 AI-Powered Insights

An AI analytics assistant could answer questions such as:

```python
Which department performed best in 2025?

Which company offered the highest package?

Which branch has the highest average package?

Which companies are hiring the most students?

How did placement performance change from 2024 to 2025?

```

---

## 📈 Advanced Visualizations

Future versions can include:

-Interactive heatmaps
-Sankey diagrams
-Treemaps
-Funnel charts
-Geographic placement maps
-Advanced KPI cards

---

## 📄 Automated Reports

Generate:

-PDF placement reports
-Department reports
-Company reports
-Annual placement reports
-Executive summary reports

---

## 📧 Automated Notifications

Automatically send placement reports through:

Email
Institutional communication systems

---

## 🔒 Privacy and Data Safety

This project may contain student-level placement information.

For production use:

>Do not expose personal information publicly.
>Do not upload real student data to a public GitHub repository.
>Use anonymized or synthetic data for demonstrations.
>Protect sensitive placement information.
>Use authentication and access control for production deployment.

Recommended public repository data:

```
Demo / Synthetic Data
```

Avoid uploading:


```
Real Student Phone Numbers
Real Email Addresses
Personal Addresses
Private Student IDs
Confidential Company Information
```

---

## 🤝 Contributing

Contributions are welcome!

If you want to improve this project:

-Fork the repository.
-Create a new branch.

```python
git checkout -b feature/new-feature
```

-Make your changes.
-Commit your changes.

```python
git add .
git commit -m "Add new placement analytics feature"
```

-Push your branch.

```python
git push origin feature/new-feature
```

-Open a Pull Request.

---

## ⭐ Support the Project

If you find this project useful:

-⭐ Star the repository
-🍴 Fork the project
-🐛 Report bugs
-💡 Suggest new features
-🤝 Contribute improvements
-📢 Share the project with others

Every contribution helps improve the project.

---

## 🙏 Thanks and Support

Thank you for checking out Smart College Placement Analytics Dashboard.

This project was created with the goal of making college placement analytics:

> Simple • Interactive • Accessible • Data-Driven

Built with ❤️ using:

Python • Streamlit • Pandas • Plotly • OpenPyXL

---








