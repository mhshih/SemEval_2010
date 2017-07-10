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
    string=open(xml).read()
    for m in re.finditer('<s>(.*?)</s>',string,re.DOTALL):
        tagged_words=list()
        for line in m.group(1).strip().replace('。\n','').split('\n'): #Replace sentence initial 。.
            n=re.match('<head.*>(.*)</head>',line)
            if n:
                head=n.group(1)
                head_id='zh'+re.match('<head id="zh(.*)">.*</head>',line).group(1)
                synset_id=d[head_id]
                tagged_words.append(TaggedWord(word=head,synset_id=synset_id,head_id=head_id))
            else:
                word=line
                tagged_words.append(TaggedWord(word=word))
        tagged_sents.append(tagged_words)
    return tagged_sents

def preprocess(example_cont):
    tr_sent_bound_mapping={ord('）'):')',ord('.'):'‧'}#,ord('。'):'，',ord('？'):'?'}
    example_cont=example_cont.replace('<','').replace('>','')   #Remove head word tag.
    example_cont=example_cont.replace('\n','').strip()          #Remove line break.
    example_cont=example_cont.replace('∥','')                   #Remove ∥那個局長的位置啊...就是買來當局長這樣子啊。∥
    example_cont=example_cont.translate({ord('﹖'):'？',ord('?'):'？'})       #Unify question mark.
    example_cont=example_cont.translate(tr_sent_bound_mapping)  #Avoid sentence boundary for parsing.
    return example_cont.split('。')[0].split('？')[0].split('！')[0].split('!')[0]+'。'     #Keep first sentence only ending with 。.

from cwn_16 import read_synset_gloss,read_lemma_synsets
from cwn_fun import read_cwnid2examples
from conllu import DCR

if __name__=='__main__':
    cwnfile='cwn_16.xml'
    synset_to_gloss=read_synset_gloss(cwnfile)
    lemma_synsets=read_lemma_synsets(cwnfile)
    cwnid2examples=read_cwnid2examples()
    cwn_ids=list() #Keep only those cwn_ids that are needed to serve as the sense inventory for ChineseAW.test WSD.
    for tagged_sent in read_tagged_sents(xml='../ChineseAW.test.xml',keyfile='../../../test-keys/ChineseAW.test.key'):
        for TW in tagged_sent:
            if TW.synset_id:# and TG.word==keyword:
                gloss=synset_to_gloss[TW.synset_id]
                for synset in lemma_synsets[TW.word]:#cwn_id)#example_cont,end='\t')
                    cwn_id=re.match('zho-16-(\d{8})-[nvrsa]',synset).group(1)
                    if cwn_id not in cwn_ids:cwn_ids.append(cwn_id)
    DGs=DCR(root='/tmp/stanford-corenlp-full-2017-06-09',fileids='ChineseAW_test_example_cont.txt.conllu').parsed_sents()
    i=0
    for cwn_id in cwn_ids:
        if cwn_id in cwnid2examples: #1,814 example_cont types, including two [""].
            if cwnid2examples[cwn_id]!=[""]: #1,812 example_cont types.
                print(cwn_id,end=' ')#.join(DGs[i].words))#triples())
                print(preprocess(example_cont=cwnid2examples[cwn_id][0]),end=' ')
                for triple,rel,triple in DGs[i].triples():print(triple,rel,triple,end=' ')
                print()
                i+=1
