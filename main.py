def merge_lists(list1,list2):
    final_dict = {}
    for x in list1:
        user_id = x["id"]
        if user_id in final_dict.keys():
            for sub_keys in x.keys():
                if sub_keys == "id":
                    continue
                else:
                    final_dict[user_id].append([sub_keys, x[sub_keys]])
        else:
            final_dict[user_id] = []
            for sub_keys in x.keys():
                if sub_keys == "id":
                    continue
                else:
                    final_dict[user_id].append([sub_keys, x[sub_keys]])
    for x in list2:
        user_id = x["id"]
        if user_id in final_dict.keys():
            for sub_keys in x.keys():
                if sub_keys == "id":
                    continue
                else:
                    final_dict[user_id].append([sub_keys, x[sub_keys]])
        else:
            final_dict[user_id] = []
            for sub_keys in x.keys():
                if sub_keys == "id":
                    continue
                else:
                    final_dict[user_id].append([sub_keys, x[sub_keys]])
    final_list = []
    for x in final_dict.keys():
        temp_dict = {}
        temp_dict["id"] = x
        for elements in final_dict[x]:
            temp_dict[elements[0]] = elements[1]
        final_list.append(temp_dict)
    return final_list

list1 = [
    {"id": "1", "name": "Shrey", "age": 25},
    {"id": "3", "age": 10, "name": "Hello"},
    {"id": "2", "name": "World", "age": 24},
]
list2 = [
    {"id": "1", "marks": 100},
    {
        "id": "3",
        "marks": 90,
        "roll_no": 11,
        "extra_info": {
            "hello": "world",
        },
    },
]
final_list = merge_lists(list1,list2)
print(final_list)