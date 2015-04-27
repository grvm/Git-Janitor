# Git Janitor

##### Helps clean unused objects in the git repo.

##### P.S. Currently, only cleans local objects.

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

`*` is a wildcard character.

* '\*pattern\*' would search for occurence of the string 'pattern' anywhere in a branch.
* 'pattern*' would search for occurence of the string 'pattern' in the starting a branch.
* '*pattern' would search for occurence of the string 'pattern' in the end of a branch.
