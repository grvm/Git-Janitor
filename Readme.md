# Git Janitor

There are times when you create temp branches, push your code on it, then merge it in the main working branch, and forget about it!!

Git Janitor helps you delete these branches from local, as well as the remote repo.

P.S. It only removes branches which have been merged into your current branch.

## Usage

##### Basic Usage
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

##### Skipping branches which match a pattern
```
git-janitor --skip-pattern='*pattern*'
```

##### If no option is specified, it works in preview mode!!

`*` is a wildcard character.

* `'*pattern*'` would search for occurence of the string 'pattern' anywhere in a branch.
* `'pattern*'` would search for occurence of the string 'pattern' in the starting a branch.
* `'*pattern'` would search for occurence of the string 'pattern' in the end of a branch.
