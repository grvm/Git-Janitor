# Git Janitor

There are times when you create temp branches, push your code on it, then merge it in the main working branch, and forget about it!!

Git Janitor helps you delete these branches from local, as well as the remote repo.

P.S. It only removes branches which have been merged into your current branch. Does not work on **Windows**

## Usage

#### Add the binary in the `dist` folder to your path, or some folder in your path to use it from any location on your system.

##### Basic Usage
Go to the location of the repo on your system which you want to clean.

```
git-janitor --preview | --clean --skip-pattern='pattern'
```

##### Preview branches that would be deleted:
```
git-janitor --preview
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
