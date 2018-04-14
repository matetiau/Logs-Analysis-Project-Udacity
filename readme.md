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
If you are logged in you can build up database with command "psql -d news -f newsdata.sql" in addition you have to run this command for building views "psql -d news -f views.sql".
After that access this databse with psql news command when loged into vagrant. 
All steps above are necessary for running this app. You can run Logs_Analysis_Tool.py for getting answers for three questions:
1 - What are the most popular three articles of all time? 
2 - Who are the most popular article authors of all time?
3 - On which days did more than 1% of requests lead to errors?


