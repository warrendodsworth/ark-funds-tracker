# setup timescaledb in docker - set pwd on first run
# docker run -d --name timescaledb -p 5432:5432 -e POSTGRES_PASSWORD=password timescale/timescaledb:latest-pg12
# docker exec -it timescaledb bash
# psql -U postgres


API_URL = 'https://paper-api.alpaca.markets'
API_KEY = 'PK4AEGUXX36HENABTA5K'
API_SECRET = 'Ba4t2RPDVEui4tms66YjuKIoKEDOxWaRNyZsc3i4'

DB_HOST = 'localhost'
DB_USER = 'postgres'
DB_PASS = 'password'
DB_NAME = 'etfdb'
