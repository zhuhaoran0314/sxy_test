import base64
import os

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5


class HandleRsa:
    def __init__(self):
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # 公共平台公钥：验签用
        with open(os.path.join(base_path,'conf','rsa_public_key_xsgg.pem'), mode='rb') as publicfile:
            pub_key = publicfile.read()
            self.public_key = RSA.importKey(pub_key)

        # 应用私钥：用于签名
        with open(os.path.join(base_path,'conf','private.pem'), mode='rb') as privatefile:
            pri = privatefile.read()
            self.private_key = RSA.importKey(pri)

        # # 应用公钥：用于测试
        # with open(os.path.join(base_path,'conf','public_key.pem'), mode='rb') as publicfile:
        #     pub_key = publicfile.read()
        #     self.pub_key = RSA.importKey(pub_key)



    # 签名
    def rsa_sign(self, data: dict):
        data_joint_str = self.__data_joint(dict_data=data)  # 将data排序，并拼接成待签名串
        hash_value = SHA256.new(data_joint_str.encode("UTF-8"))  # 将待签名串进行哈希编码
        signer = Signature_pkcs1_v1_5.new(self.private_key)
        signature = signer.sign(hash_value)  # 签名

        return base64.b64encode(signature).decode("UTF-8")


    # 验签
    def rsa_verify(self, response: dict, signature_str: str) -> bool:
        """
        验签
        :param response: 接口返参
        :param signature_str: 签名所在字段
        :return:
        """
        sign = response[signature_str]  # 获取返参中的签名
        del response[signature_str]  # 删除返参中的签名字段
        data_joint_str = self.__data_joint(dict_data=response)  # 将data排序，并拼接成待验签串
        hash_value = SHA256.new(data_joint_str.encode())  # 将待验签串进行哈希编码
        verifier = Signature_pkcs1_v1_5.new(self.public_key)

        if verifier.verify(hash_value, base64.b64decode(sign)):
            print("验签通过！")
            return True
        else:
            print("验签失败！")
            return False

    # 排序
    def dict_sorted(self, dict_data):
        sorted_data = {}
        key_list = sorted(dict_data)
        for key in key_list:
            sorted_data.update({key: dict_data[key]})
        return sorted_data

    # 拼接成待签名串
    def __data_joint(self, dict_data: dict) -> str:
        sorted_data = self.dict_sorted(dict_data=dict_data)
        data_list = []
        key_list = sorted_data.keys()
        for key in key_list:
            data_list.append(f"{key}={sorted_data[key]}")
        return "&".join(data_list)


if __name__ == '__main__':
    cl = HandleRsa()
