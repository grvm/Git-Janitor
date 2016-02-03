# Git Janitor

There are times when you create temp branches, push your code on them, merge them in the main working branch, and forget about them!!

Git Janitor frees you from the hassle. Clean and remove local or remote git branches which have already been merged in the current branch.

P.S. It only removes branches which have been merged into your current branch.

**P.P.S Works now on Windows as well.**

## Usage

#### Add the binary in the `dist` folder to your path, or some folder in your path to use it from any location on your system.

Use `dist/git-janitor.exe` if you are on **Windows**, `dist/git-janitor` **for Linux/Unix/OS X**

##### Basic Usage
Go to the location of the repo on your system which you want to clean.

```
git-janitor --clean --remote --skip-pattern='pattern'
```

##### Preview branches that would be deleted:
```
git-janitor
```

##### Delete branches
```
git-janitor --clean
```

##### Delete Remote branches
```
git-janitor --clean --remote
```

##### Skipping branches which match a pattern
```
git-janitor --skip-pattern='*pattern*'
```

`*` is a wildcard character.

* `'*pattern*'` would search for occurence of the string 'pattern' anywhere in a branch.
* `'pattern*'` would search for occurence of the string 'pattern' in the starting a branch.
* `'*pattern'` would search for occurence of the string 'pattern' in the end of a branch.

##### If no option is specified, it works in preview mode!!

### Contributions

Contribution and feedback are greatly appreciated.

_`Copyright (c) 2015 Gaurav Manchanda Under MIT License`_
