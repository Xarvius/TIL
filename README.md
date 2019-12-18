# TIL
> Today I Learned

A collection of links and concise write-ups on small things I learn day to day across a variety of languages and technologies.

## Day 1
- [What do programmers actually do?](https://www.youtube.com/watch?v=FVdQETvHBoE) 
- [Front end vs Back end | Blonde Dictionary explanation](https://www.youtube.com/watch?v=NlpK0-TLrjw)
- [What is Git and Github? Source Control —Coding For Beginners](https://www.youtube.com/watch?v=3bchX_7ANQc)
- [How to create a repository on github](https://help.github.com/en/articles/create-a-repo)

## Day 2
[Official python tutorial](https://docs.python.org/3/tutorial/)
- [Variables, loops for and while, if, functions, list, tuple, sipmle string manipulations etc.](https://www.youtube.com/playlist?reload=9&list=PLdBHMlEKo8UcOaykMssI1_X6ui0tzTNoH) (1-13)
- [Enumerate, if in](https://gist.github.com/Xarvius/375338d2bfbc9fcda2703dbd303764f9)
- [git rebase --interactive](https://www.youtube.com/watch?v=MLOxFLULJQI)
- git status | git log --decorate --oneline --graph <3

## Day 3
- [Import, file, exceptions](https://www.youtube.com/playlist?reload=9&list=PLdBHMlEKo8UcOaykMssI1_X6ui0tzTNoH) (14-17)

## Day 4
- [Class, self in class, magical methods, own exceptions](https://www.youtube.com/playlist?list=PLdBHMlEKo8UcOaykMssI1_X6ui0tzTNoH) (18-22)
- [More about magical methods](http://farmdev.com/src/secrets/magicmethod/index.html)
- 'never' git add . | git add -p <3

## Day 5
- [git](https://edu.devstyle.pl/product/git/) (config, tools)
- [5-sposobow-na-prace-z-gitem](https://devstyle.pl/2018/10/26/5-sposobow-na-prace-z-gitem/)
- [10 Sekretnych Komend Gita, O Których Nie Masz Pojęcia](https://convertkit.s3.amazonaws.com/landing_pages/incentives/000/414/200/original/devstyle-Git-10-komend.pdf?1537630848)

## Day 6
- [git](https://edu.devstyle.pl/product/git/) (tags, alias)
  - [git tag](https://gist.github.com/Xarvius/d7c472f1b554ae77232ba0f50aca627a) annotated > lightweight(temp/auto)
  - [~..^](https://gist.github.com/Xarvius/5fcda2d428a7d83937a8cdd5c2e726ff) (tag/commit navigation)
- [Own autocomplete](https://gist.github.com/Xarvius/20153299b756c59fd9622bdb9b2dbd88) //swap to alias soon

## Day 7
- [Python testing](https://realpython.com/python-testing/)
- [Virtualenvwrapper](https://virtualenvwrapper.readthedocs.io) - must have with packages

## Day 8
- [Unit Testing vs Integration Testing](http://www.softwaretestingclass.com/what-is-difference-between-unit-testing-and-integration-testing/)
- [Mocking in python](https://auth0.com/blog/mocking-api-calls-in-python/)
- [Still mocking in python](https://realpython.com/python-mock-library/#what-is-mocking)
- [Asserations test - unittest](https://kapeli.com/cheat_sheets/Python_unittest_Assertions.docset/Contents/Resources/Documents/index)

## Day 9
- [git](https://edu.devstyle.pl/product/git/) (merge, branch)
  - [merge](https://dev.to/neshaz/how-to-use-git-merge-the-correctway-25pd)
  - cherry-picking for move commit
  - no-ff in merge for no fast forward (flat merge)
  - git init --bare (create repo for share code)
  
## Day 10
- [git](https://edu.devstyle.pl/product/git/)
  - pull = fetch + merge (better fetch and manual)
  - git diff --cached (diffrence added to staged area)

## Day 11
- [git](https://edu.devstyle.pl/product/git/)
  - git checkout -- file (return file from last commit) or gut checkout commit -- file (we can use *.html - all files .html)
  - git reset --hard (reset modify from disc too) without reset only back commit whithout modify files (example: git reset @^)
  - git clean (for remove files) -n (test - only show) -i (interactive) -f (force - real delete) -x (delete file from gitignore) - fd(files and folders)
  - git stash - 'hidden' commit (git stash list - list) (git stash pop - last stash back to working copy) use only with save and own tekst
  - [.gitignore (name/ ignore folder name) (we can use pattern like *.txt, [bB]in/ (bin and Bin)](https://github.com/github/gitignore)
    - .git/info/exlude - private .gitignore
    - git check-ignore 
    - git update-index --asume-unchanged file (ignore for tracked files) --no-asume-unchanged for back
    - git ls-files -v (list files + status, 'h' for asume-unchanged)
      - git ls-files -v | grep "^[[:lower:]]" list only asume-unchanged files
    - git config include.path file_dir (include own configuration)
      - includeif.statment example: git config --global includeif.gitdir:C:/dev/work .path .gitfile (add .gitfile to global config only to repos in C:/dev/work)

## Day 12
- [git](https://edu.devstyle.pl/product/git/)
  - git reset --hard ORIG_HEAD - return before merge/rebase
  - git fetch --prune --prune-tags
- [VIM](https://www.openvim.com/tutorial.html)

## Day 13
- [git](https://edu.devstyle.pl/product/git/)
  - git rerere - merge helper (memory our chose)
  - git revert - revert changes
  - git commit --amend - edit last commit
  - git rebase - lineary history -i for interactive mode
  - filter-branch - tools for rewrite history
  - git remote update --prune - update branch (in someone delete branch, this command delete local too)
  - git blame / git gui blame - last editor (line)
  - git log -S txt -p - find txt in commit (but not in title) -S is pickaxe
  - --format=%h | clip - good help to easy copy commit (for pickaxe)
  - git bisect - bug catcher

## Day 14
- [git](https://edu.devstyle.pl/product/git/)
  - [gitsubmodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules)
  - [gitslave](http://gitslave.sourceforge.net)
  - [subtrea](https://www.atlassian.com/git/tutorials/git-subtree) (the best? for submodules still better package management)
  
## Day 15
- [python](https://www.learnpython.org/en/Welcome)
  - [Generators](https://chyla.org/blog/Python_-_Generatory/)
  - [List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
  - [Regular Expressions](https://www.learnpython.org/en/Regular_Expressions)
    - [more](https://docs.python.org/3/library/re.html#regular-expression-syntax"RE%20syntax)
  - [Multiple Function Arguments](https://www.learnpython.org/en/Multiple_Function_Arguments)

## Day 16
- [Python](https://www.programiz.com/python-programming)
  - [Global, Local and Nonlocal variables](https://www.programiz.com/python-programming/global-local-nonlocal-variables)
  - else with while, for
- [Kite](https://kite.com)

## Day 17
- [Python](https://www.programiz.com/python-programming)
  - [Numbers - Fractions](https://www.programiz.com/python-programming/numbers)
  - [Set](https://www.programiz.com/python-programming/set) - 'While using discard() if the item does not exist in the set, it remains unchanged. But remove() will raise an error in such condition.'
  
## Day 18
- [Python](https://www.programiz.com/python-programming)
  - [OOP in Python](https://www.programiz.com/python-programming/object-oriented-programming) - Inheritance, Encapsulation, Polymorphism
    - [More about inheritance](https://www.programiz.com/python-programming/multiple-inheritance)
      - Method Resolution Order (MRO) - 'In the multiple inheritance scenario, any specified attribute is searched first in the current class. If not found, the search continues into parent classes in depth-first, left-right fashion without searching same class twice.'
  - [Operator overloading](https://www.programiz.com/python-programming/operator-overloading)

## Day 19
- [Python](https://www.programiz.com/python-programming)
  - [Class iterator](https://www.programiz.com/python-programming/iterator)
  - [Closure](https://www.programiz.com/python-programming/closure)
  - [Decorators](https://www.programiz.com/python-programming/decorator)
  
  
## Day 20
- [Python](https://www.programiz.com/python-programming)
  - [@property](https://www.programiz.com/python-programming/property)
  - [Deep copy](https://www.programiz.com/python-programming/shallow-deep-copy)
  - [Asseration](https://www.programiz.com/python-programming/assert-statement)

## Day 21
- [Django](https://docs.djangoproject.com/pl/2.1/intro/)
  - [Introduction](https://docs.djangoproject.com/pl/2.1/intro/overview/)
  - [Install](https://docs.djangoproject.com/pl/2.1/intro/install/)
  
## Day 22
- [Django](https://docs.djangoproject.com/pl/2.1/intro/)
  - [Tutorial 1-3](https://docs.djangoproject.com/pl/2.1/intro/tutorial01/)
  
## Day 23
- [Java](https://javastart.pl/baza-wiedzy/java-podstawy-jezyka)

---------------------------------------------------------------------------------
## Day 25
- [Docker - install](https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-engine---community)
  - [Docker run without sudo](https://docs.docker.com/install/linux/linux-postinstall/)
  - [Basic tutorial (1-2)](https://github.com/docker/labs/tree/master/beginner/)
  
## Day 26 
- Remember the three-step guide to making model changes:
  - Change your models (in models.py).
  - Run python manage.py makemigrations to create migrations for those changes
  - Run python manage.py migrate to apply those changes to the database.
- You should always return an HttpResponseRedirect after successfully dealing with POST data. This tip isn’t specific to Django; it’s just good Web development practice
- pip freeze - installed packages
- create requirments.txt with your installed packages like name=version 
  - pip install -r requirements.txt

## Day 27
- psycopg2 need to migrate db to postgres
  - if install error on virtualenv [check](https://stackoverflow.com/questions/5420789/how-to-install-psycopg2-with-pip-on-python)
- For security, we can split django settings and docker-composer for normal and prod version.
- File .env is good places for system variables (and passwords). Add it to .gitignore.
- When u run docker-compose (containter with few docker-compose.yml) add them in command line, like: docker compose -f docker-compose.yml -f docker-compose.prod.yml
  - check them in the same way (prev command with ps on the end)
- [See](https://github.com/Xarvius/django-first)

## Day 28
- ("In django our working directory is always the folder that containts manage.py")[https://books.google.pl/books/about/Test_Driven_Development_with_Python.html?id=2CgvDwAAQBAJ&printsec=frontcover&source=kp_read_button&redir_esc=y#v=onepage&q&f=false]
- (f-strings > format() > % formating)[https://realpython.com/python-f-strings/]
