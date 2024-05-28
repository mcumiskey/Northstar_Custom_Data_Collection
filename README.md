# Northstar Custom Data Collection

 A python3 script for the Drexel Digital Navigator Team to use for generating data reports for the online digital literacy platform Northstar. 
 
 Read more about the Drexel Digital Navigator Team here: https://drexel.edu/excite/community/digital-navigators/

# Installing Python 3: 

* https://realpython.com/installing-python/
* https://docs.python-guide.org/starting/installation/
* https://developers.google.com/edu/python/set-up

# Downloading the Project / File Structure 

![Guide to finding the Code download button](https://github.com/mcumiskey/Northstar_Custom_Data_Collection/assets/29690717/61691bca-e471-4ff5-8b48-0a220e33a5f4)

* Click on the [<> Code] button near the project name
* Choose 'Download ZIP'
* Make note of where you save the project
* Unzip the files on your personal computer.
  
![view of the files on mac when downloaded](https://github.com/mcumiskey/Northstar_Custom_Data_Collection/assets/29690717/32f127f9-f65b-403e-9b32-af4f231d3a11)

* The parent folder is named "Northstar_Custom_Data_Collection"
 * There are three example exports marked with "0_example_export_..."
 * The Python script named "Northstar_Data.py"
 * The data sources from Northstar are "assessments.csv" and "time-on-task-11686-all-time.xlsx"
     * These have been pre-filled with fake example people. 
* There are also two github files LICENSE and README.md that can be ignored

# Collecting the Data  

All of the data is downloaded from Northstar: https://www.digitalliteracyassessment.org/ 

## assessments.csv

![North Star Admin Portal Assesment Overview Page](https://github.com/mcumiskey/Northstar_Custom_Data_Collection/assets/29690717/e355977f-5bc0-48a0-83c8-f975b688981f)

* On the NSOL Admin portal, go to Assessments > View all Results
  
![North Star Admin Portal All Assesments Page](https://github.com/mcumiskey/Northstar_Custom_Data_Collection/assets/29690717/cb85e2e6-aabd-4086-a6d1-f8457b4f6d18)

* Then click "Download all Results"
* Save or move your file into the "Northstar_Custom_Data_Collection" folder, replacing the existing 'assessments.csv' 

## time-on-task-11686-all-time.xlsx

![North Star Admin Portal Learners View Useage Amounts](https://github.com/mcumiskey/Northstar_Custom_Data_Collection/assets/29690717/9a00bf3c-56f3-451b-84f6-98a787c06ba9)

* On the NSOL Admin portal, go to Learners > View Useage Amounts
* Then click "Download as Spreadsheet"
* Save or move your file into the "Northstar_Custom_Data_Collection" folder, replacing the existing 'time-on-task-11686-all-time.xlsx'

# Customizing for Your Location 

This code was created for the Drexel Digital Navigators team. 

To use it for your own location you'll need to customize line 43

~~~ python
learners_df = pd.read_excel('time-on-task-11686-all-time.xlsx', 'Drexel University (Summary)')
~~~

Replace 'Drexel University (Summary)' with your location name. You can double check the name by opening the 'time-on-task-11686-all-time.xlsx' file and checking what your location's sheet is named. 

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

Custom reports can be made by adding additional code. 

## The overview report 
The basic data report is generated on line 88.

~~~ python
df.to_csv('0_example_export_learner_details_with_assessments.csv', index = False)
~~~

This is a new CSV file (named '0_example_export_learner_details_with_assessments.csv') that contains all of the sites learners and their assessments for all time. 

This document is formatted as follows: 

| Learner ID | Learner Name | Learner Email     | Invite Date | Status  | Requirements Passed                           | Tags                                   | Assessments |
|------------|--------------|-------------------|-------------|---------|----------------------------------------------|----------------------------------------|-------------|
| 201        | AAA BBB      | aaabbb@email.com | 2024-01-23  | active  | 1 |2 Complete, BFLC, K-12 Caregiver (PHLConnectED), Night Class | Mac OS, Windows, Microsoft Word, Using Email, Internet Basics, Basic Computer Skills | 

The 'Requirements Passed' column is unique to the Drexel Digital Navigator program, as we distribute laptops to learners who have completed a set of modules with a proctor. The other sections are assembled from the two data files. 

This CSV file allows us to quickly look up and sort learners while also keeping track of their assessments and status. 

## Custom reports by date 

You can define a custom date range on lines 206 and 207.

~~~ python
#May 1st 2023 - May 1st 2024
start_date = '2023-05-01'
end_date = '2024-05-01'
~~~

The following code will generate reports based on learners invited within that time frame. 

### All Learners within a time frame

Getting all of the learners invited within a time frame can be done as follows: 
~~~ python
#get_learners_by_invite_date returns a List of learners (both active and pending) who were invited to Northstar within the above date range. 'start_date' and  'end_date' can also be replaced with dates in 'YYYY-MM-DD' format
all_learners = get_learners_by_invite_date(start_date, end_date)
print("All Learners:")
#len gets the length of a list. 
print(len(all_learners))
#this function creates a CSV named '0_example_export_all_learners.csv' using the list all_learners 
export_learners_with_assessments_to_csv(all_learners, '0_example_export_all_learners.csv')
~~~

The 'print' function prints information onto the terminal. It is very useful for quickly grabbing the numbers, and we can always double check our work by opening the 0_example_export_all_learners.csv file. 

<img width="763" alt="console showing 'All learners - 3, Active Learners -2'" src="https://github.com/mcumiskey/Northstar_Custom_Data_Collection/assets/29690717/eb952c39-3ccd-423f-95c0-83798875410b">

Getting all of the active learners is very similar. We just used the get_active_learners_by_invite_date function instead. 

~~~ python
#get_active_learners_by_invite_date returns a List of ACTIVE learners who were invited to Northstar within the above date range. 
#'start_date' and 'end_date' can also be replaced with dates in 'YYYY-MM-DD' format
active_learners = get_active_learners_by_invite_date(start_date, end_date)
print("Active Learners:")
#len gets the length of a list. 
print(len(active_learners))
#this function creates a CSV named '0_example_export_active_learners' using the list active_learners
export_learners_with_assessments_to_csv(active_learners, '0_example_export_active_learners.csv')
~~~

**There are also functions for getting learners within time frames and tags. Each function has a variation to get all learners and only get active learners.**
For example, if we wanted to get a list of learners who have the tag 'Laptop' we can add the following code: 

~~~ python
#get_active_learners_by_invite_date_and_tags returns a List of ACTIVE learners who were invited to Northstar within the date range and have specific tags.  
laptop_learners = get_active_learners_by_invite_date_and_tags(start_date, end_date, ['Laptop'])
print("Number of active learners who earned a laptop:")
print(len(laptop_learners))
export_learners_with_assessments_to_csv(laptop_learners, 'laptop_learners.csv')
~~~

We can also get lists of people with multiple tags, such as 'Laptop' and 'Digital Navigator'. This will only return learners who have BOTH of the specified tags. 

~~~ python
#We can use the get_active_learners_by_invite_date_and_tags function again, just adding more tags in the square brackets [] seperated by a comma. 
dn_laptop_learners = get_active_learners_by_invite_date_and_tags(start_date, end_date, ['Laptop', 'Digital Navigator'])
print("Earned a laptop, invited via DN:")
print(len(dn_laptop_learners))
export_learners_with_assessments_to_csv(dn_laptop_learners, 'laptop_DN.csv')
~~~

Created by Miles Cumiskey as part of a 2023-2024 Americorps VISTA Service Year.
