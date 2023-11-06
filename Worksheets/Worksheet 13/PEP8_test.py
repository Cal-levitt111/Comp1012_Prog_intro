import pycodestyle as pcs
 
fchecker = pcs.Checker("summary.py", quiet=True)
file_errors = fchecker.check_all()
style = pcs.StyleGuide()
print(f"PEP 8 coding style checking ...{file_errors} violations.")
print(style.check_files(["summary.py"]))