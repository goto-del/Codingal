student_data = {"id1": {"name": ["Sara"],"class": ["V"],"subject_intergration": ["English, Maths, Science"]},
"id2" :  {"name": ["David"],"class": ["V"],"subject_intergration" : ["English, Maths, Science"]},
"id3" :  {"name": ["Sara"],"class": ["V"],"subject_intergration" : ["English, Maths, Science"]},
"id4 ":  {"name": ["Suryva"],"class": ["V"],"subject_intergration" : ["English, Maths, Science"]},        
}

result = {}
for key, value in student_data.items():
    if value not in result.values():
        result[key] = value

print(result)