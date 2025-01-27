name = input("Enter your name: ")
phy_marks = float(input("Enter Physics marks: "))
chem_marks = float(input("Enter Chemistry marks: "))
maths_marks = float(input("Enter Mathematics marks: "))

def calculate_avg(phy_marks, chem_marks, maths_marks):
  return (phy_marks+chem_marks+maths_marks)/3

report_card = f"""
Report Card
----------------------
Name: {name}\n
Physics: {phy_marks}\n
Chemistry: {chem_marks}\n
Mathematics: {maths_marks}\n
Average: {calculate_avg(phy_marks, chem_marks, maths_marks)}"""

with open(f"{name}_report_card.txt", "w") as file:
  file.write(report_card)
