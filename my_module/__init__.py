from my_module.math_module import *
import argparse
import json

def find_args():

    parser = argparse.ArgumentParser(prog="Helper", description="Описание программы")

    parser.add_argument("-nums", "--numbers", type=json.loads, help="Список чисел в формате [a, b]")
    parser.add_argument("-op", "--operation", type=str, choices=['+', '-', '*', '/'], help="Операция над числами", default="+")

    return parser.parse_args()