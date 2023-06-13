
## HOW TO USE THIS TEMPLATE ##


### 1. Git Clone this repository: ###

    git clone https://github.com/ConnorAtmos/Template

    or

    git clone git@github.com:ConnorAtmos/Template.git


### 2. Rename the project directory: ###

    mv Template <project_name>


### 3. CD into the project directory and remove the git repository: ###

    cd <project_name> && rm -rf .git


### 4. Run setup.py for next steps: ###

    python3 setup.py



# KEYWORDS #
<project_name> is the name of the project. Replace <project_name> with the name of the project (ex. {project_name}).

<project_dir> is the path to the project directory. Replace <project_dir> with the path to the project directory (ex. /home/connor/Template).

<service_name> is the name of the service. Replace <service_name> with the name of the service (ex. Template.service).

<service_path> is the path to the service file. Replace <service_path> with the path to the service file (ex. /home/connor/Template/requirements/Template.service).

<service_moved_path> is the path to the service file after it has been moved. Replace <service_moved_path> with the path to the service file after it has been moved (ex. /etc/systemd/system/Template.service).

<requirements_file> is the path to the requirements file. Replace <requirements_file> with the path to the requirements file (ex. requirements/requirements.txt).

<conda_requirements_file> is the path to the conda requirements file. Replace <conda_requirements_file> with the path to the conda requirements file (ex. requirements/conda_requirements.txt).

<conda_forge_requirements_file> is the path to the conda-forge requirements file. Replace <conda_forge_requirements_file> with the path to the conda-forge requirements file (ex. requirements/conda_forge_requirements.txt).





This is created for Ubuntu 22.04 Check your version by running "lsb_release -a"




## HOW TO INSTALL CONDA ##


Conda is a package manager for python. It is used to install python packages and conda packages.


### 1. CD into the home directory: ###

    cd ~


### 2. Run the following command to download the conda installer: ###

    wget https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh


### 3. Run the following command to install conda: ###

    bash Anaconda3-2022.05-Linux-x86_64.sh


### 4. Run the following command to update conda: ###

    conda update conda


### 5. Run the following command to install conda-forge: ###

    conda config --add channels conda-forge




## HOW TO CREATE CONDA ENVIRONMENT ##


This is for creating a new conda environment.


### 1. Run the following command to create a new conda environment: ###

    conda create --name <project_name>


### 2. Reload the bashrc file: ###

    source ~/.bashrc

    



## HOW TO CONNECT INTERPRETER TO JETBRAINS GATEWAY ##


### 1. Open the project in PyCharm ###


### 2. Go to File > Settings > Project: <project_name> > Python Interpreter ###


### 3. Click "Add Interpreter" > Add Local Interpreter > Conda Environment > Use Existing Environment ###


### 4. Click the drop down menu and select <project_name>. ###




## HOW TO INSTALL REQUIREMENTS ##


This is for installing python packages and conda packages.


### 1. CD into the project directory: ###

    cd ~/<project_name>


### 2. Activate the conda environment: ###

    conda activate <project_name>


### 3. Install the following requirements: ###

    pip install -r <requirements_file> && conda install --file <conda_requirements_file>  && conda install -c conda-forge --file <conda_forge_requirements_file>


ALTERNATIVE, RUN THE FOLLOWING COMMAND THAT DOES ALL OF THE ABOVE:

cd ~/<project_name> && conda activate <project_name> && pip install -r <requirements_file> && conda install --file <conda_requirements_file>  && conda install -c conda-forge --file <conda_forge_requirements_file>




## HOW TO INSTALL SERVICE ##


A service is a program that runs in the background. This is useful for running a program that you want to run all the time, such as a web server.


### 1. Run the following command to move the service file to the correct directory: ###

    sudo mv ~/<project_name>/requirements/<project_name>.service /etc/systemd/system/<project_name>.service


### 2. Reload the daemon: ###

    sudo systemctl daemon-reload    


### 3. Run the following command to enable the service: ###

    sudo systemctl enable <project_name>.service


### 4. Start the service: ###

    sudo systemctl restart <project_name>.service


### 5. View status of service: ###

    sudo systemctl status <project_name>.service


ALTERNATIVE, RUN THE FOLLOWING COMMAND THAT DOES ALL OF THE ABOVE:

sudo mv ~/<project_name>/requirements/<project_name>.service /etc/systemd/system/<project_name>.service && sudo systemctl daemon-reload && sudo systemctl enable <project_name>.service && sudo systemctl restart <project_name>.service && sudo systemctl status <project_name>.service




## HOW TO UNINSTALL SERVICE ##


This is for uninstalling and removing the service.


### 1. Run the following command to disable the service: ###

    sudo systemctl disable <project_name>.service


### 2. Run the following command to stop the service: ###

    sudo systemctl stop <project_name>.service


### 3. Run the following command to delete the service file: ###

    sudo rm /etc/systemd/system/<project_name>.service


ALTENATIVE, RUN THE FOLLOWING COMMAND THAT DOES ALL OF THE ABOVE:

sudo systemctl disable <project_name>.service && sudo systemctl stop <project_name>.service && sudo systemctl daemon-reload && sudo rm /etc/systemd/system/<project_name>.service




## HOW TO REMOVE CONDA ENVIRONMENT ##


This is for removing the conda environment.


### 1. Run the following command to remove the conda environment: ###

    conda env remove --name <project_name>


### 2. Reload the bashrc file: ###

    source ~/.bashrc


ALTERNATIVE, RUN THE FOLLOWING COMMAND THAT DOES ALL OF THE ABOVE:

conda env remove --name <project_name> && source ~/.bashrc





