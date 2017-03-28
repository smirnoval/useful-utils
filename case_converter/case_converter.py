"""Case converter."""


def snake_case_to_camel_case(snake_str):
    components = snake_str.split('_')
    return components[0] + "".join(x.title() for x in components[1:])


def camel_case_to_snake_case(camel_str):
    result = ''
    for i in camel_str:
        if i.isupper():
            result += '_' + i.lower()
        else:
            result += i
    return result


def dict_key_to_snake_case_key(dictionary):
    new_dictionary = {}
    for key, value in dictionary.items():
        new_dictionary[camel_case_to_snake_case(key)] = value
    return new_dictionary


def dict_key_to_camel_case_key(dictionary):
    new_dictionary = {}
    for key, value in dictionary.items():
        new_dictionary[snake_case_to_camel_case(key)] = value
    return new_dictionary


if __name__ == '__main__':
    snake_str = 'case_converter_test'
    print(snake_case_to_camel_case(snake_str))
    camel_str = 'caseConverterTest'
    print(camel_case_to_snake_case(camel_str))
    d = {'caseConverterTest': 1, 'caseConverterTest1': 2}
    k = dict_key_to_snake_case_key(d)
    print(k)
    k = dict_key_to_camel_case_key(d)
    print(k)
