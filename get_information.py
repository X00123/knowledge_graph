import wikipedia as wiki

def get_summary(name):
    return wiki.summary(name)

def get_search(name):
    return wiki.search(name)

def get_url(name):
    return wiki.page(name).url

def get_content(name):
    return wiki.page(name).content

def get_links(name):
    return wiki.page(name).links

def output(name):


    print(get_summary(name))

    print(get_search(name))

    print(get_url(name))

    print(get_links(name))

if __name__ == "__main__":
    wiki.set_lang("en")
    name = "Science fiction"
    output(name)
