def bayes(data, name, index, total_yes):
   
    name_C = 0
    yes_c = 0

    for row in data:
        if row[index] == name:
            name_C += 1
            if row[-1] == "yes":
                yes_c += 1

    return (yes_c + 1) / (total_yes + 2)


def bayesi(data, name, index, total_no):
   
    name_C = 0
    no_c = 0
+
    for row in data:
        if row[index] == name:
            name_C += 1
            if row[-1] == "no":
                no_c += 1

    return (no_c + 1) / (total_no + 2)  



data = [
    ["sunny", "hot", "high", "False", "no"],
    ["sunny", "hot", "high", "True", "no"],
    ["overcast", "hot", "high", "False", "yes"],
    ["rainy", "mild", "high", "False", "yes"],
    ["rainy", "cool", "normal", "False", "yes"],
    ["rainy", "cool", "normal", "True", "no"],
    ["overcast", "cool", "normal", "True", "yes"],
    ["sunny", "mild", "high", "False", "no"],
    ["sunny", "cool", "normal", "False", "yes"],
    ["rainy", "mild", "normal", "False", "yes"],
    ["sunny", "mild", "normal", "True", "yes"],
    ["overcast", "mild", "high", "True", "yes"],
    ["overcast", "hot", "normal", "False", "yes"],
    ["rainy", "mild", "high", "True", "no"]
]


total_yes = sum(1 for row in data if row[-1] == "yes")
total_no = len(data) - total_yes

p_yes = total_yes / len(data)
p_no = total_no / len(data)

dic = {}

for i in range(len(data[0]) - 1): 
    for row in data:
        key = row[i]
        if key not in dic:
            dic[key] = (
                bayes(data, key, i, total_yes), 
                bayesi(data, key, i, total_no)
            )

v = input("Enter features (space-separated): ").split()


v_yes, v_no = p_yes, p_no

for feature in v:
    if feature in dic:
        v_yes *= dic[feature][0]
        v_no *= dic[feature][1]


print(f"P(yes): {v_yes:.6f}, P(no): {v_no:.6f}")
print("Prediction:", "Yes" if v_yes > v_no else "No")
 
