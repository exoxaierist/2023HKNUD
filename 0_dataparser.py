# sample code for parsing data of all project, student information
import csv
import os
import re

# directories
dir_csv_id = "/X/idtest.csv"
dir_csv_profile = "/X/profilelist.csv"
dir_csv_project = "/X/csvs"
dir_target_project = "/projects"
dir_target_profile = "/profiles"
dir_img_src = "/image/image_project"

html_archive = str("archive.html")
html_students = str("students.html")

id_list = []
id_dict = {}
project_list = {}
student_list = {}
cwd = os.getcwd()

# get html snippets
with open ("X/html_source/project_comp_header.txt",'r',encoding='UTF-8') as file:
    html_project_comp_header = file.read()
with open ("X/html_source/project_comp_sub_header.txt",'r',encoding='UTF-8') as file:
    html_project_comp_sub_header = file.read()
with open ("X/html_source/project_comp_description.txt",'r',encoding='UTF-8') as file:
    html_project_comp_description = file.read()
with open ("X/html_source/project_comp_youtube.txt",'r',encoding='UTF-8') as file:
    html_project_comp_youtube = file.read()
with open ("X/html_source/project_comp_vimeo.txt",'r',encoding='UTF-8') as file:
    html_project_comp_vimeo = file.read()
with open ("X/html_source/project_comp_image.txt",'r',encoding='UTF-8') as file:
    html_project_comp_image = file.read()
with open ("X/html_source/project_top.txt",'r',encoding='UTF-8') as file:
    html_project_top = file.read()
with open ("X/html_source/project_bottom.txt",'r',encoding='UTF-8') as file:
    html_project_bottom = file.read()
with open ("X/html_source/project_student.txt",'r',encoding='UTF-8') as file:
    html_project_student = file.read()

class Project:
    title: str
    slogan: str
    desc: str
    lecture: str
    category: str
    sub_category: list

    students: list
    student_id: list
    student_role: list
    comp: list
    def __init__():
        pass
    def __init__(self,lecture,name,slogan,desc,students,student_id,student_role,comp):
        self.lecture = lecture
        self.title = name
        self.slogan = slogan
        self.desc = desc
        self.students = students
        self.student_id = student_id
        self.student_role = student_role
        self.comp = comp

class Student:
    name: str
    desc: str
    email: str
    career: str
    interests: list
    insta: str
    behance: str
    other1: str
    other2: str
    projects: list
    def __init__():
        pass
    def __init__(self,name,desc,email,career,interests,insta,behance,other1,other2,projects):
        self.name = name
        self.desc = desc
        self.email = email
        self.career = career
        self.interests = interests
        self.insta = insta
        self.behance = behance
        self.other1 = other1
        self.other2 = other2
        self.projects = projects

# read idlist.csv
with open(dir_csv_id.removeprefix('/'),'r',encoding='UTF-8') as file:
    rawdata_id = csv.reader(file)
    rawdata_id = list(rawdata_id)

# make idlist
for i in range(5,len(rawdata_id)):
    id_list.append(rawdata_id[i][1])
id_dict = {rawdata_id[i][1] : rawdata_id[i][2] for i in range(5,len(rawdata_id))}

# parse profile csv file
with open(dir_csv_profile.removeprefix('/'),'r',encoding='UTF-8') as file:
    rawdata_profile = csv.reader(file)
    rawdata_profile = list(rawdata_profile)

# make student list
for i in range(1,len(rawdata_profile)):
    student_list[rawdata_profile[i][2]] = Student(
        self=rawdata_profile[i][1],
        name=rawdata_profile[i][3],
        desc=rawdata_profile[i][4],
        email=rawdata_profile[i][5],
        career=rawdata_profile[i][6].split(','),
        interests=rawdata_profile[i][7],
        insta=rawdata_profile[i][8],
        behance=rawdata_profile[i][9],
        other1=rawdata_profile[i][10],
        other2=rawdata_profile[i][11].replace(' ','').split(','))
    for j in range(0,len(student_list[rawdata_profile[i][2]].interests)):
        student_list[rawdata_profile[i][2]].interests[j] = student_list[rawdata_profile[i][2]].interests[j].strip()



