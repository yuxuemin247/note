import json

with open("rs.json", "r", encoding="utf-8") as f:
    load_dict = json.load(f)

files_all = load_dict['category_kvs']

dic = {}
for fields in files_all:
    for k in fields['fields']:
        for i in k['file_quad_areas']:
            if not i.get('file_uri'):
                continue
            if i.get('file_uri') in dic:
                dic[i.get('file_uri')] += 1
            else:
                dic[i.get('file_uri')] = 0

    for x in fields["tables"]:
        for y in x["rows"]:
            for z in y["column_fields"]:
                for w in z["file_quad_areas"]:
                    if not w.get('file_uri'):
                        continue
                    if w.get('file_uri') in dic:
                        dic[w.get('file_uri')] += 1
                    else:
                        dic[w.get('file_uri')] = 0

print(dic)
