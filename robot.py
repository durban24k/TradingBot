import MetaTrader5 as mt5

if not mt5.initialize(login=35564619,server="MetaQuotes-Demo",password="pDn3HkjZ"):
     print("initialize() failed, error code =",mt5.last_error())
     quit()

print(mt5.terminal_info())
print(mt5.version())

mt5.shutdown()