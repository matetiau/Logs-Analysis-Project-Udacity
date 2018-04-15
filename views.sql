/*view for three most viewed articles##name = threeMostViewArticles*/
CREATE VIEW  threeMostViewArticles AS 
 SELECT articles.title AS title, count(*) AS views 
 FROM log JOIN articles 
 ON substring(path ,10) = articles.slug 
 GROUP BY title 
 ORDER BY views DESC 
 limit 3;


/*view for all logs desc with title##name = alllogsdesc*/
CREATE VIEW alllogsdesc AS 
 SELECT * FROM  threeMostViewArticles;


/*view for order of views with authors id order by views##name = theMostpopularAuthorID*/
CREATE VIEW theMostpopularAuthorID AS 
 SELECT articles.author , alllogsdesc.views
 FROM alllogsdesc
 JOIN articles ON articles.slug = alllogsdesc.title
 GROUP BY alllogsdesc.views,articles.author
 ORDER BY alllogsdesc.views desc;

/*view for order of views with authors name order by views##name = theMostpopularAuthorsNames*/
CREATE VIEW theMostpopularAuthorsNames AS
 SELECT theMostpopularAuthorID.views, authors.name
 FROM theMostpopularAuthorID 
 JOIN authors on theMostpopularAuthorID.author = authors.id
 GROUP BY theMostpopularAuthorID.views, authors.name 
 ORDER BY theMostpopularAuthorID.views desc;


/*view for most popular authors order by views sumed up for every author##name = theMostpopularAuthorsSumUp*/
CREATE VIEW theMostpopularAuthorsSumUp AS
 SELECT name, sum(views) AS views
 FROM theMostpopularAuthorsNames 
 WHERE name = name 
 GROUP BY  theMostpopularAuthorsNames.name 
 ORDER BY views desc;


/*view for count of all req from site for every day order by all status on each day*/
create view all_statuses_log AS
 SELECT DATE(time) AS date,count(log.status) AS all_status 
 FROM log 
 GROUP BY date 
 ORDER BY count(log.status);

/*view for count of bad req from site for every day order by all status on each day*/
CREATE VIEW countofbadstatus AS
 SELECT DATE(time) AS date,count(log.status) AS bad_status 
 FROM log WHERE status != '200 OK' 
 GROUP BY date,log.status 
 ORDER BY  count(log.status);

/*view for count of bad req from site for every day order by all status on each day*/
CREATE VIEW badStatusIn_ForDay AS
 SELECT all_statuses_log.date, (CAST(bad_status AS float) / CAST(all_status AS float))*100 as precent
 FROM   all_statuses_log 
 JOIN countofbadstatus 
 ON all_statuses_log.date = countofbadstatus.date 
 GROUP BY precent,all_statuses_log.date 
 ORDER BY all_statuses_log.date;

/*view for finding days where error req were more then 1% of all req*/
CREATE VIEW MoreThen1PrecentReqEqErrorsAtDay AS
 SELECT TO_CHAR(badStatusIn_ForDay.date :: DATE, 'Month dd, yyyy') AS date, CAST(precent AS decima(6,2))
 FROM badStatusIn_ForDay  
 WHERE precent > 1.00 
 GROUP BY precent,badStatusIn_ForDay.date 
 ORDER BY badStatusIn_ForDay.date;
