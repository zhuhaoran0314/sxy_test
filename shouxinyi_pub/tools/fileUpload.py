import base64

# 图片转换成base64
def image_to_base64(path):
    with open(path, 'rb') as img:
        # 使用base64进行编码
        b64encode = base64.b64encode(img.read())
        b64_encode = b64encode.decode()

        # 返回base64编码字符串
        return b64_encode

# path = r"C:\Users\DELL\Desktop\测试文件\朱浩然证件照\竹段营业执照.jpg"
# path = r"C:\Users\DELL\Desktop\测试文件\朱浩然证件照\朱浩然身份证正面.jpg"
# path = r"C:\Users\DELL\Desktop\测试文件\朱浩然证件照\朱浩然身份证反面.jpg"
path = r"C:\Users\DELL\Desktop\测试文件\朱浩然证件照\朱浩然招商卡.jpg"
# path = r"C:\Users\DELL\Desktop\测试文件\朱浩然证件照\朱浩然手持身份证.jpg"
# path = r"C:\Users\DELL\Desktop\测试文件\朱浩然证件照\邢振初建设对私卡.png"
# path = r"C:\Users\DELL\Desktop\测试文件\朱浩然证件照\邢振初身份证照片反面.jpg"
# path = r"C:\Users\DELL\Desktop\测试文件\朱浩然证件照\邢振初身份证照片正面.jpg"
base_str = image_to_base64(path)

