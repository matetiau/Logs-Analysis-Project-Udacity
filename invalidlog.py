import psycopg2

DBNAME = "news"


def mostPopularAuthors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("")
    result = c.fetchall()
    db.close()
    s = ("%" + "\n")
    lista = (s.join(map(str, result)))
    lista = lista.replace("-", "").replace("(", "") \
                 .replace(")", "").replace(",", "") \
                 .replace("'", " ").replace("Decimal", "-")
    print(lista + "%")

mostPopularAuthors()

