def isSubset(arr1,arr2):
    counter = 0
    for x in arr1:
        if(x in arr2):
            counter += 1
    return True if counter == len(arr2) else False

def courses_to_take(course_to_prereqs):
    # Fill this in.
    result = []

    while(len(result) != len(course_to_prereqs)):
        for key in course_to_prereqs:
            if(isSu bset(result,course_to_prereqs[key]) and key not in result) :
                result.append(key)

    return result


courses = {
  'CSC300': ['CSC100', 'CSC200'], 
  'CSC200': ['CSC100'], 
  'CSC100': [],
  'CSC50' : []
}
print (courses_to_take(courses))
# ['CSC100', 'CSC200', 'CSC300']