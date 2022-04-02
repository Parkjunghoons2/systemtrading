from api.Kiwoom import *
import sys

app = QApplication(sys.argv)
kiwoom = Kiwoom()

# kospi_code_list = kiwoom.get_code_list_by_market("0") # 코스피는 "0", 코스닥은 "10"
# print(kospi_code_list)
#
# for code in kospi_code_list:
#     code_name = kiwoom.get_master_code_name(code)
#     print(code, code_name)

# df = kiwoom.get_price_data('035720')
# print(df)

# deposit = kiwoom.get_deposit()

##카카오 10주를 105500에 지정가로 매수
order_result = kiwoom.send_order('send_buy_order', '1001', 1, '035720', 10, 105500, '00')
print(order_result)

app.exec_() # 항상 마지막 줄

