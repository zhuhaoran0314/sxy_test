import base64
import random

from Crypto.Cipher import AES


class HandleAes:
    """
    加密模式为:AES/ECB/PKCS7Padding
    """
    def __init__(self):
        # 秘钥，后端生成，每个服务商不一样
        self.key = "05532c893fc51d125a19ab215341f908"
        self.aes_block_size = AES.block_size

    def __pkcs7_padding(self, data,block_size=16):
        """
        AES的区块固定是128比特，也就是16字节，所以一开始要先判断明文是否小于16字节，如果小于16字节，需要补齐，为此要写一个补齐的函数。
        :data: 需要扩长度的数据
        :return: 补充长度后的数据
        """
        count = len(data.encode("utf-8"))
        add = 16 - (count % 16)
        entext = data + (chr(add) * add)
        return entext


    def aes_encode(self, data: str):
        """
        aes加密
        :param data:需要加密的数据
        :return: 加密后的数据
        """
        data = self.__pkcs7_padding(data=data)
        # 创建加密对象
        aes_obj = AES.new(key=self.key.encode("utf-8"), mode=AES.MODE_ECB)
        # 完成加密
        aes_encode = aes_obj.encrypt(data.encode("utf-8"))
        # base64编码
        aes_encode_base64 = base64.b64encode(aes_encode)
        # 将密文转化为字符串
        aes_encode_str = aes_encode_base64.decode("utf-8")

        return aes_encode_str

    def aes_decode(self, data: str):
        # 对字符串进行编码
        data_decode = data.encode("utf-8")
        # 对编码后的数据进行base64解码
        data_decode_base64 = base64.b64decode(data_decode)
        # 创建解密对象
        aes_decode_obj = AES.new(key=self.key.encode("utf-8"), mode=AES.MODE_ECB)
        # 完成解密
        aes_decode = aes_decode_obj.decrypt(data_decode_base64)
        # 去掉空格
        aes_decode = aes_decode.strip()
        # 对结果解码
        data_decode = aes_decode.decode("utf-8")

        return data_decode


if __name__ == '__main__':
    cl = HandleAes()
    # res = cl.aes_decode("yoVVfsVDStom/wqFQxVQgw==")
