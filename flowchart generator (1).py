from pyflowchart import Flowchart

with open('Mazegenerator.py') as f:
    code = f.read()

fc = Flowchart.from_code(code)
print(fc.flowchart())