from django.shortcuts import render
from app.word_cloud import *
from django.views.decorators.csrf import *

def openmap(request):
	datastr=''
	with open('app/Essay.txt', 'r') as data:
		for x in data:
			datastr=datastr+x
	datalt=datastr.split()
	count=0
	lt=[]
	for x in list(set(datalt)):
		for y in datalt:
			if x.lower()==y.lower():
				count=count+1
		freq={'letter':x,'count':count}
		lt.append(freq)
		count=0
	dic={'cloud':generate_wordcloud(datastr),'analytics':lt,'count':len(datalt)}
	return render(request,'index.html',dic)

@csrf_exempt
def generatecloud(request):
	if request.method=='POST':
		datastr=request.POST.get('text')
		datalt=datastr.split()
		count=0
		lt=[]
		for x in list(set(datalt)):
			for y in datalt:
				if x.lower()==y.lower():
					count=count+1
			freq={'letter':x,'count':count}
			lt.append(freq)
			count=0
		dic={'cloud':generate_wordcloud(datastr),'analytics':lt,'count':len(datalt)}
		return render(request,'index.html',dic)