![alt text](https://raw.githubusercontent.com/Zurek0x/SLBC-PostreSQL_BTC-Core/main/readme.data/postgresql-monitoring-.webp)
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

# BLOCK Sources
> * **http://addresses.loyce.club/blockchair_bitcoin_addresses_and_balance_LATEST.tsv.gz - Leatest BLOCK dumped (TODAY)**
> * **http://alladdresses.loyce.club/all_Bitcoin_addresses_ever_used_sorted.txt.gz - Enitre BLOCK (2009-2023)**

# Documents on postreSQL
> * **All - https://www.postgresql.org/docs/current/index.html**
> * **Maintenance & SQL Documentation - https://www.postgresql.org/docs/current/sql.html**
> * **Server Administration - https://www.postgresql.org/docs/current/admin.html**
> * **Client Interfaces - https://www.postgresql.org/docs/current/client-interfaces.html**
> * **Server Managment - https://www.postgresql.org/docs/current/server-programming.html**
> * **Server Appendixes - https://www.postgresql.org/docs/current/appendixes.html**

```
MIT License

Copyright (c) 2022 Ezekiel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
