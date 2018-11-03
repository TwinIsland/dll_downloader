# -*- coding: gb2312 -*-
# code by Wyatt Huang
# 52pojie forum


import urllib.request,re,os,zipfile,time

# 程序出错的话
def wrong():
    import os,time
    time.sleep(1)
    os.system("color 47")
    time.sleep(1)
    os.system("color 07")
    print("回车即可退出")
    input()
    os._exit(0)

def fence():
    print("===========================================")

# # rmdir /s/q
# cmd = "rmdir /s/q download_zip"
# os.system(cmd)
# os.system("cls")

# 下载进度显示
def Schedule(a, b, c):
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    if per < 100:
        print('已下载：' + '%.2f%%' % per + "\r",end = '')
    else:
        print('已下载：100%')

# 下载文件
def download_file(url):
    try:
        os.system("md DLL_downloader_working_place")
        urllib.request.urlretrieve(url, "DLL_downloader_working_place\\down_dll_temp.zip", Schedule)
    except BaseException:
        os.system("del /s /q DLL_downloader_working_place")
        os.system("rd DLL_downloader_working_place")

# 抓取网页源代码
def catch(web):
    try:
        html_doc = web
        req = urllib.request.Request(html_doc)
        webpage = urllib.request.urlopen(req,timeout=10)
        html = str(webpage.read())
        return str(html)
    except BaseException:
        print("抓取错误！  请检查你的网络！")
        wrong()

# 开始
# 删除DLL下载器生产的暂时文件夹
os.system("del /s /q DLL_downloader_working_place")
os.system("rd DLL_downloader_working_place")
os.system("cls")
print("        DLL 下载器 -- By Wyatt Huang")
fence()
resource = []
inp = input("请输入DLL名称(如 qt5.dll)：")
fence()

# 规范输入格式
try:
    inp.split(".dll")[1]
except IndexError:
    inp = inp + ".dll"
str(inp)

# 抓取资源网页源码
web = 'https://cn.dll-files.com/search/?q=' + inp.split(".")[0]
html = catch(web)

# 匹配有效的DLL文件
re_c = r'<td><a href=(.{90})'
wordreg = re.compile(re_c)
_list = re.findall(wordreg, html)
for i in _list:
    dll_name = i.split('"')[1].split("/")[1].split(".html")[0]
    resource.append(dll_name)

if len(resource) == 0:
    print("未能找到DLL资源：" + inp)
    wrong()
else:
    print("\n成功！  找到以下资源：\n")

    # 分配编号
    count = 0
    for i in resource:
        count = count + 1
        if count < 10:
            print("编号：" + str(count) + "  -----> " + i + "\n")
        else:
            print("编号：" + str(count) + " -----> " + i + "\n")
fence()

while True:
    down = int(input("请输入您要下载的DLL编号："))
    fence()
    if down != abs(down) or down == 0:
        print("输入的编号范围错误,请重新输入！")
        continue
    try:
        download_dll = resource[down - 1]
        break
    except IndexError:
        print("输入的编号范围错误,请重新输入！")
        continue

# 爬取指定DLL的详情页
html_download = catch('https://cn.dll-files.com/' + download_dll + '.html')

# href="/download/
# class="bit"
# class="zip-size"
# class="description"

# 匹配DLL的信息： description 和 bit information
re_c_bit = r'class="bit"(.{10})'
re_c_des = r'<td class="description" title="(.{90})'
re_c_link = r'href="/download/(.{90})'
re_bit = re.compile(re_c_bit)
re_des = re.compile(re_c_des)
re_link = re.compile(re_c_link)
bit = re.findall(re_bit,html_download)
des = re.findall(re_des,html_download)
link = re.findall(re_link,html_download)

# 信息导入列表
bit_list = []
des_list = []
link_list = []
for i in bit:
    bit_list.append(i.split(">")[1].split("<")[0])
for i in des:
    des_list.append(i.split('"')[0])
for i in link:
    link_list.append("https://cn.dll-files.com/download/"+i.split('"')[0])

print("\n" + download_dll + " 有以下版本：")
for i in range(int(len(des_list))):
    if i < 9:
        say = "编号：" + str(i + 1) + "  -----> " + "位数支持：" + bit_list[i] + "       描述：" + des_list[i]
    else:
        say = "编号：" + str(i + 1) + " -----> " + "位数支持：" + bit_list[i] + "       描述：" + des_list[i]
    print("\n" + say)

print()
fence()
while True:
    down = int(input("请输入您要下载的位数编号："))
    if down != abs(down) or down == 0:
        print("输入的编号范围错误,请重新输入！")
        continue
    try:
        download = link_list[down - 1]
        break
    except IndexError:
        print("输入的编号范围错误,请重新输入！")
        continue
fence()

# 爬取下载地址
print("开始下载DLL: " + download_dll)
print("正在获取下载地址。。。")
html = catch(download)
print("获取成功！")
# href="https://download.dll-files.com/

# 匹配下载地址
re_down = r'https://download.dll-files.com/(.{100})'
re_down_c = re.compile(re_down)
download_link = "https://download.dll-files.com/" + re.findall(re_down_c, html)[1].split('"')[0]

try:
    # 开始下载
    download_file(download_link)

    # 解压下载的DLL文件
    f = zipfile.ZipFile("DLL_downloader_working_place\\down_dll_temp.zip", 'r')
    for file in f.namelist():
        f.extract(file, "DLL_downloader_working_place\\")
    f.close()

    # 复制临时文件的DLL到本地
    os.system('copy DLL_downloader_working_place\\*.dll .\\')
    # 删除非DLL的文件
    os.system("del /s /q DLL_downloader_working_place")
    os.system("rd DLL_downloader_working_place")
    os.system("color 27")
    time.sleep(1)
    os.system("color 07")
    # Windows\System32
    print(download_dll + " 下载成功！")
    print("回车即可退出")
    input()

except BaseException:
    print("下载失败，请手动下载\n下载链接：" + download_link)