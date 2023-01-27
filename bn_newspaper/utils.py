import datetime

def trim_title(title):
    ret_str = ""

    for ch in title:
        if ch == ':' or ch == 'ঃ' or ch == ',':
            return ret_str
        ret_str += ch
    return ret_str


def return_items(article, top=False, category="", language='bangla'):    
    try:
        d = article.publish_date
        d = d.strftime('%Y-%m-%d %H:%M:%S')
        dt = datetime.datetime.now() + datetime.timedelta(hours=6)
        if dt.strftime('%Y-%m-%d %H:%M:%S')  < d:
            raise Exception('Date {}  wrong parsed for url {}'.format(d, article.url))
    except Exception as e:
        print(e)


    item = {
        'url': article.url,
        'category': category,
        'title': str(article.title).strip(),
        'source_url': article.source_url,
        'top_img': article.top_img,
        'movies': article.movies,
        'content': article.text,
        'keywords': list(article.keywords),
        'tags': list(article.tags),
        'publish_date': d,
        'summary': article.summary,
    }
    return item
