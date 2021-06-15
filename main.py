import re
import json
from models import TestModel
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


def form_json_model():
    schema_json = TestModel.schema_json()
    name_file_output = 'test_files/' + TestModel.__name__ + '.json'
    output_file_json = open(name_file_output, "w")
    output_file_json.write(schema_json)
    output_file_json.close()
    return name_file_output


def run_conversion(file_name_input, file_name_output):
    dict_json = get_data_json(file_name_input)
    output_file_md = open(file_name_output, "w")
    output_file_md.write("# " + output_file_md.name + '\n')
    for key, value in dict_json.items():
        output_file_md.write("## " + key + '\n')
        output_file_md.write(format_value(value, len_head=2))
        output_file_md.write('\n')
    output_file_md.close()


def main():
    # step 1
    file_name_input = form_json_model()

    # step 2
    file_name_output = "docs/test_page.md"
    run_conversion(file_name_input, file_name_output)


if __name__ == "__main__":
    main()
