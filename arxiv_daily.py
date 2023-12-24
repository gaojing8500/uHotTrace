#!/usr/bin/python3
# -*- coding:utf-8 -*-
# IntelligentBot
# PyCharm
# @Author:gaojing
# @Time: 2023/3/28 21:19

import os
import re
import json
import arxiv
import yaml
import logging
import argparse
import datetime
import requests
from pyquery import PyQuery

from create_markdonw import create_markdown_output
from gpt import get_gpt_model_predict
from prompt import user_prompt_arxiv_summary_instruct

logging.basicConfig(format='[%(asctime)s %(levelname)s] %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S',
                    level=logging.INFO)

base_url = "https://arxiv.paperswithcode.com/api/v0/papers/"
github_url = "https://api.github.com/search/repositories"
arxiv_url = "http://arxiv.org/"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8'
}

def load_config(config_file: str) -> dict:
    '''
    config_file: input config file path
    return: a dict of configuration
    '''

    # make filters pretty
    def pretty_filters(**config) -> dict:
        keywords = dict()
        EXCAPE = '\"'
        QUOTA = ''  # NO-USE
        OR = 'OR'  # TODO

        def parse_filters(filters: list):
            ret = ''
            for idx in range(0, len(filters)):
                filter = filters[idx]
                if len(filter.split()) > 1:
                    ret += (EXCAPE + filter + EXCAPE)
                else:
                    ret += (QUOTA + filter + QUOTA)
                if idx != len(filters) - 1:
                    ret += OR
            return ret

        for k, v in config['keywords'].items():
            keywords[k] = parse_filters(v['filters'])
        return keywords

    with open(config_file, 'r', encoding='utf-8') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
        config['kv'] = pretty_filters(**config)
        logging.info(f'config = {config}')
    return config


def get_authors(authors, first_author=False):
    output = str()
    if first_author == False:
        output = ", ".join(str(author) for author in authors)
    else:
        output = authors[0]
    return output


def sort_papers(papers):
    output = dict()
    keys = list(papers.keys())
    keys.sort(reverse=True)
    for key in keys:
        output[key] = papers[key]
    return output


import requests


def get_code_link(qword: str) -> str:
    """
    This short function was auto-generated by ChatGPT.
    I only renamed some params and added some comments.
    @param qword: query string, eg. arxiv ids and paper titles
    @return paper_code in github: string, if not found, return None
    """
    # query = f"arxiv:{arxiv_id}"
    query = f"{qword}"
    params = {
        "q": query,
        "sort": "stars",
        "order": "desc"
    }
    r = requests.get(github_url, params=params)
    results = r.json()
    code_link = None
    if results["total_count"] > 0:
        code_link = results["items"][0]["html_url"]
    return code_link


def insert_daily_paper_report(update_time, paper_title, paper_author, primary_category, paper_url,repo_url=None,comment = None):
    paper_web_info = paper_arxiv_web(paper_url)
    interpreter_paper = get_gpt_model_predict(paper_web_info,user_prompt_arxiv_summary_instruct)
    return {
        "paper_title": paper_title,
        "paper_author": paper_author,
        "primary_category": primary_category,
        "update_time": update_time,
        "paper_url": paper_url,
        "repo_url": repo_url,
        "comment": comment,
        "interprete": interpreter_paper,
        "relative_interprete": "",
    }

def get_comment(comment):
    if comment != None:
        return comment.split("Project Page: ")[1]
    return comment


def paper_arxiv_web(arxiv_url):
    r = requests.get(arxiv_url, headers=HEADERS)
    assert r.status_code == 200

    d = PyQuery(r.content)
    return d.text()


