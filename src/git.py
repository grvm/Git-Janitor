import os, re

from color import Color

class Git:

  def __init__(self, args):
    self.args = args

  def skip_pattern(self):
    pattern = re.compile("--skip-pattern=(.+)")
    strng = " ".join(self.args)
    mtch = pattern.search(strng)
    if mtch != None:
      return mtch.group(1)
    else:
      return ""

  def current_branch(self):
    return os.popen("git rev-parse --abbrev-ref HEAD").read().strip()

  def merged_branches(self):
    return self.sanitize_branch_list(os.popen("git branch --merged").readlines())

  def pattern_matching_branches(self):
    if self.skip_pattern_exists():
      cmd = "git branch --list '"+ str(self.skip_pattern()) + "' --merged"
      branches = self.sanitize_branch_list(os.popen(cmd).readlines())
      if len(branches) == 0:
        print Color.BOLD + Color.FAIL_COLOR + "No branch name matches the given skip pattern: " + " " + Color.UNDERLINE + str(self.skip_pattern()) + Color.ENDC
      return branches
    else:
      return []

  def delete_branches(self):
    os.popen("git branch -D " + " ".join(self.branches_to_be_deleted()))

  def sanitize_branch_list(self, branches):
    return [x.replace("*", "").strip() for x in branches]

  def skip_pattern_exists(self):
    return str(self.skip_pattern()) != ""
