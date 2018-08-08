import json

fh = open('old_log.txt', 'r', encoding='utf-8')

courts_dict = []

for each in fh:
        each = each.strip()
        each_splitted = each.split(';delimiter;')

        court_name = each_splitted[0]
        court_address = each_splitted[1]

        courts_dict.append({
            'court_name' : court_name,
            'court_address' : court_address
        })

json_string = json.dumps(courts_dict, ensure_ascii=False, indent = 2)

fh = open('courts.json', 'w', encoding='utf-8')
fh.write(json_string)
fh.close()

fh.close()
