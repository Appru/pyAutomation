# Import yfinance package
import yfinance as yf
import pandas 

# Set the start and end date
start_date = '1990-01-01'
end_date = '2024-08-1'

# Set the ticker
ticker = 'CCO'

# Get the data
data = yf.download(ticker, start_date, end_date)

# Print 5 rows
data.tail()

data.to_csv("./data/data2.csv")

print(data.tail())