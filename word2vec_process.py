# -*- coding: utf-8 -*-

from __future__ import print_function
import logging
import os.path
import argparse
import codecs
import sys
import jieba
from gensim.corpora import WikiCorpus

parser = argparse.ArgumentParser(description = 'word2vec_process.py')

parser.add_argument("-data", required = True, help = 'Path to the Corpus.')
parser.add_argument("-output", required = True, help = 'Path to the output file.')
parser.add_argument("-jieba", required = True, help = 'Flag to judge using jieba or not.')

opt = parser.parse_args()

if __name__ == '__main__':

	program = os.path.basename(sys.argv[0])
	logger = logging.getLogger(program)

	logging.basicConfig(format = '%(asctime)s: %(levelname)s: %(message)s')
	logging.root.setLevel(level = logging.INFO)
	logger.info("running %s" % ' '.join([sys.argv[0], opt.data, opt.output, opt.jieba]))

	inpt, outpt = opt.data, opt.output
	count = 0

	output = codecs.open(outpt, 'w', 'utf-8')
	wiki = WikiCorpus(inpt, lemmatize = False, dictionary = {})
	for text in wiki.get_texts():
		if opt.jieba == 'True':
			seg_list = jieba.cut("".join(text), cut_all = False)
			output.write(' '.join(seg_list) + '\n')
		else:
			output.write(' '.join(text) + '\n')
		output.flush()
		
		count += 1
		if (count % 10000 == 0):
			logger.info("Saved " + str(count) + " articles")

	output.close()
	logger.info("Finished Saved " + str(count) + " articles")
