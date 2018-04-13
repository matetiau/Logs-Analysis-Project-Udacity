Hello. This is program written in python 2.7 and it can extract data from database of newspaper. For running this program you need Linux VM with Vagrant and python 2.7 installed on your machine, vagrant file and newspaper database. Links for those programs and files:

https://www.virtualbox.org/wiki/Downloads
https://www.vagrantup.com/downloads.html
https://www.python.org/downloads/
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f73b_vagrantfile/vagrantfile
Put this file in new folder open command line from this folder and wirte vagrant up.
After that you can log in with vagrant ssh. After this step just cd /vagrant and use ls command you will see all files there. 
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
After downloading this file put it in directory /vagrant from step before.
For building VM after turn off just write vagrant up and log into with vagrant ssh. 
If you are logged in you can build up database with command psql -d news -f newsdata.sql.
After that access this databse with psql news command when loged into vagrant. 
All steps above are necessary for running this app. After that you complete all steps above and create views in psql news that are after this instruction. You can run Logs_Analysis_Tool.py for getting answers for three questions:
1 - What are the most popular three articles of all time? 
2 - Who are the most popular article authors of all time?
3 - On which days did more than 1% of requests lead to errors?

The views here can be create by simply copy paste them when you are logged in to vagrant ssh in /vagrant when you are in psql news. It is necessary to create those views in psql for running program to get correct answers

#view for three most viewed articles##name = threeMostViewArticles#
create view  threeMostViewArticles as select substring as title,views from(select substring(path ,10), count(*) as views from log where path like '_a%' group by path order by views desc limit 3) as threeMostPopularArticles;

#view for all logs desc with title##name = alllogsdesc#
create view  alllogsdesc as select substring as title,views from(select substring(path ,10), count(*) as views from log where path like '_a%' group by path order by views desc) as sokoko;


#view for order of views with authors id order by views##name = theMostpopularAuthorID#
create view theMostpopularAuthorID as  SELECT articles.author , alllogsdesc.views
FROM alllogsdesc
join articles on articles.slug = alllogsdesc.title
group by alllogsdesc.views,articles.author
order by alllogsdesc.views desc;

#view for order of views with authors name order by views##name = theMostpopularAuthorsNames#
create view theMostpopularAuthorsNames as
select theMostpopularAuthorID.views, authors.name
from theMostpopularAuthorID join authors on theMostpopularAuthorID.author = authors.id
group by theMostpopularAuthorID.views, authors.name 
order by theMostpopularAuthorID.views desc;

#view for most popular authors order by views sumed up for every author##name = theMostpopularAuthorsSumUp#
create view theMostpopularAuthorsSumUp as
select name, sum(views) as views from theMostpopularAuthorsNames where name = name group by  theMostpopularAuthorsNames.name order by views desc;


#view for count of all req from site for every day order by all status on each day#
create view all_statuses_log as
select DATE(time) as date,count(log.status) as all_status from log group by date order by count(log.status);

#view for count of bad req from site for every day order by all status on each day#
create view countofbadstatus as
select DATE(time) as date,count(log.status) as bad_status from log where status != '200 OK' group by date,log.status order by count(log.status);

#view for count of bad req from site for every day order by all status on each day#
create view badStatusIn_ForDay as
select all_statuses_log.date, (CAST(bad_status AS float) / CAST(all_status AS float))*100 as precent from all_statuses_log join countofbadstatus on 
all_statuses_log.date = countofbadstatus.date group by precent,all_statuses_log.date order by all_statuses_log.date;

#function in psql for finding days where error req were more then 1% of all req#
create view MoreThen1PrecentReqEqErrorsAtDay as
select TO_CHAR(badStatusIn_ForDay.date :: DATE, 'Month dd, yyyy') as date, CAST(precent AS decimal(6,2)) from badStatusIn_ForDay where precent > 1.00 group by precent,badStatusIn_ForDay.date order by badStatusIn_ForDay.date;
