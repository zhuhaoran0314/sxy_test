import requests
import Yaml_util
from shouxinyi_pub.tools.fileUpload import base_str
from shouxinyi_pub.tools.handle_aes import HandleAes
from shouxinyi_pub.tools.handle_data import HandleData
from shouxinyi_pub.tools.handle_rsa import HandleRsa
from shouxinyi_pub.tools.handle_replace import HandleReaplace
yaml_data = Yaml_util.YamlUtil.read_yaml()


class SendRequest:
    def __init__(self):
        self.handle_aes = HandleAes()
        self.handle_data = HandleData()
        self.hanle_rsa = HandleRsa()
        self.handle_replace = HandleReaplace()


    def send_request(self,res_type):

        if res_type == 1:
            url = yaml_data[0]["url"]
            headers = yaml_data[0]["headers"]
            data = yaml_data[0]["data"]
            # 拼接公共参数
            data: dict = self.handle_data.joint_pub_param(data=data)
            # 签名
            sign = self.hanle_rsa.rsa_sign(data=data)
            print("签名：", sign)
            # 组装签名
            data.update({"signature": sign})
            # aes加密
            data = self.handle_replace.replace_t(data=data)
            # 发送请求
            res = requests.request(method="post", url=url, headers=headers, json=data).json()
            print("应答：", res)
            if res["message"] == '操作成功':
                print(f'商户编号：{res["merchantCode"]}')
            else:
                print(f'提示：{res["message"]}')
            # 验签
            res = self.hanle_rsa.rsa_verify(response=res, signature_str="signature")
            print(res)

        elif res_type == 2:
            url = yaml_data[1]["url"]
            headers = yaml_data[1]["headers"]
            data = yaml_data[1]["data"]
            data: dict = self.handle_data.joint_pub_param(data=data)
            sign = self.hanle_rsa.rsa_sign(data=data)
            print("签名：", sign)
            data.update({"signature": sign})
            data = self.handle_replace.settle_replace(data=data)
            res = requests.request(method="post", url=url, headers=headers, json=data).json()
            print("应答：", res)
            print(f'提示：{res["message"]}')
            res = self.hanle_rsa.rsa_verify(response=res, signature_str="signature")
            print(res)

        elif res_type == 3:
            url = yaml_data[2]["url"]
            headers = yaml_data[2]["headers"]
            data = yaml_data[2]["data"]
            data: dict = self.handle_data.joint_pub_param(data=data)
            sign = self.hanle_rsa.rsa_sign(data=data)
            print("签名：", sign)
            data.update({"signature": sign})
            res = requests.request(method="post", url=url, headers=headers, json=data).json()
            print("应答：", res)
            print(f'提示：{res["message"]}')
            res = self.hanle_rsa.rsa_verify(response=res, signature_str="signature")
            print(res)

        elif res_type == 4:
            url = yaml_data[3]["url"]
            headers = yaml_data[3]["headers"]
            data = yaml_data[3]["data"]
            data: dict = self.handle_data.joint_pub_param(data=data)
            sign = self.hanle_rsa.rsa_sign(data=data)
            print("签名：", sign)
            data.update({"signature": sign})
            res = requests.request(method="post", url=url, headers=headers, json=data).json()
            print("应答：", res)
            print(f'提示：{res["message"]}')
            res = self.hanle_rsa.rsa_verify(response=res, signature_str="signature")
            print(res)

        elif res_type == 5:
            url = yaml_data[4]["url"]
            headers = yaml_data[4]["headers"]
            data = yaml_data[4]["data"]
            data: dict = self.handle_data.joint_pub_param(data=data)
            sign = self.hanle_rsa.rsa_sign(data=data)
            print("签名：", sign)
            data.update({"signature": sign})
            res = requests.request(method="post", url=url, headers=headers, json=data).json()
            print("应答：", res)
            print(f'提示：{res["message"]}')
            res = self.hanle_rsa.rsa_verify(response=res, signature_str="signature")
            print(res)

        elif res_type == 6:
            url = yaml_data[5]["url"]
            headers = yaml_data[5]["headers"]
            data = yaml_data[5]["data"]
            data: dict = self.handle_data.joint_pub_param(data=data)
            sign = self.hanle_rsa.rsa_sign(data=data)
            print("签名：", sign)
            data.update({"signature": sign})
            res = requests.request(method="post", url=url, headers=headers, json=data).json()
            print("应答：", res)
            print(f'提示：{res["message"]}  余额:{res["balance"]}')
            res = self.hanle_rsa.rsa_verify(response=res, signature_str="signature")
            print(res)

        elif res_type == 7:
            url = yaml_data[6]["url"]
            headers = yaml_data[6]["headers"]
            data = yaml_data[6]["data"]
            data: dict = self.handle_data.joint_pub_param(data=data)
            sign = self.hanle_rsa.rsa_sign(data=data)
            print("签名：", sign)
            data.update({"signature": sign})
            res = requests.request(method="post", url=url, headers=headers, json=data).json()
            print("应答：", res)
            print(f'提示：{res["message"]}')
            res = self.hanle_rsa.rsa_verify(response=res, signature_str="signature")
            print(res)

        elif res_type == 8:
            url = yaml_data[7]["url"]
            headers = yaml_data[7]["headers"]
            data = yaml_data[7]["data"]
            data: dict = self.handle_data.joint_pub_param(data=data)
            sign = self.hanle_rsa.rsa_sign(data=data)
            print("签名：", sign)
            data.update({"signature": sign})
            data = self.handle_replace.replace_p(data=data)
            res = requests.request(method="post", url=url, headers=headers, json=data).json()
            print("应答：", res)
            if res["message"] == '操作成功':
                print(f'商户编号：{res["merchantCode"]}')
            else:
                print(f'提示：{res["message"]}')
            res = self.hanle_rsa.rsa_verify(response=res, signature_str="signature")
            print(res)

        elif res_type == 9:
            url = yaml_data[8]["url"]
            headers = yaml_data[8]["headers"]
            data = yaml_data[8]["data"]
            data: dict = self.handle_data.joint_pub_param(data=data)
            sign = self.hanle_rsa.rsa_sign(data=data)
            print("签名：", sign)
            data.update({"signature": sign})
            data = self.handle_replace.replace_ea(data=data)
            res = requests.request(method="post", url=url, headers=headers, json=data).json()
            print("应答：", res)
            if res["message"] == '操作成功':
                print(f'商户编号：{res["merchantCode"]}')
            else:
                print(f'提示：{res["message"]}')
            res = self.hanle_rsa.rsa_verify(response=res, signature_str="signature")
            print(res)

        elif res_type == 10:
            url = yaml_data[9]["url"]
            headers = yaml_data[9]["headers"]
            data = yaml_data[9]["data"]
            data: dict = self.handle_data.joint_pub_param(data=data)
            sign = self.hanle_rsa.rsa_sign(data=data)
            print("签名：", sign)
            data.update({"signature": sign})
            data = self.handle_replace.replace_eb(data=data)
            res = requests.request(method="post", url=url, headers=headers, json=data).json()
            print("应答：", res)
            if res["message"] == '操作成功':
                print(f'商户编号：{res["merchantCode"]}')
            else:
                print(f'提示：{res["message"]}')
            res = self.hanle_rsa.rsa_verify(response=res, signature_str="signature")
            print(res)

        elif res_type == 11:
            url = "https://sit-open.moneypots.cn/oapi/merchant/fileUpload"
            headers = {"Content-Type": "application/json;charset=utf-8"}
            data = {"fileName": "yyzz.jpg","base64File": base_str}
            data: dict = self.handle_data.joint_pub_param(data=data)
            sign = self.hanle_rsa.rsa_sign(data=data)
            print("签名：", sign)
            data.update({"signature": sign})
            res = requests.request(method="post", url=url, headers=headers, json=data).json()
            print("应答：", res)
            print(f'图片地址：{res["fileUrl"]}')
            res = self.hanle_rsa.rsa_verify(response=res, signature_str="signature")
            print(res)