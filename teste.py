from newsdataapi import NewsDataApiClient
key = 'pub_4134944160e86b1fb06065fdfed9e21969f24'
urlNews = NewsDataApiClient(apikey=key)

noticia = urlNews.news_api(country='br',category='politics', prioritydomain='top')
a = noticia['results'][0]['title']
print(a)






