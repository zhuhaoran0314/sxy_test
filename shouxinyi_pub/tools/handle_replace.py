from shouxinyi_pub.tools.handle_aes import HandleAes

class HandleReaplace:
    def __init__(self):
        self.handle_aes = HandleAes()
        # 需要进行AES加密的接口参数
        # 小微进件参数
        self.conf_t = {"legalMobile": "18595455023",
                       "legalName": "朱浩然",
                       "legalCertNo": "412723200003145537",
                       "bankCardNo": "6214832638019328",
                       "bankReserveMobile": "18595455023",
                       "bankAccountName": "朱浩然",
                       "contactName": "朱浩然",
                       "contactPhone": "16600000000"
                       }
        # 个体对私卡进件参数
        self.conf_p = {"legalMobile": "18657942291",
                       "legalName": "邢振初",
                       "legalCertNo": "330721198704217519",
                       "bankCardNo": "6224490106111743",
                       "bankReserveMobile": "18657942291",
                       "bankAccountName": "邢振初",
                       "contactName": "朱浩然",
                       "contactPhone": "16600000000"
                       }
        # 企业法人非受益人进件参数
        self.conf_ea = {"legalMobile": "18657942291",
                        "legalName": "邢振初",
                        "legalCertNo": "330721198704217519",
                        "bankCardNo": "6224490106111743",
                        "bankReserveMobile": "18657942291",
                        "bankAccountName": "邢振初",
                        "beneficiaryName": "朱浩然",
                        "beneficiaryIdCard": "4127232000031455337",
                        "beneficiaryPhone": "18595455023",
                        "contactName": "朱浩然",
                        "contactPhone": "16600000000"
                        }
        # 企业为受益人进件参数
        self.conf_eb = {"legalMobile": "18657942291",
                        "legalName": "邢振初",
                        "legalCertNo": "330721198704217519",
                        "bankCardNo": "1001294809300051977",
                        "bankReserveMobile": "18657942291",
                        "bankAccountName": "邢振初",
                        "beneficiaryName": "邢振初",
                        "beneficiaryIdCard": "330721198704217519",
                        "beneficiaryPhone": "18657942291",
                        "contactName": "朱浩然",
                        "contactPhone": "16600000000"
                        }
        # 修改结算卡接口
        self.settle_conf = {"bankCardNo": "6214832638019328",
                            "bankReserveMobile": "18595455023",
                            "bankAccountName": "朱浩然"}

    def replace_t(self,data:dict):
        for key in self.conf_t.keys():
            data[key]=self.handle_aes.aes_encode(data[key])
        return data

    def replace_p(self,data:dict):
        for key in self.conf_p.keys():
            data[key]=self.handle_aes.aes_encode(data[key])
        return data

    def replace_ea(self,data:dict):
        for key in self.conf_ea.keys():
            data[key]=self.handle_aes.aes_encode(data[key])
        return data

    def replace_eb(self,data:dict):
        for key in self.conf_eb.keys():
            data[key]=self.handle_aes.aes_encode(data[key])
        return data

    def settle_replace(self,data:dict):
        for key in self.settle_conf.keys():
            data[key]=self.handle_aes.aes_encode(data[key])
        return data

if __name__ == '__main__':
    string = "12312312"
