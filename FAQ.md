# FAQ

**Contents**

- [I can't install dotapatch](#i-cant-install-dotapatch)
    - [--user](#--user)
        - [Temporarily add .local to PATH](#temporarily-add-local-to-path)
        - [Permanently add .local to PATH](#permanently-add-local-to-path)
    - [sudo](#sudo)


# I can't install dotapatch

`PermissionError` means `pip` (or `setup.py`) doesn't have the necessary privileges to install python modules.

    $ pip install dotapatch
    PermissionError: [Errno 13] Permission denied: '/usr/local/lib/pythonx.y/dist-packages/dotapatch-x.y.z.dist-info'

You can solve that by either using the [--user](#--user) flag or giving [root access](#sudo) to `pip` (or `setup.py`). Both methods work exactly the same for `pip` **and** `setup.py`.

## --user

Install **dotapatch** using the `--user` flag. The module will be installed (in linux) under `~/.local/bin` and `~/.local/lib/pythonx.y/dist-packages/`.

    $ pip install dotapatch --user
    $ dotapatch --version

If `--version` returns `dotapatch: v2.0`, you can stop here. It's all set!

Otherwise, you might see the following **error**.

    dotapatch: command not found

Which means you need to add `.local` to `PATH`. You can add it either [temporarily](#temporarily-add-local-to-path) or [permanently](#permanently-add-local-to-path).

### Temporarily add .local to PATH

Every time you open the Terminal, you'll have to execute the following command:

    $ PATH=$PATH:$HOME/.local/bin

`dotapatch` should work now:

    $ dotapatch --version
    dotapatch: v2.0

### Permanently add .local to PATH

Open the `.bashrc` file (under your user directory):

    $ cd 
    $ gedit .bashrc

Find the `export PATH` line (yours might be slightly different):

    export PATH=/usr/local/p/versions/python:$PATH

Append `:$HOME/.local/bin` to the end of that line. Don't forget to include **colon**:

    export PATH=/usr/local/p/versions/python:$PATH:$HOME/.local/bin

Open a new Terminal. `dotapatch` should work now:

    $ dotapatch --version
    dotapatch: v2.0

Remember, you'll need to modify the `.bashrc` only **once**!

## sudo

Only install pip modules using `sudo` if it's from a trusted source. The `--user` flag should be enough. Anyways:

    $ sudo -H pip install dotapatch
    $ dotapatch --version
    dotapatch: v2.0
