import os, random
DIR = os.path.dirname(os.path.abspath(__file__))
def get():
    PIC_DIR = os.path.join(DIR, 'memes')
    files = os.listdir(PIC_DIR)
    target = random.choice(files)
    target = os.path.join(PIC_DIR, target)
    return target
def venom():
    VID_DIR = os.path.join(DIR, 'videos', 'Venom.mp4')
    return VID_DIR
