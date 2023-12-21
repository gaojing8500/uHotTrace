import requests
from pyquery import PyQuery

from gpt import get_gpt_model_predict
from prompt import user_prompt_huggingface_summary_instruct

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8'
}
def get_datasets_type(download_link):
    return download_link.split('/')[1]

def insert_huggingface(repo_name,download_link,download_update_time,model_interprete=None):
    link = "https://huggingface.co"+download_link
    type = get_datasets_type(download_link)
    model_brief = get_model_brief_information(link,type)
    if len(model_brief)>=1:
        model_brief = get_gpt_model_predict(model_brief[0],user_prompt_huggingface_summary_instruct,model='local')
    author_or_organization = repo_name.split('/')[0]
    return {
    "模型仓库名": repo_name,
    "发布机构": author_or_organization,
    "更新时间/下载量/收藏量": download_update_time,
    "模型下载地址": link,
    "模型简要": model_brief,
    "相关解读": model_interprete
    }

def get_model_brief_information(model_link,type=None):
    r = requests.get(model_link, headers=HEADERS)
    assert r.status_code == 200
    d = PyQuery(r.content)
    text_list = []
    if type != 'datasets':
        items = d('section')
        for item in items:
            i = PyQuery(item)
            text = i.text()
            text_list.append(text)
        return text_list
    else:
        items = d('div.prose')
        for item in items:
            i = PyQuery(item)
            text = i.text()
            text_list.append(text)
        return text_list


def scrape_huggingface():
    daily_huggingface_model_data_report = []

    url = 'https://huggingface.co/'
    r = requests.get(url, headers=HEADERS)
    assert r.status_code == 200

    d = PyQuery(r.content)
    items = d('article')
    count = 0
    for item in items:
        i = PyQuery(item)
        desc = i("a.block").text().split('\n')
        if desc[0] != '':
            repo_name= desc[0]
            download_update_time = desc[1:len(desc)]
            #获取href
            download_link = i('a.block').attr('href')
            result = insert_huggingface(repo_name,download_link,download_update_time)
            daily_huggingface_model_data_report.append(result)
    return daily_huggingface_model_data_report

