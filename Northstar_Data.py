import pandas as pd

class Learner:
    def __init__(self, learner_id, name, email, invite_date, status, location, tags):
        self.learner_id = learner_id
        self.name = name
        self.email = email
        self.invite_date = invite_date[0:10]
        self.status = status
        self.location = location
        self.tags = tags
        self.assessments = {}
         # Initialize variable to track number of assessments passed with proctor
        self.passed_with_proctor = 0

    def add_assessment(self, assessment):
        self.assessments[assessment.topic] = assessment
        if assessment.topic in [
            'Basic Computer Skills',
            'Internet Basics',
            'Using Email',
            'Windows',
            'Mac OS',
            'Your Digital Footprint'
        ] and assessment.proctored == 'Y' and assessment.passed == 'Y':
            self.passed_with_proctor += 1

    def __str__(self):
        return f"Learner ID: {self.learner_id}, Name: {self.name}, Email: {self.email}, Status: {self.status}, Location: {self.location}, Tags: {self.tags}, Assessments: {self.assessments}"


class Assessment:
    def __init__(self, topic, start_date, duration, passed, proctored):
        self.topic = topic
        self.start_date = start_date[0:10]
        self.duration = duration
        self.passed = passed
        self.proctored = proctored
    
    def __str__(self):
        return f"{self.topic}, Start Date: {self.start_date}, Duration: {self.duration}, Passed: {self.passed}, Proctored: {self.proctored}"

# Read learners data from Excel file
learners_df = pd.read_excel('time-on-task-11686-all-time.xlsx', 'Drexel University (Summary)')

# Create a dictionary to store learners by their names
learners_dict = {name: Learner(learner_id, name, email, invite_date, status, location, tags) 
                 for learner_id, name, email, invite_date, status, location, tags 
                 in zip(learners_df['Learner ID'], learners_df['Learner Name'], learners_df['Learner Email'], 
                        learners_df['Learner Invite Date'], learners_df['Learner Status'], 
                        learners_df['Northstar Location'], learners_df['Tags'])}

# Read assessments data from CSV file
assessments_df = pd.read_csv('assessments.csv')

# Iterate over assessments and add them to the respective learners
for index, row in assessments_df.iterrows():
    name = row['User Name']
    if name in learners_dict:
        learner = learners_dict[name]
        assessment = Assessment(row['Topic'], row['Start'], row['Duration (h:mm:ss)'], row['Passed'], row['Proctored'])
        learner.add_assessment(assessment)

# Create a list to store learner details
learner_details = []

# Iterate over learners
for learner in learners_dict.values():
    # Convert assessments to a comma-separated list
    assessments_str = ', '.join([str(assessment) for assessment in learner.assessments])
    #make learner
    learner_info = {
        'Learner ID': learner.learner_id,
        'Learner Name': learner.name,
        'Learner Email': learner.email,
        'Invite Date': learner.invite_date,
        'Status': learner.status,
        'Requirements Passed': learner.passed_with_proctor,
        'Tags': learner.tags,
        'Assessments': assessments_str
    }
    # Append learner info to learner_details list
    learner_details.append(learner_info)

# Convert the list of dictionaries into a DataFrame
df = pd.DataFrame(learner_details)

# Export the DataFrame to a CSV file
df.to_csv('0_example_export_learner_details_with_assessments.csv', index = False)

def get_learners_by_invite_date(start_date, end_date):
    """
    Retrieve active learners who have been invited within a specific time frame.

    Args:
    - start_date (str): Start date of the time frame in 'yyyy-mm-dd' format.
    - end_date (str): End date of the time frame in 'yyyy-mm-dd' format.

    Returns:
    - list: List of active learners invited within the specified time frame.
    """
    all_learners = [learner for learner in learners_dict.values() if isinstance(learner.tags, str) and "Staff" not in learner.tags]
    return [learner for learner in all_learners if start_date <= learner.invite_date <= end_date]

def get_learners_by_invite_date_and_tags(start_date, end_date, tags=[]):
    """
    Retrieve active learners who have been invited within a specific time frame and have specific tags.

    Args:
    - start_date (str): Start date of the time frame in 'yyyy-mm-dd' format.
    - end_date (str): End date of the time frame in 'yyyy-mm-dd' format.
    - tags (list): List of tags to filter learners. Learners must have all of these tags.

    Returns:
    - list: List of active learners invited within the specified time frame and having specific tags.
    """
    active_learners = get_learners_by_invite_date(start_date, end_date)
    return [learner for learner in active_learners if all(tag in learner.tags.split(', ') for tag in tags)]

