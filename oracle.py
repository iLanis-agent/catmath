import json, math

def tenths(x):
    return math.floor(x * 10 + 0.5) / 10

def fixed1(x):
    return f"{tenths(x):.1f}"

def box_truth(cats):
    if cats <= 0:
        raise ValueError("the cat count must be above zero")
    boxes = cats + 1
    cat_word = "cat" if cats == 1 else "cats"
    box_word = "box" if boxes == 1 else "boxes"
    verb = "asks" if cats == 1 else "ask"
    return f"{cats} {cat_word} {verb} {boxes} litter {box_word} honestly."

def litter_truth(cats):
    if cats <= 0:
        raise ValueError("the cat count must be above zero")
    pounds = tenths(cats * 20)
    bags = tenths(pounds / 40)
    cat_word = "cat goes" if cats == 1 else "cats go"
    return f"{cats} {cat_word} through {fixed1(pounds)} pounds a month, {fixed1(bags)} of a 40-pound bag honestly."

def depth_truth(inches):
    if inches <= 0:
        raise ValueError("the depth must be above zero")
    d = tenths(inches)
    if d < 2:
        band = "too shallow to bury, and the smells win"
    elif d <= 3:
        band = "right in the sweet spot"
    else:
        band = "deep enough to waste and track"
    return f"{fixed1(d)} inches of litter reads {band} honestly."

cases = []

def add(fn_name, args):
    try:
        fn = {"boxTruth": box_truth, "litterTruth": litter_truth, "depthTruth": depth_truth}[fn_name]
        cases.append({"fn": fn_name, "args": args, "result": fn(*args)})
    except ValueError as e:
        cases.append({"fn": fn_name, "args": args, "error": str(e)})

# boxTruth
add("boxTruth", [1])    # 1 cat asks 2 boxes
add("boxTruth", [2])    # 3 boxes
add("boxTruth", [4])    # 5 boxes
add("boxTruth", [0])    # error
# litterTruth
add("litterTruth", [1]) # 20.0 pounds, 0.5 bag
add("litterTruth", [2]) # 40.0 pounds, 1.0 bag
add("litterTruth", [3]) # 60.0 pounds, 1.5 bags
add("litterTruth", [0]) # error
# depthTruth
add("depthTruth", [2.5])  # sweet spot
add("depthTruth", [1.5])  # too shallow
add("depthTruth", [2])    # edge -> sweet spot
add("depthTruth", [3])    # edge -> sweet spot
add("depthTruth", [4])    # too deep
add("depthTruth", [0])    # error

with open("expected.json", "w") as f:
    json.dump(cases, f, indent=2)
    f.write("\n")
print(f"{len(cases)} cases written")
for c in cases:
    print(c["fn"], c["args"], "->", c["result"] if "result" in c else "ERR: " + c["error"])
