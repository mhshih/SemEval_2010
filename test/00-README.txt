


			     SEMEVAL-2010
			    -------------

  TASK 17: All-words Word Sense Disambiguation on a Specific Domain

			     (WSD-domain)



 


The test data packages contains the following:


  00-README.txt			  this file
  Instructions.txt                instructions to participate
  all-words.dtd                   dtd for input files
  English/
	EnglishAW.test.xml       input file for WSD
	EnglishAW.faketest.key	 fake gold standard

  Italian/
	ItalianAW.test.xml       input file for WSD
	ItalianAW.faketest.key	 fake gold standard

  Dutch/
	DutchAW.test.xml         input file for WSD
	DutchAW.faketest.key	 fake gold standard

  Chinese/
	ChineseAW.test.xml       input file for WSD
	ChineseAW.faketest.key	 fake gold standard

  scorer2/                        scorer program


Differences from the trial data and the test data:
--------------------------------------------------

- The trial data included a short target text from a general domain,
  while the test data includes target texts from the environment
  domain

- The dtd in the trial data has been enriched to accommodate sentence
  boundaries and, in the case of Dutch, to properly encode component
  lemmas of compounds.
  
- Multiword terms and adjectives are not tagged in the test data,
  and therefore only single word nouns and verbs need to be tagged.


Answer format
--------------

The answer format is similar to the fake gold standard formats (please
check EnglishAW.faketest.key, etc.). It needs to follow the same order
and keep three columns. You only need to change the string in the last
column with the sense keys returned by your system.
 
Alternatively, the answer format also allows systems to return
multiple weighted senses. Please check
scoring/sampletask.system.answers in the trial dataset for an example.


Multi-word expressions
-----------------------

(This version of the dataset does not contain Multi-word expressions)

The indicated "head" of a multi-word expression (indicated by a
combination of the sats="..." attribute and additional <sat...>
elements) should only be tagged with a WordNet sensekey corresponding
to the entire multi-word expression.  If no such sensekey exists, the
answer key should remain blank.

Note: The word in the expression identified as the "head" is just the
first noun, adjective, or verb in the expression.  The POS of the
expression as a whole may differ from the POS of the word identified
as the head.


Scoring
-------

Use as follows:

$ cd scorer2
$ ./score.pl sampletask.system.answers sampletask.key

scorer.pl sorts both files in alphanumeric order and calls to
scorer2, the official scorer from past SemEval/Senseval WSD
competitions.

Note that sensemaps (as mentioned in the scoring software) are not
used.


WordNets
--------

Wordnets are available in LMF format from the task website: 

 http://xmlgroup.iit.cnr.it/kyoto/index.php?option=com_content&view=article&id=143&Itemid=129

Check the documentation about LMF in the following link:

 http://xmlgroup.iit.cnr.it/SemEval2010/download.php


BackgroundDocuments
-------------------

Documents from the same domain as the test documents are available for
all languages from the task website:

 http://xmlgroup.iit.cnr.it/kyoto/index.php?option=com_content&view=article&id=143&Itemid=129





