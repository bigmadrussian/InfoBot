import json
import requests
from bs4 import BeautifulSoup


def komedia_film():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
    }

    url = "https://w.mxfilm.top/filmy/komedija/"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    articles_cards = soup.find_all("a", class_="th-in with-mask")

    kom_film = {}
    for article in articles_cards:
        article_year = article.find("div", class_="th-series").text.strip()
        article_name_film = article.find("div", class_="th-title").text.strip()
        article_desc = article.find("img").text.strip()
        article_url = f'https://w.mxfilm.top{article.get("href")}'


        article_id = article_url.split("/")[-1]
        article_id = article_id[:-4]

        kom_film[article_id] = {
            "article_year": article_year,
            "article_name_film": article_name_film,
            "article_url": article_url,
            "article_desc": article_desc,
        }

    with open("kom_film.json", "w") as file:
        json.dump(kom_film, file, indent=4, ensure_ascii=False)


def action_movie_film():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
    }

    url = "https://w.mxfilm.top/filmy/boevik/"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    articles_cards = soup.find_all("a", class_="th-in with-mask")

    action_film = {}
    for article in articles_cards:
        article_year = article.find("div", class_="th-series").text.strip()
        article_name_film = article.find("div", class_="th-title").text.strip()
        article_desc = article.find("img").text.strip()
        article_url = f'https://w.mxfilm.top{article.get("href")}'


        article_id = article_url.split("/")[-1]
        article_id = article_id[:-4]

        # print(f"{article_title} | {article_url} | {article_date_timestamp}")

        action_film[article_id] = {
            "article_year": article_year,
            "article_name_film": article_name_film,
            "article_url": article_url,
            "article_desc": article_desc,
        }

    with open("action_film.json", "w") as file:
        json.dump(action_film, file, indent=4, ensure_ascii=False)


def horror_film():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
    }

    url = "https://w.mxfilm.top/filmy/uzhasy/"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    articles_cards = soup.find_all("a", class_="th-in with-mask")

    horor_film = {}
    for article in articles_cards:
        article_year = article.find("div", class_="th-series").text.strip()
        article_name_film = article.find("div", class_="th-title").text.strip()
        article_desc = article.find("img").text.strip()
        article_url = f'https://w.mxfilm.top{article.get("href")}'


        article_id = article_url.split("/")[-1]
        article_id = article_id[:-4]

        # print(f"{article_title} | {article_url} | {article_date_timestamp}")

        horor_film[article_id] = {
            "article_year": article_year,
            "article_name_film": article_name_film,
            "article_url": article_url,
            "article_desc": article_desc,
        }

    with open("horor_film.json", "w") as file:
        json.dump(horor_film, file, indent=4, ensure_ascii=False)


def drama_film():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
    }

    url = "https://w.mxfilm.top/filmy/drama/"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    articles_cards = soup.find_all("a", class_="th-in with-mask")

    dram_film = {}
    for article in articles_cards:
        article_year = article.find("div", class_="th-series").text.strip()
        article_name_film = article.find("div", class_="th-title").text.strip()
        article_desc = article.find("img").text.strip()
        article_url = f'https://w.mxfilm.top{article.get("href")}'


        article_id = article_url.split("/")[-1]
        article_id = article_id[:-4]

        # print(f"{article_title} | {article_url} | {article_date_timestamp}")

        dram_film[article_id] = {
            "article_year": article_year,
            "article_name_film": article_name_film,
            "article_url": article_url,
            "article_desc": article_desc,
        }

    with open("dram_film.json", "w") as file:
        json.dump(dram_film, file, indent=4, ensure_ascii=False)


def thriller_film():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
    }

    url = "https://w.mxfilm.top/filmy/triller/"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    articles_cards = soup.find_all("a", class_="th-in with-mask")

    th_film = {}
    for article in articles_cards:
        article_year = article.find("div", class_="th-series").text.strip()
        article_name_film = article.find("div", class_="th-title").text.strip()
        article_desc = article.find("img").text.strip()
        article_url = f'https://w.mxfilm.top{article.get("href")}'


        article_id = article_url.split("/")[-1]
        article_id = article_id[:-4]

        # print(f"{article_title} | {article_url} | {article_date_timestamp}")

        th_film[article_id] = {
            "article_year": article_year,
            "article_name_film": article_name_film,
            "article_url": article_url,
            "article_desc": article_desc,
        }

    with open("th_film.json", "w") as file:
        json.dump(th_film, file, indent=4, ensure_ascii=False)


def fantastic_film():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
    }

    url = "https://w.mxfilm.top/filmy/fantastika/"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    articles_cards = soup.find_all("a", class_="th-in with-mask")

    fantasy_film = {}
    for article in articles_cards:
        article_year = article.find("div", class_="th-series").text.strip()
        article_name_film = article.find("div", class_="th-title").text.strip()
        article_desc = article.find("img").text.strip()
        article_url = f'https://w.mxfilm.top{article.get("href")}'


        article_id = article_url.split("/")[-1]
        article_id = article_id[:-4]

        # print(f"{article_title} | {article_url} | {article_date_timestamp}")

        fantasy_film[article_id] = {
            "article_year": article_year,
            "article_name_film": article_name_film,
            "article_url": article_url,
            "article_desc": article_desc,
        }

    with open("fantasy_film.json", "w") as file:
        json.dump(fantasy_film, file, indent=4, ensure_ascii=False)


def military_film():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
    }

    url = "https://w.mxfilm.top/filmy/voennyj/"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    articles_cards = soup.find_all("a", class_="th-in with-mask")

    mil_film = {}
    for article in articles_cards:
        article_year = article.find("div", class_="th-series").text.strip()
        article_name_film = article.find("div", class_="th-title").text.strip()
        article_desc = article.find("img").text.strip()
        article_url = f'https://w.mxfilm.top{article.get("href")}'


        article_id = article_url.split("/")[-1]
        article_id = article_id[:-4]

        # print(f"{article_title} | {article_url} | {article_date_timestamp}")

        mil_film[article_id] = {
            "article_year": article_year,
            "article_name_film": article_name_film,
            "article_url": article_url,
            "article_desc": article_desc,
        }

    with open("mil_film.json", "w") as file:
        json.dump(mil_film, file, indent=4, ensure_ascii=False)


def detectives_film():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
    }

    url = "https://w.mxfilm.top/filmy/detektiv/"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    articles_cards = soup.find_all("a", class_="th-in with-mask")

    det_film = {}
    for article in articles_cards:
        article_year = article.find("div", class_="th-series").text.strip()
        article_name_film = article.find("div", class_="th-title").text.strip()
        article_desc = article.find("img").text.strip()
        article_url = f'https://w.mxfilm.top{article.get("href")}'


        article_id = article_url.split("/")[-1]
        article_id = article_id[:-4]

        # print(f"{article_title} | {article_url} | {article_date_timestamp}")

        det_film[article_id] = {
            "article_year": article_year,
            "article_name_film": article_name_film,
            "article_url": article_url,
            "article_desc": article_desc,
        }

    with open("det_film.json", "w") as file:
        json.dump(det_film, file, indent=4, ensure_ascii=False)


def main():
    # get_first_news()
    # print(komedia_film())
    # print(action_movie_film())
    # print(horror_film())
    # print(drama_film())
    # print(thriller_film())
    # print(fantastic_film())
    # print(military_film())
    print(detectives_film())


if __name__ == '__main__':
    main()