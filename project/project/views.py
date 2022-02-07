#  We have created this file

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello kajal")
    # params={'name':'kajal','place':'Uttar Pradesh'}
    return render(request,'index.html')

def analyze(request):
    # Get the text
    djtext=request.POST.get('text' ,'default')
    removepunc=request.POST.get('removepunc' ,'off')
    # print(removepunc)
    capfirst=request.POST.get('capfirst' ,'off')
    newlineremover=request.POST.get('newlineremove' ,'off')
    spaceremove=request.POST.get('spaceremove' ,'off')
    charcount=request.POST.get('charcount' ,'off')

    # print(removepunc)
    # print(djtext)
    # analyzed=djtext
    if removepunc=="on":
        punctuations='''"[](),//--//::;'?&$*&#<>_--"'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char

        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)

    if capfirst=="on":
        analyzed=""
        for char in djtext:
                analyzed = analyzed+char.upper()
        params={'purpose':'Being Capitalize','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)

    if newlineremover=="on":
        analyzed=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed = analyzed+char
        params={'purpose':'Newline Remover','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)
    
    if spaceremove=="on":
        analyzed=""
        for index,char in enumerate(djtext):
            # if djtext[index]==" " and djtext[index+1]==" ":
            #     pass
            # else:
            #     analyzed = analyzed+char
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed+char
        params={'purpose':'Space Remover','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)

    if charcount=="on":
        analyzed=0
        for char in djtext:   
            analyzed +=1
        params={'purpose':'Char Counter','analyzed_text':analyzed}
        # djtext=analyzed
        # return render(request,'analyze.html',params)
    if(removepunc!="on" and capfirst!="on" and newlineremover!="on" and  spaceremove!="on" and charcount!="on"):
        return HttpResponse("Error")  
    # else:
    #     return HttpResponse("Error")
    return render(request,'analyze.html',params)

def index(request):
    return HttpResponse("<h1>Hello World</h1><a href='https://web.whatsapp.com/'>Whatsapp</a><a href='https://www.facebook.com/'>Facebook</a><a href='https://www.instagram.com/'>Instagram</a><a href ='https://www.telegram.com/'>Telegram</a><a href ='https://www.linkedin.com/'>Linkedin</a>")

'''def about(request):
    return HttpResponse("Hello kajal")

def newlineremove(request):
    return HttpResponse("newline remover")

def capitalizefirst(request):
    return HttpResponse("capitalize first<a href='/'>back</a> ")

def removepunc(request):
    # Get the text
    djtext=request.GET.get('text' ,'default')
    print(djtext)
    return HttpResponse("removepunctuation")

def endlineremove(enrequest):
    return HttpResponse("endline remover")'''