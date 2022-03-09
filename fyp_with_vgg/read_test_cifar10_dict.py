import json 

def read_labels(json_path = "test_cifar10_labels.json"):
    with open(json_path,'r', encoding='UTF-8') as f:
        load_dict = json.load(f)
    return  load_dict

# label_list = ['airplane', 'automobile', 'bird', 'cat', 'deer','dog', 'frog', 'horse', 'ship','truck']
# print(label_list[load_dict['510016.jpg']])
    



