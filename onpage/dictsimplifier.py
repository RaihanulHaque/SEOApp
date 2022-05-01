

def simplify(obj):
    """Simplifies multi level dictionary extracted from json"""
    simplified_obj = {}

    def extract(obj):
        for key in obj:
            if isinstance(obj[key], (dict, list)):
                if isinstance(obj[key], dict):
                    extract(obj[key])
                if isinstance(obj[key], list):
                    for elem in obj[key]:
                        if isinstance(elem, dict):
                            extract(elem)
                        else:
                            simplified_obj[key] = obj[key]
            else:
                simplified_obj[key] = obj[key]
        return simplified_obj

    return extract(obj)
