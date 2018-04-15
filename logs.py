import psycopg2

DBNAME = "news"




def get_alltime():
    """What are three most popular articles of all time?"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select * from threeMostViewArticles;")
    posts = c.fetchall()
    db.close()
    print('Three most popular articles of all time:')
    for post in posts:
        print('- "{}" - {} views'.format(post[0], post[1]))


