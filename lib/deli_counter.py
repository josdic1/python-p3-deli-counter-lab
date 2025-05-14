people = ["Amanda", "Annette", "Ruchi", "Jason", "Logan", "Spencer", "Avi", "Joe", "Rachel", "Lindsey"]

katz_deli = ["Ruchi", "Jason"]
line_text = "The line is currently: "


def line(line_names):
  if len(line_names) == 0:
    print("The line is currently empty.")
  elif len(line_names) > 0:
    updated_line = [] 
    updated_str = [] 
    for index, name in enumerate(line_names):
      updated_line.append(f"{index + 1}. {name}")
    updated_str = " ".join(updated_line)
    output = f"{line_text}{updated_str}"
    line_info = output
    print(line_info)
      
def take_a_number(line, name):
  add_name = line.append(name)
  print(add_name)

# f"Welcome, {name}. You are number {index} in line."
print(take_a_number(katz_deli, "Paul"))

def now_serving():
    pass
 
