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
Download the Udacity virtual machine configuration into a fresh new directory and start it from there.
Launch Vagrant VM by running `vagrant up`, you can the log in with `vagrant ssh`

To load the data, use the command `psql -d news -f newsdata.sql` to connect a database and run the necessary SQL statements.

The database includes three tables:
- Authors table
- Articles table
- Log table

### Creating views

  - The 3 most popluar Articles of all time:
  
        create view popular_articles as select title,count(title) 
        as views from articles, log where log.path = concat('/article/',
        articles.slug) group by title order by views desc;
  
  - The most popular authors of all time:        
        
        create view popular_authors as select authors.name,
        count(articles.author) as views from articles, log, authors where 
        log.path = concat('/article/',articles.slug) and 
        articles.author = authors.id group by authors.name order by views desc;
  
  - Days with more than 1% of request errors:
        
        create view error_status as select * from 
        (select time::timestamp::date as Date, round((sum(case log.status when 
        '404 NOT FOUND' then 1 else 0 end)*100.0)/count(log.status), 2) 
        as error_percent from log group by time::timestamp::date order 
        by error_percent desc) as subq where error_percent >1;
   

To execute the program, run `python main.py` from the command line.
