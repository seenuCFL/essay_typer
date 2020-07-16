from django.shortcuts import render
from rest_framework.views import APIView
from bs4 import BeautifulSoup
from rest_framework.response import Response
from urllib.request import urlopen
from rest_framework.renderers import TemplateHTMLRenderer
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
class Home(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'magical_notepad/home.html' 

    def get(self, request):
        return Response(data = None)

class Data(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'magical_notepad/notepad.html'
    def getKeyword(self, request):
        try:
            keyword = request.POST['keyword']
        except(KeyError):
            return render(request, 'magical_notepad/home.html', {'Describe word clearly'})
        else:
            l = keyword.split(' ')
            keyword = '_'.join(l)
            return keyword
        return HttpResponseRedirect(reverse('magical_notepad:home'))

    def crawl(self, request):
        keyword = self.getKeyword(request)
        url = 'https://en.wikipedia.org/wiki/'+keyword
        html = urlopen(url)
        soup = BeautifulSoup(html, "lxml")
        p = soup.find_all('p')
        text = ""
        for i in p:
            text+=i.text
        l = text.split('. ')
        fl = []
        for i in l:
            if i == "" or i ==" " or len(i)<4:
                continue
            else:
                for j in range(0,100):
                    i = i.replace('['+str(j)+']', '')
                fl.append(i+'.')
        text = ""
        for i in fl:
            text+=i
        fl = []
        fl.append(keyword)
        fl.append(text)
        return fl

    def post(self, request):
        l = self.crawl(request)
        keyword = l[0]
        data = l[1]
        l = []
        l = keyword.split('_')
        keyword = ' '.join(l)
        return Response({'content':data, 'keyword':keyword})