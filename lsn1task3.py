import yaml

inp_dict = {'dict_el_1': ['list_el_1', 'list_el_2', 'list_el_3'],
            'dict_el_2': 38,
            'dict_el_3': {'d3el_1': '€', 'd3el_2': 'Ё'}
}

with open('file.yaml', 'w') as f_n:
    yaml.dump(inp_dict, f_n, default_flow_style=False, allow_unicode = True)
