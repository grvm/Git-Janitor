import os, re

from formatter import Formatter

class Git:

  def __init__(self, args):
    self.args = args

  def skip_pattern(self):
    pattern = re.compile("--skip-pattern=(.+)")
    strng = " ".join(self.args)
    mtch = pattern.search(strng)
    return mtch.group(1) if mtch else ""

  def current_branch(self):
    return os.popen("git rev-parse --abbrev-ref HEAD").read().strip()

  def merged_branches(self):
    return self.sanitize_branch_list(os.popen("git branch --merged").readlines())

  def pattern_matching_branches(self):
    if self.skip_pattern_exists():
      cmd = "git branch --list '"+ str(self.skip_pattern()) + "' --merged"
      branches = self.sanitize_branch_list(os.popen(cmd).readlines())
      self.warn_if_no_branch_matches_pattern(branches)
      return branches
    else:
      return []

  def sanitize_branch_list(self, branches):
    return [x.replace("*", "").strip() for x in branches]

  def skip_pattern_exists(self):
    return str(self.skip_pattern()) != ""

  def warn_if_no_branch_matches_pattern(self, branches):
    if len(branches) == 0:
      Formatter.print_pretty_bold_message(Formatter.FAIL_COLOR, "No branch name matches the given skip pattern: " + " " + Formatter.UNDERLINE + str(self.skip_pattern()))
