#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    word = input("Введите слово: ")
    k = int(input("Введите номер буквы, которую нужно переместить в начало: "))

    new_word = word[k - 1] + word[:k - 1] + word[k:]

    print("Новое слово:", new_word)
