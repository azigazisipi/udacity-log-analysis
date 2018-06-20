# Logs Analysis

Udacity Log Analysis Project

## About

This is the solution for the Logs Analysis project in Udacity Full Stack Nanodegree course.
In this, we have to execute complex queries on a large database to extract required stats.

## To Run

### Prerequisites:
- Python3
- Vagrant
- VirtualBox

### Setup
1. Install Vagrant And VirtualBox
2. Clone this repository

### To Run

Download `newsdata.sql` from Udacity course page.

Launch Vagrant VM by running `vagrant up`, you can the log in with `vagrant ssh`

To load the data, use the command `psql -d news -f newsdata.sql` to connect a database and run the necessary SQL statements.

The database includes three tables:
- Authors table
- Articles table
- Log table

To execute the program, run `python main.py` from the command line.
