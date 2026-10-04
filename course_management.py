import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource

# ============================================================
# COURSE MANAGEMENT SYSTEM
# ============================================================
print("=" * 60)
print("COURSE MANAGEMENT SYSTEM")
print("=" * 60)

# ------------------------------------------------------------
# 1. COURSE DATA USING PANDAS
# ------------------------------------------------------------
course_data = {
    "Course_ID": ["C101", "C102", "C103", "C104", "C105", "C106", "C107", "C108"],
    "Course_Name": [
        "Python Programming",
        "Data Science",
        "Web Development",
        "Database Management",
        "Machine Learning",
        "Cloud Computing",
        "Cyber Security",
        "Java Programming",
    ],
    "Students": [45, 38, 52, 41, 35, 30, 28, 47],
    "Duration_Months": [4, 5, 6, 4, 6, 5, 5, 4],
    "Fee": [5000, 7000, 6500, 4500, 8000, 7500, 6000, 5500],
    "Average_Marks": [82, 85, 78, 80, 88, 76, 84, 81],
}

courses = pd.DataFrame(course_data)

print("\nCOURSE DETAILS")
print("-" * 60)
print(courses.to_string(index=False))

# ------------------------------------------------------------
# 2. NUMPY CALCULATIONS
# ------------------------------------------------------------
students = np.array(courses["Students"])
fees = np.array(courses["Fee"])
marks = np.array(courses["Average_Marks"])

print("\nNUMPY STATISTICS")
print("-" * 60)
print("Total Students:", np.sum(students))
print("Average Students per Course:", round(np.mean(students), 2))
print("Maximum Students:", np.max(students))
print("Minimum Students:", np.min(students))
print("Average Course Fee:", round(np.mean(fees), 2))
print("Highest Course Fee:", np.max(fees))
print("Lowest Course Fee:", np.min(fees))
print("Overall Average Marks:", round(np.mean(marks), 2))

# ------------------------------------------------------------
# 3. PANDAS ANALYSIS
# ------------------------------------------------------------
print("\nPANDAS ANALYSIS")
print("-" * 60)

print("Course with Maximum Enrollment:")
print(courses.loc[courses["Students"].idxmax(), ["Course_Name", "Students"]].to_string())

print("\nCourse with Highest Average Marks:")
print(courses.loc[courses["Average_Marks"].idxmax(), ["Course_Name", "Average_Marks"]].to_string())

print("\nCourse with Highest Fee:")
print(courses.loc[courses["Fee"].idxmax(), ["Course_Name", "Fee"]].to_string())

# ------------------------------------------------------------
# 4. ADDITIONAL COLUMN
# ------------------------------------------------------------
courses["Total_Revenue"] = courses["Students"] * courses["Fee"]

print("\nCOURSE REVENUE")
print("-" * 60)
print(courses[["Course_Name", "Students", "Fee", "Total_Revenue"]].to_string(index=False))

# ------------------------------------------------------------
# 5. SCIPY STATISTICAL ANALYSIS
# ------------------------------------------------------------
print("\nSCIPY STATISTICAL ANALYSIS")
print("-" * 60)

# One sample t-test: checking whether average marks are significantly different from 75
t_statistic, p_value = stats.ttest_1samp(marks, 75)
print("T-Statistic:", round(t_statistic, 4))
print("P-Value:", round(p_value, 4))

if p_value < 0.05:
    print("Result: Average marks are significantly different from 75.")
else:
    print("Result: No significant difference from 75.")

# ------------------------------------------------------------
# 6. SCIPY CORRELATION
# ------------------------------------------------------------
correlation, correlation_p = stats.pearsonr(students, marks)
print("\nCorrelation between Students and Average Marks:")
print("Correlation:", round(correlation, 4))
print("P-Value:", round(correlation_p, 4))

# ------------------------------------------------------------
# 7. MATPLOTLIB GRAPH - ENROLLMENT
# ------------------------------------------------------------
plt.figure(figsize=(10, 6))
plt.bar(courses["Course_Name"], courses["Students"])
plt.title("Students Enrolled in Each Course")
plt.xlabel("Courses")
plt.ylabel("Number of Students")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ------------------------------------------------------------
# 8. MATPLOTLIB GRAPH - AVERAGE MARKS
# ------------------------------------------------------------
plt.figure(figsize=(10, 6))
plt.plot(courses["Course_Name"], courses["Average_Marks"], marker="o")
plt.title("Average Marks by Course")
plt.xlabel("Courses")
plt.ylabel("Average Marks")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# ------------------------------------------------------------
# 9. BOKEH INTERACTIVE GRAPH
# ------------------------------------------------------------
source = ColumnDataSource(courses)
bokeh_plot = figure(
    x_range=courses["Course_Name"].tolist(),
    title="Course Enrollment - Interactive Bokeh Graph",
    x_axis_label="Course",
    y_axis_label="Students",
    width=900,
    height=500,
)
bokeh_plot.vbar(
    x="Course_Name",
    top="Students",
    width=0.6,
    source=source,
)
bokeh_plot.xaxis.major_label_orientation = 0.8
show(bokeh_plot)

# ------------------------------------------------------------
# 10. FINAL SUMMARY
# ------------------------------------------------------------
print("\n" + "=" * 60)
print("COURSE SUMMARY")
print("=" * 60)
print("Total Courses:", len(courses))
print("Total Students:", np.sum(students))
print("Average Marks:", round(np.mean(marks), 2))
print("Total Revenue:", np.sum(courses["Total_Revenue"]))
print("\nCourse with Maximum Students:", courses.loc[courses["Students"].idxmax(), "Course_Name"])
print("Course with Highest Marks:", courses.loc[courses["Average_Marks"].idxmax(), "Course_Name"])
print("Course with Highest Revenue:", courses.loc[courses["Total_Revenue"].idxmax(), "Course_Name"])
print("\nCourse Management System Completed Successfully!")
print("=" * 60)