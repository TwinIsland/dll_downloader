# -*- coding: gb2312 -*-
# code by Wyatt Huang
# 52pojie forum


import urllib.request,re,os,zipfile,time

# �������Ļ�
def wrong():
    import os,time
    time.sleep(1)
    os.system("color 47")
    time.sleep(1)
    os.system("color 07")
    print("�س������˳�")
    input()
    os._exit(0)

def fence():
    print("===========================================")

# # rmdir /s/q
# cmd = "rmdir /s/q download_zip"
# os.system(cmd)
# os.system("cls")

# ���ؽ�����ʾ
def Schedule(a, b, c):
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    if per < 100:
        print('�����أ�' + '%.2f%%' % per + "\r",end = '')
    else:
        print('�����أ�100%')

# �����ļ�
def download_file(url):
    try:
        os.system("md DLL_downloader_working_place")
        urllib.request.urlretrieve(url, "DLL_downloader_working_place\\down_dll_temp.zip", Schedule)
    except BaseException:
        os.system("del /s /q DLL_downloader_working_place")
        os.system("rd DLL_downloader_working_place")

# ץȡ��ҳԴ����
def catch(web):
    try:
        html_doc = web
        req = urllib.request.Request(html_doc)
        webpage = urllib.request.urlopen(req,timeout=10)
        html = str(webpage.read())
        return str(html)
    except BaseException:
        print("ץȡ����  ����������磡")
        wrong()

# ��ʼ
# ɾ��DLL��������������ʱ�ļ���
os.system("del /s /q DLL_downloader_working_place")
os.system("rd DLL_downloader_working_place")
os.system("cls")
print("        DLL ������ -- By Wyatt Huang")
fence()
resource = []
inp = input("������DLL����(�� qt5.dll)��")
fence()

# �淶�����ʽ
try:
    inp.split(".dll")[1]
except IndexError:
    inp = inp + ".dll"
str(inp)

# ץȡ��Դ��ҳԴ��
web = 'https://cn.dll-files.com/search/?q=' + inp.split(".")[0]
html = catch(web)

# ƥ����Ч��DLL�ļ�
re_c = r'<td><a href=(.{90})'
wordreg = re.compile(re_c)
_list = re.findall(wordreg, html)
for i in _list:
    dll_name = i.split('"')[1].split("/")[1].split(".html")[0]
    resource.append(dll_name)

if len(resource) == 0:
    print("δ���ҵ�DLL��Դ��" + inp)
    wrong()
else:
    print("\n�ɹ���  �ҵ�������Դ��\n")

    # ������
    count = 0
    for i in resource:
        count = count + 1
        if count < 10:
            print("��ţ�" + str(count) + "  -----> " + i + "\n")
        else:
            print("��ţ�" + str(count) + " -----> " + i + "\n")
fence()

while True:
    down = int(input("��������Ҫ���ص�DLL��ţ�"))
    fence()
    if down != abs(down) or down == 0:
        print("����ı�ŷ�Χ����,���������룡")
        continue
    try:
        download_dll = resource[down - 1]
        break
    except IndexError:
        print("����ı�ŷ�Χ����,���������룡")
        continue

# ��ȡָ��DLL������ҳ
html_download = catch('https://cn.dll-files.com/' + download_dll + '.html')

# href="/download/
# class="bit"
# class="zip-size"
# class="description"

# ƥ��DLL����Ϣ�� description �� bit information
re_c_bit = r'class="bit"(.{10})'
re_c_des = r'<td class="description" title="(.{90})'
re_c_link = r'href="/download/(.{90})'
re_bit = re.compile(re_c_bit)
re_des = re.compile(re_c_des)
re_link = re.compile(re_c_link)
bit = re.findall(re_bit,html_download)
des = re.findall(re_des,html_download)
link = re.findall(re_link,html_download)

# ��Ϣ�����б�
bit_list = []
des_list = []
link_list = []
for i in bit:
    bit_list.append(i.split(">")[1].split("<")[0])
for i in des:
    des_list.append(i.split('"')[0])
for i in link:
    link_list.append("https://cn.dll-files.com/download/"+i.split('"')[0])

print("\n" + download_dll + " �����°汾��")
for i in range(int(len(des_list))):
    if i < 9:
        say = "��ţ�" + str(i + 1) + "  -----> " + "λ��֧�֣�" + bit_list[i] + "       ������" + des_list[i]
    else:
        say = "��ţ�" + str(i + 1) + " -----> " + "λ��֧�֣�" + bit_list[i] + "       ������" + des_list[i]
    print("\n" + say)

print()
fence()
while True:
    down = int(input("��������Ҫ���ص�λ����ţ�"))
    if down != abs(down) or down == 0:
        print("����ı�ŷ�Χ����,���������룡")
        continue
    try:
        download = link_list[down - 1]
        break
    except IndexError:
        print("����ı�ŷ�Χ����,���������룡")
        continue
fence()

# ��ȡ���ص�ַ
print("��ʼ����DLL: " + download_dll)
print("���ڻ�ȡ���ص�ַ������")
html = catch(download)
print("��ȡ�ɹ���")
# href="https://download.dll-files.com/

# ƥ�����ص�ַ
re_down = r'https://download.dll-files.com/(.{100})'
re_down_c = re.compile(re_down)
download_link = "https://download.dll-files.com/" + re.findall(re_down_c, html)[1].split('"')[0]

try:
    # ��ʼ����
    download_file(download_link)

    # ��ѹ���ص�DLL�ļ�
    f = zipfile.ZipFile("DLL_downloader_working_place\\down_dll_temp.zip", 'r')
    for file in f.namelist():
        f.extract(file, "DLL_downloader_working_place\\")
    f.close()

    # ������ʱ�ļ���DLL������
    os.system('copy DLL_downloader_working_place\\*.dll .\\')
    # ɾ����DLL���ļ�
    os.system("del /s /q DLL_downloader_working_place")
    os.system("rd DLL_downloader_working_place")
    os.system("color 27")
    time.sleep(1)
    os.system("color 07")
    # Windows\System32
    print(download_dll + " ���سɹ���")
    print("�س������˳�")
    input()

except BaseException:
    print("����ʧ�ܣ����ֶ�����\n�������ӣ�" + download_link)