import os, getpass, time

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

ALTERNATIVE, RUN THE FOLLOWING COMMAND THAT DOES ALL OF THE ABOVE:
cd {project_dir} && conda activate {project_name} && pip install -r {requirements_file} && conda install --file {conda_requirements_file}  && conda install -c conda-forge --file {conda_forge_requirements_file}

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

def format_for_readme(text, document_path = ""):
    global documentation

    if document_path != "":
        documentation += f"## {document_path.split('/')[-1].replace('-', ' ')} ##\n\n"

    new_text = ""
    for line in text.split("\n"):
        if line.startswith("-=["):
            new_text += f"## {line[3:-3]} ##\n" + "\n"
            if document_path  != "":
                documentation += f"[{line[3:-3]}](/{document_path}#{line[3:-3].lower().replace(' ', '-')})\n\n"
        elif len(line) > 0 and line[0] in "1234567890":
            new_text += f"### {line} ###\n" + "\n"
            #new_text += line + "\n" + "\n"

        elif line.startswith("=="):
            new_text += "\n"
        elif len(line) == 0:
            new_text += "\n"
        else:
            new_text += line + "\n" + "\n"
    return new_text


if output_instructions:

    additional_instructions = format_for_readme(additional_instructions)

    turn_to_readme = format_for_readme(output, document_path="docs/INSTRUCTIONS.md")

    with open("README.md", "w") as f:

        if project_name == "Template":
            f.write(additional_instructions)

            f.write("[For Documentation, Click Here](docs/DOCS.md)\n\n")

    with open(docs_folder + "/INSTRUCTIONS.md", "w") as f:

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

                    file_document_path = docs_folder+"/"+ (str(file_path).strip().replace("/", "-").upper().split(".PY")[0]) + ".md"

                    file2 = open(file_document_path, "w")


                    documentation += f"## {file_document_path} ##\n\n"





                    # read the file as a list
                    lines = f.readlines()
                    #for i in range(len(lines)):
                    #    lines[i] = lines[i].replace("\n", "")

                    def get_function_name(line):
                        return line.strip().split("def ")[1].split("(")[0]

                    def get_function_documentation(i, offset=0):
                        if lines[i].strip().startswith("def "):
                            return ""

                        if len(lines) <= i:
                            return ""
                        if lines[i].strip() == "\"\"\"":
                            docs = ""
                            j = i+1
                            while j < len(lines) and lines[j].strip() != "\"\"\"":
                                docs += lines[j]
                                j += 1
                            return docs
                        else:
                            if offset > 10:
                                return ""
                            else:
                                return get_function_documentation(i+1, offset=offset+1)




                    for i, line in enumerate(lines):
                        # If we find a function definition
                        if line.startswith("def"):


                            name = get_function_name(line)
                            file2.write(f"# {name} #\n\n")

                            function_declaration = line

                            file2.write(f"### [{function_declaration.strip()}](./../{file_path}#L{i+1}) ###\n\n")
                            # https://github.com/ConnorAtmos/Template/blob/master/toolbox/database.py#L8
                            # https://github.com/ConnorAtmos/Template/blob/master/docs/toolbox/database.py#L8

                            documentation += f"### [{name}](/{file_document_path}#{name.lower().replace(' ', '-')}) ###\n\n"
                            documentation += f"[{function_declaration.strip()}](./../{file_path}#L{i+1}) \n\n"

                            documents = get_function_documentation(i+1)


                            sections = ["Notes", "Parameters", "Returns", "Examples", "References"]
                            data = {}
                            for section in sections:
                                data[section] = []

                            for section in sections:

                                if section not in documents:
                                    continue

                                file2.write(section + "\n\n")


                                sect_back = documents.find(section) + len(section)+1

                                while documents[sect_back] == "\n" or documents[sect_back] == "-":
                                    sect_back += 1
                                sect_front = 9999999
                                for sect2 in sections:
                                    if sect2 == section:
                                        continue
                                    sect_front2 = documents.find(sect2)
                                    if sect_front2 != -1:
                                        if sect_front2 < sect_front and sect_front2 > sect_back:
                                            sect_front = sect_front2
                                section_combined = documents[sect_back:sect_front].strip()

                                # remove first line if its first character is a dash
                                if section_combined[0] == "-":
                                    section_combined = section_combined.split("\n", 1)[1]

                                file2.write("```python\n" + section_combined + "\n```\n\n")

                    file2.close()




    with open(docs_folder + "/DOCS.md", "w") as f:

        f.write("# DOCUMENTATION TABLE OF CONTENTS #\n\n")

        f.write(f"This is the documentation for the project {project_name}.\n\n")

        f.write(documentation)




print(output)
