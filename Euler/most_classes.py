course_dict = {'Jason Siefer':['Ruby', 'Rails', 'Tech found'],
               'Kenneth Love':['Python', 'Python basics'],
               'Scott Riggs':['Labview', 'Python']
               }

def courses(some_dict):
  class_list=[]
  for list_of_courses in some_dict.values():
    for items in list_of_courses:
      class_list.append(items)
  return class_list

def most_classes(course_dict):
  max_count = 0
  for key in course_dict:
      if len(course_dict[key]) > max_count:
          overworked_teacher = key
          max_count = len(course_dict[key])
  return overworked_teacher

def num_teachers(course_dict):
  count = 0
  for key in course_dict:
      count = count + 1
  return count

def stats(course_dict):
  teacher_info = []
  all_teachers = []
  for key in course_dict:
      teacher_info = [key, len(course_dict[key])]
      all_teachers.append(teacher_info)
  return all_teachers

print courses(course_dict)
	