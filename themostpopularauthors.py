import psycopg2

DBNAME = "news"


def mostPopularAuthors():
    """Who are three most popular authors of all time?"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select * from theMostpopularAuthorsSumUp;")
    posts = c.fetchall()
    db.close()
    print('Three most popular authors of all time:')
    for post in posts:
        print('- "{}" - {} views'.format(post[0], post[1]))
