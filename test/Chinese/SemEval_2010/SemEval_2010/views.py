from collections import defaultdict
from cwn_16 import read_synset_gloss
from ChineseAW_test import read_tagged_sents
from django.http import HttpResponse

def home(request):
    keyword='增加'
#   tagged_words=list()
    synset_sents=defaultdict(list)
    synset_gloss=read_synset_gloss('cwn_16.xml')
    for tagged_sent in read_tagged_sents(text='../ChineseAW.test.xml',keyfile='../../../test-keys/ChineseAW.test.key'):
        ss=''
        for word,synset in tagged_sent:
            if synset and word==keyword:#tagged_words.append(word+' '+synset)
                ss=synset_gloss[synset]#synset
#           else:tagged_words.append(word)
        if ss:synset_sents[ss].append(' '.join([word for word,synset in tagged_sent]))
    res=keyword+'<table>'
    for synset,sents in synset_sents.items():
        res+='<tr><td>%s</td>' % synset
        res+='<td><ol><li>%s</ol></td></tr>' % '<li>'.join(sents)
    return HttpResponse(res+'</table>')#'<br>'.join(tagged_words))

