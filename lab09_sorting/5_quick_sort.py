def raw_input_to_dict(raw):
    raw_arr = raw.split(",")
    name, numerical_values = raw_arr[0], raw_arr[1:]
    wins, loss, draws, scored, conceded = list(map(int, numerical_values))

    return {
        "name": name,
        "wins": wins,
        "loss": loss,
        "draws": draws,
        "scored": scored,
        "conceded": conceded
    }

def print_football_club(football_club):
    print(f"['{football_club['name']}', {{'points': {football_club['points']}}}, {{'gd': {football_club['gd']}}}]")

def get_compare_values(dict_input):
    football_club = { "name": dict_input["name"] }

    football_club["points"] = dict_input["wins"] * 3 + dict_input["draws"]
    football_club["gd"] = dict_input["scored"] - dict_input["conceded"]

    return football_club

def compare(a, operator, b):
    commands = {
        ">" : lambda x, y : x > y,
        "<" : lambda x, y : x < y,
        ">=": lambda x, y : x >= y,
        "<=": lambda x, y : x <= y,
        "==": lambda x, y : x == y,
    }

    if a["points"] == b["points"]:
        return commands[operator](a["gd"], b["gd"])
    
    return commands[operator](a["points"], b["points"])

def partition(arr, low, high):
    pivot = arr[high]

    i = (low-1)

    for k in range(low, high):
        if compare(arr[k], ">", pivot):
            i += 1
            arr[i], arr[k] = arr[k], arr[i]
    
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1
    
def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        
        quick_sort(arr, low, pivot-1)
        quick_sort(arr, pivot+1, high)
    

arr = list(map(raw_input_to_dict, input("Enter Input : ").split("/")))
arr = list(map(get_compare_values, arr))

quick_sort(arr, 0, len(arr)-1)

print("== results ==")
for ele in arr:
    print_football_club(ele)