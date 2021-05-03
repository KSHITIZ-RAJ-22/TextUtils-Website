#created by Kshitiz Raj

from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def about(reuest):
    return render(reuest,'about.html')

def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charactercounter=request.POST.get('charactercounter','off')
    # This condition is used to remove puncuations
    if removepunc=='on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyze=''
        for char in djtext:
            if char not in punctuations:
                analyze=analyze+char
        params={'purpose':'Removed Punctuations','analyzed_text':analyze}
        djtext=analyze

    # This condition is used to make all the character to Upper Case
    if fullcaps=='on':
        analyze=''
        for word in djtext:
            up=word.upper()
            analyze=analyze+up
        params = {'purpose': 'Converted to Upper Case', 'analyzed_text': analyze}
        djtext=analyze

    # This condition is used to remove new line Character
    if newlineremover=='on':
        analyze=''
        for word in djtext:
            if word!='\n' and word!='\r':
                analyze=analyze+word
        params = {'purpose': 'Removed New Line Character', 'analyzed_text': analyze}
        djtext=analyze

    # This condition is used to remove extra white space
    if extraspaceremover=='on':
        analyze=''
        length=len(djtext)
        lastword=''
        for index,word in enumerate(djtext):
            lastword=word
            if index+1<length:
                if djtext[index]!=' ' and djtext[index+1]!=' ':
                    analyze=analyze+word
                elif djtext[index]!=' ' and djtext[index+1]==' ':
                    analyze=analyze+word
                elif djtext[index] == ' ' and djtext[index + 1] != ' ':
                    analyze = analyze + word
        analyze = analyze + lastword
        params = {'purpose': 'Extra Spaces Removed', 'analyzed_text': analyze}
        djtext=analyze

    # This condition is used to to count number of characters of the resultant output
    if charactercounter=='on':
        count=0
        for char in djtext:
            count=count+1
        params = {'purpose': 'Counting Characters', 'analyzed_text':djtext+'\nThe no of characters in the given text is: '+str(count)}

    # This shows error message if none of the options is choosen
    if(removepunc!='on' and fullcaps!='on' and newlineremover!='on' and extraspaceremover!='on' and charactercounter!='on'):
        return render(request,'error.html')

    return render(request, 'analyze.html', params)