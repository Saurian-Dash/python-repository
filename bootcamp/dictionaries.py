# Create placeholder dictionary

fields = ('name', 'age', 'city')
values = ['saur', 'dash', 40]

def main():

    output_01 = dict_from_keys(fields)
    output_02 = fill_template(output_01, values)
    print(output_02)

    output_03 = dict_from_keys(['id', 'description', 'currency', 'amount'])
    output_04 = fill_template(output_03, [123, 'Gadget 01', 'GBP', 199.99])
    print(output_04)


def dict_from_keys(*args):

    template = dict.fromkeys(*args, None)
    return template


def fill_template(tem, *args):

    for key, val in zip(tem.keys(), *args): 
        tem[key] = val

    return tem


if __name__ == '__main__':
    main()