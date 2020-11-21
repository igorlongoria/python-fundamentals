'''
Write a decorator function that wraps text passed to it in a html <p> tag.

'''

def decorator_func(initial_func):
    def wrapper_func():
        return f'<p>{initial_func()}</p>'
    return wrapper_func


def im_a_paragraph():
    print("What's up I'm a paragraph")

paragraph = decorator_func(im_a_paragraph)
paragraph()