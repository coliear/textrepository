from csv import DictReader

data_rdr = DictReader(open('C:/Users/何长乐/Desktop/11/mn.csv', 'rt', encoding="utf-8"))
header_rdr = DictReader(open('C:/Users/何长乐/Desktop/11/mn_headers.csv', 'rt', encoding="utf-8"))
data_rows = [d for d in data_rdr]
header_rows = [h for h in header_rdr]
print(data_rows[:5])
print(header_rows[:5])
