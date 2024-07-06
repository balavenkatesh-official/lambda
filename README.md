<ol>
    <li>
        <p>create iam role with&nbsp;</p>
        <pre><code class="language-php">AmazonS3FullAccess 
AmazonRDSFullAccess 
CloudWatchFullAccess</code></pre>
    </li>
    <li>create a s3 bucket</li>
    <li>create lambda function</li>
    <li>
        <p>create lambda layer</p>
        <pre><code class="language-php">mkdir -p build/python/lib/python3.8/site-packages
pip install mysql-connector -t build/python/lib/python3.8/site-packages
cd build
zip -r python.zip python</code></pre>
        <p>upload on the lambda layer and attach to the lambda function&nbsp;</p>
        <p>&nbsp;</p>
    </li>
    <li>copy and paste the code from use <strong>read-data-from-s3-to-write-rds.py</strong></li>
    <li>add the created bucket to lambda triggers</li>
    <li>
        <p>create rds database and update <strong>host, username, password, db-name</strong> on the code</p>
        <p>&nbsp;</p>
        <pre><code class="language-php">create database employeedb; 
use employeedb; 
create table employee(empid int,empname varchar(40),empaddress varchar(40)); 
select * from employee;</code></pre>
    </li>
    <li>upload the csv file and check the trigger is working</li>
    <li>finally you get the records on rds database</li>
</ol>

https://onlinehtmleditor.dev/
