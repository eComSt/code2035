import wikipedia

def get_wiki_article(article):
    wikipedia.set_lang("ru")
    try:
        return f"{wikipedia.summary(article)}"
    except:
        return f"Не удалось найти информацию по теме {article}"