def preprocess(string): #Remove s049 sentence initial.
    return string.replace('<s>\n！\n）\n，\n「\n<head id="zh1.s049.1000">政府</head>\n','<s>「\n<head id="zh1.s049.1000">政府</head>\n')


def read_key_to_dict(keyfile):
    d=dict()
    for line in open(keyfile):
        text,head_id,key=line.split()
        d[head_id]=key
    return d

class TaggedWord:
    def __init__(self,word,synset_id=None,head_id=None):
        self.word=word
        self.synset_id=synset_id
        self.head_id=head_id

import re

def read_tagged_sents(xml='ChineseAW.test.xml',keyfile='ChineseAW.test.key'):#,cwn='cwn_16.xml'):
    d=read_key_to_dict(keyfile=keyfile)
    tagged_sents=list() #[(word,synset_id/None)]
#   synset_gloss=read_synset_gloss(cwn)
    string=preprocess(open(xml).read())
    for m in re.finditer('<s>(.*?)</s>',string,re.DOTALL):
        tagged_words=list()
        for line in m.group(1).strip().replace('。\n','').split('\n'): #Replace sentence initial 。.
            n=re.match('<head.*>(.*)</head>',line)
            if n:
                head=n.group(1)
                head_id='zh'+re.match('<head id="zh(.*)">.*</head>',line).group(1)
                synset_id=d[head_id]
#               definition_gloss=synset_gloss[synset_id]
                tagged_words.append(TaggedWord(word=head,synset_id=synset_id,head_id=head_id))
            else:
                word=line
                tagged_words.append(TaggedWord(word=word))
        tagged_sents.append(tagged_words)
    return tagged_sents

from cwn_16 import read_synset_gloss,read_lemma_synsets
from cwn_fun import read_cwnid2example

sentence_boundary_mapping={ord('。'):'，',ord('？'):'?',ord('）'):')',ord('.'):'‧'} #Already skipped sentence initial . 

if __name__=='__main__':
    keyword='有'#增加'為
    cwnfile='cwn_16.xml'
    synset_gloss=read_synset_gloss(cwnfile)
    lemma_synsets=read_lemma_synsets(cwnfile)
    cwnid2example=read_cwnid2example()
    cwn_ids=list()
    for tagged_sent in read_tagged_sents(xml='../ChineseAW.test.xml',keyfile='../../../test-keys/ChineseAW.test.key'):
        if tagged_sent[0].word in ['。','？']:#,'1','2','3','4','5','6']:continue #Skip 。,？ or number only sentences.
#           print(tagged_sent[0].word)
            continue
#       else:print(' '.join([TG.word.translate(sentence_boundary_mapping) for TG in tagged_sent])+'。')
        for TG in tagged_sent:
            if TG.word=='.':continue #Skip sentence initial .
#           if word in sentence_boundary_mapping:print(sentence_boundary_mapping[word],end=' ')
#           else:print(word,end=' ')#,synset_id,sep='\t',end='\t')
#           if word=='。':print(word)
            if TG.synset_id:# and TG.word==keyword:
                gloss=synset_gloss[TG.synset_id]
#               example_cont=''
#               if cwn_id:example_cont=cwn_id_to_example_cont(cwn_id=cwn_id)#.group(1))
#               if example_cont:example_cont=example_cont[0].strip()
#               else:example_cont=''
#               print(TG.word) #1,204 head word tokens (398 types)to disambiguate.
                for synset in lemma_synsets[TG.word]:#cwn_id)#example_cont,end='\t')
#                   print(synset) #2,308 synset_id types (zho-16-03010901-n~zho-16-10011102-n).
                    cwn_id=re.match('zho-16-(\d{8})-[nvrsa]',synset).group(1)
#                   print(cwn_id) #2,308 cwn_id types (03010901-n~10011102-n).
#                   if synset==TG.synset_id:print(synset) #All 1,204 tagged synset_ids in cwn_dirty.sqlite!
#                   if cwn_id in cwnid2example:print(cwnid2example[cwn_id]) #1,608 []
                    if cwn_id not in cwn_ids:cwn_ids.append(cwn_id)
    for cwn_id in cwn_ids:
#       print(cwn_id)#2,308 cwn_id types.
        if cwn_id in cwnid2example: #1,814 example_cont types, including two [""].
            if cwnid2example[cwn_id]!=[""]: #1,812 example_cont types.
                example_cont=cwnid2example[cwn_id][0].replace('\n','').strip()
#               print(example_cont) #1,812 example_cont tokens; 1,811 types.
                example_cont=example_cont.replace('<','').replace('>','') #1,812 example_cont tokens; 1,804 types.
                print(example_cont[:-1].translate(sentence_boundary_mapping)+example_cont[-1].translate({ord('﹖'):'？'}))

                    
#               if example_cont:example_cont=''.join(re.match('(.*?)<(%s)>(.*)' % TG.word,example_cont).groups()) #Remove < >.
#               print(TG.word,example_cont)
#               for synset in lemma_synsets[word]:print('',synset,synset_gloss[synset],sep='\t')
#           else:print()
#       print('。')
