# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 23:27:17 2020

@author: Nikeah
"""


import os
from fundamental_data_grab.utils.stock_data_utils import get_data_as_csv


path = r"C:\Users\Nikeah\Desktop\FundamentalDataGrab"
if not os.path.exists(path):
    os.mkdir(path)


def write_data_to_file(csv_data, filename):
    full_file_path = os.path.join(path, filename)
    with open(full_file_path, "a") as f:
        f.write("Symbol,PriceToBook,TrailingEPS,ForwardEPS,TrailingPE,ForwardPE,PEGRatio,MarketCap,ShortName\n")
        for line in csv_data:
            f.write(line + "\n")


def main():
    semiconductor_stock_symbols = ["INTC", "TXN", "IBM", "NVDA", "AMD", "AVGO", "QCOM", "QRVO", "SWKS", "XLNX"]
    tech_stock_symbols = ["SHOP", "MSFT", "GOOG", "AAPL", "AMZN", "CRM", "NFLX", "PYPL", "IBM", "CSCO", "UBER", "WORK", "ZM", "ADBE", "ORCL"]
    clean_energy_symbols = ["NEE", "CSIQ", "FSLR", "SEDG", "PLUG", "SPWR", "OPTT"]
    ev_symbols = ["TSLA", "NKLA", "GM", "F", "HMC", "TM", "NIO"]
    finance_symbols = ["JPM", "BAC", "WFC", "GS", "C", "BK", "AXP"]
    
    print("Semiconductor")
    semiconductor_csv = list(map(get_data_as_csv, semiconductor_stock_symbols))
    write_data_to_file(semiconductor_csv, "Semicoductor_Fundamentals_20201201.csv")
    
    print("Tech")
    tech_stock_csv = list(map(get_data_as_csv, tech_stock_symbols))
    write_data_to_file(tech_stock_csv, "Tech_Fundamentals_20201201.csv")
    
    print("Clean Energy")
    clean_energy_csv = list(map(get_data_as_csv, clean_energy_symbols))
    write_data_to_file(clean_energy_csv, "CleanEnergy_Fundamentals_20201201.csv")
    
    print("EV")
    ev_csv = list(map(get_data_as_csv, ev_symbols))
    write_data_to_file(ev_csv, "EV_Fundamentals_20201201.csv")
    
    print("Finance")
    finance_csv = list(map(get_data_as_csv, finance_symbols))
    write_data_to_file(finance_csv, "Finance_Fundamentals_20201201.csv")


if __name__ == "__main__":
    main()