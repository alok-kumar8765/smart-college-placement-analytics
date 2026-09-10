import io
import re

import pandas as pd
import plotly.express as px
import streamlit as st


# ============================================================
# 1. PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Smart College Placement Analytics",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Smart College Placement Analytics Dashboard")
st.markdown(
    "### Theme: Navachar — Zero-Code Analytics for College Placement Cells"
)


# ============================================================
# 2. REQUIRED COLUMNS
# ============================================================

REQUIRED_COLUMNS = [
    "Student_ID",
    "Student_Name",
    "Year",
    "Branch",
    "Company",
    "Package",
    "Placement_Status",
    "Location"
]


# ============================================================
# 3. FUNCTION TO CHECK ENGLISH-ONLY TEXT
# ============================================================

def contains_non_english_text(value):
    """
    Returns True if the text contains characters outside
    the allowed English/Latin character range.

    Numbers, spaces and common punctuation are allowed.
    """

    if pd.isna(value):
        return False

    text = str(value)

    # Allow:
    # English alphabets
    # Numbers
    # Spaces
    # Common punctuation
    allowed_pattern = r"^[A-Za-z0-9\s.,;:!?@#$%&*()_\-+/\\'\"°₹|[\]{}]+$"

    return not bool(re.fullmatch(allowed_pattern, text))


def check_dataframe_language(dataframe):
    """
    Checks all text cells in the dataframe.
    Returns details of non-English values if found.
    """

    invalid_values = []

    for column in dataframe.columns:

        # Only inspect object/string columns
        if dataframe[column].dtype == "object":

            for row_number, value in dataframe[column].items():

                if pd.isna(value):
                    continue

                if contains_non_english_text(value):

                    invalid_values.append({
                        "Row": row_number + 2,
                        "Column": column,
                        "Value": str(value)
                    })

    return invalid_values


# ============================================================
# 4. FILE UPLOAD
# ============================================================

st.sidebar.header("📁 Upload Placement Data")

uploaded_file = st.sidebar.file_uploader(
    "Upload Placement Data",
    type=["csv", "xlsx"],
    help="Only CSV and XLSX files are supported."
)


# ============================================================
# 5. SHOW INSTRUCTIONS BEFORE FILE UPLOAD
# ============================================================

