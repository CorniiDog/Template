import os, re

# Set project directory to current directory

project_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(project_dir)
home_dir = os.path.expanduser("~")

project_name = os.path.basename(project_dir)
path_to_conda_python = f"{home_dir}/anaconda3/envs/{project_name}/bin/python3"
file_to_run = "main.py"

requirements_folder = "requirements"
storage_folder = "storage"
toolbox_folder = "toolbox"
requirements_file = f"{requirements_folder}/requirements.txt"
conda_requirements_file = f"{requirements_folder}/conda_requirements.txt"
conda_forge_requirements_file = f"{requirements_folder}/conda_forge_requirements.txt"

docs_folder = "docs"

output_instructions = True

conda_install_link = "https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh"
conda_file = conda_install_link.split("/")[-1]

if not os.path.exists(requirements_folder):
    os.mkdir(requirements_folder)

if not os.path.exists(storage_folder):
    os.mkdir(storage_folder)

path_to_services = "/etc/systemd/system"
service_name = f"{project_name}.service"

requirements_abs_path = os.path.join(project_dir, requirements_folder)
storage_abs_path = os.path.join(project_dir, storage_folder)

# Create a new file called "VR_Storage_System.service"
service_path = os.path.join(storage_abs_path, service_name)
service_moved_path = os.path.join(path_to_services, service_name)

f = open(service_path, "w")

f.write(f"""
[Unit]
Description={project_name}
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=connor
ExecStart={path_to_conda_python} {file_to_run}
WorkingDirectory={project_dir}
Restart=always
RestartSec=120

[Install]
WantedBy=multi-user.target
""")

f.close()


apt_get_str = ""
with open("requirements/apt_get_requirements.txt", "r") as f:
    for line in f:
        apt_get_str += line.strip() + " "
if len(apt_get_str) > 0:
    apt_get_str = "sudo apt-get install -y " + apt_get_str
else:
    apt_get_str = "[No apt-get requirements]"


output = ""
documentation = ""

# Iterate through instructions folder
for file in sorted(os.listdir("instructions")):
    with open(f"instructions/{file}", "r") as f:
        output += "=" * 10 + "\n\n"

        output += "-=[" + file.replace(".txt", "").replace("_", " ").upper() + "]=-\n\n"

        output += f.read() + "\n\n"

# Replace <project_name> with the project name
output = output.replace("<project_name>", project_name)
# Replace <conda_file> with the conda file
output = output.replace("<conda_file>", conda_file)
# Replace <conda_install_link> with the conda install link
output = output.replace("<conda_install_link>", conda_install_link)
# Replace <project_dir> with the project directory
output = output.replace("<project_dir>", project_dir)
# Replace <requirements_file> with the requirements file
output = output.replace("<requirements_file>", requirements_file)
# Replace <conda_requirements_file> with the conda requirements file
output = output.replace("<conda_requirements_file>", conda_requirements_file)
# Replace <conda_forge_requirements_file> with the conda forge requirements file
output = output.replace("<conda_forge_requirements_file>", conda_forge_requirements_file)
# Replace <apt_get_str> with the apt-get string
output = output.replace("<apt_get_str>", apt_get_str)
# Replace <service_path> with the service path
output = output.replace("<service_path>", service_path)
# Replace <service_moved_path> with the service moved path
output = output.replace("<service_moved_path>", service_moved_path)
# Replace <service_name> with the service name
output = output.replace("<service_name>", service_name)


