import time
import uuid


class HandleData:
    def __init__(self):
        pass

    def __del_null_value_keys(self, data: dict) -> dict:
        del_keys = self.__get_null_value_keys(data=data)
        for key in del_keys:
            del data[key]
        return data

    def __get_null_value_keys(self, data: dict) -> list:
        """去除请求参数中的值为空的字段"""
        del_keys = []
        for key, val in data.items():
            if val == "":
                del_keys.append(key)

        return del_keys

    def joint_pub_param(self, data: dict) -> dict:
        data["appid"] = "202213218664651111"
        data["transNonce"] = str(uuid.uuid4())
        data["transDate"] = int(time.time() * 1000)
        self.__del_null_value_keys(data=data)
        return data


if __name__ == '__main__':
    cl = HandleData()
    data = {"aaa": "1", "bbb": "yyy", "ccc": ""}
    res = cl.joint_pub_param(data)
    print(res)

