from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
     return render(request,"home.html")

def About(request):
    return render(request,"About.html")     

def count(request):
    Fulltext =request.GET['Fulltext']

    wordlist = Fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #increase here
            worddictionary[word] += 1
        else:
            # Add to the worddictionary
            worddictionary[word]= 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, "count.html",{'Fulltext':Fulltext,'count':len(wordlist), 'sortedwords': sortedwords})
