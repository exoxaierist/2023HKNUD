# sample code for parsing data of all project, student information
import csv
import os
import re

# directories
dir_csv_id = "/X/1010_idlist.csv"
dir_csv_profile = "/X/1010_profile.csv"
dir_csv_project = "/X/csvs"
dir_target_project = "/projects"
dir_target_profile = "/profiles"
dir_img_src = "/image/image_project"

target_archive = str("archive.html")
target_students = str("students.html")

id_list = []
id_dict = {}
project_list = {}
student_list = {}
cwd = os.getcwd()

# get html snippets
with open("X/html_source/archive_project.txt",'r',encoding='UTF-8') as file:
    html_archive_project = file.read()

with open("X/html_source/students_item.txt",'r',encoding='UTF-8') as file:
    html_students_item = file.read()

with open ("X/project_template.html",'r',encoding='UTF-8') as file:
    html_project = file.read()
with open ("X/html_source/project_comp_text1.txt",'r',encoding='UTF-8') as file:
    html_project_comp_text1 = file.read()
with open ("X/html_source/project_comp_text2.txt",'r',encoding='UTF-8') as file:
    html_project_comp_text2 = file.read()
with open ("X/html_source/project_comp_youtube.txt",'r',encoding='UTF-8') as file:
    html_project_comp_youtube = file.read()
with open ("X/html_source/project_comp_vimeo.txt",'r',encoding='UTF-8') as file:
    html_project_comp_vimeo = file.read()
with open ("X/html_source/project_comp_image.txt",'r',encoding='UTF-8') as file:
    html_project_comp_image = file.read()
with open ("X/html_source/project_comp_link.txt",'r',encoding='UTF-8') as file:
    html_project_comp_link = file.read()
with open ("X/html_source/project_student.txt",'r',encoding='UTF-8') as file:
    html_project_student = file.read()

with open ("X/profile_template.html",'r',encoding='UTF-8') as file:
    html_profile = file.read()
with open ("X/html_source/profile_link_insta.txt",'r',encoding='UTF-8') as file:
    html_profile_link_insta = file.read()
with open ("X/html_source/profile_link_behance.txt",'r',encoding='UTF-8') as file:
    html_profile_link_behance = file.read()

class Project:
    title: str
    slogan: str
    desc: str
    lecture: str
    category: str
    sub_category: str

    students: list
    student_id: list
    student_role: list
    comp: list
    def __init__(self):
        pass

class Student:
    name: str
    desc: str
    email: str
    career: str
    insta: str
    behance: str
    projects: list
    def __init__(self):
        pass
    def __init__(self,name,desc,email,career,insta,behance):
        self.name = name
        self.desc = desc
        self.email = email
        self.career = career
        self.insta = insta
        self.behance = behance
        self.projects = []

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
    student_list[rawdata_profile[i][1]] = Student(
        name=rawdata_profile[i][2],
        desc=rawdata_profile[i][3],
        email=rawdata_profile[i][5],
        career=rawdata_profile[i][4],
        insta=rawdata_profile[i][6],
        behance=rawdata_profile[i][7])



# make projects list
for filename in os.listdir(cwd + dir_csv_project +"/"):
    if filename.removesuffix(".csv") in id_list:
        _instance = Project()
        _id = filename.removesuffix(".csv")
        # read csv file into list
        with open( dir_csv_project.removeprefix('/') + '/' + filename,'r',encoding="UTF-8") as file:
            rawdata_project = csv.reader(file)
            rawdata_project = list(rawdata_project)
        _instance.category = rawdata_project[3][1]
        _instance.sub_category = rawdata_project[3][3]
        _instance.title = rawdata_project[4][1]
        _instance.slogan = rawdata_project[5][1]
        _instance.lecture = rawdata_project[1][1]
        _instance.desc = rawdata_project[6][1]
        # make students list
        students = []
        student_id = []
        for i in range(5,len(rawdata_project[0])):
            students.append(rawdata_project[0][i])
            student_id.append(rawdata_project[1][i])
            if rawdata_project[1][i] in student_list:
                student_list[rawdata_project[1][i]].projects.append(_id);
        _instance.students = students
        _instance.student_id = student_id
        # make comp list
        comp = []
        for i in range(9,len(rawdata_project)):
            comp.append(rawdata_project[i])
        _instance.comp = comp
        # make project dictionary
        project_list[filename.removesuffix(".csv")] = _instance
        



def make_project_item(id,sub):
    _info = project_list[id]
    filterList = "filter" + id[:2].upper()
    filterList += " filter" + project_list[id].category
    filterList += " filter" + project_list[id].sub_category
    return html_archive_project.\
        replace("$SLOGAN",_info.slogan).\
        replace("$STUDENTS",' '.join(_info.students)).\
        replace("$TITLE",_info.title).\
        replace("$CATEGORY",_info.category).\
        replace("$ID",id).\
        replace("$FILTER",filterList).\
        replace("$DIR","../" if sub else "")







