import requests as r
from .models import News,Comment,SubComment



def collect_data ():
  #first part is to collect list of all news
  list_url='https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'
  result=r.get(url=list_url)
  data=result.json()
  total_list=data

  print('starting...')
  for i in total_list:
    if not News.objects.filter(id1=i):
      news_url='https://hacker-news.firebaseio.com/v0/item/'+str(i)+'.json?print=pretty'
      news_result=r.get(url=news_url)
      news_data=news_result.json()
      #setting variables for news models
      id1=news_data.get('id')
      title=news_data.get('title')
      type1=news_data.get('type')
      url=news_data.get('url')
      by=news_data.get('by')
      api=False

      #saving news
      News.objects.create(id1=id1,title=title,type1=type1,url=url,by=by,api=api)


      #collecting all comments under news
      comments=news_data.get('kids')
      for j in comments or []:
        if j != None:
        
          comment_url='https://hacker-news.firebaseio.com/v0/item/'+str(j)+'.json?print=pretty'
          comment_result=r.get(url=comment_url)
          comment_data=comment_result.json()
          
          id2=comment_data.get('id')
          text2=comment_data.get('text')
          type2=comment_data.get('type')
          by2=comment_data.get('by')
          news=News.objects.get(id1=id1)
          kids=comment_data.get('kids')

          Comment.objects.create(id1=id2,text=text2,type1=type2,by=by2,news=news)

          #collecting subcomment
          for k in kids or []:
            if k != None:
        
              subcomment_url='https://hacker-news.firebaseio.com/v0/item/'+str(k)+'.json?print=pretty'
              subcomment_result=r.get(url=subcomment_url)
              subcomment_data=subcomment_result.json()

              id3=subcomment_data.get('id')
              text3=subcomment_data.get('text')
              type3=subcomment_data.get('type')
              by3=subcomment_data.get('by')
              comment=Comment.objects.get(id1=id2)

              SubComment.objects.create(id1=id3,text=text3,type1=type3,by=by3,comment=comment)
            else:
              pass
        else:
          pass
