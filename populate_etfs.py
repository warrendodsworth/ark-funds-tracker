import config
import csv
import psycopg2
import psycopg2.extras

# update stock set is_etf=TRUE where symbol in ('ARKK', 'ARKQ', 'PRNT', 'IZRL', 'ARKG', 'ARKF', 'ARKW')

connection = psycopg2.connect(
    host=config.DB_HOST, database=config.DB_NAME, user=config.DB_USER, password=config.DB_PASS)

cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

cursor.execute("select * from stock where is_etf = TRUE")

etfs = cursor.fetchall()

print('Hi there', etfs)

dates = ['2021-01-25', '2021-01-26']

for current_date in dates:
    for etf in etfs:
        print(etf['symbol'])

        with open(f"data/{current_date}/{etf['symbol']}.csv") as f:
            reader = csv.reader(f)
            next(reader)  # skip csv headers row
            for row in reader:
                ticker = row[3]

                if ticker:  # check for rows that have a symbol
                    shares = row[5]
                try:
                    weight = row[7]
                except Exception as e:
                    print(row)

                cursor.execute("""
                        SELECT * FROM stock WHERE symbol = %s
                    """, (ticker,))
                stock = cursor.fetchone()
                if stock:
                    cursor.execute("""
                            INSERT INTO etf_holding (etf_id, holding_id, dt, shares, weight)
                            VALUES (%s, %s, %s, %s, %s)
                        """, (etf['id'], stock['id'], current_date, shares, weight))

connection.commit()
