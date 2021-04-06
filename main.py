import os
import random
from hangman_ascii_art import HANGMANPICS as pics
from hangman_ascii_art import LOGO
from hangman_words_test import words

# Hangman ascii art and wordbank
# https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c

MAX_STAGE = 6

# 윈도우즈의 경우 "cls", 기타는 "clear"
def cls():
    """화면 클리어"""
    os.system("cls" if os.name == "nt" else "clear")


def game_over():
    print("GAME OVER")


def get_input(guessed_word):
    while True:
        guessing = input("영문 한 글자를 입력하세요! ")
        guessing = guessing.strip().lower()

        if guessing in guessed_word:
            print(f"{guessing}은 이미 사용한 문자입니다.", end=" ")
        elif guessing.isalpha() and len(guessing) == 1:
            return guessing


def game():
    chosen_word = random.choice(words)
    print(chosen_word)  ### 개발시에만 사용

    guessed_word_list = ["_"] * len(chosen_word)  # 사용자가 입력한 글자들의 리스트
    guessed_word = "".join(guessed_word_list)

    stage = 0

    while True:
        guessing = get_input(guessed_word)

        cls()
        if guessing in chosen_word:
            for position, letter in enumerate(chosen_word):
                if guessing == letter:
                    guessed_word_list[position] = guessing
            guessed_word = "".join(guessed_word_list)  # 사용자가 입력한 글자로 만든 단어
            print(guessed_word)
            if guessed_word == chosen_word:
                print("축하합니다. 맞추셨네요!!!. 이기셨습니다!!!")
                break
            if stage == 0:
                pass
            else:
                print(pics[stage - 1])
        else:
            print(f"입력하신 {guessing}은 단어에 없습니다.")
            stage += 1
            print(pics[stage - 1])

            if stage > MAX_STAGE:
                game_over()
                break


while True:
    print(LOGO)
    game()
    answer = input("계속하시겠습니까? 계속하시려면 엔터를, 끝내시려면 'n'을 입력하세요")
    if answer.strip().lower() == "n":
        break
