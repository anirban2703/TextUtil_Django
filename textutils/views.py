#I have created this file --Anirban Ghosh

from django.http import HttpResponse
from django.shortcuts import render


# Code for urls examples

# def index(request):
#     return HttpResponse('''<h1>Github </h1> <a href="https://github.com/anirban2703">Link</a>''')


# def about(request):
#     return HttpResponse("about Anirban")



#Code for making pipeline



def index(request):

     return render(request, 'index2.html')

def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extarspaceremover = request.POST.get('extarspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    # printing the values
    # print(removepunc)
    # print(djtext)



    #check the checkboxes

    #if text is empty

    if djtext == '':
        return HttpResponse('Please Write some text')

    # for remove punctuations
    if removepunc == 'on':
        punctuations ='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
    # analyse the text
    #     return render(request, 'analyze2.html', params)

    # for fullcaps

    if fullcaps == 'on':
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()

        params = {'purpose': 'Changed to UpperCase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze2.html', params)


     # for newlineremover

    if newlineremover == 'on':
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != '\r':
                analyzed += char

        params = {'purpose': 'New line remover', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze2.html', params)

    # for extarspaceremover

    if extarspaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]== ' '):
                 analyzed += char

        params = {'purpose': 'extarspaceremover', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze2.html', params)


    # for charcount

    if charcount == 'on':
        analyzed = 0
        for char in djtext:
            if not(char == ' '):
               analyzed += 1

        params = {'purpose': 'charcount', 'analyzed_text': analyzed}

        # return render(request, 'analyze2.html', params)

    return render(request, 'analyze2.html', params)

# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("newlineremove ")
#
# def spaceremove(request):
#     return HttpResponse("spaceremove ")
#
# def cahrcount(request):
#     return HttpResponse("cahrcount ")


