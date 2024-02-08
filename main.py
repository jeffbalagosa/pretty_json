import json


def pretty_print_json(json_input):
    if isinstance(json_input, str):
        json_object = json.loads(json_input)
    elif isinstance(json_input, dict):
        json_object = json_input
    else:
        raise ValueError("Input should be a JSON string or a dictionary.")
    return json.dumps(json_object, indent=4)


# Ask for user input
json_input = input("Enter a JSON string or a dictionary: ")
print(pretty_print_json(json_input))
