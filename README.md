## ![alt text](https://raw.githubusercontent.com/Zurek0x/SLBC-PostreSQL_BTC-Core/main/readme.data/postgresql-monitoring-.webp)
## ✅Short Length Bitcoin Core - Better Bitcoin Core✅
Short Length Bitcoin Core or *SLBC* is a clone of the Bitcoin Core that has been shortened, compressed, cutted and applied to PostgreSQL Database, Unlike the Bitcoin Core that is 400Gb that stores ***Transactions, Wallets, Wallet ID's, Blocks, Hashes, Etc*** Our database only contains the functional requirements for most public projects like ***Wallets, Wallet ID's, Wallet Balances, Etc***.

## ✅File Comparisons✅
> * **Bitcoin Core (2009 - 2023 - Uncompressed) - 400GB**
> * **Bitcoin Core Contains [:Transactions, Wallets, Wallet ID's, Transaction Blocks, Mneomic Phrases, Etc:]**
> * **PostreSQL Core (2009 - 2023 - Compressed) - 26-33GB**
> * **PostreSQL Core Contains [:Wallets, Wallet ID's, Balances:]**


## ✅Block Installation✅
We utilize what we call BLOCKS for our database, Essentially we dump the bitcoin core **400Gb** and swap out everything only for the essentials we need like ***Wallets, Wallet ID's, Wallet Balances*** Saving us over **370Gb of Data** and publish it under a specific date, We dump new BLOCKS every day or two at the link here -> **http://addresses.loyce.club/**

## ✅Support✅
* **Windows 10/11 22H1+22H2 (TESTED - OK)**
* **Debian Based Linux Distro's (Ubuntu/Lubuntu/Debnian TESTED - OK)**

## ✅SETUP✅

## ℹ️ NOTICE ℹ️
**This ISN'T a guide on how to fully setup a bitcoin database, We are just providing the necessary info to setup and start a server for beginners, For long term support you will need Basic > Advanced knowledge with Python & PostgreSQL to insure that
Your server is running well, Your database is running well and to fix issues and bugs that may occur.
If there is a minor error, Do not create a issue in our issues tab.**

## ℹ️ Install PostgreSQL ℹ️

https://github.com/Zurek0x/SLBC-PostreSQL_BTC-Core/blob/main/readme.data/185788464-b4d02e62-1069-4a29-83d4-95bb2cbc9e51.mp4

## ℹ️ Create Table ℹ️
```sql
CREATE TABLE hunter(
address VARCHAR(80) not null,
balance VARCHAR(30) not null
);
```
https://github.com/Zurek0x/SLBC-PostreSQL_BTC-Core/blob/main/readme.data/185788481-044d26ed-213e-4a86-8c8d-118395f85225.mp4


## ℹ️ Install Flask psycopg2 waitress ℹ️
```python
pip install flask
pip install psycopg2
pip install waitress
```
https://github.com/Zurek0x/SLBC-PostreSQL_BTC-Core/blob/main/readme.data/185788486-e08b1685-db89-4af1-b6a5-9267798ac20c.mp4


## ℹ️ Import and Use ℹ️

Import your list off addresses with Balance.The  first time that you try to import PostgreSQL will give you error reguarding Binary Path in the Preferences dialog. To Resolve  Correct The Binary Path pgAdmin 4  PostgreSQL 14. We need to set the bin path of the PostgreSQL installation which is not done at the time of installation. You will need to update the PATH on your PostgreSQL. 

```
C:\Program Files\PostgreSQL\15\bin
```

```bash
set FLASK_APP=app.py
set FLASK_ENV=development
flask run --host=0.0.0.0
```
https://github.com/Zurek0x/SLBC-PostreSQL_BTC-Core/blob/main/readme.data/185788493-6b38bdbd-d327-4606-926d-54c2ea898cb3.mp4

```
http://127.0.0.1:5000/balance?active=1FeexV6bAHb8ybZjqQMjJrcCrHGW9sb6uF
```

# 💡 Index Database 💡

You will Find Without indexing the Databse the Request will be slow. More Information ( https://www.tutorialspoint.com/postgresql/postgresql_indexes.htm )

## 💥Unique Indexes💥

Unique indexes are used not only for performance, but also for data integrity. A unique index does not allow any duplicate values to be inserted into the table. The basic syntax is as follows −
```sql
CREATE UNIQUE INDEX index_name
on table_name (column_name);
```
## 💥Partial Indexes💥

A partial index is an index built over a subset of a table; the subset is defined by a conditional expression (called the predicate of the partial index). The index contains entries only for those table rows that satisfy the predicate. The basic syntax is as follows −
```sql
CREATE INDEX index_name
on table_name (conditional_expression);
```


https://github.com/Zurek0x/SLBC-PostreSQL_BTC-Core/blob/main/readme.data/185800209-0e772b64-dd85-41b3-aaec-99d0952d73e6.mp4

```sql
CREATE INDEX index_hunter
ON hunter (address, balance);
```

# 🦞Usage🦞
The best way to use the PostgreSQL Index/Classes is to implement it within your code.
```python
# Python Example #
import psycopg2

# PostgreSQL Server Settings #
final_balance = 'balance'
address = 'address'
conn = psycopg2.connect(dbname="bitcoin", user='postgres',

                        password='1234', host='localhost', port=5432)
cursor = conn.cursor()
table = "hunter"

# Function to Get BTC and Return Value of Wallet #
def GetBTC(addrU):
    try:
        query = "SELECT * FROM " + table + " WHERE address = '" + addrU + "';"
        cursor.execute(query)
        try:
            res = cursor.fetchall()
            return res[0]
        except: 
            return ['0', '0']
    except:
        return -1

r = GetBTC("1FeexV6bAHb8ybZjqQMjJrcCrHGW9sb6uF")
print("whole value" + str(r))
print("address" + str(r[0]))
print("balance" + str(r[1]))
```
# ⚙️Extra Information⚙️
> * ℹ️ **The SQL Language - https://www.postgresql.org/docs/current/sql.html**
> * ℹ️ **Server Administration - https://www.postgresql.org/docs/current/admin.html**
> * ℹ️ **Server Administration - https://www.postgresql.org/docs/current/admin.html**
> * ℹ️ **Client Interfaces - https://www.postgresql.org/docs/current/client-interfaces.html**
> * ℹ️ **Server Programming - https://www.postgresql.org/docs/current/server-programming.html**
> * ℹ️ **Reference - https://www.postgresql.org/docs/current/reference.html**
> * ℹ️ **Internals - https://www.postgresql.org/docs/current/internals.html**
> * ℹ️ **Appendixes - https://www.postgresql.org/docs/current/appendixes.html**

# LICENSED WITH MIT #
