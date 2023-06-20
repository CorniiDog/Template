[Back to DOCS.md](DOCS.md)



## 0. HOW TO USE THIS TEMPLATE ##


### 1. Git Clone this repository: ###

    git clone https://github.com/ConnorAtmos/Template

    or

    git clone git@github.com:ConnorAtmos/Template.git


### 2. Rename the project directory: ###

    mv Template <project_name>


### 3. CD into the project directory and remove the git repository: ###

    cd <project_name> && rm -rf .git


### 4. Run structure_builder.py for next steps: ###

    python3 structure_builder.py




## 1. HOW TO INSTALL ANACONDA ##


Conda is a package manager for python. It is used to install python packages and conda packages.


### 1. CD into the home directory: ###

    cd ~


### 2. Run the following command to download the conda installer: ###

    wget <conda_install_link>


### 3. Run the following command to install conda: ###

    bash <conda_file>


### 4. Run the following command to update conda: ###

    conda update conda


### 5. Run the following command to install conda-forge: ###

    conda config --add channels conda-forge






## 2. HOW TO CREATE CONDA ENVIRONMENT ##


This is for creating a new conda environment.


### 1. Run the following command to create a new conda environment: ###

    conda create --name <project_name>


### 2. Reload the bashrc file: ###

    source ~/.bashrc






## 3. HOW TO CONNECT INTERPRETER TO JETBRAINS GATEWAY ##


### 1. Open the project in PyCharm ###


### 2. Go to File > Settings > Project: <project_name> > Python Interpreter ###


### 3. Click "Add Interpreter" > Add Local Interpreter > Conda Environment > Use Existing Environment ###


### 4. Click the drop down menu and select <project_name>. ###





## 4. HOW TO INSTALL REQUIREMENTS ##


This is for installing python packages and conda packages.


### 1. CD into the project directory: ###

    cd <project_dir>


### 2. Activate the conda environment: ###

    conda activate <project_name>


### 3. Install the following requirements: ###

    pip install -r <requirements_file> && conda install --file <conda_requirements_file>  && conda install -c conda-forge --file <conda_forge_requirements_file>


### 4. Install the following apt-get requirements: ###

    <apt_get_str>






## 5. HOW TO INSTALL SERVICE ##


A service is a program that runs in the background. This is useful for running a program that you want to run all the time, such as a web server.


### 1. Run the following command to move the service file to the correct directory: ###

    sudo mv <service_path> <service_moved_path>


### 2. Reload the daemon: ###

    sudo systemctl daemon-reload


### 3. Run the following command to enable the service: ###

    sudo systemctl enable <service_name>


### 4. Start the service: ###

    sudo systemctl restart <service_name>


### 5. View status of service: ###

    sudo systemctl status <service_name>


ALTERNATIVE, RUN THE FOLLOWING COMMAND THAT DOES ALL OF THE ABOVE:

sudo mv <service_path> <service_moved_path> && sudo systemctl daemon-reload && sudo systemctl enable <service_name> && sudo systemctl restart <service_name> && sudo systemctl status <service_name>


To stop the service, run:

    sudo systemctl stop <service_name>


To disable the service, run:

    sudo systemctl disable <service_name>





## A. HOW TO REMOVE CONDA ENVIRONMENT ##


This is for removing the conda environment.


### 1. Run the following command to remove the conda environment: ###

    conda env remove --name <project_name>


### 2. Reload the bashrc file: ###

    source ~/.bashrc


ALTERNATIVE, RUN THE FOLLOWING COMMAND THAT DOES ALL OF THE ABOVE:

conda env remove --name <project_name> && source ~/.bashrc





## B. HOW TO UNINSTALL SERVICE ##


This is for uninstalling and removing the service.


### 1. Run the following command to disable the service: ###

    sudo systemctl disable <service_name>


### 2. Run the following command to stop the service: ###

    sudo systemctl stop <service_name>


### 3. Run the following command to delete the service file: ###

    sudo rm <service_moved_path>


ALTENATIVE, RUN THE FOLLOWING COMMAND THAT DOES ALL OF THE ABOVE:

sudo systemctl disable <service_name> && sudo systemctl stop <service_name> && sudo systemctl daemon-reload && sudo rm <service_moved_path>