if uploaded_file is None:

    st.info(
        "ℹ️ Please upload a CSV or XLSX placement file "
        "to generate the interactive dashboard."
    )

    st.markdown("### 📋 Required File Structure")

    st.write(
        "Your file should contain the following columns:"
    )

    required_table = pd.DataFrame({
        "Required Column": REQUIRED_COLUMNS
    })

    st.dataframe(
        required_table,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("### 📌 Example Data")

    example_data = pd.DataFrame({
        "Student_ID": ["STU001", "STU002", "STU003"],
        "Student_Name": [
            "Aarav Sharma",
            "Ananya Singh",
            "Rohan Verma"
        ],
        "Year": [2024, 2024, 2025],
        "Branch": ["CSE", "IT", "ECE"],
        "Company": ["TCS", "Infosys", "Microsoft"],
        "Package": [7.5, 9.2, 18.5],
        "Placement_Status": [
            "Placed",
            "Placed",
            "Placed"
        ],
        "Location": [
            "Pune",
            "Bangalore",
            "Hyderabad"
        ]
    })

    st.dataframe(
        example_data,
        use_container_width=True,
        hide_index=True
    )

    st.stop()


# ============================================================
# 6. READ CSV OR XLSX FILE
# ============================================================

try:

    file_extension = uploaded_file.name.lower().split(".")[-1]

    if file_extension == "csv":

        # Read CSV file
        df = pd.read_csv(uploaded_file)

    elif file_extension == "xlsx":

        # Read Excel file
        df = pd.read_excel(uploaded_file, engine="openpyxl")

    else:

        st.error(
            "❌ Unsupported file type. "
            "Only CSV and XLSX files are supported."
        )

        st.stop()


except Exception as e:

    st.error(
        f"❌ Unable to read the uploaded file: {e}"
    )

    st.stop()


# ============================================================
# 7. CLEAN COLUMN NAMES
# ============================================================

df.columns = (
    df.columns
    .astype(str)
    .str.strip()
)


# ============================================================
# 8. CHECK REQUIRED COLUMNS
# ============================================================

missing_columns = [
    column
    for column in REQUIRED_COLUMNS
    if column not in df.columns
]

if missing_columns:

    st.error(
        "❌ The uploaded file is missing required columns."
    )

    st.write("Missing columns:")

    for column in missing_columns:
        st.write(f"- `{column}`")

    st.info(
        "Please make sure your file uses the required "
        "column names exactly as shown."
    )

    st.stop()


# ============================================================
# 9. CHECK FOR NON-ENGLISH LANGUAGE
# ============================================================

invalid_language_values = check_dataframe_language(df)

if invalid_language_values:

    st.error(
        "❌ Only English language data is supported."
    )

    st.warning(
        "The uploaded file contains text written in a "
        "language or character set other than English."
    )

    st.markdown("### ⚠️ Detected Non-English Data")

    invalid_df = pd.DataFrame(invalid_language_values)

    st.dataframe(
        invalid_df.head(20),
        use_container_width=True,
        hide_index=True
    )

    st.info(
        "Please replace the detected non-English values "
        "with English text and upload the file again."
    )

    st.stop()


# ============================================================
# 10. DATA CLEANING
# ============================================================

# Remove completely empty rows
df = df.dropna(how="all")

# Remove extra spaces from text columns
for column in df.select_dtypes(include="object").columns:

    df[column] = (
        df[column]
        .astype(str)
        .str.strip()
    )


# Convert Year to numeric where possible
df["Year"] = pd.to_numeric(
    df["Year"],
    errors="coerce"
)


# Convert Package to numeric
df["Package"] = pd.to_numeric(
    df["Package"],
    errors="coerce"
)


# Remove rows where Year or Package is invalid
df = df.dropna(
    subset=["Year", "Package"]
)


# ============================================================
# 11. SIDEBAR FILTERS
# ============================================================

st.sidebar.header("🔎 Dashboard Filters")


# Year filter
years = sorted(
    df["Year"].unique().tolist(),
    reverse=True
)

year_options = ["All Years"] + years

selected_year = st.sidebar.selectbox(
    "📅 Placement Year",
    year_options
)


# Branch filter
branches = sorted(
    df["Branch"].dropna().unique().tolist()
)

branch_options = ["All Branches"] + branches

selected_branch = st.sidebar.selectbox(
    "🏫 Department / Branch",
    branch_options
)


# Company filter
companies = sorted(
    df["Company"].dropna().unique().tolist()
)

company_options = ["All Companies"] + companies

selected_company = st.sidebar.selectbox(
    "🏢 Company",
    company_options
)


# Location filter
locations = sorted(
    df["Location"].dropna().unique().tolist()
)

location_options = ["All Locations"] + locations

selected_location = st.sidebar.selectbox(
    "📍 Job Location",
    location_options
)


# Placement status filter
statuses = sorted(
    df["Placement_Status"]
    .dropna()
    .unique()
    .tolist()
)

status_options = ["All Statuses"] + statuses

selected_status = st.sidebar.selectbox(
    "✅ Placement Status",
    status_options
)


# ============================================================
# 12. APPLY FILTERS
# ============================================================

filtered_df = df.copy()


if selected_year != "All Years":

    filtered_df = filtered_df[
        filtered_df["Year"] == selected_year
    ]


if selected_branch != "All Branches":

    filtered_df = filtered_df[
        filtered_df["Branch"] == selected_branch
    ]


if selected_company != "All Companies":

    filtered_df = filtered_df[
        filtered_df["Company"] == selected_company
    ]


if selected_location != "All Locations":

    filtered_df = filtered_df[
        filtered_df["Location"] == selected_location
    ]


if selected_status != "All Statuses":

    filtered_df = filtered_df[
        filtered_df["Placement_Status"] == selected_status
    ]


# ============================================================
# 13. HANDLE EMPTY FILTER RESULT
# ============================================================

if filtered_df.empty:

    st.warning(
        "⚠️ No records found for the selected filters."
    )

    st.stop()


# ============================================================
# 14. CALCULATE KPIs
# ============================================================

total_students = len(filtered_df)

placed_df = filtered_df[
    filtered_df["Placement_Status"]
    .astype(str)
    .str.lower()
    .eq("placed")
]

placed_students = len(placed_df)

placement_rate = (
    placed_students / total_students * 100
    if total_students > 0
    else 0
)


highest_package = filtered_df["Package"].max()

lowest_package = filtered_df["Package"].min()

average_package = filtered_df["Package"].mean()

median_package = filtered_df["Package"].median()

total_companies = filtered_df["Company"].nunique()

total_branches = filtered_df["Branch"].nunique()


# ============================================================
# 15. KPI CARDS
# ============================================================

st.markdown("## 📊 Placement Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "👨‍🎓 Total Students",
    total_students
)

col2.metric(
    "✅ Placed Students",
    placed_students
)

col3.metric(
    "📈 Placement Rate",
    f"{placement_rate:.2f}%"
)

col4.metric(
    "🏢 Companies",
    total_companies
)


col5, col6, col7, col8 = st.columns(4)

col5.metric(
    "🏆 Highest Package",
    f"₹ {highest_package:.2f} LPA"
)

col6.metric(
    "📉 Lowest Package",
    f"₹ {lowest_package:.2f} LPA"
)

col7.metric(
    "📊 Average Package",
    f"₹ {average_package:.2f} LPA"
)

col8.metric(
    "📌 Median Package",
    f"₹ {median_package:.2f} LPA"
)


# ============================================================
# 16. HIGHEST AND LOWEST PACKAGE STUDENTS
# ============================================================

st.markdown("---")
st.markdown("## 🏆 Package Highlights")


highest_student = filtered_df.loc[
    filtered_df["Package"].idxmax()
]

lowest_student = filtered_df.loc[
    filtered_df["Package"].idxmin()
]


high_col, low_col = st.columns(2)


with high_col:

    st.success("🏆 Highest Package")

    st.markdown(
        f"### {highest_student['Student_Name']}"
    )

    st.write(
        f"**Student ID:** {highest_student['Student_ID']}"
    )

    st.write(
        f"**Branch:** {highest_student['Branch']}"
    )

    st.write(
        f"**Company:** {highest_student['Company']}"
    )

    st.write(
        f"**Package:** ₹ {highest_student['Package']:.2f} LPA"
    )

    st.write(
        f"**Year:** {int(highest_student['Year'])}"
    )

    st.write(
        f"**Location:** {highest_student['Location']}"
    )


with low_col:

    st.warning("📉 Lowest Package")

    st.markdown(
        f"### {lowest_student['Student_Name']}"
    )

    st.write(
        f"**Student ID:** {lowest_student['Student_ID']}"
    )

    st.write(
        f"**Branch:** {lowest_student['Branch']}"
    )

    st.write(
        f"**Company:** {lowest_student['Company']}"
    )

    st.write(
        f"**Package:** ₹ {lowest_student['Package']:.2f} LPA"
    )

    st.write(
        f"**Year:** {int(lowest_student['Year'])}"
    )

    st.write(
        f"**Location:** {lowest_student['Location']}"
    )


# ============================================================
# 17. YEAR-WISE PLACEMENT ANALYSIS
# ============================================================

st.markdown("---")
st.markdown("## 📅 Year-wise Placement Analysis")


year_analysis = (
    filtered_df
    .groupby("Year")
    .agg(
        Students=("Student_ID", "count"),
        Average_Package=("Package", "mean"),
        Highest_Package=("Package", "max")
    )
    .reset_index()
)


fig_year = px.bar(
    year_analysis,
    x="Year",
    y="Students",
    color="Year",
    text="Students",
    title="Year-wise Placement Count"
)

fig_year.update_layout(
    showlegend=False
)

st.plotly_chart(
    fig_year,
    use_container_width=True
)


# ============================================================
# 18. BRANCH-WISE PLACEMENT ANALYSIS
# ============================================================

st.markdown("---")
st.markdown("## 🏫 Department-wise Placement Analysis")


branch_analysis = (
    filtered_df
    .groupby("Branch")
    .agg(
        Students_Placed=("Student_ID", "count"),
        Average_Package=("Package", "mean"),
        Highest_Package=("Package", "max")
    )
    .reset_index()
)


branch_col1, branch_col2 = st.columns(2)


with branch_col1:

    fig_branch_count = px.bar(
        branch_analysis,
        x="Branch",
        y="Students_Placed",
        color="Branch",
        text="Students_Placed",
        title="Department-wise Placement Count"
    )

    st.plotly_chart(
        fig_branch_count,
        use_container_width=True
    )


with branch_col2:

    fig_branch_package = px.bar(
        branch_analysis,
        x="Branch",
        y="Average_Package",
        color="Branch",
        text_auto=".2f",
        title="Department-wise Average Package"
    )

    fig_branch_package.update_yaxes(
        title="Average Package (LPA)"
    )

    st.plotly_chart(
        fig_branch_package,
        use_container_width=True
    )


# ============================================================
# 19. YEAR × BRANCH HEATMAP
# ============================================================

st.markdown("---")
st.markdown("## 🔥 Year × Department Placement Heatmap")


year_branch = pd.pivot_table(
    filtered_df,
    values="Student_ID",
    index="Branch",
    columns="Year",
    aggfunc="count",
    fill_value=0
)


fig_heatmap = px.imshow(
    year_branch,
    text_auto=True,
    color_continuous_scale="Blues",
    title="Placement Count by Year and Department"
)

st.plotly_chart(
    fig_heatmap,
    use_container_width=True
)


# ============================================================
# 20. COMPANY-WISE HIRING ANALYSIS
# ============================================================

st.markdown("---")
st.markdown("## 🏢 Company-wise Hiring Analysis")


company_analysis = (
    filtered_df
    .groupby("Company")
    .agg(
        Students_Hired=("Student_ID", "count"),
        Highest_Package=("Package", "max"),
        Lowest_Package=("Package", "min"),
        Average_Package=("Package", "mean")
    )
    .reset_index()
    .sort_values(
        "Students_Hired",
        ascending=False
    )
)


company_col1, company_col2 = st.columns(2)


with company_col1:

    fig_company_hiring = px.bar(
        company_analysis.head(15),
        x="Company",
        y="Students_Hired",
        color="Company",
        text="Students_Hired",
        title="Top Hiring Companies"
    )

    fig_company_hiring.update_layout(
        xaxis_tickangle=-45,
        showlegend=False
    )

    st.plotly_chart(
        fig_company_hiring,
        use_container_width=True
    )


with company_col2:

    top_paying_companies = (
        company_analysis
        .sort_values(
            "Highest_Package",
            ascending=False
        )
        .head(15)
    )

    fig_company_package = px.bar(
        top_paying_companies,
        x="Company",
        y="Highest_Package",
        color="Company",
        text_auto=".2f",
        title="Highest Package by Company"
    )

    fig_company_package.update_layout(
        xaxis_tickangle=-45,
        showlegend=False
    )

    fig_company_package.update_yaxes(
        title="Highest Package (LPA)"
    )

    st.plotly_chart(
        fig_company_package,
        use_container_width=True
    )


# ============================================================
# 21. PACKAGE DISTRIBUTION
# ============================================================

st.markdown("---")
st.markdown("## 💰 Package Distribution")


fig_package = px.histogram(
    filtered_df,
    x="Package",
    nbins=15,
    color="Branch",
    title="Package Distribution Across Students",
    labels={
        "Package": "Package (LPA)"
    }
)

st.plotly_chart(
    fig_package,
    use_container_width=True
)


# ============================================================
# 22. BRANCH-WISE COMPANY PACKAGE ANALYSIS
# ============================================================

st.markdown("---")
st.markdown("## 🏫 Company Performance by Department")


branch_company_analysis = (
    filtered_df
    .groupby(["Branch", "Company"])
    .agg(
        Students=("Student_ID", "count"),
        Highest_Package=("Package", "max"),
        Average_Package=("Package", "mean")
    )
    .reset_index()
    .sort_values(
        "Highest_Package",
        ascending=False
    )
)


st.dataframe(
    branch_company_analysis,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# 23. TOP STUDENTS
# ============================================================

st.markdown("---")
st.markdown("## 🥇 Top Package Holders")


top_students = (
    filtered_df
    .sort_values(
        "Package",
        ascending=False
    )
    .head(10)
)


top_students_display = top_students[
    [
        "Student_ID",
        "Student_Name",
        "Year",
        "Branch",
        "Company",
        "Package",
        "Location"
    ]
].copy()


top_students_display["Package"] = (
    top_students_display["Package"]
    .map(lambda x: f"₹ {x:.2f} LPA")
)


st.dataframe(
    top_students_display,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# 24. DETAILED STUDENT RECORDS
# ============================================================

st.markdown("---")
st.markdown("## 🔎 Detailed Student Placement Records")


search_student = st.text_input(
    "Search by Student Name or Student ID",
    placeholder="Example: Rahul or STU001"
)


search_result = filtered_df.copy()


if search_student:

    search_text = search_student.strip().lower()

    search_result = search_result[
        search_result["Student_Name"]
        .astype(str)
        .str.lower()
        .str.contains(
            search_text,
            na=False
        )
        |
        search_result["Student_ID"]
        .astype(str)
        .str.lower()
        .str.contains(
            search_text,
            na=False
        )
    ]


st.dataframe(
    search_result,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# 25. DOWNLOAD FILTERED DATA AS EXCEL
# ============================================================

st.markdown("---")
st.markdown("## 📥 Report Generation")


buffer = io.BytesIO()


with pd.ExcelWriter(
    buffer,
    engine="openpyxl"
) as writer:

    filtered_df.to_excel(
        writer,
        index=False,
        sheet_name="Placement_Report"
    )


download_year = (
    str(selected_year)
    if selected_year != "All Years"
    else "All_Years"
)


st.download_button(
    label="📥 Download Filtered Excel Report",
    data=buffer.getvalue(),
    file_name=f"Placement_Report_{download_year}.xlsx",
    mime=(
        "application/vnd.openxmlformats-officedocument."
        "spreadsheetml.sheet"
    )
)


# ============================================================
# 26. FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "Smart College Placement Analytics Dashboard | "
    "Navachar — Zero-Code Analytics for Placement Cells"
)