# make projects list
for filename in os.listdir(cwd + dir_csv_project +"/"):
    if filename.removesuffix(".csv") in id_list:
        _instance = Project()
        _id = filename.removesuffix(".csv")
        # read csv file into list
        with open( dir_csv_project.removeprefix('/') + '/' + filename,'r',encoding="UTF-8") as file:
            rawdata_project = csv.reader(file)
            rawdata_project = list(rawdata_project)
        _instance.title = rawdata_project[3][1]
        _instance.category = id_dict[_id]
        _instance.slogan = rawdata_project[4][1]
        _instance.lecture = rawdata_project[1][1]
        _instance.desc = rawdata_project[5][1]
        # make students list
        students = []
        student_role = []
        student_id = []
        for i in range(4,len(rawdata_project[0])):
            students.append(rawdata_project[0][i])
            student_id.append(rawdata_project[1][i])
            student_role.append(rawdata_project[2][i])
            if rawdata_project[1][i] in student_list.keys:
                student_list[rawdata_project[1][i]].projects.appen(rawdata_project[1][i]);
        _instance.students = students
        _instance.student_role = student_role
        _instance.student_id = student_id
        # make comp list
        comp = []
        for i in range(9,len(rawdata_project)):
            comp.append((rawdata_project[i][0], rawdata_project[i][1]))
        _instance.comp = comp
        # make project dictionary
        project_list[filename.removesuffix(".csv")] = _instance

with open("X/html_source/archive_project.txt",'r',encoding='UTF-8') as file:
    html_archive_project = file.read()

def make_project_item(id):
    _info = project_list[id]
    filterList = "filter" + id[:2].upper()
    return html_archive_project.\
        replace("$DESC",_info.slogan).\
        replace("$STUDENTS",' '.join(_info.students)).\
        replace("$TITLE",_info.title).\
        replace("$CATEGORY",_info.category).\
        replace("$ID",id).\
        replace("$FILTER",filterList)







# edit archive html file
with open(html_archive,'r',encoding='UTF-8') as file:
    html = file.read()

_project_items:str
for key in project_list.keys:
    _project_items += make_project_item(key)
    
html = re.sub(r"<!--PROJECT LIST START-->(.*?)<!--PROJECT LIST END-->",f"<!--PROJECT LIST START-->{_project_items}<!--PROJECT LIST END-->",html,flags=re.DOTALL)
with open(html_archive,'w',encoding='UTF-8') as file:
    file.write(html)



# edit students html file
with open(html_archive,'r',encoding='UTF-8') as file:
    html = file.read()

_student_items:str

html = re.sub(r"<!--STUDENT LIST START-->(.*?)<!--STUDENT LIST END-->",f"<!--STUDENT LIST START-->{_student_items}<!--STUDENT LIST END-->",html,flags=re.DOTALL)
with open(html_archive,'w',encoding='UTF-8') as file:
    file.write(html)


# create project html files
for key, info in project_list.items():
    print("writing project : ", key)
    html = open(dir_target_project.removeprefix('/') + '/' + key + ".html",'w',encoding="UTF-8")

    students_html:str = ""
    for i,name in enumerate(info.students):
        students_html += html_project_student.replace("$STUDENT",name)
    html.write(html_project_top.
        replace("$CLASS",info.lecture).
        replace("$TITLE",info.title).
        replace("$MOTO",info.slogan).
        replace("$DESC",info.desc).
        replace("$STUDENTS_HTML", students_html).
        replace("$ID",key))

    # composition
    for section in info.comp:
        if section[0] == "header":
            # header
            html.write(html_project_comp_header.replace("$CONTENT",section[1]))
        elif section[0] == "sub_header":
            # sub_header
            html.write(html_project_comp_sub_header.replace("$CONTENT",section[1]))
        elif section[0] == "description":
            # description
            html.write(html_project_comp_description.replace("$CONTENT",section[1]))
        elif section[0] == "image":
            # image
            html.write(html_project_comp_image.replace("$CONTENT", section[1]).replace("$ID",key))
        elif section[0] == "youtube":
            # youtube
            html.write(html_project_comp_youtube.replace("$CONTENT",section[1]))
        elif section[0] == "vimeo":
            # vimeo
            html.write(html_project_comp_vimeo.replace("$CONTENT",section[1]))
        
    # add students
    for index, studentid in enumerate(info.student_id):
        snippet = html_project_student
        snippet = snippet.replace("$NAME",info.students[index]).replace("$ROLE",info.student_role[index] if len(info.students)>1 else "").replace("$LINK",dir_target_profile + '/' + studentid + ".html")

    # get releated projects
    related_projects_id = []
    for _student_id in info.student_id:
        for _project_id in student_list[_student_id].projects:
            if _project_id not in related_projects_id:
                related_projects_id.append(_project_id)
    
    related_projects:str
    for _id in related_projects_id:
        related_projects += make_project_item(_id)

    # add footer and other stuffs
    html.write(html_project_bottom)



# create profile html files

for key,info in student_list:
    print("writing profile : ", key)
    html = open(dir_target_profile.removeprefix('/') + '/' + key + ".html",'w',encoding="UTF-8")

    

print("-----DONE!-----")