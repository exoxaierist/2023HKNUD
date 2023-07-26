# sample code for parsing data of all project, student information
import csv
import os
import re

# directories
idcsv = "/X/idlist.csv"
profilecsv = "/X/profilelist.csv"
projectcsv = "/X/csvs"
image_root = "/image/image_project"
html_project_dir = "/projects"
html_profile_dir = "/profiles"

archive_html_src = str("archive.html")

idlist = []
project_dict = {}
student_dict = {}
cwd = os.getcwd()

class Project:
    lecture: str
    name: str
    slogan: str
    desc: str
    students: list
    student_id: list
    student_role: list
    comp: list

    def __init__(self,lecture,name,slogan,desc,students,student_id,student_role,comp):
        self.lecture = lecture
        self.name = name
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


# check if element is in list
def check_list(item,list):
    for data in list:
        if item == data:
            return True
    return False

# read idlist.csv
with open(idcsv.removeprefix('/'),'r',encoding='UTF-8') as file:
    idcsvr = csv.reader(file)
    idcsvr = list(idcsvr)

# make idlist
for i in range(5,len(idcsvr)):
    idlist.append(idcsvr[i][1])

# parse profile csv file
with open(profilecsv.removeprefix('/'),'r',encoding='UTF-8') as file:
    profilecsvr = csv.reader(file)
    profilecsvr = list(profilecsvr)

# make student list
for i in range(1,len(profilecsvr)):
    student_dict[profilecsvr[i][2]] = Student(profilecsvr[i][1],profilecsvr[i][3],profilecsvr[i][4]
    ,profilecsvr[i][5],profilecsvr[i][6].split(','),profilecsvr[i][7],profilecsvr[i][8],profilecsvr[i][9],profilecsvr[i][10],profilecsvr[i][11].replace(' ','').split(','))
    for j in range(0,len(student_dict[profilecsvr[i][2]].interests)):
        student_dict[profilecsvr[i][2]].interests[j] = student_dict[profilecsvr[i][2]].interests[j].strip()

# parse project csv files
for filename in os.listdir(cwd + projectcsv):
    if check_list(filename.removesuffix(".csv"), idlist):
        # read csv file into list
        with open( projectcsv.removeprefix('/') + '/' + filename,'r',encoding="UTF-8") as file:
            csvr = csv.reader(file)
            csvr = list(csvr)
        # make students list
        students = []
        student_role = []
        student_id = []
        for i in range(3,len(csvr[0])):
            students.append(csvr[0][i])
            student_id.append(csvr[1][i])
            student_role.append(csvr[2][i])
        # make comp list
        comp = []
        for i in range(9,len(csvr)):
            comp.append((csvr[i][0], csvr[i][1]))
        # make project dictionary
        project_dict[filename.removesuffix(".csv")] = Project(csvr[1][1],csvr[3][1],csvr[4][1],csvr[5][1],students,student_id,student_role,comp)

# get html snippets
with open ("X/html_source/project_banner.txt",'r',encoding='UTF-8') as file:
    html_project_banner = file.read()
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

# create project html files
for key, info in project_dict.items():
    image_folder = image_root + '/' + key + '/'
    html = open(html_project_dir.removeprefix('/') + '/' + key + ".html",'w',encoding="UTF-8")
    html.write(html_project_top.replace("$LECTURE",info.lecture).replace("$NAME",info.name).replace("$SLOGAN",info.slogan).replace("$DESC",info.desc).replace("$STUDENTS", ', '.join(info.students)))

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
            html.write(html_project_comp_image.replace("$CONTENT",image_folder + section[1]))
        elif section[0] == "youtube":
            # youtube
            html.write(html_project_comp_youtube.replace("$CONTENT",section[1]))
        elif section[0] == "vimeo":
            # vimeo
            html.write(html_project_comp_vimeo.replace("$CONTENT",section[1]))
        
    # add students
    for index, studentid in enumerate(info.student_id):
        snippet = html_project_student
        snippet = snippet.replace("$NAME",info.students[index]).replace("$ROLE",info.student_role[index] if len(info.students)>1 else "").replace("$LINK",html_profile_dir + '/' + studentid + ".html")

    # add footer and other stuffs
    html.write(html_project_bottom)

# edit archive html file
with open(archive_html_src,'r',encoding='UTF-8') as file:
    html = file.read()
with open("X/html_source/archive_project.txt",'r',encoding='UTF-8') as file:
    html_archive_project = file.read()

project_archive = ''
for key,info in project_dict.items():
    project_archive += html_archive_project.replace("$ID",key).replace("$DESC",info.slogan).replace("$STUDENTS",' '.join(info.students)).replace("$NAME",info.name).replace("$CATEGORY",info.lecture)
html = re.sub(r"<!--PROJECT LIST START-->(.*?)<!--PROJECT LIST END-->",f"<!--PROJECT LIST START-->{project_archive}<!--PROJECT LIST END-->",html,flags=re.DOTALL)
with open(archive_html_src,'w',encoding='UTF-8') as file:
    file.write(html)



print("-----DONE!-----")