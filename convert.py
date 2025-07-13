input_text = input()
output_txt = input_text.replace("└── ", "-").replace("|","  ").replace("├──", "-")
print(output_txt)