# edit archive html file
with open(target_archive,'r',encoding='UTF-8') as file:
    html = file.read()

_project_items = ""
for key in project_list:
    _project_items += make_project_item(key,False)
    
html = re.sub(r"<!--PROJECT LIST START-->(.*?)<!--PROJECT LIST END-->",f"<!--PROJECT LIST START-->{_project_items}<!--PROJECT LIST END-->",html,flags=re.DOTALL)
with open(target_archive,'w',encoding='UTF-8') as file:
    file.write(html)



# edit students html file
with open(target_students,'r',encoding='UTF-8') as file:
    html = file.read()

_student_items = ""
_sorted_student_list = sorted(student_list.items(), key=lambda x:x[1].name)
for key,info in _sorted_student_list:
    _student_items += html_students_item.\
        replace("$NAME",info.name).\
        replace("$CAREER",info.career).\
        replace("$ID",key)
html = re.sub(r"<!--STUDENT LIST START-->(.*?)<!--STUDENT LIST END-->",f"<!--STUDENT LIST START-->{_student_items}<!--STUDENT LIST END-->",html,flags=re.DOTALL)
with open(target_students,'w',encoding='UTF-8') as file:
    file.write(html)





# create project html files
for key, info in project_list.items():
    #print("writing project : ", key)
    html = open(dir_target_project.removeprefix('/') + '/' + key + ".html",'w',encoding="UTF-8")
    
    # student info
    _students=""
    for i,name in enumerate(info.students):
        _students += html_project_student.replace("$NAME",name).replace("$ID",info.student_id[i])
    
    # basign information
    _write = html_project.\
        replace("$LECTURE",info.lecture).\
        replace("$TITLE",info.title).\
        replace("$SLOGAN",info.slogan).\
        replace("$DESC",info.desc).\
        replace("$STUDENTS", _students).\
        replace("$ID",key)



    # composition
    _comp =""
    for _temp in info.comp:
        
        if _temp[0] == "text_1":
            # header
            _comp += html_project_comp_text1.\
                       replace("$CONTENT1",_temp[1]).\
                        replace("$CONTENT2",_temp[2]).\
                        replace("$CONTENT3",_temp[3])
        elif _temp[0] == "text_2":
            # sub_header
            _comp += html_project_comp_text2.\
                       replace("$CONTENT1",_temp[1]).\
                        replace("$CONTENT2",_temp[2])
        elif _temp[0] == "image":
            # image
            _comp += html_project_comp_image.\
                       replace("$CONTENT1", _temp[1]).\
                        replace("$ID",key)
        elif _temp[0] == "youtube":
            # youtube
            _comp += html_project_comp_youtube.\
                       replace("$CONTENT1",_temp[1])
        elif _temp[0] == "vimeo":
            # vimeo
            _comp += html_project_comp_vimeo.\
                       replace("$CONTENT1",_temp[1])
        elif _temp[0] == "link":
            # link
            _comp += html_project_comp_link.\
                       replace("$CONTENT1",_temp[1]).\
                       replace("$CONTENT2",_temp[2])
    


    _write = _write.replace("<!--COMP-->",_comp)
    
    # get releated projects
    related_projects_id = []
    for _student_id in info.student_id:
        if _student_id in student_list.keys():
            for _project_id in student_list[_student_id].projects:
                if _project_id not in related_projects_id and _project_id != key:
                    related_projects_id.append(_project_id)
    related_projects=""
    for _id in related_projects_id:
        related_projects += make_project_item(_id,True)
    _write = _write.replace("<!--PROJECT LIST-->",related_projects)

    html.write(_write)
    



# create profile html files

for key,info in student_list.items():
    #print("writing profile : ", key)
    html = open(dir_target_profile.removeprefix('/') + '/' + key + ".html",'w',encoding="UTF-8")
    
    _write_link =""
    if info.insta != "":
        _write_link += html_profile_link_insta.replace("$INSTA",info.insta.replace("@",""))
    if info.behance != "":
        if not info.behance.startswith("http"):
            info.behance = "http://" + info.behance
        _write_link += html_profile_link_behance.replace("$BEHANCE",info.behance)
    
    _write_projects =""
    for _id in info.projects:
        _write_projects += make_project_item(_id,True)

    _write = html_profile.\
        replace("$ID",key).\
        replace("$NAME",info.name).\
        replace("$CAREER",info.career).\
        replace("$DESC",info.desc).\
        replace("$EMAIL",info.email).\
        replace("<!--LINK-->",_write_link).\
        replace("<!--PROJECT LIST-->",_write_projects)


    html.write(_write)  
    

print("-----DONE!-----")