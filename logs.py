import psycopg2

DBNAME = "news"

# What are the most popular three articles of all time? #


def get_alltime():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select * from threeMostViewArticles")
    posts = c.fetchall()
    db.close()
    s = (" -views" + "\n")
    lista = (s.join(map(str, posts)))
    lista = lista.replace("L", "").replace("-", " ").replace("(", "") \
        .replace(")", "").replace(",", "").replace("'", "-")
    print lista.title() + " views"


get_alltime()








