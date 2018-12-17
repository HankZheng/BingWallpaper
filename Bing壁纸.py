import urllib.request
import re
import os

global_path = os.getcwd()#获取当前路径


def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36')
    page = urllib.request.urlopen(req,)
    html = page.read().decode('utf-8')
    return html

def get_img(html):
    p0 = r'<img class=".*?".*?data-progressive="(.*?.jpg)"'
    imglist0 = re.findall(p0,html)
    imglist = [x.replace('800x480','1920x1080') for x in imglist0]
    print (imglist)
    path = global_path + '\\' +'图片'
 
    try:
        os.mkdir(path)
    except FileExistsError:
        #如果该文件存在则覆盖保存
        pass
    os.chdir(path)

    # 添加header
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36')]
    urllib.request.install_opener(opener)
    
    for each in imglist:

        filename = each.split("/")[-1]      
        urllib.request.urlretrieve(each,filename,)


if __name__ == '__main__':    
    url1 = "https://bing.ioliu.cn/"
    for i in range(1,2):
        url = url1 + '?p=' + str(i)
        get_img(open_url(url))