if output_instructions:

    def format_for_readme(text, document_path=""):
        global documentation

        if document_path != "":
            documentation += f"## {document_path.split('/')[-1].replace('-', ' ')} ##\n\n"

        new_text = ""
        for text_line in text.split("\n"):
            if text_line.startswith("-=["):
                new_text += f"## {text_line[3:-3]} ##\n" + "\n"
                if document_path != "":
                    documentation += f"[{text_line[3:-3]}](/{document_path}#{text_line[3:-3].lower().replace(' ', '-')})\n\n"
            elif len(text_line) > 0 and text_line[0] in "1234567890":
                new_text += f"### {text_line} ###\n" + "\n"
                # new_text += line + "\n" + "\n"

            elif text_line.startswith("=="):
                new_text += "\n"
            elif len(text_line) == 0:
                new_text += "\n"
            else:
                new_text += text_line + "\n" + "\n"
        return new_text


    turn_to_readme = format_for_readme(output, document_path="docs/INSTRUCTIONS.md")

    with open("README.md", "w") as f:

        f.write("[For Documentation, Click Here](docs/DOCS.md)\n\n")

        # Add all lines from ABOUT.md to README.md
        with open("ABOUT.md", "r") as about:
            for line in about.readlines():
                f.write(line)
            f.write("\n\n")

    with open(docs_folder + "/INSTRUCTIONS.md", "w") as f:

        # Provide link to go back to DOCS.md
        f.write(f"[Back to DOCS.md](DOCS.md)\n\n")

        f.write(turn_to_readme)

    documentation += f"# API #\n\n"

    # walk through every .py file in the toolbox folder
    for root, dirs, files in os.walk(project_dir):
        for file in files:
            if file[0] == ".":
                continue

            if file.endswith(".py"):
                # open the file
                with open(os.path.join(root, file), "r") as f:

                    # Get path between project directory and file
                    file_path = os.path.join(root, file).replace(project_dir, "")

                    if file_path.startswith("/"):
                        file_path = file_path[1:]

                    # Split the path into folders
                    folders = str(file_path).split("/")
                    last_part = folders[-1].split(".")[0]

                    file_document_path = docs_folder + "/" + (str(file_path).strip().replace("/", "-").upper().split(".PY")[0]) + ".md"

                    file2 = open(file_document_path, "w")

                    # Provide link to go back to DOCS.md
                    file2.write(f"[Back to DOCS.md](DOCS.md)\n\n")

                    # Turn into a "from ... import ..." statement
                    join_stuff = ".".join(folders[:-1])

                    if len(join_stuff) == 0:
                        import_statement = "import " + last_part
                    else:
                        import_statement = "from " + ".".join(folders[:-1]) + " import " + last_part
                    file2.write(f"Import Statement: `{import_statement}`\n\n")

                    # Turn into a "from ... import *" statement
                    # Remove extension first
                    folders[-1] = folders[-1].split(".")[0]

                    import_statement = "from " + ".".join(folders) + " import *"
                    file2.write(f"Alternative Import Statement: `{import_statement}`\n\n")


                    # read the file as a list
                    lines = f.readlines()


                    def get_function_name(text_line):
                        return text_line.strip().split("def ")[1].split("(")[0]

                    def get_class_name(text_line):
                        return text_line.strip().split("class ")[1].split("(")[0].split(":")[0]


                    def count_spaces_at_beginning(text_line):
                        count = 0
                        for c in text_line:
                            if c == " ":
                                count += 1
                            else:
                                break
                        return count


                    def get_function_documentation(k, offset=0):

                        if len(lines) <= k:
                            return ""

                        if lines[k].strip().startswith("def "):
                            return ""

                        if len(lines) <= k:
                            return ""
                        if lines[k].strip() == "\"\"\"":
                            docs = ""
                            j = k + 1
                            while j < len(lines) and lines[j].strip() != "\"\"\"":
                                docs += lines[j]
                                j += 1
                            return docs
                        else:
                            if offset > 10:
                                return ""
                            else:
                                return get_function_documentation(k + 1, offset=offset + 1)

                    def get_class_documentation(k, offset=0):

                        if len(lines) <= k:
                            return ""

                        if lines[k].strip().startswith("class "):
                            return ""

                        if len(lines) <= k:
                            return ""
                        if lines[k].strip() == "\"\"\"":
                            docs = ""
                            j = k + 1
                            while j < len(lines) and lines[j].strip() != "\"\"\"":
                                docs += lines[j]
                                j += 1
                            return docs
                        else:
                            if offset > 10:
                                return ""
                            else:
                                return get_class_documentation(k + 1, offset=offset + 1)

                    def document_data(i, name, line, other_docs, parent_string="", obj_type="function"):

                        # Remove underscores from front and back only, not in the middle
                        name = name.strip("_")

                        name = parent_string + name

                        file2.write(f"# {obj_type + ' ' + name} #\n\n")


                        class_declaration = line


                        file2.write(f"### [{class_declaration.strip()}](./../{file_path}#L{i + 1}) ###\n\n")

                        file_documentation = f"/{file_document_path}#{obj_type}-{name.lower().replace(' ', '-').replace('.', '')}"
                        writing_header = f"\n\n### [{obj_type + ' ' + name}]({file_documentation}) ###\n\n"

                        documents = get_class_documentation(i + 1)

                        sections = ["Notes", "Parameters", "Returns", "Examples", "References"]

                        new_documentation = ""
                        for section in sections:
                            if section in documents:
                                file2.write(section + "\n\n")
                                new_documentation += section + "\n\n"

                                sect_back = documents.find(section) + len(section) + 1

                                while documents[sect_back] == "\n" or documents[sect_back] == "-":
                                    sect_back += 1
                                sect_front = 9999999
                                for sect2 in sections:
                                    if sect2 == section:
                                        continue
                                    sect_front2 = documents.find(sect2)
                                    if sect_front2 != -1:
                                        if sect_front > sect_front2 > sect_back:
                                            sect_front = sect_front2
                                section_combined = documents[sect_back:sect_front].strip()

                                # remove first line if its first character is a dash
                                if section_combined[0] == "-":
                                    section_combined = section_combined.split("\n", 1)[1]

                                file2.write("```python\n" + section_combined + "\n```\n\n")
                                new_documentation += "```python\n" + section_combined + "\n```\n\n"

                        class_declaration_reference = f"[{class_declaration.strip()}](./../{file_path}#L{i + 1}) \n\n"

                        # Add dropdown to other_docs with the documentation
                        other_docs += f"\n<details>\n<summary>\n\n{writing_header}\n\n</summary>\n\n{class_declaration_reference + new_documentation}\n\n</details>\n\n"

                        # Add small github divider
                        #other_docs += "<p align=\"center\">_</p>\n\n"

                        # Identify the level of tabbing for the class
                        tab_level = count_spaces_at_beginning(line)

                        # Identify level of tabbing for any statements after the class
                        tab_level2 = 0
                        for j in range(i+1, len(lines)):
                            # If there is text, then set the tab level
                            if len(lines[j].strip()) > 0:
                                tab_level2 = count_spaces_at_beginning(lines[j])
                                break


                        # Locate functions and classes within the class, if their tab level is equal to tab_level2
                        # Once the tab level is less than tab_level2, then we know we have reached the end of the class
                        for j in range(i+1, len(lines)):
                            if count_spaces_at_beginning(lines[j]) == tab_level2:

                                if lines[j].strip().startswith("def "):
                                    name2 = get_function_name(lines[j])
                                    other_docs = document_data(j, name2, lines[j], other_docs, parent_string=name+".", obj_type="function")
                                elif lines[j].strip().startswith("class "):
                                    name2 = get_class_name(lines[j])
                                    other_docs = document_data(j, name2, lines[j], other_docs, parent_string=name+".", obj_type="class")

                            if count_spaces_at_beginning(lines[j]) < tab_level2:
                                # if not empty
                                if len(lines[j].strip()) > 0:
                                    break


                        return other_docs

                    found = False
                    other_docs = ""
                    for i, line in enumerate(lines):

                        # If we find a class definition
                        if line.startswith("class"):
                            found = True

                            name = get_class_name(line)
                            other_docs = document_data(i, name, line, other_docs, obj_type="class")

                        # If we find a function definition
                        elif line.startswith("def"):
                            found = True

                            name = get_function_name(line)
                            other_docs = document_data(i, name, line, other_docs, obj_type="function")

                    if found:

                        # Provide link to md file
                        documentation += f"\n<details>\n<summary>\n\n## Documentation For [{file_path}](/{file_document_path})\n\n</summary>\n\n{other_docs}<br></details>\n\n"

                        #Provide The documentation for the file


                    file2.close()

    with open(docs_folder + "/DOCS.md", "w") as f:

        # Add the capability to go back to README.md
        f.write(f"[Back to README.md](/README.md)\n\n")

        f.write("# DOCUMENTATION TABLE OF CONTENTS #\n\n")

        f.write(f"This is the documentation for the project {project_name}.\n\n")

        f.write(documentation)





# Remove blank lines from output
output = "\n".join([s for s in output.splitlines() if s.strip() != ""])

# Color the lines (like === and ---) red
output = re.sub(r"^(=+)$", r"\033[91m\1\033[0m", output, flags=re.MULTILINE)

print(output)