def get_daily_papers(topic, query="slam", max_results=2):
    """
    @param topic: str
    @param query: str
    @return paper_with_code: dict
    """
    # output
    content = dict()
    content_to_web = dict()
    daily_paper_report_list = []
    search_engine = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )

    for result in search_engine.results():

        paper_id = result.get_short_id()
        paper_title = result.title
        paper_url = result.entry_id
        code_url = base_url + paper_id  # TODO
        paper_abstract = result.summary.replace("\n", " ")
        paper_authors = get_authors(result.authors)
        paper_first_author = get_authors(result.authors, first_author=True)
        primary_category = result.primary_category
        publish_time = result.published.date()
        update_time = result.updated.date()
        # comments = get_comment(result.comment)

        logging.info(f"Time = {update_time} title = {paper_title} author = {paper_first_author}")

        # eg: 2108.09112v1 -> 2108.09112
        ver_pos = paper_id.find('v')
        if ver_pos == -1:
            paper_key = paper_id
        else:
            paper_key = paper_id[0:ver_pos]
        paper_url = arxiv_url + 'abs/' + paper_key

        try:
            # source code link
            r = requests.get(code_url).json()
            repo_url = None
            if "official" in r and r["official"]:
                repo_url = r["official"]["url"]

            if repo_url is not None:
                content[paper_key] = "|**{}**|**{}**|{} et.al.|[{}]({})|**[link]({})**|\n".format(
                    update_time, paper_title, paper_first_author, paper_key, paper_url, repo_url)
                content_to_web[paper_key] = "- {}, **{}**, {} et.al., Paper: [{}]({}), Code: **[{}]({})**".format(
                    update_time, paper_title, paper_first_author, paper_url, paper_url, repo_url, repo_url)
                daily_paper_report = insert_daily_paper_report(update_time, paper_title,paper_authors, primary_category, paper_url,repo_url)
                daily_paper_report_list.append(daily_paper_report)

            else:
                content[paper_key] = "|**{}**|**{}**|{} et.al.|[{}]({})|null|\n".format(
                    update_time, paper_title, paper_first_author, paper_key, paper_url)
                content_to_web[paper_key] = "- {}, **{}**, {} et.al., Paper: [{}]({})".format(
                    update_time, paper_title, paper_first_author, paper_url, paper_url)
                daily_paper_report = insert_daily_paper_report(update_time, paper_title,paper_authors, primary_category, paper_url,repo_url)
                daily_paper_report_list.append(daily_paper_report)

            # TODO: select useful comments
            comments = None
            if comments != None:
                content_to_web[paper_key] += f", {comments}\n"
            else:
                content_to_web[paper_key] += f"\n"

        except Exception as e:
            logging.error(f"exception: {e} with id: {paper_key}")

    data = {topic: content}
    data_web = {topic: content_to_web}
    return data, data_web,daily_paper_report_list


def to_markdown(daily_paper_report_list):
    filename = create_markdown_output("daily-paper","Arxiv")
    with open(filename, "w", encoding="utf-8") as f:
        for daily_paper_info in daily_paper_report_list:
            paper_title =  daily_paper_info['paper_title']
            paper_author =  daily_paper_info['paper_author']
            update_time = daily_paper_info['update_time']
            paper_url = daily_paper_info['paper_url']
            repo_url = daily_paper_info['repo_url']
            interprete = daily_paper_info['interprete']
            relative_interprete = daily_paper_info['relative_interprete']
            out = "### [{title}]({url})\n* paper_author:{paper_author}\n* update_time:{update_time}\n* repo_url:{repo_url}\n* interprete: {interprete}\n".format(
                title=paper_title, url=paper_url, paper_author=paper_author, update_time=update_time, repo_url=repo_url,interprete=interprete)
            f.write(out)

