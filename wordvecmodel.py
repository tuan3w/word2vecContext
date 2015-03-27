#!/usr/bin/env python


from corpus import KDDCorpus, TreeContextCorpus
import gensim, logging
logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)
import pdb

#word2vec
from gensim.models.word2vec import Word2Vec

def main():
    sentences = KDDCorpus('./dat2', './data2')
    sentences = TreeContextCorpus(maxA=2, maxB=3, maxC=10, maxD=10)
    logging.info('Learning Word2Vec model')
    model =Word2Vec(sentences,      #dataset
                    sg = 1,         # use skipgram
                    min_count=0,    #keep all word
                    size=200,       #size of vector
                    workers=3,      # number of workers
                    window=3,       # window context
                    hs = 1,
                    #cbow_mean=1,    # use average bow
                    #negative = 5,
                    iter=200
                    )

    # just use model for compute distance
    model.init_sims(replace=True)

    pdb.set_trace()






if __name__ == '__main__':
    main()
