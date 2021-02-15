from difflib import Differ
import json
import requests
def add_tags(tag, word):
    return "<%s>%s</%s>" % (tag, word, tag)

def lambda_handler():
    #response_1 = requests.get("http://api.open-notify.org/astros.json")
    response_1 = {"fruit": "Apple","size": "Large","color": "Red"}
    #d1 = json.loads(response_1)
    #response_2 = requests.get("http://api.open-notify.org/astros.json")
    response_2 = {"fruit": "Apple","size": "Large","color": "Blue"}
    #d2 = json.loads(response_2)
    dif = Differ()
    df = list(dif.compare(str(response_1).split(), str(response_2).split()))

    final_output = []
    for i in range(len(df)):
        df[i] = ''.join(str(df[i]).split())
    # Add the strike though and Underline to documents
    for i in range(len(df)):
        if (ord(df[i][0]) == 43):
            # print(add_tags('i', df[i].replace("+","")))
            final_output.append(add_tags('ins', df[i].replace("+", "")))
        elif (ord(df[i][0]) == 45):
            # print(add_tags('i', df[i].replace("-","")))
            final_output.append(add_tags('del', df[i].replace("-", "")))
        elif (ord(df[i][0]) == 63):
            # print(add_tags('i', df[i].replace("?","")))
            print("")
        else:
            final_output.append(df[i])
        # Print Result
    new_output = ' '.join(final_output)
    final_output_str = ''
    # Make color combinations for New and Old text and write in html file.
    new_output = new_output.replace('<ins>', '<font color = "green">')
    new_output = new_output.replace('</ins>', '</font>')
    new_output = new_output.replace('<del>', '<span style="color: red"><del>')
    new_output = new_output.replace('</del>', '</del></span>')
    new_output = (new_output.replace("'", '"'))
    new_output = (new_output.replace("True", 'true'))
    new_output = (new_output.replace("False", 'false'))
    print(new_output)
    return {
        'statusCode': 200,
        'body': json.dumps(new_output)
    }
print(lambda_handler())
