# Command Line Tool boilerplate

Find and do stuff

### Example:

```
$ tool -h
```

## Dependencies
- Python3
- Pyenv
- zsh complete

## Installing to the pyenv 'tools3'

**Installation**

```
pyenv activate tools3
pip install .
pyenv deactivate

# or use the script:
reinstall
```

**Uninstalling**

```
pyenv activate tools3
pip uninstall tool
pyenv deactivate
```

**Development**

```
pyenv local tools3 3.6.0
pytest
# For multiple environment release
tox
```

**zsh Completion**

```
Add script to .oh-my-zsh/custom/plugins
using:
$ ./scripts/setup_completions 
```

