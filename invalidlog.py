import psycopg2

DBNAME = "news"

# On which days did more than 1% of requests lead to errors? #


def daysDidMoreThan1Precent():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select * from MoreThen1PrecentReqEqErrorsAtDay")
    result = c.fetchall()
    db.close()
    s = (" % errors" + "\n")
    lista = (s.join(map(str, result)))
    lista = lista.replace("(", "") \
        .replace(")", "").replace("'", "").replace('datetime.date', "") \
        .replace('Decimal', "-").replace('     ', "")
    print('Days with more than 1% of request errors:'+"\n" + lista+" % errors")
