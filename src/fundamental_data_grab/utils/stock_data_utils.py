# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 22:01:35 2020

@author: Nikeah
"""


import logging
import yfinance as yf
#import yahoo_fin.stock_info as si
from fundamental_data_grab.models.symbol_fundamentals import SymbolFundamentals


logging.basicConfig(level = logging.INFO)
logger = logging.getLogger("StockDataUtils")


def get_data_as_csv(symbol):
    data = get_fundamentals(symbol, 2020)
    if data is not None:
        return data.to_csv()
    return ""


def get_fundamentals(symbol, year):
    symbol_ticker = yf.Ticker(symbol)
    symbol_info = symbol_ticker.info
    
    #quote_table = si.get_quote_table(symbol)
    #return quote_table
    
    try:
        return SymbolFundamentals(symbol_info)
    except Exception as e:
        logger.error("Error processing: {0}".format(symbol))
        logger.error(e)
        return None
