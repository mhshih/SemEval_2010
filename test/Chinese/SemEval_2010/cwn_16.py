from collections import defaultdict
import re

def read_lemma_synsets(xml='cwn_16.xml'):
    d=defaultdict(list) #d[lemma]=synset_id
    string=open(xml).read()
    for m in re.finditer('<Lemma writtenForm="(.*?)".*?synset="(.*?)"',string,re.DOTALL):
        lemma=m.group(1)
        synset_id=m.group(2)
        d[lemma].append(synset_id)
    return d

def read_synset_gloss(xml='cwn_16.xml'):
    d=dict() #d[synset_id]=definition_gloss
    string=open(xml).read()
    for m in re.finditer('<Synset id="(.*?)".*?</Synset>',string,re.DOTALL):
        synset_id=m.group(1)
        definition_gloss=re.search('<Definition gloss="(.*?)">',m.group(0),re.DOTALL).group(1)
        d[synset_id]=definition_gloss
    return d

if __name__=='__main__':
#   for synset_id,definition_gloss in read_synset_gloss('../../cwn_16.xml').items():
#       print(synset_id,definition_gloss)
    for lemma,synset_ids in read_lemma_synsets('cwn_16.xml').items():
        print('\n'.join(synset_ids))
