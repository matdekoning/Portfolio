from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from home.forms import TwitterForm
from django import forms
from textblob import TextBlob


import sys, tweepy


def index(request):
    consumerKey = "TqxgSFD1oZ6jJAfN2Ga637ALR"
    consumerSecret = "C4M8LudufIIwMP3p3imZR0rmzK7iv1hrgzSPaHGRXOfB7sGAb3"
    accessToken = "2373876566-xq0McaA1p6FVCd0Um55R0zOqUxDOARJGfIkGB5L"
    accessTokenSecret = "RfyYMEfecGgLjtqtlaCgmZGpekQpUmp8AFA8qlFbaVU3R"

    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessToken, accessTokenSecret)
    api = tweepy.API(auth)
    tag = request.POST.get("post")
    searchTerm = tag
    noOfSearchTerms = int(20)

    tweets = tweepy.Cursor(api.search, q=searchTerm).items(noOfSearchTerms)

    def percentage(part, whole):
        return 100 * float(part) / float(whole)

    positive = 0
    negative = 0
    neutral = 0
    polarity = 0
    messages = list()
    i = 0
    for tweet in tweets:
        i += 1
        if(i<=10):
            messages.append(tweet)

        analysis = TextBlob(tweet.text)
        polarity += analysis.sentiment.polarity

        if (analysis.sentiment.polarity == 0):
            neutral += 1
        if (analysis.sentiment.polarity > 0.00):
            positive += 1
        if (analysis.sentiment.polarity < 0.00):
            negative += 1

    positive = percentage(positive, noOfSearchTerms)
    negative = percentage(negative, noOfSearchTerms)
    neutral = percentage(neutral, noOfSearchTerms)

    if (neutral > (positive+negative)/2):
        mood = "neutral"
    if (negative >= (positive+neutral)/2):
        mood = "negative"
    if (positive >= (negative+neutral)/2):
        mood = "positive"

    return render(request, 'twitter.html', {'tag':tag, 'messages':messages, 'pos':positive, 'neut':neutral, 'neg': negative})

