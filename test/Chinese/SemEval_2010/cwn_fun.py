from sqlite3 import connect
conn=connect('cwn_dirty_20160927.sqlite')
cursor=conn.cursor()
def lemma_type_to_lemma_ids(lemma_type='晃'): #return lemma_ids=['080601',] or None
    cursor.execute('select lemma_id from cwn_lemma where lemma_type="%s"' % lemma_type)
    return cursor.fetchall()#[0]    return [lemma_id[0] for lemma_id in cursor.fetchall()]#[0]
def lemma_id_to_sense_ids(lemma_id='093020'): #return sense_id=['08060101',] or None
    cursor.execute('select sense_id from cwn_sense where lemma_id="%s"' % lemma_id)
    return cursor.fetchall()#[0]   return [sense_id[0] for sense_id in cursor.fetchall()]#[0]
def sense_id_to_sense_def(sense_id='08060101'): #return sense_def or None
    cursor.execute('select sense_def from cwn_sense where sense_id="%s"' % sense_id)
    return cursor.fetchone()#[0]
def cwn_id_to_example_cont(cwn_id='03000101'): #return example_cont or None
    cursor.execute('select example_cont from cwn_example where cwn_id="%s"' % cwn_id)
    return cursor.fetchone()#[0]

from collections import defaultdict
def read_cwnid2examples():
    cwnid2example=defaultdict(list)
    cursor.execute('select cwn_id,example_cont from cwn_example')
    for cwn_id,example_cont in cursor.fetchall():
        cwnid2example[cwn_id].append(example_cont)
    return cwnid2example


if __name__=='__main__':

    for cwn_id,example_conts in read_cwnid2examples().items():
#       print(cwn_id) #32,322 cwn_id types.
        for example_cont in example_conts:
#           print(cwn_id,[example_cont]) #91,785 example_cont tokens (91,775 uniq + 10 duplicated).
            print([example_cont]) #91,785 example_cont tokens

    cursor.execute('select cwn_id,example_cont from cwn_example')
#   for cwn_id,example_cont in cursor.fetchall():print([example_cont.strip()])

    conn.close()
'''
    cursor.execute('select sense_id,sense_def from cwn_sense')
    sense_id_sense_def=cursor.fetchall()
    for sense_id,sense_def in sense_id_sense_def:
#       print(sense_id,sense_def)
        cursor.execute('select lemma_type from cwn_lemma where lemma_id="%s"' % sense_id[:6])
#       if not cursor.fetchall():print(sense_id,sense_def,cwn_id_to_example_cont(sense_id))

    cursor.execute('select lemma_id,lemma_type from cwn_lemma')
    for lemma_id,lemma_type in cursor.fetchall():
        for sense_id in lemma_id_to_sense_ids(lemma_id):
            sense_def=sense_id_to_sense_def(sense_id)
'''

