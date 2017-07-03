def read_key_to_dict(keyfile):
    d=dict()
    for line in open(keyfile):
        text,head_id,key=line.split()
        d[head_id]=key
    return d


import re

def read_tagged_sents(text='ChineseAW.test.xml',keyfile='ChineseAW.test.key'):#,cwn='cwn_16.xml'):
    d=read_key_to_dict(keyfile=keyfile)
    tagged_sents=list() #[(word,synset_id/None)]
#   synset_gloss=read_synset_gloss(cwn)
    string=open(text).read()
    for m in re.finditer('<s>(.*?)</s>',string,re.DOTALL):
        tagged_words=list()
        for line in m.group(1).strip().replace('。\n','').split('\n'):
            n=re.match('<head.*>(.*)</head>',line)
            if n:
                head=n.group(1)
                head_id='zh'+re.match('<head id="zh(.*)">.*</head>',line).group(1)
                synset_id=d[head_id]
#               definition_gloss=synset_gloss[synset_id]
                tagged_words.append((head,synset_id))
            else:tagged_words.append((line,None))
        tagged_sents.append(tagged_words)
    return tagged_sents

from cwn_16 import read_synset_gloss,read_lemma_synsets

if __name__=='__main__':
    keyword='有'#增加'為
    cwnfile='cwn_16.xml'
    synset_gloss=read_synset_gloss(cwnfile)
    lemma_synsets=read_lemma_synsets(cwnfile)
    for tagged_sent in read_tagged_sents(text='../ChineseAW.test.xml',keyfile='../../../test-keys/ChineseAW.test.key'):
        for word,synset_id in tagged_sent:
        #   print(word,synset_id)#,sep='\t',end='\t')
            if synset_id and word==keyword:
                gloss=synset_gloss[synset_id]
#               print(word,synset_id,gloss)
#               for synset in lemma_synsets[word]:print('',synset,synset_gloss[synset],sep='\t')
#           else:print()
        print()
