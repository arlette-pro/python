# 1. Update Values in Dictionaries and Lists

x = [ [5,2,3], [10,8,9] ] 
# 1. Change the value of 10 in x to be 15
x[1][0] = 15
print(x)

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
# 2. change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]["last_name"] = "Bryant"
print(students)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# 3. change value 20 in  to 30
z[0]['y'] = 30
print(z)



""" 2. iterate Through a List of Dictionaries- create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops
through each dictionary in the list and prints each key and associated value.
"""

def iterateDictionary(some_list):
    for dictionary in some_list:
       for key, val in dictionary.items():
         print(key, " - ", val)
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students) 


"""3. Get Values From a list Dictionaries
Create a function iterateDictionay(key_name, some_list) that, given a list of dictionaries and a key name,
the function prints the calue stored in that key each dictionary. For example, iterateDictionary('first_name, students) should ouput
"""

def iterateDictionary2(key_name, some_list):
   for dictionary in some_list:
      if key_name in dictionary:
         print(dictionary[key_name])

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary2("first_name", students)
iterateDictionary2("last_name", students)


"""4-iterate Through a Dictionary with List values
Create a function printinfo(some_dict) that given a dictionary whose values are all list,
prints the name of each key with the size of its list, and then prints the associated values within each key's list.
"""

def printInfo(some_dict):
   for key_name, value_list in some_dict.items():
      print(len(value_list), key_name)
      for val in value_list:
           print(val)
        
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)





