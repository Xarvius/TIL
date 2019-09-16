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
