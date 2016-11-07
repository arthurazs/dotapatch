# Dota 2: Changelog formatted as it should.

[![CircleCI](https://circleci.com/gh/arthurazs/dotapatch.svg?style=shield)](https://circleci.com/gh/arthurazs/dotapatch)

**dotapatch** is a software which aims the automation of formatting `simple text changelog` into `clear html changelog`.

Check the [Gameplay Update 6.88f](https://arthurazs.github.io/dotapatch/688f.html). This is the latest patch parsed using **dotapatch**.

## TL;DR
The changelog file **must** have the following format:

```
6.88f:
--
* Purifying Flames manacost increased from 50/60/70/80 to 80/85/90/95
* Torrent cooldown increased from 10 to 16/14/12/10
* Ghostship Rum damage reduction changed from 50% to 40/45/50%
* Shadow Poison manacost increased from 40 to 55
* Atrophy Aura attack damage reduction changed from 18/26/34/42% to 10/20/30/40%
* Fixed Return working on Centaur Illusions
```
Run `$ dotapatch <filename>`. Replace `<filename>` with the **changelog filename**.

    $ dotapatch 688f

Make sure that `<filename>` is in your current directory. You can also provide the `path` to the changelog.

    $ dotapatch /home/arthurazs/Desktop/changelogs/688f

You can also [clone (or download)](https://help.github.com/articles/cloning-a-repository/) this [repository](/../../) and run **dotapatch** without installing:

    $ cd dotapatch
    $ python -m dotapatch /home/arthurazs/Desktop/changelogs/688f

## Getting started
You will need python 2.7 or higher.

    $ sudo apt-get install python

### How does it work
There are 3 main files:

1. [**patch.py**](/dotapatch/patch.py)
    - Reads the changelog and decides what each line represents (item, base hero or ability)
2. [data.py](/dotapatch/data.py)
    - Handles the [HeropediaData](https://www.dota2.com/jsfeed/heropediadata?feeds=herodata,itemdata,abilitydata) **data fetching**
3. [model.py](/dotapatch/model.py)
    - Generates the formatted **html** file

There are 2 important folders as well:

1. [templates](/dotapatch/templates)
    - This is where the changelog file **must** be stored
2. [data](/dotapatch/data)
    - This is where the data from HeropediaData is stored

## Using dotapatch

### Setting environment up

[Clone (or download)](https://help.github.com/articles/cloning-a-repository/) this [repository](/../../). Head over to **dotapatch** folder.

    $ cd dotapatch
    
**OPTIONAL** Install **dotapatch**. You might need to use `sudo -H`.

    $ python setup.py install

### Gathering a new changelog

1. Go to [dota2 news](https://www.dota2.com/news/updates/) page and locate the latest **patch**.
2. Copy and save it as a file. The content you save **must** start with the patch name followed by colon (e.g. `6.88f:`). The second line won't be read, so you can leave it with anything other than a real changelog line (e.g. `--`). **All** the following lines **must** start with a star/asterisk (e.g. `* Anti-mage magic resistance reduced by a lot`).

    ```
    6.88f:
    --
    * Purifying Flames manacost increased from 50/60/70/80 to 80/85/90/95
    * Torrent cooldown increased from 10 to 16/14/12/10
    * Ghostship Rum damage reduction changed from 50% to 40/45/50%
    * Shadow Poison manacost increased from 40 to 55
    * Atrophy Aura attack damage reduction changed from 18/26/34/42% to 10/20/30/40%
    * Morph Replicate cast time increased from 0.25 to 0.35
    * Morphling base damage reduced by 4
    * Drow Ranger strength gain reduced from 1.9 to 1.6
    * Purification cast range reduced from 700 to 575
    * Purification cast point reduced from 0.25 to 0.2
    * Purification cooldown reduced from 10 to 9
    * Repel duration rescaled from 4/6/8/10 to 5/6/7/8
    * Repel cooldown reduced from 14 to 20/18/16/14
    * Outworld Devourer base damage reduced by 6
    * Starfall Scepter cooldown increased from 9 to 10
    * Faceless Void base armor reduced by 1
    * Stifling Dagger cast range reduced from 825/950/1075/1200 to 525/750/975/1200 
    * Spark Wraith no longer dispels (still slows)
    * Arc Warden movement speed reduced by 10
    * Healing Ward manacost increased from 120/125/130/135 to 140
    * Smoke Screen slow reduced from 19/21/23/25% to 13/17/21/25%
    * Track movement speed bonus reduced from 20% to 16/18/20%
    * Nyx's Scepter Burrow cast time increased from 1 to 1.5
    * Flamebreak knockback no longer interrupts channeling spells (behaves like blinding light)
    * Flamebreak burn duration increased from 3/4/5/6 to 4/5/6/7 (total damage increased)
    * Fixed Return working on Centaur Illusions
    ```

### Running dotapatch

If you've installed **dotapatch**, head over to the folder where you saved the changelog file and run **dotapatch**.

    $ cd Desktop/changelogs
    $ dotapatch 688f

If you haven't installed **dotapatch**, head over to the **dotapatch** folder and run **dotapatch** as a **module**.

    $ cd Desktop/dotapatch
    $ python -m dotapatch /home/arthurazs/Desktop/changelogs/688f

Once the software finishes running, it will tell you where the generated HTML was saved.

## Built with
**dotapatch** uses the following libraries:
- [ast](https://docs.python.org/3.4/library/ast.html)
    - Transforms data from HeropediaData into dictionary
- [os.path](https://docs.python.org/3.4/library/os.path.html)
    - Makes sure all directories are created
    - Checks if HeropediaData was arealdy fetched, reducing internet usage and code runtime
- [argparse](https://docs.python.org/3.4/library/argparse.html)
    - Enables the use of arguments. Try `$ ./patch.py -h`
- collections.[defaultdict](https://docs.python.org/3.4/library/collections.html#collections.defaultdict)
    - defaultdict(list) stores each line of the changelog inside a list (inside a dictionary)
    - Each `dictionary.keys()` (hero) stores `dictionary.values()` (hero changes)
    - `dictionary.values()` returns a list with all changes
- [requests](https://github.com/kennethreitz/requests)
    - Fetches HeropediaData files
- [logging](https://docs.python.org/3.4/library/logging.html)
    - Manage *dotapatch* logs
- [unittest](https://docs.python.org/3.4/library/unittest.html)
    - Base for the tests
    - [nose](http://nose.readthedocs.io/en/latest/) test suite (nosetests)
        - [--rednose](https://github.com/JBKahn/rednose) plugging which improves readability
- [setuptools](https://github.com/pypa/setuptools)
    - Setup manager

## Authors
- [**Arthur Zopellaro**](https://github.com/arthurazs)
    - *Creator*

## Task list

 - **TODO** see [projects](/../../projects).
 - **Changelog** see [releases](/../../releases).

## Contributing
I need your help improving **dotapatch**! Please open [new issues](/../../issues/new) if you have any feedback, questions or ideias. Also, feel free to open [pull requests](/../../compare) if you want to help me improve some of the code.

## License
This project is licensed under the [MIT License](LICENSE).
