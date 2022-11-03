# Short Length Bitcoin Core - PostreSQL Fork;
This is a short cut version of the Bitcoin Core Database imported to the PostreSQL Datbase,
We used a cached version of the Bitcoin Core from certain Dates and import it into the PostreSQL Database
that can be called through the API.

# How We Use Short Length;
We dump all Transactions and Funded bitcoin wallets from a certain date (EX: 11/3/2022)
and dump it to a DATABASE File that we can import to our Database, By doing this we save hundreds of gigabytes
while also get recently funded and recently used bitcoin wallets that may be active.
**Service We Use >> http://alladdresses.loyce.club/daily_updates/ - Speci** 

# Auto Updated Lists;
Every day a new updated list of Bitcoin Wallet Adresses is published to loyce.club,
We are although not affiliated with them but do use there dumps under Fair Use,
There is also ALL used adresses **from 2009-Present_Day at 27-30Gb of Data**

# File Comparisons
> * **Bitcoin Core (2009 - 2023 - Uncompressed) - 400GB**
> * **Bitcoin Core Contains [:Transactions, Wallets, Wallet ID's, Transaction Blocks:]**
> * **PostreSQL Core (2009 - 2023 - Compressed) - 26-33GB**
> * **PostreSQL Core Contains [:Wallets, Wallet ID's, Balances:]**

# Database Features;
> Database Features
> * Lots of customization options
> * Better support for the Bitcoin Core
> * Lower RAM & CPU Usage
> * Lower Storage Space
> * Windows 10/11 & Debian Linux Support
>
> Database Functions
> * Bitcoin Wallet Searcher and Re-Finder (Based on Date)
> * Bitcoin Wallet Balance Searcher and Re-Finder (Based on Wallet)
> * HTTP/S Secured Connection based from LocalHost -> Port
>
> Database Updates
> * Functions to download Multiple Leatest or Previous wallet dumps
> * Functions to download Specific Dated or Previous wallet dumps
> * Auto Updating Features and Options

# How to Setup
## ℹ️ Install PostgreSQL ℹ️

https://user-images.githubusercontent.com/88630056/185788464-b4d02e62-1069-4a29-83d4-95bb2cbc9e51.mp4


## ℹ️ Create Table ℹ️
```
CREATE TABLE hunter(
address VARCHAR(80) not null,
balance VARCHAR(30) not null
);
```
https://user-images.githubusercontent.com/88630056/185788481-044d26ed-213e-4a86-8c8d-118395f85225.mp4


## ℹ️ Install Flask psycopg2 waitress ℹ️
```
pip install flask
pip install psycopg2
pip install waitress
```
https://user-images.githubusercontent.com/88630056/185788486-e08b1685-db89-4af1-b6a5-9267798ac20c.mp4


## ℹ️ Import and Use ℹ️

Import your list off addresses with Balance.The  first time that you try to import PostgreSQL will give you error reguarding Binary Path in the Preferences dialog. To Resolve  Correct The Binary Path pgAdmin 4  PostgreSQL 14. We need to set the bin path of the PostgreSQL installation which is not done at the time of installation. You will need to update the PATH on your PostgreSQL. 

```
C:\Program Files\PostgreSQL\14\bin
```

```
set FLASK_APP=app.py
set FLASK_ENV=development
flask run --host=0.0.0.0
```
https://user-images.githubusercontent.com/88630056/185788493-6b38bdbd-d327-4606-926d-54c2ea898cb3.mp4

```
http://127.0.0.1:5000/balance?active=1FeexV6bAHb8ybZjqQMjJrcCrHGW9sb6uF
```

# 💡 Index Database 💡

You will Find Without indexing the Databse the Request will be slow. More Information ( https://www.tutorialspoint.com/postgresql/postgresql_indexes.htm )

## Unique Indexes

Unique indexes are used not only for performance, but also for data integrity. A unique index does not allow any duplicate values to be inserted into the table. The basic syntax is as follows −

CREATE UNIQUE INDEX index_name
on table_name (column_name);

## Partial Indexes

A partial index is an index built over a subset of a table; the subset is defined by a conditional expression (called the predicate of the partial index). The index contains entries only for those table rows that satisfy the predicate. The basic syntax is as follows −

CREATE INDEX index_name
on table_name (conditional_expression);



https://user-images.githubusercontent.com/88630056/185800209-0e772b64-dd85-41b3-aaec-99d0952d73e6.mp4


```
CREATE INDEX index_hunter
ON hunter (address, balance);
```


# Much more to Add. Information and Programs coming Here soon... Happy Hunting

![image](https://user-images.githubusercontent.com/88630056/185788729-6b1434d5-23e2-4c2d-9a49-0995f428eb1d.png)