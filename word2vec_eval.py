# -*- coding: utf-8 -*-

import logging
import os.path
import sys
import argparse
import gensim
from gensim.models import KeyedVectors

parser = argparse.ArgumentParser(description = 'word2vec_model.py')

parser.add_argument("-mode", required = True, help = 'Choose the mode of our model.')
parser.add_argument("-vector", required = True, help = 'Name of the Vector Output.')

opt = parser.parse_args()

if __name__ == '__main__':
	program = os.path.basename(sys.argv[0])
	logger = logging.getLogger(program)

	logging.basicConfig(format = '%(asctime)s: %(levelname)s: %(message)s')
	logging.root.setLevel(level = logging.INFO)
	logger.info("running %s" % ' '.join([sys.argv[0], opt.mode, opt.vector]))

	inpt, mode = opt.vector, opt.mode

	model = gensim.models.KeyedVectors.load_word2vec_format(inpt, binary = False)

	if mode == 'similar':
		logger.info("MSG : 'similar' mode.")
		while True:
			if word == '-1':
				break
			word = input("Please input word(press -1 to exit): ")
			logger.info(model.most_similar(word))
	if mode == 'similarity':
		logger.info("MSG : 'similarity' mode.")
		while True:
			if word == '-1':
				break
			word = input("Please input two word split by space(press -1 to exit): ").split()
			logger.info(model.similarity(word[0], word[1]))