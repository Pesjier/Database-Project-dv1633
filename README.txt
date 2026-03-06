Hello!

To run this project, please follow these steps:

1.0 - Installation
You are going to need to install:
- Flask -> https://flask.palletsprojects.com/en/stable/installation/
- MySQL connector - > https://dev.mysql.com/doc/connector-python/en/ 

2.0 - Database prep
We have two folders named "SQLScripts" and "DataGeneration" respectively.

First open the "SQLScripts" folder in Visual studio code and open the "RunAllScripts.py" file there.
Now fill in your database details and run the program to populate your database with tables and procedures etc.

Secondly, open the "DataGeneration" folder in Visual studio code and open the "inser_data.py" file.
Once again fill in your database details and run the program to fill your tables with data to use.

Optionally, you can change some parameters in the "GenerateData.py" program to get more/less data etc.

IMPORTANT - File paths are local so you MUST have working repository as the folders where the python file is.

3.0
Open the "VacationProject" folder in the base folder.
Locate the "database_connect.py" file under "VacationProject/website/database_connect.py" and fill in your database details.
Now you can run the "main.py" file and visit 127.0.0.1:5000 in your browser to view the website.