import csv

file_path = r"E:\Dropbox\Management Accounts (P&L Template)\Live Data\Budget\2019_NTST_PNDL_BDGT.csv"
output_path = r"C:\Users\Saurian\python\bootcamp\data\data.csv"


def main():
    help(quote_all)
    quote_all(file_path, output_path)


def quote_all(in_path, out_path):
    '''
    Reads .csv data from input_path, encloses all values in
    "double-quotes", then writes cleaned data to output_path.

    ::: Params :::
    in_path: Path to source file
    out_path: Path to output file
    '''
    with open(in_path, 'r', encoding='utf8') as in_file:

        print(f'Reading data from: {in_path}...')
        csv_data = csv.reader(in_file)

        with open(out_path or 'data.csv', 'w', encoding='utf8', newline='') as out_file:

            print(f'Writing data to: {out_path}...')
            csv_writer = csv.writer(out_file, quoting=csv.QUOTE_ALL)

            for row in csv_data:
                csv_writer.writerow(row)

    print('Done!')


if __name__ == '__main__':

    main()