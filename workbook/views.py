from django.shortcuts import render, HttpResponse
from django.views import View
from django.core.exceptions import ObjectDoesNotExist
from .models import Word
from .crawling import get_mean


class SearchView(View):

    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponse('로그인 하시오')
        word = request.GET.get('word')
        context = {'word': self.get_word(word, request.user)}
        return render(request, 'workbook/search.html', context)

    def get_word(self, word, user):
        if not word:
            return

        word = word.lower()
        try:
            word = Word.objects.get(user=user, text=word)
        except ObjectDoesNotExist:
            word = Word(user=user, text=word, mean=get_mean(word))
            word.save()
        return word

