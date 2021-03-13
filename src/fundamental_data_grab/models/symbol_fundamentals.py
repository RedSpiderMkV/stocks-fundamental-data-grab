# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 21:45:40 2020

@author: Nikeah
"""

class SymbolFundamentals(object):
    def __init__(self, symbol_info):
        self._symbol = symbol_info["symbol"]
        self._forward_pb = -10000 if symbol_info["priceToBook"] is None else symbol_info["priceToBook"]
        self._trailing_eps = -10000 if symbol_info["trailingEps"] is None else symbol_info["trailingEps"]
        self._forward_eps = -10000 if symbol_info["forwardEps"] is None else symbol_info["forwardEps"]
        self._forward_pe = -10000 if symbol_info["forwardPE"] is None else symbol_info["forwardPE"]
        self._trailing_pe = -10000 if symbol_info["trailingPE"] is None else symbol_info["trailingPE"]
        self._peg_ratio = -10000 if symbol_info["pegRatio"] is None else symbol_info["pegRatio"]
        self._market_cap = int(symbol_info["marketCap"])
        self._short_name = symbol_info["shortName"]
        
    @property
    def symbol(self):
        return self._symbol
    
    @property
    def forward_pb(self):
        return self._forward_pb
    
    @property
    def trailing_eps(self):
        return self._trailing_eps
    
    @property
    def forward_eps(self):
        return self._forward_eps

    @property
    def forward_pe(self):
        return self._forward_pe

    @property
    def trailing_pe(self):
        return self._trailing_pe
    
    @property
    def peg_ratio(self):
        return self._peg_ratio
    
    @property
    def market_cap(self):
        return self._market_cap
    
    @property
    def shortname(self):
        return self._short_name
    
    def show(self):
        data_str = """
        Symbol: {0}
        PriceToBook: {1:.2f}
        TrailingEPS: {2:.2f}
        ForwardEPS: {3:.2f}
        TrailingPE: {4:.2f}
        ForwardPE: {5:.2f}
        PEGRatio: {6:.2f}
        MarketCap: {7:.2f} billion
        """.format(self._symbol, self._forward_pb, self._trailing_eps, self._forward_eps, 
        self._trailing_pe, self._forward_pe, self._peg_ratio, self._market_cap / 10**9)
    
        print(data_str)
        
    def to_csv(self):
        data_str = "{0},{1:.2f},{2:.2f},{3:.2f},{4:.2f},{5:.2f},{6:.2f},{7:.2f} billion,{8}".format(self._symbol, self._forward_pb, self._trailing_eps, self._forward_eps, 
        self._trailing_pe, self._forward_pe, self._peg_ratio, self._market_cap / 10**9, self._short_name)

        return data_str