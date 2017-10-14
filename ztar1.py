__author__ = 'Kalyan'

max_marks = 20

problem_notes = '''
You are given an list  of (student, marks) tuples.
You job is to sort by student marks and return a list of (mark, [list of students who got that mark])
tuples in descending order of marks. The order of students in the sublist should follow the
order in original list.

e.g if input is [("karthik", 20), ("mohan", 10), ("ajay", 20), ("sita", 30)]
then result should be [(30, ["sita"]), (20, ["karthik", "ajay"]), (10, ["mohan"])].

Use the builtin python data structures and functions to solve this problem.

Constraints:
1. Raise a ValueError on None
2. Assume that the scores is a list with valid data otherwise
'''

def topper_sort(scores):
       unq_scores=set([x[1] for x in scores])
       unq_scores=sorted(list(unq_scores),reverse=True)
       z=[(j,[l[0] for l in scores if l[1]==j ]) for j in unq_scores]
       print z
       return z

assert [(30, ["sita"]), (20, ["karthik", "ajay"]), (10, ["mohan"])]==topper_sort([("karthik", 20), ("mohan", 10), ("ajay", 20), ("sita", 30)])

