import FinanceDataReader as fdr

import yfinance as yf

def __main__():
  # df = fdr.DataReader("VIX", "2023-08-12", "2024-08-12")
  # df = fdr.DataReader("VIX")
  # df = fdr.DataReader('KS11', '2020')
  # df = fdr.DataReader('S&P500')
  # df = fdr.DataReader('AAPL, TSLA, AMZN', '2020')
  # df = fdr.DataReader('KS200')
  # df = fdr.DataReader('AAPL', '2017')
  msft = yf.Ticker("VIX")
  print(msft.news)

  # print(df)
  # print("test\n\n{0}").format(df)


__main__();