import os

from git import Git
from formatter import Formatter

class Worker:

  def __init__(self, args):
    self.args = args
    self.git = Git(args)

  def branches_to_be_deleted(self):
    branches = self.branches_to_be_deleted_excluding_skipped()
    if len(branches) > 0:
      Formatter.print_pretty_bold_message(Formatter.WARNING_COLOR, "Following local branches would be deleted:")
      return branches
    else:
      Formatter.print_pretty_bold_message(Formatter.FAIL_COLOR, "No branches to be deleted")
      return []

  def branches_to_be_deleted_excluding_skipped(self):
    branches = list(set(self.git.merged_branches()).difference(self.git.pattern_matching_branches()))
    self.exclude_current_branch(branches)
    return branches

  def delete_branches(self, remote=False):
    if len(self.branches_to_be_deleted()) > 0:
      self.delete_local_branches()
      if remote:
        self.delete_remote_branches()
      Formatter.print_pretty_bold_message(Formatter.OK_COLOR, "Cleaned Successfully!!")

  def delete_remote_branches(self):
    try:
      os.popen("git push origin --delete " + " ".join(self.branches_to_be_deleted()))
    except:
      print "There was an error deleting remote branches: ", sys.exc_info()[0]

  def delete_local_branches(self):
    os.popen("git branch -D " + " ".join(self.branches_to_be_deleted()))

  def exclude_current_branch(self, branches):
    if(self.git.current_branch() in branches):
      branches.remove(self.git.current_branch())
