import requests
from lxml import etree

url="https://www.zhihu.com/question/385019055"

def get_url_name(myurl):
    ua = 'user-agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'

    header = {'user-agent':ua}
    response = requests.get(myurl,headers=header)

    selector = etree.HTML(response.text)

    answer_text = selector.xpath('//div[@class="RichContent RichContent--unescapable"]/div/span[@class="RichText ztext CopyrightRichText-richText"]')
    if len(answer_text) >= 15:
        with open('./answer.txt','w',encoding='utf-8') as fw:
            fw.writelines(answer_text)


if __name__="__main__":
    get_url_name(url)