import wikipedia as wiki

#基本信息
def get_summary(name):
    return wiki.summary(name)

#相关名词
def get_search(name):
    return wiki.search(name)

#搜索链接
def get_url(name):
    return wiki.page(name).url

#得到全文的信息
def get_content(name):
    return wiki.page(name).content

#相关推荐
def get_links(name):
    return wiki.page(name).links

def output(name):

    print("简介")
    print(get_summary(name))
    print("相关搜索词")
    print(get_search(name))
    print("介绍链接")
    print(get_url(name))
    # print("介绍全文")
    # print(get_content(name))
    print("相关推荐")
    print(get_links(name))

if __name__ == "__main__":
    wiki.set_lang("en")
    name = "Science fiction"
    output(name)