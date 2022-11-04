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