def get_active_learners_by_invite_date_and_tags_excluding_tags(start_date, end_date, tags=[], exclude_tags=[]):
    """
    Retrieve active learners who have been invited within a specific time frame, have specific tags, and exclude specific tags.

    Args:
    - start_date (str): Start date of the time frame in 'yyyy-mm-dd' format.
    - end_date (str): End date of the time frame in 'yyyy-mm-dd' format.
    - tags (list): List of tags to filter learners. Learners must have at least one of these tags.
    - exclude_tags (list): List of tags to exclude. Learners with any of these tags will not be included in the result.

    Returns:
    - list: List of active learners invited within the specified time frame, having specific tags, and excluding specific tags.
    """
    active_learners = get_learners_by_invite_date(start_date, end_date)
    return [learner for learner in active_learners if all(tag in learner.tags.split(', ') for tag in tags) and not any(tag in learner.tags.split(', ') for tag in exclude_tags)]

def get_active_learners_by_invite_date(start_date, end_date):
    """
    Retrieve active learners who have been invited within a specific time frame.

    Args:
    - start_date (str): Start date of the time frame in 'yyyy-mm-dd' format.
    - end_date (str): End date of the time frame in 'yyyy-mm-dd' format.

    Returns:
    - list: List of active learners invited within the specified time frame.
    """
    active_learners = [learner for learner in learners_dict.values() if learner.status == "active" and "Staff" not in learner.tags]
    return [learner for learner in active_learners if start_date <= learner.invite_date <= end_date]

def get_active_learners_by_invite_date_and_tags(start_date, end_date, tags=[]):
    """
    Retrieve active learners who have been invited within a specific time frame and have specific tags.

    Args:
    - start_date (str): Start date of the time frame in 'yyyy-mm-dd' format.
    - end_date (str): End date of the time frame in 'yyyy-mm-dd' format.
    - tags (list): List of tags to filter learners. Learners must have all of these tags.

    Returns:
    - list: List of active learners invited within the specified time frame and having specific tags.
    """
    active_learners = get_active_learners_by_invite_date(start_date, end_date)
    return [learner for learner in active_learners if all(tag in learner.tags.split(', ') for tag in tags)]

def get_active_learners_by_invite_date_and_tags_excluding_tags(start_date, end_date, tags=[], exclude_tags=[]):
    """
    Retrieve active learners who have been invited within a specific time frame, have specific tags, and exclude specific tags.

    Args:
    - start_date (str): Start date of the time frame in 'yyyy-mm-dd' format.
    - end_date (str): End date of the time frame in 'yyyy-mm-dd' format.
    - tags (list): List of tags to filter learners. Learners must have all of these tags.
    - exclude_tags (list): List of tags to exclude. Learners with any of these tags will not be included in the result.

    Returns:
    - list: List of active learners invited within the specified time frame, having specific tags, and excluding specific tags.
    """
    active_learners = get_active_learners_by_invite_date(start_date, end_date)
    return [learner for learner in active_learners if all(tag in learner.tags.split(', ') for tag in tags) and not any(tag in learner.tags.split(', ') for tag in exclude_tags)]

def export_learners_with_assessments_to_csv(learners, filename):
    """
    Export list of learners with assessments to a nicely formatted CSV file using pandas.

    Args:
    - learners (list): List of learner objects.
    - filename (str): Name of the CSV file to be exported.
    """
    learner_details = []
    for learner in learners:
        assessments_str = ', '.join([str(assessment) for assessment in learner.assessments.values()])
        learner_info = {
            'Learner ID': learner.learner_id,
            'Learner Name': learner.name,
            'Learner Email': learner.email,
            'Invite Date': learner.invite_date,
            'Status': learner.status,
            'Tags': learner.tags,
            'Assessments': assessments_str
        }
        learner_details.append(learner_info)

    df = pd.DataFrame(learner_details)
    df.to_csv(filename, index=False)

# Example usage:
start_date = '2023-05-01'
end_date = '2024-05-01'

counter = 0
all_learners = get_learners_by_invite_date(start_date, end_date)
print("All Learners:")
for learner in all_learners:
    counter+=1
print(counter)
export_learners_with_assessments_to_csv(all_learners, '0_example_export_all_learners.csv')

counter = 0
active_learners = get_active_learners_by_invite_date(start_date, end_date)
print("Active Learners:")
for learner in active_learners:
    counter+=1
print(counter)
export_learners_with_assessments_to_csv(active_learners, '0_example_export_active_learners.csv')

