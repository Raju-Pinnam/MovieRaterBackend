import os, random, string


def get_rand_str(size=25, chars=string.ascii_letters + string.digits):
    r_str = ''.join(random.choice(chars) for _ in range(size))
    return r_str


def get_file_ext(file):
    basename = os.path.basename(file)
    return os.path.splitext(basename)
