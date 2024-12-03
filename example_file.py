import google.generativeai as genai
import os
from google.generativeai import GenerationConfig
# Replace 'YOUR_API_KEY' with your actual Google Generative AI API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyCv-vtQRNrCtB6PCJ0SsH3R7AQXUUmLBpc"
# Call genai.configure() to initialize the library and load the environment variables
genai.configure()
#/content/page_4.png
# File path to the uploaded table image
file_path1 = os.path.join("media", "/content/page_196.png")  # Replace with your file path
file_path = os.path.join("media", "/content/page_33 (1).png")
file_path2 = os.path.join("media", "/content/page_41.png")
file_path3 = os.path.join("media", "/content/page_32.png")
file_path4 = os.path.join("media", "/content/page_59.png")
file_path5 = os.path.join("media", "/content/page_14.png")
#file_path3 = os.path.join("media", "/content/table-22-13.jpg")
#file_path4 = os.path.join("media", "/content/table-21-12.jpg")

myfile1 = genai.upload_file(file_path1)
myfile_ex = genai.upload_file(file_path)
myfile_ex2 = genai.upload_file(file_path2)
myfile_ex3 = genai.upload_file(file_path3)
myfile_ex4 = genai.upload_file(file_path4)
myfile_ex5 = genai.upload_file(file_path5)
Examples=[
{
"input_table": f"{myfile_ex}",
"output":"""```json
{{
  "Table": {{
    "Flattened Columns": [
      "Background characteristic",
      "Employed in the 12 months preceding the survey_Currently employed",
      "Employed in the 12 months preceding the survey_Not currently employed",
      "Not employed in the 12 months preceding the survey",
      "Total",
      "Number of women"
    ],
    "Flattened Rows": [
      "Age_15–19",
      "Age_20–24",
      "Age_25–29",
      "Age_30–34",
      "Age_35–39",
      "Age_40–44",
      "Age_45–49",
      "Marital status_Never married",
      "Marital status_Married or living together",
      "Marital status_Divorced/separated/widowed",
      "Number of living children_0",
      "Number of living children_1–2",
      "Number of living children_3–4",
      "Number of living children_5+",
      "Ethnic group_Brahmin/Chhetri",
      "Ethnic group_Dalit",
      "Ethnic group_Janjati",
      "Ethnic group_Madhesi",
      "Ethnic group_Muslim",
      "Ethnic group_Other",
      "Residence_Urban",
      "Residence_Rural",
      "Ecological zone_Mountain",
      "Ecological zone_Hill",
      "Ecological zone_Terai",
      "Province_Koshi Province",
      "Province_Koshi Province_Urban",
      "Province_Koshi Province_Rural",
      "Province_Madhesh Province",
      "Province_Madhesh Province_Urban",
      "Province_Madhesh Province_Rural",
      "Province_Bagmati Province",
      "Province_Bagmati Province_Urban",
      "Province_Bagmati Province_Rural",
      "Province_Gandaki Province",
      "Province_Gandaki Province_Urban",
      "Province_Gandaki Province_Rural",
      "Province_Lumbini Province",
      "Province_Lumbini Province_Urban",
      "Province_Lumbini Province_Rural",
      "Province_Karnali Province",
      "Province_Karnali Province_Urban",
      "Province_Karnali Province_Rural",
      "Province_Sudurpaschim Province",
      "Province_Sudurpaschim Province_Urban",
      "Province_Sudurpaschim Province_Rural",
      "Education_No education",
      "Education_Basic education (1–8)",
      "Education_Lower basic education (1–5)",
      "Education_Upper basic education (6–8)",
      "Education_Secondary (9–12)",
      "Education_Lower secondary (9–10)",
      "Education_Higher secondary (11–12)",
      "Education_More than secondary (13 and above)",
      "Wealth quintile_Lowest",
      "Wealth quintile_Second",
      "Wealth quintile_Third",
      "Wealth quintile_Fourth",
      "Wealth quintile_Highest",
      "Total"
    ]
  }}
}}
```"""},
{
"input_table": f"{myfile_ex2}",
"output":"""```json
{{
  "Table": {{
    "Flattened Columns": [
      "Background Characteristic",
      "Average Number of Cigarettes Smoked Per Day (<5)",
      "Average Number of Cigarettes Smoked Per Day (5–9)",
      "Average Number of Cigarettes Smoked Per Day (10–14)",
      "Average Number of Cigarettes Smoked Per Day (15–24)",
      "Average Number of Cigarettes Smoked Per Day (≥25)",
      "Total (%)",
      "Number of Men Who Smoke Cigarettes Daily"
    ],
    "Flattened Rows": [
      "Age_15–19",
      "Age_20–24",
      "Age_25–29",
      "Age_30–34",
      "Age_35–39",
      "Age_40–44",
      "Age_45–49",
      "Ethnic Group_Brahmin/Chhetri",
      "Ethnic Group_Dalit",
      "Ethnic Group_Janajati",
      "Ethnic Group_Madhesi",
      "Ethnic Group_Muslim",
      "Ethnic Group_Other",
      "Residence_Urban",
      "Residence_Rural",
      "Ecological Zone_Mountain",
      "Ecological Zone_Hill",
      "Ecological Zone_Terai",
      "Province_Koshi Province (Urban, Rural)",
      "Province_Madhesh Province (Urban, Rural)",
      "Province_Bagmati Province (Urban, Rural)",
      "Province_Gandaki Province (Urban, Rural)",
      "Province_Lumbini Province (Urban, Rural)",
      "Province_Karnali Province (Urban, Rural)",
      "Province_Sudurpashchim Province (Urban, Rural)",
      "Education_No education",
      "Education_Basic education (1–8)",
      "Education_Lower basic education (1–5)",
      "Education_Upper basic education (6–8)",
      "Education_Secondary (9–12)",
      "Education_Lower secondary (9–10)",
      "Education_Higher secondary (11–12)",
      "Education_More than secondary (13 and above)",
      "Wealth Quintile_Lowest",
      "Wealth Quintile_Second",
      "Wealth Quintile_Middle",
      "Wealth Quintile_Fourth",
      "Wealth Quintile_Highest"
    ]
  }}
}}
```
"""
},
{
"input_table": f"{myfile_ex5}",
"output":"""
```json
{{
  "Table": {{
    "Flattened Columns": [
      "Background characteristic",
      "Net attendance_ratio_Male",
      "Net attendance_ratio_Female",
      "Net attendance_ratio_Total",
      "Net attendance_ratio_Gender parity index",
      "Net attendance_ratio_Male",
      "Net attendance_ratio_Female",
      "Net attendance_ratio_Total",
      "Net attendance_ratio_Gender parity index"
    ],
    "Flattened Rows": [
  "LOWER BASIC SCHOOL (GRADES 1–5)_Residence_Urban",
  "LOWER BASIC SCHOOL (GRADES 1–5)_Residence_Rural",
  "LOWER BASIC SCHOOL (GRADES 1–5)_Ecological zone_Mountain",
  "LOWER BASIC SCHOOL (GRADES 1–5)_Ecological zone_Hill",
  "LOWER BASIC SCHOOL (GRADES 1–5)_Ecological zone_Terai",
  "LOWER BASIC SCHOOL (GRADES 1–5)_Province_Koshi Province",
  "LOWER BASIC SCHOOL (GRADES 1–5)_Province_Koshi Province_Urban",
  "LOWER BASIC SCHOOL (GRADES 1–5)_Province_Koshi Province_Rural",
  "LOWER BASIC SCHOOL (GRADES 1–5)_Province_Madhesh Province",
  "LOWER BASIC SCHOOL (GRADES 1–5)_Province_Madhesh Province_Urban",
  "LOWER BASIC SCHOOL (GRADES 1–5)_Province_Madhesh Province_Rural",
  "LOWER BASIC SCHOOL (GRADES 1–5)_Province_Bagmati Province",
  "LOWER BASIC SCHOOL (GRADES 1–5)_Province_Bagmati Province_Urban",
  "LOWER BASIC SCHOOL (GRADES 1–5)_Province_Bagmati Province_Rural",
  "LOWER BASIC SCHOOL (GRADES 1–5)_Province_Gandaki Province",
  "LOWER BASIC SCHOOL (GRADES 1–5)_Province_Gandaki_Urban",
  "LOWER BASIC SCHOOL (GRADES 1–5)_Province_Gandaki_Rural",
  "LOWER BASIC SCHOOL (GRADES 1–5)_Province_Lumbini Province",
  "LOWER BASIC SCHOOL (GRADES 1–5)_Province_Lumbini_Province_Urban",
  "LOWER BASIC SCHOOL (GRADES 1–5)_Province_Lumbini_Rural",
  "LOWER BASIC SCHOOL (GRADES 1–5)_Province_Karnali Province",
  "LOWER BASIC SCHOOL (GRADES 1–5)_Province_Karnali_Urban",
  "LOWER BASIC SCHOOL (GRADES 1–5)_Province_Karnali_Rural",
  "LOWER BASIC SCHOOL (GRADES 1–5)_Province_Sudurpashchim Province",
  "LOWER BASIC SCHOOL (GRADES 1–5)_Province_Sudurpashchim_Urban",
  "LOWER BASIC SCHOOL (GRADES 1–5)_Province_Sudurpashchim_Rural",
  "LOWER BASIC SCHOOL (GRADES 1–5)_Wealth quintile_Lowest",
  "LOWER BASIC SCHOOL (GRADES 1–5)_Wealth quintile_Second",
  "LOWER BASIC SCHOOL (GRADES 1–5)_Wealth quintile_Middle",
  "LOWER BASIC SCHOOL (GRADES 1–5)_Wealth quintile_Fourth",
  "LOWER BASIC SCHOOL (GRADES 1–5)_Wealth quintile_Highest",
  "LOWER BASIC SCHOOL (GRADES 1–5)_Total"
  "UPPER BASIC SCHOOL (GRADES 6–8)_Residence_Urban",
  "UPPER BASIC SCHOOL (GRADES 6–8)_Residence_Rural",
  "UPPER BASIC SCHOOL (GRADES 6–8)_Ecological zone_Mountain",
  "UPPER BASIC SCHOOL (GRADES 6–8)_Ecological zone_Hill",
  "UPPER BASIC SCHOOL (GRADES 6–8)_Ecological zone_Terai",
  "UPPER BASIC SCHOOL (GRADES 6–8)_Province_Koshi Province",
  "UPPER BASIC SCHOOL (GRADES 6–8)_Province_Koshi Province_Urban",
  "UPPER BASIC SCHOOL (GRADES 6–8)_Province_Koshi Province_Rural",
  "UPPER BASIC SCHOOL (GRADES 6–8)_Province_Madhesh Province",
  "UPPER BASIC SCHOOL (GRADES 6–8)_Province_Madhesh Province_Urban",
  "UPPER BASIC SCHOOL (GRADES 6–8)_Province_Madhesh Province_Rural",
  "UPPER BASIC SCHOOL (GRADES 6–8)_Province_Bagmati Province",
  "UPPER BASIC SCHOOL (GRADES 6–8)_Province_Bagmati Province_Urban",
  "UPPER BASIC SCHOOL (GRADES 6–8)_Province_Bagmati Province_Rural",
  "UPPER BASIC SCHOOL (GRADES 6–8)_Province_Gandaki Province",
  "UPPER BASIC SCHOOL (GRADES 6–8)_Province_Gandaki_Urban",
  "UPPER BASIC SCHOOL (GRADES 6–8)_Province_Gandaki_Rural",
  "UPPER BASIC SCHOOL (GRADES 6–8)_Province_Lumbini Province",
  "UPPER BASIC SCHOOL (GRADES 6–8)_Province_Lumbini_Province_Urban",
  "UPPER BASIC SCHOOL (GRADES 6–8)_Province_Lumbini_Rural",
  "UPPER BASIC SCHOOL (GRADES 6–8)_Province_Karnali Province",
  "UPPER BASIC SCHOOL (GRADES 6–8)_Province_Karnali_Urban",
  "UPPER BASIC SCHOOL (GRADES 6–8)_Province_Karnali_Rural",
  "UPPER BASIC SCHOOL (GRADES 6–8)_Province_Sudurpashchim Province"
  "UPPER BASIC SCHOOL (GRADES 6–8)_Province_Sudurpashchim urban"
  "UPPER BASIC SCHOOL (GRADES 6–8)_Province_Sudurpashchim rural"


    ]
  }}
  ```
  """
},
{

"input_table": f"{myfile_ex3}",
"output":"""```json
{{
  "Table": {{
    "Flattened Columns": [
      "Employed in the 12 months preceding the survey_Currently employed",
      "Employed in the 12 months preceding the survey_Not currently employed",
      "Not employed in the 12 months preceding the survey",
      "Total",
      "Number of women"
    ],
    "Flattened Rows": [
      "Age_15–19",
      "Age_20–24",
      "Age_25–29",
      "Age_30–34",
      "Age_35–39",
      "Age_40–44",
      "Age_45–49",
      "Marital status_Never married",
      "Marital status_Married or living together",
      "Marital status_Divorced/separated/widowed",
      "Number of living children_0",
      "Number of living children_1–2",
      "Number of living children_3–4",
      "Number of living children_5+",
      "Ethnic group_Brahmin/Chhetri",
      "Ethnic group_Dalit",
      "Ethnic group_Janajati",
      "Ethnic group_Madhesi",
      "Ethnic group_Muslim",
      "Ethnic group_Other",
      "Residence_Urban",
      "Residence_Rural",
      "Ecological zone_Mountain",
      "Ecological zone_Hill",
      "Ecological zone_Terai",
      "Province_Koshi Province",
      "Province_Koshi Province_Urban",
      "Province_Koshi Province_Rural",
      "Province_Madhesh Province",
      "Province_Madhesh Province_Urban",
      "Province_Madhesh Province_Rural",
      "Province_Bagmati Province",
      "Province_Bagmati Province_Urban",
      "Province_Bagmati Province_Rural",
      "Province_Gandaki Province",
      "Province_Gandaki_Urban",
      "Province_Gandaki_Rural",
      "Province_Lumbini Province",
      "Province_Lumbini_Province_Urban",
      "Province_Lumbini_Rural",
      "Province_Karnali Province",
      "Province_Karnali_Urban",
      "Province_Karnali_Rural",
      "Province_Sudurpashchim Province",
      "Province_Sudurpashchim_Urban",
      "Province_Sudurpashchim_Rural",
      "Education_No education",
      "Education_Basic education (1–8)",
      "Education_Lower basic education (1–5)",
      "Education_Upper basic education (6–8)",
      "Education_Secondary (9–12)",
      "Education_Lower secondary (9–10)",
      "Education_Higher secondary (11–12)",
      "Education_More than secondary (13 and above)",
      "Wealth quintile_Lowest",
      "Wealth quintile_Second",
      "Wealth quintile_Middle",
      "Wealth quintile_Fourth",
      "Wealth quintile_Highest",
      "Total"
    ]
  }}
}}
```
"""
},
{


"input_table": f"{myfile_ex4}",
"output":"""```json
{{
  "Table": {{
    "Flattened Columns": [
      "Background characteristic",
      "Among all respondents_Percentage who have heard of COVID-19",
      "Among all respondents_Number",
      "Among respondents who have heard of COVID-19_Percentage who report fever as common symptom",
      "Among respondents who have heard of COVID-19_Percentage who report cough as common symptom",
      "Among respondents who have heard of COVID-19_Percentage who report shortness of breath and breathing difficulties as common symptoms",
      "Among respondents who have heard of COVID-19_Percentage who know that COVID-19 can be prevented",
      "Among respondents who have heard of COVID-19_Percentage who are taking measures to reduce the risk of being infected with COVID-19",
      "Number of women"
    ],
    "Flattened Rows": [
      "Age_15–19",
      "Age_20–24",
      "Age_25–29",
      "Age_30–34",
      "Age_35–39",
      "Age_40–44",
      "Age_45–49",
      "Marital status_Never married",
      "Marital status_Married or living together",
      "Marital status_Divorced/separated/widowed",
      "Ethnic group_Brahmin/Chhetri",
      "Ethnic group_Dalit",
      "Ethnic group_Janajati",
      "Ethnic group_Madhesi",
      "Ethnic group_Muslim",
      "Ethnic group_Other",
      "Residence_Urban",
      "Residence_Rural",
      "Ecological zone_Mountain",
      "Ecological zone_Hill",
      "Ecological zone_Terai",
      "Province_Koshi Province",
      "Province_Koshi Province_Urban",
      "Province_Koshi Province_Rural",
      "Province_Madhesh Province",
      "Province_Madhesh Province_Urban",
      "Province_Madhesh Province_Rural",
      "Province_Bagmati Province",
      "Province_Bagmati Province_Urban",
      "Province_Bagmati Province_Rural",
      "Province_Gandaki Province",
      "Province_Gandaki_Urban",
      "Province_Gandaki_Rural",
      "Province_Lumbini Province",
      "Province_Lumbini_Province_Urban",
      "Province_Lumbini_Rural",
      "Province_Karnali Province",
      "Province_Karnali_Urban",
      "Province_Karnali_Rural",
      "Province_Sudurpashchim Province",
      "Province_Sudurpashchim_Urban",
      "Province_Sudurpashchim_Rural",
      "Education_No education",
      "Education_Basic education (1–8)",
      "Education_Lower basic education (1–5)",
      "Education_Upper basic education (6–8)",
      "Education_Secondary (9–12)",
      "Education_Lower secondary (9–10)",
      "Education_Higher secondary (11–12)",
      "Education_More than secondary (13 and above)",
      "Wealth quintile_Lowest",
      "Wealth quintile_Second",
      "Wealth quintile_Middle",
      "Wealth quintile_Fourth",
      "Wealth quintile_Highest",
      "Total"
    ]
  }}
}}
```
"""
}
]