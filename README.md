# lambda

1. create iam role with
   AmazonS3FullAccess
   AmazonRDSFullAccess
   CloudWatchFullAccess

2. create a s3 bucket
   
3. create lambda function
   
5. copy and paste the code from use read-data-from-s3-to-write-rds.py

6. add the created bucket to lambda triggers

7. create rds database and update host,username,password,db-name on the code

   create database employeedb;
   use employeedb;
   create table employee(empid int,empname varchar(40),empaddress varchar(40));
   select * from employee;
   
9. upload the csv file and check the trigger is working

10. finally you get the records on rds database
   
