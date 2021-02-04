def is_valid_parentheses(string: str) -> bool:
    len_string = len(string)
    if len_string % 2 != 0:
        return False
    equal = {
        '(': ')',
        '[': ']',
        '{': '}',
    }
    for i in range((len_string // 2)):
        try:
            if equal[string[i]] != string[-i - 1]:
                return False
        except KeyError:
            return False
    return True


if __name__ == '__main__':
    tests = (
        ('({[]})', True),
        ('([])', True),
        (')[](', False),
        ('([(]])', False),
        ('(([])', False),
        ('[(])', False),
        ('(((()))', False),
    )
    for subject, result in tests:
        assert is_valid_parentheses(subject) == result, print(subject, result)
