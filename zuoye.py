yuan=input("请输入明文：")
miyao=input("请输入密钥:")
#改为大写
yuan=yuan.upper()
#改为大写
miyao=miyao.upper()
yuanzhu=[]
miyaozhu=[]
i=0
a=0
#结果的ascii值
miwen=0
#将明文和密钥放进列表
for z in yuan:
    yuanzhu.append(z)
    i+=1
for z in miyao:
    miyaozhu.append(z)
    a+=1

# this is dele the code
# print(str(miyaozhu),","+str(yuanzhu))
# hello world
i=0
miwenString = ""
for i in range(len(yuanzhu)):
    a=i%len(miyaozhu)
    #公式
    miwen=(ord(yuanzhu[i])+ord(miyaozhu[a]))%26+65
    miwenString += chr(miwen)

print("密文："+miwenString)