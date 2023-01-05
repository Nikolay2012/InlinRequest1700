'''
    Модуль який показує шлях до файлу який ми вкажемо як параметер функії
'''
import os
def path_file(file_path):
    abs_path = __file__.split("/")
    del abs_path[-1]
    del abs_path[-1]
    abs_path = "/".join(abs_path)
    abs_path = os.path.join(abs_path, file_path)
    return abs_path