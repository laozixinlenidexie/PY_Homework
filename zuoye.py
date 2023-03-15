yuan=input("请输入明文：")
miyao=input("请输入密钥:")
#改为大写
yuan=yuan.upper()
#改为大写
miyao=miyao.upper()
yuanzhu=[]
miyaozhu=[]
mimazu=[]
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
print(str(miyaozhu),","+str(yuanzhu))
i=0
miwenString = ""
for i in range(len(yuanzhu)):
    a=i%len(miyaozhu)
    #公式
    miwen=(ord(yuanzhu[i])+ord(miyaozhu[a]))%26+65
    mimazu.append(miwen)
    miwenString += chr(miwen)
print("密文："+miwenString,mimazu)
#解密
for i in range(len(mimazu)):
    a=i%len(miyaozhu);
    #判断密文和密钥的大小决定使用什么公式
    if(mimazu[i]<ord(miyaozhu[a])):
        yuanzhu[i]=chr(mimazu[i]+65+26-ord(miyaozhu[a]));
    else:
        yuanzhu[i]=chr(mimazu[i]+65-ord(miyaozhu[a]));
print("原文："+str(yuanzhu))