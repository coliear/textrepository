from csv import DictReader
import csv
data_rdr = DictReader(open('mn.csv', 'rt', encoding="utf-8"))
header_rdr = DictReader(open('mn_headers.csv', 'rt', encoding="utf-8"))
data_rows = [d for d in data_rdr]
header_rows = [h for h in header_rdr]
print(data_rows[:5])
print(header_rows[:5])
for data_dict in data_rows[:5]:
    for a, b in data_dict.items():
           print(a, b)