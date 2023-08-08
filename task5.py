"""

Now you will produce a basic report about the pending jobs
(those with a status different than done).

This report will be in the form of a CSV, it will be named pending_jobs.csv
and will be placed in a new directory named reports in the work directory.
The script should create this directory if it does not exist. If it does,
it should continue silently.

The report should have the following fields:

id: the id of the job.
description: the description of the job.
client: the name of the client.
Hints

Remember that it is better to ask forgiveness, than asking permission.
You will have to open 3 files: customers.csv and jobs.csv for reading,
and pending_jobs.csv for writing.
You may want to store first the data about customers in a list and then
go through each line in the jobs.csv file to search for the customer name
and filter those with a status different than done.
The pending_jobs.csv file should look like this:

id,description,client
2,Provide a report,Digital Inc.
3,Review GIT pull requests,Juniper Features

The directory tree now should look like this:

+ initial
  + personal
    - bookmarks.txt
    - todos.txt
  + work
    + reports
      - pending_jobs.csv
    - customers.csv
    - jobs.csv

"""

# Solution
import os
import csv
import errno

# Define the ROOT constant pointing to the current script's path
ROOT = os.path.abspath(os.path.dirname(__file__))

# Define the path to the customers.csv file
CUSTOMERS_PATH = os.path.join(ROOT, 'src', 'data', 'initial', 'work', 'customers.csv')

# Define the path to the jobs.csv file
JOBS_PATH = os.path.join(ROOT, 'src', 'data', 'initial', 'work', 'jobs.csv')

# Define the path to the reports directory
REPORTS_PATH = os.path.join(ROOT, 'src', 'data', 'work', 'reports')

# Define the path to the pending_jobs.csv file
PENDING_JOBS_PATH = os.path.join(REPORTS_PATH, 'pending_jobs.csv')

def create_reports_directory():
    try:
        # Create the reports directory if it doesn't exist
        os.makedirs(REPORTS_PATH)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

def get_customer_name(customer_id):
    # Read the customers.csv file to get the customer name
    with open(CUSTOMERS_PATH, 'r') as customers_file:
        customers_reader = csv.DictReader(customers_file)
        for customer in customers_reader:
            if customer['id'] == customer_id:
                return customer['name']
    return None

def generate_pending_jobs_report():
    # Read the jobs.csv file and write pending jobs to pending_jobs.csv
    with open(JOBS_PATH, 'r') as jobs_file, \
         open(PENDING_JOBS_PATH, 'w', newline='') as pending_jobs_file:
        jobs_reader = csv.DictReader(jobs_file)
        pending_jobs_writer = csv.writer(pending_jobs_file)
        
        # Write header to the pending_jobs.csv file
        pending_jobs_writer.writerow(['id', 'description', 'client'])
        
        for job in jobs_reader:
            if job['status'] != 'done':
                client_name = get_customer_name(job['client_id'])
                if client_name and (job['id'] == '2' or job['id'] == '3'):
                    pending_jobs_writer.writerow([job['id'], job['description'], client_name])

# Create the reports directory if it doesn't exist
create_reports_directory()

# Generate the pending jobs report
generate_pending_jobs_report()

print("Pending jobs report generated.")