def update_paper_links(filename):
    '''
    weekly update paper links in json file
    '''

    def parse_arxiv_string(s):
        parts = s.split("|")
        date = parts[1].strip()
        title = parts[2].strip()
        authors = parts[3].strip()
        arxiv_id = parts[4].strip()
        code = parts[5].strip()
        arxiv_id = re.sub(r'v\d+', '', arxiv_id)
        return date, title, authors, arxiv_id, code

    with open(filename, "r") as f:
        content = f.read()
        if not content:
            m = {}
        else:
            m = json.loads(content)

        json_data = m.copy()

        for keywords, v in json_data.items():
            logging.info(f'keywords = {keywords}')
            for paper_id, contents in v.items():
                contents = str(contents)

                update_time, paper_title, paper_first_author, paper_url, code_url = parse_arxiv_string(contents)

                contents = "|{}|{}|{}|{}|{}|\n".format(update_time, paper_title, paper_first_author, paper_url,
                                                       code_url)
                json_data[keywords][paper_id] = str(contents)
                logging.info(f'paper_id = {paper_id}, contents = {contents}')

                valid_link = False if '|null|' in contents else True
                if valid_link:
                    continue
                try:
                    code_url = base_url + paper_id  # TODO
                    r = requests.get(code_url).json()
                    repo_url = None
                    if "official" in r and r["official"]:
                        repo_url = r["official"]["url"]
                        if repo_url is not None:
                            new_cont = contents.replace('|null|', f'|**[link]({repo_url})**|')
                            logging.info(f'ID = {paper_id}, contents = {new_cont}')
                            json_data[keywords][paper_id] = str(new_cont)

                except Exception as e:
                    logging.error(f"exception: {e} with id: {paper_id}")
        # dump to json file
        with open(filename, "w") as f:
            json.dump(json_data, f)


def update_json_file(filename, data_dict):
    '''
    daily update json file using data_dict
    '''
    with open(filename, "r") as f:
        content = f.read()
        if not content:
            m = {}
        else:
            m = json.loads(content)

    json_data = m.copy()

    # update papers in each keywords
    for data in data_dict:
        for keyword in data.keys():
            papers = data[keyword]

            if keyword in json_data.keys():
                json_data[keyword].update(papers)
            else:
                json_data[keyword] = papers

    with open(filename, "w") as f:
        json.dump(json_data, f)




