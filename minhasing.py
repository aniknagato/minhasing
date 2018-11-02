import random


def dna_shingle(dna, k):
    # this function should return a list of all k-shingles.

    if k > 0:
        shingle_list = []
        for i in range(0, len(dna) - 1 - k):
            shingle = dna[i:i + k]
            shingle_list.append(shingle)
    else:
        print("K cannot be 0")
    return shingle_list


def shingle2decimal(dna):
    # this function returns a number
    values = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    decimal_value = 0
    for index in range(0, len(dna)):
        decimal_value += 4 ** index * values[dna[len(dna) - 1 - index]]
    return decimal_value


def shingle2vector(dna, k):
    # this returns a vector representation of DNA string
    vector_shingles = [0] * 4 ** k
    shingle_list = dna_shingle(dna, k)

    for items in shingle_list:
        shingle_number = shingle2decimal(items)
        vector_shingles[shingle_number] = 1

    return vector_shingles


def minhash_dna(permutation, dna, k):
    # return a number that is a minhash of dna
    vector = shingle2vector(dna, k)
    x = [-1] * len(vector)
    for i in range(len(vector)):
        x[i] = vector[permutation[i]]
        if x[i] == 1:
            return permutation[i]









