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
    string=open(xml).read()
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

tr_sent_bound_mapping={ord('）'):')',ord('.'):'‧'}#,ord('。'):'，',ord('？'):'?'}
def preprocess(example_cont):
    example_cont=example_cont.replace('<','').replace('>','')   #Remove head word tag.
    example_cont=example_cont.replace('\n','').strip()          #Remove line break.
    example_cont=example_cont.replace('∥','')                   #Remove ∥那個局長的位置啊...就是買來當局長這樣子啊。∥
    example_cont=example_cont.translate({ord('﹖'):'？',ord('?'):'？'})       #Unify question mark.
    example_cont=example_cont.translate(tr_sent_bound_mapping)  #Avoid sentence boundary for parsing.
#   if example_cont[-1] in ['。','？','！']:return example_cont      
#   return example_cont+'。'                                    #Assert ending with sentency boundary mark.
    return example_cont.split('。')[0].split('？')[0].split('！')[0].split('!')[0]+'。'     #Keep first sentence only ending with 。.

from cwn_16 import read_synset_gloss,read_lemma_synsets
from cwn_fun import read_cwnid2examples
if __name__=='__main__':
    keyword='有'#增加'為
    cwnfile='cwn_16.xml'
    synset_gloss=read_synset_gloss(cwnfile)
    lemma_synsets=read_lemma_synsets(cwnfile)
    cwnid2examples=read_cwnid2examples()
    cwn_ids=list()
    for tagged_sent in read_tagged_sents(xml='../ChineseAW.test.xml',keyfile='../../../test-keys/ChineseAW.test.key'):
        if tagged_sent[0].word in ['。','？']:#,'1','2','3','4','5','6']:continue #Skip。,？ or number only sentences.
            continue
        for TG in tagged_sent:
            if TG.word=='.':continue #Skip sentence initial .
            if TG.synset_id:# and TG.word==keyword:
                gloss=synset_gloss[TG.synset_id]
#               print(gloss)
                for synset in lemma_synsets[TG.word]:#cwn_id)#example_cont,end='\t')
                    cwn_id=re.match('zho-16-(\d{8})-[nvrsa]',synset).group(1)
                    if cwn_id not in cwn_ids:cwn_ids.append(cwn_id)
    for cwn_id in cwn_ids:
        if cwn_id in cwnid2examples: #1,814 example_cont types, including two [""].
            if cwnid2examples[cwn_id]!=[""]: #1,812 example_cont types.
#               example_cont=cwnid2example[cwn_id][0].replace('\n','').strip()
#               example_cont=example_cont.replace('<','').replace('>','') #1,812 example_cont tokens; 1,804 types.
#               print(example_cont[:-1].translate(sentence_boundary_mapping)+example_cont[-1].translate({ord('﹖'):'？'}))
                print(preprocess(example_cont=cwnid2examples[cwn_id][0]))