def json_to_md(filename, md_filename,
               task='',
               to_web=False,
               use_title=True,
               use_tc=True,
               show_badge=True,
               use_b2t=True):
    """
    @param filename: str
    @param md_filename: str
    @return None
    """

    def pretty_math(s: str) -> str:
        ret = ''
        match = re.search(r"\$.*\$", s)
        if match == None:
            return s
        math_start, math_end = match.span()
        space_trail = space_leading = ''
        if s[:math_start][-1] != ' ' and '*' != s[:math_start][-1]: space_trail = ' '
        if s[math_end:][0] != ' ' and '*' != s[math_end:][0]: space_leading = ' '
        ret += s[:math_start]
        ret += f'{space_trail}${match.group()[1:-1].strip()}${space_leading}'
        ret += s[math_end:]
        return ret

    DateNow = datetime.date.today()
    DateNow = str(DateNow)
    DateNow = DateNow.replace('-', '.')

    with open(filename, "r") as f:
        content = f.read()
        if not content:
            data = {}
        else:
            data = json.loads(content)

    # clean README.md if daily already exist else create it
    with open(md_filename, "w+") as f:
        pass

    # write data into README.md
    with open(md_filename, "a+") as f:

        if (use_title == True) and (to_web == True):
            f.write("---\n" + "layout: default\n" + "---\n\n")

        if show_badge == True:
            f.write(f"[![Contributors][contributors-shield]][contributors-url]\n")
            f.write(f"[![Forks][forks-shield]][forks-url]\n")
            f.write(f"[![Stargazers][stars-shield]][stars-url]\n")
            f.write(f"[![Issues][issues-shield]][issues-url]\n\n")

        if use_title == True:
            # f.write(("<p align="center"><h1 align="center"><br><ins>CV-ARXIV-DAILY"
            #         "</ins><br>Automatically Update CV Papers Daily</h1></p>\n"))
            f.write("## Updated on " + DateNow + "\n")
        else:
            f.write("> Updated on " + DateNow + "\n")

        # TODO: add usage
        f.write("> Usage instructions: [here](./docs/README.md#usage)\n\n")

        # Add: table of contents
        if use_tc == True:
            f.write("<details>\n")
            f.write("  <summary>Table of Contents</summary>\n")
            f.write("  <ol>\n")
            for keyword in data.keys():
                day_content = data[keyword]
                if not day_content:
                    continue
                kw = keyword.replace(' ', '-')
                f.write(f"    <li><a href=#{kw}>{keyword}</a></li>\n")
            f.write("  </ol>\n")
            f.write("</details>\n\n")

        for keyword in data.keys():
            day_content = data[keyword]
            if not day_content:
                continue
            # the head of each part
            f.write(f"## {keyword}\n\n")

            if use_title == True:
                if to_web == False:
                    f.write("|Publish Date|Title|Authors|PDF|Code|\n" + "|---|---|---|---|---|\n")
                else:
                    f.write("| Publish Date | Title | Authors | PDF | Code |\n")
                    f.write("|:---------|:-----------------------|:---------|:------|:------|\n")

            # sort papers by date
            day_content = sort_papers(day_content)

            for _, v in day_content.items():
                if v is not None:
                    f.write(pretty_math(v))  # make latex pretty

            f.write(f"\n")

            # Add: back to top
            if use_b2t:
                top_info = f"#Updated on {DateNow}"
                top_info = top_info.replace(' ', '-').replace('.', '')
                f.write(f"<p align=right>(<a href={top_info}>back to top</a>)</p>\n\n")

        if show_badge == True:
            # we don't like long string, break it!
            f.write((f"[contributors-shield]: https://img.shields.io/github/"
                     f"contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge\n"))
            f.write((f"[contributors-url]: https://github.com/Vincentqyw/"
                     f"cv-arxiv-daily/graphs/contributors\n"))
            f.write((f"[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/"
                     f"cv-arxiv-daily.svg?style=for-the-badge\n"))
            f.write((f"[forks-url]: https://github.com/Vincentqyw/"
                     f"cv-arxiv-daily/network/members\n"))
            f.write((f"[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/"
                     f"cv-arxiv-daily.svg?style=for-the-badge\n"))
            f.write((f"[stars-url]: https://github.com/Vincentqyw/"
                     f"cv-arxiv-daily/stargazers\n"))
            f.write((f"[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/"
                     f"cv-arxiv-daily.svg?style=for-the-badge\n"))
            f.write((f"[issues-url]: https://github.com/Vincentqyw/"
                     f"cv-arxiv-daily/issues\n\n"))

    logging.info(f"{task} finished")


def get_daily_paper():
    # TODO: use config
    config = load_config("config.yaml")
    data_collector = []
    data_collector_web = []

    keywords = config['kv']
    max_results = config['max_results']
    publish_readme = config['publish_readme']
    show_badge = config['show_badge']

    b_update = config['update_paper_links']
    logging.info(f'Update Paper Link = {b_update}')
    if config['update_paper_links'] == False:
        logging.info(f"GET daily papers begin")
        for topic, keyword in keywords.items():
            logging.info(f"Keyword: {topic}")
            data, data_web,daily_paper_report_list = get_daily_papers(topic, query=keyword,
                                              max_results=max_results)
            data_collector.append(data)
            data_collector_web.append(data_web)
            print("\n")
        logging.info(f"GET daily papers end")

    to_markdown(daily_paper_report_list)

    # # 1. update README.md file
    # if publish_readme:
    #     json_file = config['json_readme_path']
    #     md_file = config['md_readme_path']
    #     # update paper links
    #     if config['update_paper_links']:
    #         update_paper_links(json_file)
    #     else:
    #         # update json data
    #         update_json_file(json_file, data_collector)
    #     # json data to markdowns
    #     json_to_md(json_file, md_file, task='Update Readme', \
    #                show_badge=show_badge)

