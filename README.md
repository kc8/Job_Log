# Application Tracker

CLI tool to used to track application status for various jobs I have applied to. This tool uses
a Postgres database. The code is missing the connection strings to the DB so nothing 
should be returned when run

## Getting Started

You may down and create a secrets.json file inside the ./tracker directory. Within there 
you will need a json string with a databsase connection string. 
```
{
  "db_con_string" : "[YOUR-DB-CONNECTION-STRING-HERE]"
}

```
You will also need a alembic.ini file if you plan to us ethe alembic module to keep your 
database up to date. You will need to add your DB connection string inside this file as well. 
```
sqlalchemy.url = [YOUR-DB-CONNECTION-STRING-HERE]
```
A sample file can be found in the project directory called alembic_sample.ini
### Prerequisites

You will need SQLAlcemy, Click and Alembic for this project to work correctly. 

You will also need a datbase with the same tables in the ./tracker/models.py file. Please
take a look there for more info about the database. 

### Installing

You can also run setup.py to create a module but this project is meant to work as a CLI

### TO-DO

I do plan to create a standalone package for this application with a CLI interface. 

### Sample output

```
Welcome to Kyle's Job Tracker!
Please use 'help' to see a detailed list of commands
Displaying all jobs with status of applied
Company Name | Date Applied  | Resume Version | Position Applied | Status
Name | 2020-02-13 | 02022020 | Position Name | 0
Some Company | 2020-02-14 | 02022020 | Make Believe Dev at Some Company | 0


```