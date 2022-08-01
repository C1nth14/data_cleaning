# Data Cleaning

For this project, I looked at the dataset al_results_2020 and was tasked with preparing it for analysis. 

### Process
1. Removing unwanted columns like Zscore, gender and syllabus.
2. Create a birthday column by combining the birth_day, birth_month and birth_year columns and dropping them.
3. Removing the rows with missing values that were indicated as '-'.
4. Removing rows where the student was absent for all the assessments.
5. Checking that all the dates were valid.

I used functional programming to tackle this project.

Author: Susan Cynthia Musiime