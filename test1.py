from csv import reader

data_rdr = reader(open('mn.csv', 'rt',encoding="utf-8"))
header_rdr = reader(open('mn_headers_updated.csv', 'rt',encoding="utf-8"))
data_rows = [d for d in data_rdr]
header_rows = [h for h in header_rdr if h[0] in data_rows[0]]
all_short_headers = [h[0] for h in header_rows]
print('data_rows', data_rows[0])
print('header_rows:',header_rows)
skip_index = []
final_header_rows = []
# for header in data_rows[0]:
#     if header not in all_short_headers:
#         index = data_rows[0].index(header)
#         skip_index.append(index)
#     else:
#         for head in header_rows:
#             if head[0] == header:
#                 final_header_rows.append(head)
#                 break
# new_data = []
# for row in data_rows[1:]:
#     new_row = []
#     for i, d in enumerate(row):
#         if i not in skip_index:
#             new_row.append(d)
#     new_data.append(new_row)
# zipped_data = []
# for drow in new_data:
#     zipped_data.append(zip(final_header_rows, drow))
