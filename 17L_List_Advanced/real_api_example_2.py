import requests


def BBC_news_func():

    # source, sortBy and apiKey
    query_params = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": "4dbc17e007ab436fb66416009dfb59a8"
    }
    main_url = " https://newsapi.org/v1/articles"

    # fetching data in json format
    result = requests.get(main_url, params=query_params)
    bbc_page_format = result.json()

    # getting all articles in a string article
    articles = bbc_page_format["articles"]

    # contain all trending news
    result = []

    for current_story in articles:
        result.append(current_story["title"])

    for i in range(len(result)):
        # printing all trending news
        print(i + 1 , result[i])


# Driver Code
if __name__ == 'main':
    # function call
    BBC_news_func()