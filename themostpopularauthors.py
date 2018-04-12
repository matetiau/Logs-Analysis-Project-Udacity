import psycopg2

DBNAME = "news"


def mostPopularAuthors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select * from theMostpopularAuthorsSumUp;")
    result = c.fetchall()
    db.close()
    s = ("views" + "\n")
    lista = (s.join(map(str, result)))
    lista = lista.replace("-", "").replace("(", "") \
                 .replace(")", "").replace(",", "") \
                 .replace("'", " ").replace("Decimal", "-")
    print("Most popular authors:" + "\n" + lista + "views")

mostPopularAuthors()

