""" #PEP 8 PYTHON ENHANCEMENT PROPOSAL  MAKE OUR CODE LOOK GOOD
#pepes.python .pep 8 org
#"readabiity counts" it all about consitency 
#indentattion and tabs,spaces and maximun line and blank lines and imports and furthermore

pylint :
it a linter reed from top to bottom 
pip install pylint

 pylint style.py
************* Module style
style.py:27:0: C0206: Consider iterating with .items() (consider-using-dict-items)

-----------------------------------
Your code has been rated at 6.67/10

pycodestyle  form pep8
it can do reformating style  it fix it 
pycodestyle style.py
style.py:3:45: W291 trailing whitespace
style.py:4:80: E501 line too long (90 > 79 characters)
style.py:7:36: W291 trailing whitespace
style.py:12:80: E501 line too long (82 > 79 characters)
style.py:18:39: W291 trailing whitespace
style.py:23:80: E501 line too long (121 > 79 characters)
style.py:31:19: E231 missing whitespace after ':'
style.py:31:27: E231 missing whitespace after ','
style.py:31:35: E231 missing whitespace after ':'

    

Black: it is opininated
pip install black"""
# we have nore dicts than screen
""" students = {"name":"veera","name1":"sri","nam":"kim","nme":"era","ame":"jyo","kame":"ve","fame":"ion","iame":"veera"}
for student in students:
    print(student,students[student]) """

for student in students:
    print(student, students[student])

# so we use black style.py
students = {"name":"veera","name1":"sri","nam":"kim","nme":"era","ame":"jyo","kame":"ve","fame":"ion","iame":"veera"}
for student in students:
    print(student,students[student])

# it changes to 
students = {
    "name": "veera",
    "name1": "sri",
    "nam": "kim",
    "nme": "era",
    "ame": "jyo",
    "kame": "ve",
    "fame": "ion",
    "iame": "veera",
}
