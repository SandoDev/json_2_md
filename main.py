import re
import json
"""
Datatypes json

1. string
2. number
3. boolean
4. null
5. object
6. array
"""


def get_data_json(path_file: str):
    input_file_json = open(path_file, "r")
    dict_json = json.load(input_file_json)
    return dict_json


def form_head(len_head):
    head_num = ''.join('#' for _ in range(len_head))
    return head_num + ' '


def format_value(value, len_head=1):
    """
    Es necesario utilizar recursividad para ajustar este metodo
    """
    final_str = ''
    len_head += 1
    if isinstance(value, list):
        for obj in value:
            final_str += '* '+str(obj)+'\n'
        if final_str == '':
            final_str = '[]'
    elif isinstance(value, dict):
        head_num = form_head(len_head)
        for key, value_dict in value.items():
            final_str += head_num + key + '\n'
            final_str += format_value(value_dict, len_head)+'\n'
        if final_str == '':
            final_str = '{}'
    else:
        final_str = str(value) + '\n'
    return final_str


def main(file_name_input, file_name_output):
    dict_json = get_data_json(file_name_input)
    output_file_md = open(file_name_output, "w")
    for key, value in dict_json.items():
        output_file_md.write("# " + key + '\n')
        output_file_md.write(format_value(value))
        output_file_md.write('\n')
    output_file_md.close()


if __name__ == "__main__":
    file_name_input = "test_files/openapi.json"
    #file_name_input = "test_files/example.json"
    file_name_output = "test_files/output_open.md"
    #file_name_output = "test_files/output.md"
    main(file_name_input, file_name_output)
