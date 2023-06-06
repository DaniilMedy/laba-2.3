#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    sentence = input("Введите предложение: ")
    new_sentence = ""

    for i in range(len(sentence)):
        if (i + 1) % 3 == 0:
            new_sentence += "а"
        else:
            new_sentence += sentence[i]

    print(new_sentence)

