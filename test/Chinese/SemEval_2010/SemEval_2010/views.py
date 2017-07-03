from ChineseAW_test import read_tagged_sents
from django.http import HttpResponse

def home(request):
    tagged_words=list()
    for tagged_sent in read_tagged_sents(text='../ChineseAW.test.xml',keyfile='../../../test-keys/ChineseAW.test.key'):
        for word,synset in tagged_sent:
            if synset:tagged_words.append(word+' '+synset)
            else:tagged_words.append(word)
    return HttpResponse('<br>'.join(tagged_words))

