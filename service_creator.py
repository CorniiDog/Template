import os, getpass

# Set project directory to current directory

project_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(project_dir)
home_dir = os.path.expanduser("~")

project_name = "Machine_Learning"
path_to_conda_python = f"{home_dir}/anaconda3/envs/Machine_Learning/bin/python3"
file_to_run = "main.py"
requirements_file = "requirements/requirements.txt"
conda_requirements_file = "requirements/conda_requirements.txt"
conda_forge_requirements_file = "requirements/conda_forge_requirements.txt"

run_instructions = False
output_instructions = False

conda_install_link = "https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh"
conda_file = conda_install_link.split("/")[-1]

if run_instructions:
    project_name = input("Enter project name (i.e. \"VR Storage System\"): ")
    path_to_conda_python = input(
        "Enter path to conda python (i.e. \"/home/connor/anaconda3/envs/VR_Storage_System/bin/python3\"): ")
    file_to_run = input("Enter file to run (i.e. \"main.py\"): ")

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

This is created for Ubuntu 22.04 Check your version by running \"lsb_release -a\

==============================

-=[HOW TO INSTALL CONDA]=-

Conda is a package manager for python. It is used to install python packages and conda packages.

1. Run the following command to download the conda installer:
    wget {conda_install_link}

2. Run the following command to install conda:
    bash {conda_file}

3. Run the following command to update conda:
    conda update conda

4. Run the following command to install conda-forge:
    conda config --add channels conda-forge

ALTERNATIVE, RUN THE FOLLOWING COMMAND THAT DOES ALL OF THE ABOVE:
wget {conda_install_link} && bash {conda_file} && conda update conda && conda config --add channels conda-forge

==============================

-=[HOW TO CREATE CONDA ENVIRONMENT]=-

This is for creating a new conda environment.

1. Run the following command to create a new conda environment:
    conda create --name {project_name}

2. Reload the bashrc file:
    source ~/.bashrc

ALTERNATIVE, RUN THE FOLLOWING COMMAND THAT DOES ALL OF THE ABOVE:
conda create --name {project_name} && conda activate {project_name} && source ~/.bashrc

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

if output_instructions:
    with open("service_installation.txt", "w") as f:
        f.write(output)

print(output)
