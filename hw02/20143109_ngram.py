#-*- coding:utf-8 -*-
import sys
from konlpy.tag import Kkma
import re

BI = 2
TRI = 3

class NGram:
    def __init__(self, args):
        self.syllable_split_var = []
        self.ngram = []

        with open(args, "r", encoding='UTF8') as f:
            self.data = f.read()
            pattern = '[^\t\n\r\f\v\w]'
            repl = ''
            self.data = re.sub(pattern=pattern, repl=repl, string=self.data)

    def syllable_split(self, num_gram):
        if 0 < num_gram < 5:
            text = tuple(self.data)
            self.ngram = [text[x:x + num_gram] for x in range(0, len(text) - num_gram + 1)]
            return self.ngram
        elif num_gram == 5:
            text = tuple(self.data)
            self.ngram = []
            for i in range(len(text) - 1):
                self.ngram.extend([text[i:i + 2], text[i:i + 3]])
            return self.ngram
        else:
            print("num_gram error")
            return []

class KonLPy:
    def __init__(self, args):
        kkma = Kkma()
        with open(args, "r", encoding='UTF8') as f:
            self.data = f.read()
            self.konlpy_split = kkma.nouns(self.data)
        print(self.konlpy_split)
        self.set_nouns = set(self.konlpy_split)

def check_similarity(sen_01, sen_02, is_konlpy=False):
    if not is_konlpy:
        same_count = 0
        for (i, tuples) in enumerate(sen_01):
            if len(sen_02) > i and sen_01[i] == sen_02[i]:
                same_count += 1
        return (same_count/len(sen_01)) * 100
    else:
        same_count = len(sen_01 & sen_02)
        return (same_count/len(sen_01)) * 100

def n_gram_model(n_gram_num):

    n_gram_1 = NGram(args_1)
    n_gram_1_syllable_split = n_gram_1.syllable_split(n_gram_num)
    print(n_gram_1_syllable_split)
    n_gram_2 = NGram(args_2)
    n_gram_2_syllable_split = n_gram_2.syllable_split(n_gram_num)
    print(n_gram_2_syllable_split)

    n_gram_similarity_percentage = check_similarity(n_gram_1_syllable_split, n_gram_2_syllable_split)
    if n_gram_num == BI:
        print(f'bi_gram similarity = {n_gram_similarity_percentage}%')
    elif n_gram_num == TRI:
        print(f'tri_gram similarity = {n_gram_similarity_percentage}%')
    elif n_gram_num == 5:
        print(f'bi+tri_gram similarity = {n_gram_similarity_percentage}%')


if __name__ == '__main__':
    args_1, args_2 = sys.argv[1], sys.argv[2]
    
    n_gram_model(BI)
    n_gram_model(TRI)
    n_gram_model(5)

    kon_01 = KonLPy(args_1)
    kon_02 = KonLPy(args_2)
    kon_similarity_percentage = check_similarity(kon_01.set_nouns, kon_02.set_nouns, True)

    print(f'konlpy similarity = {kon_similarity_percentage}%')