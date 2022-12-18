def text_up(func):
    def wrap(results):
        res = func(results)
        return res.upper()
    return wrap


@text_up
def get_text(results):
    results = ' '.join(results)
    return results


print(get_text(['Hello', 'World', 'I', 'am', 'Yury']))
