#! /usr/bin/env python
''' Generates a text file of the desired size made up of random words on lines of
    roughly random length.  The words come from the system-provided Webster's 2nd
    edition dictionary at /usr/share/dict/web2

    NOTE:  command line inputs n_words and out_size must come in as ints, and
    the path to the linux system's Websters dictionary might vary by installation.
    I have not added extensive exception handling for these issues, this is a quick
    and dirty program I makde to give me sample input for playing with Hadoop and Spark.

    Inputs:     argv[1] --> n_words, int:  the number of unique words to draw from
                argv[2] --> outname, str: the output file name including the path
                argv[3] --> out_size, int: approx desired file size in Mb

    Output:     randText.txt = text file of random words

    Example usage to make a 1Gb text file using a 5000 word vocabulary:

                $ ./genWordFile.py 5000 randText.txt 1000
'''
import sys ; import os; import random ; from datetime import datetime
import numpy as np ; np.random.seed(datetime.now().microsecond)

def main():

    # get all ~2E+05 words from the linux root text file made from
    # Webster's Second International dictionary
    with open('/usr/share/dict/web2', mode='r') as websters:
        all_words = websters.read().split('\n')

    # from the full set of words, cut down to requested amount of randomly
    # selected words to become the vocabulary
    n_words = int(sys.argv[1])
    inds_list = np.random.randint( 0, len(all_words), size = n_words ).tolist()
    vocab = [ all_words[i] for i in inds_list ]

    # output file
    outname = sys.argv[2]
    outfile = open(outname,mode='w')
    print('\nFilling output file '+outname,end='\n\n')

    # counter to track approximate output file size
    fudge_factor = 1.2
    desired_bytes = 1.e6 * fudge_factor * int(sys.argv[3])
    total_bytes = 0

    while total_bytes < desired_bytes:

        # pick a random length for sentences (between 20 and 80 words)
        line_len = np.random.randint(15,61)

        # from the vocabulary, randomy create "sentences" (one line for output file)
        inds_list = np.random.randint( 0, len(vocab), size = line_len ).tolist()
        some_words = [ vocab[i] for i in inds_list ]
        line = ' '.join(some_words)

        total_bytes += sys.getsizeof(line)
        outfile.write(line+'\n')

    outfile.close()
    os.system('ls -lh '+outname)


if (__name__ == '__main__'):
    main()
