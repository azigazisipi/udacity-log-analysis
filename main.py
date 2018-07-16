#!/usr/bin/env python

import psycopg2

# Create connection


def con(dbname="news"):
    try:
        db = psycopg2.connect("dbname={}".format(dbname))
        cur = db.cursor()
        return db, cur
    except:
        print("Error in connecting to database")

""""
"""" If you would like to run views from code, uncomment this part 1/3 """"
#Views


view1 = "create or replace view popular_articles as select title,count(title) \
        as views from articles, log where log.path = concat('/article/', \
        articles.slug) group by title order by views desc"

view2 = "create or replace view popular_authors as select authors.name, \
        count(articles.author) as views from articles, log, authors where \
        log.path = concat('/article/',articles.slug) and \
        articles.author = authors.id group by authors.name order by views desc"

view3 = "create or replace view error_status as select * from \
        (select time::timestamp::date as Date, round((sum(case log.status \
        when '404 NOT FOUND' then 1 else 0 end)*100.0)/count(log.status), 2) \
        as error_percent from log group by time::timestamp::date order \
        by error_percent desc) as subq where error_percent >1"
"""

# Queries
query1 = "select * from popular_articles limit 3"

query2 = "select * from popular_authors"

query3 = "select * from error_status"

"""
"""" If you would like to run views from code, uncomment this part 2/3 """"
#Create views
def view_articles():
    try:
        db, cur = con()
        cur.execute(view1)
        db.commit()
        db.close()
    except:
        print("Error in creating view popular_articles")
def view_authors():
    try:
        db, cur = con()
        cur.execute(view2)
        db.commit()
        db.close()
    except:
        print("Error in creating view popular_authors")
def view_logs():
    try:
        db, cur = con()
        cur.execute(view3)
        db.commit()
        db.close()
    except:
        print("Error in creating view error_status")

"""
# Run queries


def most_popular_articles():
    db, cur = con()
    cur.execute(query1)
    result = cur.fetchall()
    db.close()
    print "\nThe 3 most popluar Articles of all time:\n"
    for i in range(0, len(result), 1):
        print "\"" + result[i][0] + "\" - " + str(result[i][1]) + " views"


def most_popular_authors():
    db, cur = con()
    cur.execute(query2)
    result = cur.fetchall()
    db.close()
    print "\nThe most popular authors of all time:\n"
    for i in range(0, len(result), 1):
        print "\"" + result[i][0] + "\" - " + str(result[i][1]) + " views"


def error_logs():
    db, cur = con()
    cur.execute(query3)
    result = cur.fetchall()
    db.close()
    print "\nDays with more than 1% of request errors:\n"
    for i in range(0, len(result), 1):
        print str(result[i][0]) + " - "+str(round(result[i][1], 2))+"% errors"

if __name__ == '__main__':

    """
    """" If you would like to run views from code, uncomment this part 3/3 """"
    view_articles()
    view_authors()
    view_logs()
    """

    most_popular_articles()
    most_popular_authors()
    error_logs()
