# function that takes list form file splits it into a new list so that each name is in a seperate list with its contact info, and then uses a while loop to extract the names 
def split_list_n2_names(old_list, new_list, names_list):	
	x = 0
	y= 1
	while x< (len(old_list)):
		new_list.append(old_list[x].split(","))
		x+=1
	while y< (len(old_list)):
		names_list.append(new_list[y][0])
		y += 1
	return names_list

#Use the function to extract the names of the employees  list in to the names_roster list	
split_roster = []
names_roster =[]

with open("all_employees.csv", "r") as employees_file:
	roster = employees_file.read().split("\n")	

roster_names = split_list_n2_names(roster, split_roster, names_roster)

employees_file.close()

#Use the function to extract the names of the survey csv in to the names_suvey list	
split_survey =[]
names_survey = []

with open("survey.csv", "r") as survey_file:
	results = survey_file.read().split("\n")

survey_names= split_list_n2_names(results, split_survey, names_survey)

survey_file.close()

#Print the names of the employees that took the survey
for index, names in enumerate(survey_names):
	if names in roster_names:
		print "{0} took the survey! Here's her info:".format(names)
		print "Twitter:", split_survey[index+1][2]
		print "GitHub:", split_survey[index+1][3]
		print "Phone:", split_survey[index+1][1]

#Begin to update all the contacts by creating a new nested dictionary to add all contacts	
with open("all_employees.csv", "r") as employees_file:
	roster = employees_file.read().split("\n")	

new_list = []
new_dict = {}

#Create a list within a list so that Contacts and their infor are in its own list sperate from other contacts to help make a nested dictionary
x=0
while x< len(roster):
		new_list.append(roster[x].split(","))
		x+=1

y = 1

for index,items in enumerate(new_list):
	while y<len(new_list):
		items = {new_list[y][0]: {'email':new_list[y][1], 'phone': new_list[y][2], 'department':new_list[y][3], 'position':new_list[y][4]}}
		new_dict.update(items)
		y+=1

employees_file.close()

with open("survey.csv", "r") as survey_file:
	results = survey_file.read().split("\n")

survey_list =[]

a = 0
while a < len(results):
	survey_list.append(results[a].split(","))
	a+=1

z = 1

#Puts new list in a nested dictionary format
for index,items in enumerate(survey_list):
	while z<len(survey_list):
		survey_contacts = {survey_list[z][0]:{'phone':survey_list[z][1],'twitter':survey_list[z][2], 'github': survey_list[z][3]}}
		new_dict.update(survey_contacts)
		z+=1 

survey_file.close()

#Writes new csv of the employee list with updated contact info
with open('employee_list_updated.csv', 'w') as new_file:
	new_file.write('name, phone,  email, twitter, github, department, position\n')
	for contact,info in new_dict.items():
		new_file.write("{0}, {1}, {2}, {3}, {4}, {5}, {6}\n".format(contact, info['phone'], new_dict.get(contact).get('email'), new_dict.get(contact).get('twitter'), new_dict.get(contact).get('github'), new_dict.get(contact).get('department'), new_dict.get(contact).get('position') ));
	new_file.close()
	


