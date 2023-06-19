import os

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
    apt_get_str = "sudo apt get install -y " + apt_get_str
else:
    apt_get_str = "[No apt-get requirements]"


output = f"""

==============================

This is created for Ubuntu 22.04 Check your version by running \"lsb_release -a\"

==============================

-=[HOW TO INSTALL CONDA]=-

Conda is a package manager for python. It is used to install python packages and conda packages.

1. CD into the home directory:
    cd ~

2. Run the following command to download the conda installer:
    wget {conda_install_link}

3. Run the following command to install conda:
    bash {conda_file}

4. Run the following command to update conda:
    conda update conda

5. Run the following command to install conda-forge:
    conda config --add channels conda-forge

==============================

-=[HOW TO CREATE CONDA ENVIRONMENT]=-

This is for creating a new conda environment.

1. Run the following command to create a new conda environment:
    conda create --name {project_name}

2. Reload the bashrc file:
    source ~/.bashrc
    
==============================

-=[HOW TO CONNECT INTERPRETER TO JETBRAINS GATEWAY]=-

1. Open the project in PyCharm

2. Go to File > Settings > Project: {project_name} > Python Interpreter

3. Click "Add Interpreter" > Add Local Interpreter > Conda Environment > Use Existing Environment

4. Click the drop down menu and select {project_name}.

==============================

-=[HOW TO INSTALL REQUIREMENTS]=-

This is for installing python packages and conda packages.

1. CD into the project directory:
    cd {project_dir}

2. Activate the conda environment:
    conda activate {project_name}

3. Install the following requirements:
    pip install -r {requirements_file} && conda install --file {conda_requirements_file}  && conda install -c conda-forge --file {conda_forge_requirements_file}
    
4. Install the following apt-get requirements:
    {apt_get_str}

==============================

-=[HOW TO INSTALL SERVICE]=-

A service is a program that runs in the background. This is useful for running a program that you want to run all the time, such as a web server.

1. Run the following command to move the service file to the correct directory:
    sudo mv {service_path} {service_moved_path}

2. Reload the daemon:
    sudo systemctl daemon-reload    

3. Run the following command to enable the service:
    sudo systemctl enable {service_name}

4. Start the service:
    sudo systemctl restart {service_name}

5. View status of service:
    sudo systemctl status {service_name}

ALTERNATIVE, RUN THE FOLLOWING COMMAND THAT DOES ALL OF THE ABOVE:
sudo mv {service_path} {service_moved_path} && sudo systemctl daemon-reload && sudo systemctl enable {service_name} && sudo systemctl restart {service_name} && sudo systemctl status {service_name}

==============================

-=[HOW TO UNINSTALL SERVICE]=-

This is for uninstalling and removing the service.

1. Run the following command to disable the service:
    sudo systemctl disable {service_name}

2. Run the following command to stop the service:
    sudo systemctl stop {service_name}

3. Run the following command to delete the service file:
    sudo rm {service_moved_path}

ALTENATIVE, RUN THE FOLLOWING COMMAND THAT DOES ALL OF THE ABOVE:
sudo systemctl disable {service_name} && sudo systemctl stop {service_name} && sudo systemctl daemon-reload && sudo rm {service_moved_path}

==============================

-=[HOW TO REMOVE CONDA ENVIRONMENT]=-

This is for removing the conda environment.

1. Run the following command to remove the conda environment:
    conda env remove --name {project_name}

2. Reload the bashrc file:
    source ~/.bashrc

ALTERNATIVE, RUN THE FOLLOWING COMMAND THAT DOES ALL OF THE ABOVE:
conda env remove --name {project_name} && source ~/.bashrc

==============================

"""

additional_instructions = """
## HOW TO USE THIS TEMPLATE ##

1. Git Clone this repository:
    git clone https://github.com/ConnorAtmos/Template
    or
    git clone git@github.com:ConnorAtmos/Template.git

2. Rename the project directory:
    mv Template <project_name>

3. CD into the project directory and remove the git repository:
    cd <project_name> && rm -rf .git

4. Run setup.py for next steps:
    python3 setup.py

"""

