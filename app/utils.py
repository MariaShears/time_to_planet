# prints python datastructures as json
def pprint(output):
    print(json.dumps(output, sort_keys=True, indent=4))