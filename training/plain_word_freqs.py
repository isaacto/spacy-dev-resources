#!/usr/bin/env python
from __future__ import unicode_literals

import codecs
import glob
from collections import Counter
import warnings

from future.utils import iteritems
import plac
from tqdm import tqdm


def count_words(fpath):
    with codecs.open(fpath, encoding="utf8") as f:
        words = f.read().split()
        counter = Counter(words)
    return counter


def main(input_glob, out_loc, workers=None):
    if workers is not None:
        warnings.warn("workers argument is no longer needed", DeprecationWarning)
    df_counts = Counter()
    word_counts = Counter()
    for fpath in tqdm(glob.glob(input_glob)):
        wc = count_words(fpath)
        df_counts.update(wc.keys())
        word_counts.update(wc)
    with codecs.open(out_loc, "w", encoding="utf8") as f:
        for word, df in iteritems(df_counts):
            f.write(u"{freq}\t{df}\t{word}\n".format(word=repr(word), df=df, freq=word_counts[word]))


if __name__ == "__main__":
    plac.call(main)
