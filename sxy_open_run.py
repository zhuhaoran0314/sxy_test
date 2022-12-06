from sxy_open_res import SendRequest
# 接口目录           注：进件需要更换data中的merchantNo
# 1:小微商户进件
# 2:商户修改结算卡
# 3:商户信息查询
# 4:商户修改基础信息
# 5:商户修改费率
# 6:查询商户余额
# 7:商户余额提现
# 8:个体商户对私卡进件
# 9:企业商户对公卡进件（不支持对私） ---法人不是受益人
# 10:企业商户对公卡进件（不支持对私） ---法人是受益人
# 11:文件上传


cls = SendRequest()
cls.send_request(2)