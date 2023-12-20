from arxiv_daily import get_daily_paper
from github_trend import job
from huggingface_trend import scrape_huggingface


def test_get_daily_paper():
    get_daily_paper()

def test_github_trend():
    job()

def test_huggingface_trend():
    scrape_huggingface()



if __name__ == "__main__":
    print("welcome hot trace")
    test_huggingface_trend()