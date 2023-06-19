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

## Documentation For [main.py](/docs/MAIN.md) ##

- [def print_hi(name: str) -> None:](./../main.py#L147) 

<details><summary>Documentation For print_hi</summary><br>Notes

```python
        ello
```

Parameters

```python
        name : str
            The name of the person to greet
```

Returns

```python
        None
            This function does not return anything
```

Examples

```python
        print_hi('PyCharm')
```

References

```python
        https://www.jetbrains.com/help/pycharm/creating-and-running-your-first-python-project.html
```

</details>

## Documentation For [toolbox/database.py](/docs/TOOLBOX-DATABASE.md) ##

- [def load_key(platform: str) -> str | None:](./../toolbox/database.py#L148) 

<details><summary>Documentation For load_key</summary><br>Notes

```python
        This function is used to load keys from a secure location
```

Parameters

```python
        platform: str
            The key to be loaded (e.g. '<google_api_key>')
```

Returns

```python
        str or None
            This function returns the key if it exists, otherwise it returns None
```

Examples

```python
        key = load_key('google')
```

References

```python
        https://www.nylas.com/blog/making-use-of-environment-variables-in-python/
```

</details>

