import os, random
def get():
    DIR = os.path.dirname(os.path.abspath(__file__))
    PIC_DIR = os.path.join(DIR, 'memes')
    files = os.listdir(PIC_DIR)
    target = random.choice(files)
    target = os.path.join(PIC_DIR, target)
    return target