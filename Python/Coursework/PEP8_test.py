import pycodestyle as pcs
 
fchecker = pcs.Checker("function_exercise_q4.py", quiet=True)
file_errors = fchecker.check_all()
style = pcs.StyleGuide()
print(f"PEP 8 coding style checking ...{file_errors} violations.")
print(style.check_files(["function_exercise_q4.py"]))