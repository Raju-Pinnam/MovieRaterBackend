from django.utils.text import slugify

from ab_main.utils import get_rand_str, get_file_ext


def movie_image_path(instance, file):
    title = slugify(instance.title)
    filename, ext = get_file_ext(file)
    new_filename = f'{instance.title}{get_rand_str(size=3)}{ext}'
    f_path = f'movies/{title}/{new_filename}'
    return f_path


def gen_movie_slug(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
    movie_slug_exist = instance.__class__.objects.filter(slug=slug).exists()
    if movie_slug_exist:
        new_slug = f'{slug}{get_rand_str(size=5)}'
        return gen_movie_slug(instance, new_slug)
    return slug
