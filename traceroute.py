# -*- coding:utf-8 -*-
__author__ = 'SpaceNet'
__status__ = "production"
__version__ = '1.0'
__date__    = '2017/7/13'

import time, re, sys, subprocess, os
from bs4 import BeautifulSoup
from urllib.request import *
from urllib.parse import *

proc_files = set()
ret = False

def main(url, argv):
    """
    search a link that include given string as srgv[2] from html of given url as argv[1]
    and show the network route of url by the command of traceroute (tracert for Windows)
    Returns:
        None
    """
    global ret
    if ret : return
    url = check_url(url)
    html = get_html(url)
    if html is None: return
    if url in proc_files: return
    proc_files.add(url)

    links = enum_links(html, url)
    try:
        for link_url in links:
            if ret : return
            if not re.search(r"^http", link_url): continue
            if re.search(r".css$", link_url): continue
            s = "文字列（'" + argv[2] + "'）が含まれるURLを探しています：" + link_url
            sys.stdout.write("\r\033[K%s" % s)
            sys.stdout.flush()
            time.sleep(0.1)
            if re.search(r"" + argv[2], link_url):
                print("\n------------------------------------------------")
                print("文字列（'", argv[2], "'）が出現するURLが見つかりました。")
                print(link_url)
                s_command = None
                if os.name == 'nt': s_command = "tracert " + urlparse(link_url).netloc
                else : s_command = "traceroute " + urlparse(link_url).netloc
                print("上記URLに対するネットワークの経路情報を出力します。")
                subprocess.call(s_command, shell=True)
                ret = True
                return
            if re.search(r".(html|htm)$", link_url):
                main(link_url, argv)
                continue
            proc_files.add(url)

    except FileNotFoundError:
        print("お使いのコンピューダではtracerouteコマンド又はtracertコマンドが実行できないため実行エラーとなりました。")
        print("traceroute又はtracertをインストールしてください。")
    except Exception as e:
        print(e)


def enum_links(html, base):
    """
    enumerate urls from given html
    Returns:
        url
    """
    soup = BeautifulSoup(html, "html.parser")
    links = soup.select("a[href]")
    result = []
    for a in links:
        href = a.attrs['href']
        url = urljoin(base, href)
        result.append(url)
    return result


def check_url(url):
    """
    put "index.html" at the end of url if it's a directory, ended by "/"
    Returns:
        url
    """
    if re.search(r"/$", url):
        url += "index.html"
    return url


def get_html(url):
    try:
        o = urlparse(url)
        url = o.scheme + "://" + o.netloc + quote(o.path)
        return urlopen(url).read()
    except Exception as e:
        print("\nURLの解析に失敗しました。URLが正しくありません。 : ", url)
        print(e)
        return None


if __name__ == "__main__":

    if len(sys.argv) == 3:
        s = sys.argv[1].split('/').pop() # check the string of the last directory
        if re.search(r"^$", s): pass
        elif re.search(r"\S+\.\S+$",s): pass
        else: sys.argv[1] += "/"  # if the given url don't have "/" at the end

        print("右記URLの解析を行います。：",sys.argv[1])
        main(sys.argv[1], sys.argv)

    else:
        print('コマンド引数の数が正しくありません。以下形式でURLと文字列を指定してください')
        print("$ python", sys.argv[0], "URL 文字列")
        quit()
