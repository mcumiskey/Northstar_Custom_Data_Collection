# Northstar Custom Data Collection

 A python3 script for the Drexel Digital Navigator Team to use for generating Data Reports on Northstar. Read more about the Drexel Digital Navigator Team here: https://drexel.edu/excite/community/digital-navigators/

# Installing Python 3: 
* https://realpython.com/installing-python/
* https://docs.python-guide.org/starting/installation/
* https://developers.google.com/edu/python/set-up

# Downloading the Project / File Structure 

![image](https://github.com/mcumiskey/Northstar_Custom_Data_Collection/assets/29690717/61691bca-e471-4ff5-8b48-0a220e33a5f4)

* Click on the [<> Code] button near the project name
* Choose 'Download ZIP'
* Make note of where you save the project
* Unzip the files on your personal computer.
  
![image](https://github.com/mcumiskey/Northstar_Custom_Data_Collection/assets/29690717/32f127f9-f65b-403e-9b32-af4f231d3a11)

* The parent folder is named "Northstar_Custom_Data_Collection"
 * There are three example exports marked with "0_example_export_..."
 * The Python script named "Northstar_Data.py"
 * The data sources from Northstar are "assessments.csv" and "time-on-task-11686-all-time.xlsx"
  * These have been pre-filled with fake example people. 
* There are also two github files LICENSE and README.md that can be ignored

# Collecting the Data  

All of the data is downloaded from Northstar: https://www.digitalliteracyassessment.org/ 

## assessments.csv

![image](https://github.com/mcumiskey/Northstar_Custom_Data_Collection/assets/29690717/e355977f-5bc0-48a0-83c8-f975b688981f)

* On the NSOL Admin portal, go to Assessments > View all Results
  
![image](https://github.com/mcumiskey/Northstar_Custom_Data_Collection/assets/29690717/cb85e2e6-aabd-4086-a6d1-f8457b4f6d18)

* Then click "Download all Results"
* Save or move your file into the "Northstar_Custom_Data_Collection" folder, replacing the existing 'assessments.csv' 

## time-on-task-11686-all-time.xlsx

![image](https://github.com/mcumiskey/Northstar_Custom_Data_Collection/assets/29690717/9a00bf3c-56f3-451b-84f6-98a787c06ba9)

* On the NSOL Admin portal, go to Learners > View Useage Amounts
* Then click "Download as Spreadsheet"
* Save or move your file into the "Northstar_Custom_Data_Collection" folder, replacing the existing 'time-on-task-11686-all-time.xlsx' 

# Running the Script 

## For macOS:

**Open Terminal:** Launch the Terminal application on your macOS. You can find it in the Applications folder under Utilities, or you can use Spotlight Search (Cmd + Space, then type "Terminal").

**Navigate to the Script Directory:** Use the cd command to navigate to the directory where your Python script and data files are located. For example:

~~~
cd path/to/your/script/directory/Northstar_Custom_Data_Collection
~~~

**Run the Script:** Once you're in the correct directory, you can run the Python script by entering the following command:

~~~
python3 Northstar_Data.py
~~~

**This assumes that you have Python 3 installed on your macOS.** If you only have one version of Python installed, you can use the python command instead of python3

## For Windows:

**Open Command Prompt:** Open the Command Prompt application on your Windows computer. You can do this by searching for "Command Prompt" in the Start menu.

**Navigate to the Script Directory:** Use the cd command to navigate to the directory where your Python script and data files are located. For example:

~~~
cd path/to/your/script/directory/Northstar_Custom_Data_Collection
~~~

**Run the Script:** Once you're in the correct directory, you can the your Python script by entering the following command:

~~~
python3 Northstar_Data.py
~~~

**This assumes that you have Python installed on your Windows computer and that it's added to your system's PATH variable.** If you have multiple versions of Python installed, you may need to specify the version, such as python3 instead of python.

# Creating Custom Reports
* TBA

 Created by Miles Cumiskey as part of a 2023-2024 Americorps VISTA Service Year.