documentation = ""

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


    additional_instructions = format_for_readme(additional_instructions)

    turn_to_readme = format_for_readme(output, document_path="docs/INSTRUCTIONS.md")

    with open("README.md", "w") as f:

        f.write("[For Documentation, Click Here](docs/DOCS.md)\n\n")

        # Add all lines from ABOUT.md to README.md
        with open("ABOUT.md", "r") as about:
            for line in about.readlines():
                f.write(line)
            f.write("\n\n")

        if project_name == "Template":
            f.write(additional_instructions)


    with open(docs_folder + "/INSTRUCTIONS.md", "w") as f:

        # Provide link to go back to DOCS.md
        f.write(f"[Back to DOCS.md](DOCS.md)\n\n")

        f.write("# KEYWORDS #\n")

        # Rename the project name to <project_name>
        f.write(
            "- *<project_name>* is the name of the project. Replace <project_name> with the name of the project (ex. {project_name}).\n\n")
        turn_to_readme = turn_to_readme.replace(project_name, "<project_name>")

        # Replace the project directory with <project_dir>
        f.write(
            f"- *<project_dir>* is the path to the project directory. Replace <project_dir> with the path to the project directory (ex. {project_dir}).\n\n")
        turn_to_readme = turn_to_readme.replace(project_dir, "<project_dir>")

        turn_to_readme = turn_to_readme.replace(home_dir, "~")

        # Replace the service name with <service_name>
        f.write(
            f"- *<service_name>* is the name of the service. Replace <service_name> with the name of the service (ex. {service_name}).\n\n")
        turn_to_readme = turn_to_readme.replace(service_name, "<service_name>")

        # Replace the service path with <service_path>
        f.write(
            f"- *<service_path>* is the path to the service file. Replace <service_path> with the path to the service file (ex. {service_path}).\n\n")
        turn_to_readme = turn_to_readme.replace(service_path, "<service_path>")

        # Replace the service moved path with <service_moved_path>
        f.write(
            f"- *<service_moved_path>* is the path to the service file after it has been moved. Replace <service_moved_path> with the path to the service file after it has been moved (ex. {service_moved_path}).\n\n")
        turn_to_readme = turn_to_readme.replace(service_moved_path, "<service_moved_path>")

        # Replace the requirements file with <requirements_file>
        f.write(
            f"- *<requirements_file>* is the path to the requirements file. Replace <requirements_file> with the path to the requirements file (ex. {requirements_file}).\n\n")
        turn_to_readme = turn_to_readme.replace(requirements_file, "<requirements_file>")

        # Replace the conda requirements file with <conda_requirements_file>
        f.write(
            f"- *<conda_requirements_file>* is the path to the conda requirements file. Replace <conda_requirements_file> with the path to the conda requirements file (ex. {conda_requirements_file}).\n\n")
        turn_to_readme = turn_to_readme.replace(conda_requirements_file, "<conda_requirements_file>")

        # Replace the conda-forge requirements file with <conda_forge_requirements_file>
        f.write(
            f"- *<conda_forge_requirements_file>* is the path to the conda-forge requirements file. Replace <conda_forge_requirements_file> with the path to the conda-forge requirements file (ex. {conda_forge_requirements_file}).\n\n")
        turn_to_readme = turn_to_readme.replace(conda_forge_requirements_file, "<conda_forge_requirements_file>")

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
                    print(file_path)

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

                    def document_data(i, name, line, other_docs, parent_string=""):
                        name = parent_string + name

                        file2.write(f"# {name} #\n\n")


                        class_declaration = line


                        file2.write(f"### [{class_declaration.strip()}](./../{file_path}#L{i + 1}) ###\n\n")


                        other_docs += f"### [{name}](/{file_document_path}#{name.lower().replace(' ', '-').replace('.', '')}) ###\n\n"

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

                        # Add dropdown to other_docs with the documentation
                        other_docs += f"<details><summary>Documentation For {name}</summary><br>{new_documentation}</details>\n\n"
                        other_docs += f"- [{class_declaration.strip()}](./../{file_path}#L{i + 1}) \n\n"

                        # Add small github divider
                        other_docs += "<p align=\"center\">_</p>\n\n"

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
                                    other_docs = document_data(j, name2, lines[j], other_docs, parent_string=name+".")
                                elif lines[j].strip().startswith("class "):
                                    name2 = get_class_name(lines[j])
                                    other_docs = document_data(j, name2, lines[j], other_docs, parent_string=name+".")

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
                            other_docs = document_data(i, name, line, other_docs)

                        # If we find a function definition
                        elif line.startswith("def"):
                            found = True

                            name = get_function_name(line)
                            other_docs = document_data(i, name, line, other_docs)

                    if found:

                        # Provide link to md file
                        documentation += f"## Documentation For [{file_path}](/{file_document_path}) ##\n\n"

                        #Provide The documentation for the file
                        documentation += other_docs


                    file2.close()

    with open(docs_folder + "/DOCS.md", "w") as f:

        # Add the capability to go back to README.md
        f.write(f"[Back to README.md](/README.md)\n\n")

        f.write("# DOCUMENTATION TABLE OF CONTENTS #\n\n")

        f.write(f"This is the documentation for the project {project_name}.\n\n")

        f.write(documentation)

print(output)
