import os

def leerme(narchivo):
    return open(os.path.join(os.path.dirname(os.path.abspath(__file__)), narchivo)).read()

if __name__ == '__main__':
    print(leerme('README'))

