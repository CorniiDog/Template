import os, getpass, time

# Set project directory to current directory

project_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(project_dir)
home_dir = os.path.expanduser("~")

project_name = os.path.basename(project_dir)
path_to_conda_python = f"{home_dir}/anaconda3/envs/{project_name}/bin/python3"
file_to_run = "main.py"
requirements_file = "requirements/requirements.txt"
conda_requirements_file = "requirements/conda_requirements.txt"
conda_forge_requirements_file = "requirements/conda_forge_requirements.txt"

run_instructions = False
output_instructions = True

conda_install_link = "https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh"
conda_file = conda_install_link.split("/")[-1]

path_to_services = "/etc/systemd/system"
service_name = f"{project_name}.service"

# Create a new file called "VR_Storage_System.service"
service_path = os.path.join(project_dir, "requirements", service_name)
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

def format_for_readme(text):
    new_text = ""
    for line in text.split("\n"):
        if line.startswith("-=["):
            new_text += f"## {line[3:-3]} ##\n" + "\n"

        elif len(line) > 0 and line[0] in "1234567890":
            new_text += f"### {line[3:]} ###\n" + "\n"

        elif line.startswith("=="):
            new_text += "\n"
        elif len(line) == 0:
            new_text += "\n"
        else:
            new_text += line + "\n" + "\n"
    return new_text


if output_instructions:

    additional_instructions = format_for_readme(additional_instructions)

    turn_to_readme = format_for_readme(output)

    with open("README.md", "w") as f:

        if project_name == "Template":
            f.write(additional_instructions)
        else:
            f.write("\n\n\nNOTE: The following below is automatically generated. To regenerate this file, run \"python3 setup.py\".\n\n")

            f.write(turn_to_readme)

print(output)
