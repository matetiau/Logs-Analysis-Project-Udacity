#view for three most viewed articles#
create view  threeMostViewArticles as select substring as title,views from(select substring(path ,10), count(*) as views from log where path like '_a%' group by path order by views desc limit 3) as threeMostPopularArticles;


#view for all logs desc with title#
create view  alllogsdesc as select substring as title,views from(select substring(path ,10), count(*) as views from log where path like '_a%' group by path order by views desc) as sokoko;

#view for slug and author#
create view slugandauthor as select slug, author from articles;

#view for order of views with authors id order by views#
create view theMostpopularAuthorID as  SELECT articles.author , alllogsdesc.views
FROM alllogsdesc
join articles on articles.slug = alllogsdesc.title
group by alllogsdesc.views,articles.author
order by alllogsdesc.views desc;

#view for order of views with authors name order by views#
create view theMostpopularAuthorsNames as
select theMostpopularAuthorID.views, authors.name
from theMostpopularAuthorID join authors on theMostpopularAuthorID.author = authors.id
group by theMostpopularAuthorID.views, authors.name 
order by theMostpopularAuthorID.views desc;

#view for most popular authors order by views sumed up for every author#
create view theMostpopularAuthorsSumUp as
select name, sum(views) as views from theMostpopularAuthorsNames where name = name group by  theMostpopularAuthorsNames.name order by views desc;
