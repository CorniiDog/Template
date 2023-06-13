# DOCUMENTATION TABLE OF CONTENTS #

This is the documentation for the project Template.

## INSTRUCTIONS.md ##

[HOW TO INSTALL CONDA](/docs/INSTRUCTIONS.md#how-to-install-conda)

[HOW TO CREATE CONDA ENVIRONMENT](/docs/INSTRUCTIONS.md#how-to-create-conda-environment)

[HOW TO CONNECT INTERPRETER TO JETBRAINS GATEWAY](/docs/INSTRUCTIONS.md#how-to-connect-interpreter-to-jetbrains-gateway)

[HOW TO INSTALL REQUIREMENTS](/docs/INSTRUCTIONS.md#how-to-install-requirements)

[HOW TO INSTALL SERVICE](/docs/INSTRUCTIONS.md#how-to-install-service)

[HOW TO UNINSTALL SERVICE](/docs/INSTRUCTIONS.md#how-to-uninstall-service)

[HOW TO REMOVE CONDA ENVIRONMENT](/docs/INSTRUCTIONS.md#how-to-remove-conda-environment)

# API #

## main.py ##

### [Test:.__init__](/docs/MAIN.md#test:.__init__) ###

- [Test:.    def __init__(self, name: str, age: int):](./../main.py#L5) 

### [Test:.__str__](/docs/MAIN.md#test:.__str__) ###

- [Test:.    def __str__(self):](./../main.py#L33) 

### [print_hi](/docs/MAIN.md#print_hi) ###

- [def print_hi(name: str) -> None:](./../main.py#L60) 

## setup.py ##

### [format_for_readme](/docs/SETUP.md#format_for_readme) ###

- [def format_for_readme(text, document_path=""):](./../setup.py#L218) 

### [get_function_name](/docs/SETUP.md#get_function_name) ###

- [def get_function_name(text_line):](./../setup.py#L349) 

### [get_class_name](/docs/SETUP.md#get_class_name) ###

- [def get_class_name(text_line):](./../setup.py#L352) 

### [count_spaces_at_beginning](/docs/SETUP.md#count_spaces_at_beginning) ###

- [def count_spaces_at_beginning(text_line):](./../setup.py#L357) 

### [get_function_documentation](/docs/SETUP.md#get_function_documentation) ###

- [def get_function_documentation(k, offset=0):](./../setup.py#L367) 

## toolbox/database.py ##

### [get](/docs/TOOLBOX-DATABASE.md#get) ###

- [def get(name: str) -> object | None:](./../toolbox/database.py#L9) 

### [save](/docs/TOOLBOX-DATABASE.md#save) ###

- [def save(name: str, data: any) -> None:](./../toolbox/database.py#L40) 

### [delete_database](/docs/TOOLBOX-DATABASE.md#delete_database) ###

- [def delete_database(name: str) -> object | None:](./../toolbox/database.py#L75) 

### [save_key](/docs/TOOLBOX-DATABASE.md#save_key) ###

- [def save_key(platform: str, key: str, override: bool = False) -> None:](./../toolbox/database.py#L113) 

### [load_key](/docs/TOOLBOX-DATABASE.md#load_key) ###

- [def load_key(platform: str) -> str | None:](./../toolbox/database.py#L148) 

