# Author: Paul Quaife
# Date: 2/12/2021
# Description: Takes a list of names, then adds surname Kardashian.

def add_surname(first_names_list):

    full_list = [name+' Kardashian' for name in first_names_list if name[0] == 'K']
    return full_list
