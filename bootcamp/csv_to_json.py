import csv
import json

source_file = open('scientists.csv', 'r')

def csv_to_json(f):
  
  with f:

    fields = next(csv.reader(f, delimiter=','))
    values = csv.DictReader(f, fields, delimiter=',')
    headers = [row['name'] for row in values]
    f.seek(0)
    output = json.dumps(
      [
        {
          'name':        row['name'],
          'field':       row['field'],
          'born':        row['born'],
          'nobel_prize': row['nobel_prize'],
          'extract_ref': row['name'].replace(' ', '_').lower()
        } for row in values
      ]
    )

  return headers, output


print(csv_to_json(source_file))