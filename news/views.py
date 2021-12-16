from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse
from .tasks import collect_data
from rest_framework.generics import ListCreateAPIView, ListAPIView,RetrieveUpdateDestroyAPIView
from .models import News,Comment
from .serializers import NewsSerializer
from django.core.paginator import Paginator,EmptyPage


# Create your views here.

def home(request):
  return render(request,'home.html')

def bot(request):
  collect_data()
  return HttpResponse('bot works')


class NewsListFiltered(ListAPIView):

    serializer_class=NewsSerializer
    queryset=News.objects.all()

    def get_queryset(self):
        title = self.kwargs['title']
        return News.objects.filter(title__icontains=title)

class NewsList(ListCreateAPIView):

    serializer_class=NewsSerializer
    queryset=News.objects.all()

    

class NewsDetail(RetrieveUpdateDestroyAPIView):

    serializer_class=NewsSerializer
    queryset=News.objects.all()
    lookup_fields='id1'


    def perform_update(self, serializer):
      instance = self.get_object()
      go=instance.api
      if go!=True:
        pass
      
      else:
        serializer.save()
        return Response('Instance updated')


    def perform_destroy(self, instance):
      go=instance.api


      if go!=True:
        pass
      
      else:
        instance.delete()
        return Response('Instance Deleted')


def NewsListView(request, page=1):
    

    if request.POST:
      search=request.POST.get('search')
      dataset = News.objects.filter(title__icontains=search)
      paginator = Paginator(dataset, 10)
      try:
          data = paginator.page(page)
      except EmptyPage:
          # if we exceed the page limit we return the last page 
          data = paginator.page(paginator.num_pages)
      context = {
              'dataset':data
          }
      return render(request,'list.html',context)
    else: 
      dataset = News.objects.all()
      paginator = Paginator(dataset, 10)
      try:
          data = paginator.page(page)
      except EmptyPage:
          # if we exceed the page limit we return the last page 
          data = paginator.page(paginator.num_pages)
      context = {
              'dataset':data
          }
      return render(request,'list.html',context)
       

      

def NewsDetailView(request,_id):
    
    data =News.objects.get(id1 =_id)
    comments = Comment.objects.filter(news = data)
    


    context = {
            'data':data,
            'comments':comments
        }
    return render(request,'detail.html',context)