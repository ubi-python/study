# coding=utf-8

class Person:
    def __init__(self):
        print("init call")

    def __del__(self):
        print("del call")

person = Person()