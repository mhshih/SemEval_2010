


			     SEMEVAL-2010
			    -------------

  TASK 17: All-words Word Sense Disambiguation on a Specific Domain

			     (WSD-domain)



 


The trial data packages contains the following:


  00-README.txt			  this file
  Instructions.txt                instructions to participate
  all-words.dtd                   dtd for input files
  English/
	EnglishAW.trial.xml       input file for WSD
	EnglishAW.trial.key	  gold standard
	WordNet			  wordnet to be used as sense inventory
        BackgroundDocuments       extra documents from the same domain         				  


  scorer2/                        scorer program


The test data will also include:

  Italian/
  Dutch/
  Chinese/
				  Directories with information analogue
				  to the English directory in the 
				  training data


Differences from the trial data and the test data:
--------------------------------------------------

- The trial data includes a short target text from a general domain, while the 
  test data will include target texts from the environment domain

- The trial data includes only English

- The trial data includes a few background documents. We plan to gather more 
  background documents, and make them available as easly as possible. The
  release of the data will be announced in the task mailing list
  


Answer format
--------------

The answer format is similar to the gold standard format, but,
alternatively, it allows systems to return multiple weighted
senses. Please check scoring/sampletask.system.answers for an example.


Multi-word expressions
-----------------------

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

$  cd scoring
$  ./scorer2 sampletask.system.answers sampletask.key

Note sensemaps (as mentioned in the scoring software) are not used.


WordNet
-------

Wordnets are included in LMF format. Check the documentation in 
the following link:

http://xmlgroup.iit.cnr.it/kyoto/index.php?option=com_content&view=article&id=143&Itemid=129



Background Documents
--------------------

We include some documents about the domain, which participants are
free to use to improve their WSD programs. Further documents will be released 
soon, and announed in the task mailing list.




