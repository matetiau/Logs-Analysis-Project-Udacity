import psycopg2

DBNAME = "news"




def daysDidMoreThan1Precent():
    """On which days did more than 1% of requests lead to errors?"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select * from MoreThen1PrecentReqEqErrorsAtDay")
    posts = c.fetchall()
    db.close()
    print('Three most popular articles of all time:')
    for post in posts:
        print('- "{}" - {} views'.format(post[0], post[1]))
