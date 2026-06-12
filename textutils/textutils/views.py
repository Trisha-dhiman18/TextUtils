# " I have created this file - Trisha"
from string import punctuation

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    
    return render(request, 'index.html', )
    

def ex1(request):
    s = '''<h2>Navigation Bar<br></h2>
    <a href="https://www.facebook.com/">Facebook</a><br>
    <a href="https://www.youtube.com/">YouTube</a><br>
    <a href="https://www.instagram.com/">Instagram</a><br>
    <a href="https://www.linkedin.com/">LinkedIn</a><br>'''
    return HttpResponse(s)

def analyze(request):
    # Get the text from the request
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    extraspaceremove = request.POST.get('extraspaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')

    

    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuation', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)
    
    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    
    if newlineremove == "on":
        analyzed = ""
        for char in djtext:
            if char !='\n' and char !='\r':
                analyzed = analyzed + char
            
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if extraspaceremove == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] ==' ' and djtext[index+1] ==' '):
                analyzed = analyzed + char
        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    
    if charcount == "on":
        analyzed = 0
        for char in djtext:
            if char != ' ':
                analyzed = analyzed + 1
        params = {'purpose': 'Number of Characters', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    
    if removepunc != "on" and fullcaps != "on" and newlineremove != "on" and extraspaceremove != "on" and charcount != "on":
        return HttpResponse("Please select any operation and try again.")
    
    return render(request, 'analyze.html', params)




