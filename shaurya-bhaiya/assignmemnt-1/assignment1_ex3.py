import pandas as pd

import pandas as pd

file_id = "1OekIEbM6phQNRAZZOfh4optv5Cjh_iQG"
file_url = f"https://drive.google.com/uc?id={file_id}"
# showed an error while directly copying the shareable link; hence used this format suggested by chatgpt. didnt quite understand though

file_data = pd.read_csv(file_url)

categories = []
for value in file_data.iloc[:,0]:  # assuming the categories are in the first column
    if value < 0.3:
        categories.append("Low")
    elif 0.3 <= value < 0.7:
        categories.append("Medium")
    else:
        categories.append("High")
file_data['Category'] = categories
new_file_data = file_data[file_data["Category"]!="Low"]
new_file_data.to_csv("new_file_data.csv", index=False)
