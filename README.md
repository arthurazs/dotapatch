# Dota 2: Changelog formatted as it should.
**dota2patches** is a software which aims the automation of formatting `simple text changelog` into `clear html changelog`.

Check the [Gameplay Update 6.88f](https://arthurazs.github.io/dota2patches/688f.html). This is the latest patch parsed using **dota2patches**.

## TL;DR
The changelog file **must** be saved inside `changelogs/` and **must** have the following format:

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
Run `$ ./patch.py -f <filename>`. Replace `<filename>` with the **changelog filename**.

    $ ./patch.py -f 688f

## Getting started
You will need python3.

    $ sudo apt-get install python3

### How does it work
There are 3 main files:

1. **patch.py**
    - Reads the changelog and decides what each line represents (item, base hero or ability)
2. data.py
    - Handles the [HeropediaData](https://www.dota2.com/jsfeed/heropediadata?feeds=herodata,itemdata,abilitydata) **data fetching**
3. model.py
    - Formats the **simple text** into **html**

There are 2 important folders as well:

1. **changelogs**
    - This is where the new changelog file **must** be stored
2. data
    - This is where the data from HeropediaData is stored

### Running dota2patches
1. [Clone (or download)](https://help.github.com/articles/cloning-a-repository/) this repository.
2. Go to [dota2 news](https://www.dota2.com/news/updates/) page and locate the latest patch.
3. Copy and save it as a file inside `changelogs/`. The content you save **must** follow this format:

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
4. `$ cd dota2patches/`
5. run `$ ./patch.py -f <filename>`. Replace `<filename>` with the name of the file you saved at the **3rd step**. Example:

    ```
    $ ./patch.py -f 688f
    ```
6. You will get some feedback after the code finishes running. You can check the generated file under `dota2patches/<filename>`. Bear in mind `<filename>` should be the name you used at the **5th step**.

## Built with
dota2patches uses the following libraries:
- [ast](https://docs.python.org/3.4/library/ast.html)
    - Transforms data from HeropediaData into dictionary
- [os.path](https://docs.python.org/3.4/library/os.path.html)
    - Makes sure all directories are created
    - Checks if HeropediaData was arealdy fetched, reducing internet usage (also makes the code to run faster)
- [argparse](https://docs.python.org/3.4/library/argparse.html)
    - Enables the use of arguments. Try `$ ./patch.py -h`
- [defaultdict](https://docs.python.org/3.4/library/collections.html#collections.defaultdict)
    - defaultdict(list) permits each line of the changelog to be stored inside a list (inside a dictionary).
    - Each hero > `dictionary.keys()` stores a list with his changes > `dictionary.values()` (which returns a list).

## Authors
- [**Arthur Zopellaro**](https://github.com/arthurazs)
    - *Creator*

## Task list
- [x] Fix name bug (like using io instead of wisp)
- [ ] Ensure alphabetical order (See [#1](/../../issues/1))

## Contributing
I need your help improving [patch.py](patch.py). Please open [new issues](/../../issues/new) if you have any feedback, questions or ideias. Also, feel free to open `pull requests` if you can think of any improvements in the code.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
