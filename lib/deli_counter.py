KATZ_DELI = []
OTHER_DELI = ["Logan", "Avi", "Spencer"]
ANOTHER_DELI = ["Amanda", "Annette", "Ruchi", "Jason", "Logan", "Spencer", "Avi", "Joe", "Rachel", "Lindsey"]

line_text = "The line is currently: "
next_in_line_alert = "Currently serving "
empty_line_alert = "There is nobody waiting to be served!"

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
    print(output)
      

def take_a_number(line, name):
  formatted = []
  line.append(name)
  for index, l in enumerate(line):
    p = f"{index}. {l}"
    formatted.append(p)
    position = len(formatted) 
  print(f"Welcome, {name}. You are number {position} in line.")


def now_serving(line):
  if len(line) == 0:
    print(empty_line_alert)
  else:
    current = line.pop(0)
    print(f"{next_in_line_alert}{current}.")


print(now_serving(OTHER_DELI)) 

 
