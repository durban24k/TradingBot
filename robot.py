import MetaTrader5 as mt5

if not mt5.initialize():
     print("initialize() failed, error code =",mt5.last_error())
     quit()

account=123456 #this is the login
password=" " # password to be entered
authorize_login = mt5.login(account,password)
if authorize_login:
     print(mt5.account_info())
     print("Show account_info()")
     account_info_dict=mt5.account_info()._asdict()
     for prop in account_info_dict:
          print("   {}={}".format(prop,account_info_dict[prop]))
else:
     print("failed to connect at account #{}, error code: {}".format(account, mt5.last_error()))

mt5.shutdown()