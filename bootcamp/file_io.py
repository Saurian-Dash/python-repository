def read_csv(f):

    with open(f, 'r', encoding='utf8'):
        data = f.read()
        return data


def copy_and_reverse(src, dest):
    
    with open(src, 'r') as s:
        
        data = s.read()
    
    with open(dest, 'w') as d:
        
        for x in range(len(data), 0, -1):
            
            d.write(x)


def statistics(file_name):
    
    with open(file_name, 'r') as f:
        
        data = f.read()
        lines = data.split('\n')
        words = data.split()

        return {
            'lines': len(lines),
            'words': len(words),
            'characters': len(data)
        }


def find_and_replace(file_name, old, new):

    with open(file_name, 'r+', encoding='utf8') as f:

        data = f.read()
        cleaned_data = data.replace(old, new)
        f.seek(0)
        f.write(cleaned_data)
        f.truncate()


print(statistics('data\\test_text.txt'))