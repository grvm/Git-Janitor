import os

from git import Git
from color import Color

class Worker:

  def __init__(self, args):
    self.args = args
    self.git = Git(args)

  def branches_to_be_deleted(self):
    branches = list(set(self.git.merged_branches()).difference(self.git.pattern_matching_branches()))
    self.remove_current_branch(branches)
    if len(branches) > 0:
      print Color.BOLD + Color.WARNING_COLOR + "Following local branches would be deleted:" + Color.ENDC
      return branches
    else:
      print Color.BOLD + Color.FAIL_COLOR + "No branches to be deleted" + Color.ENDC
      return []

  def delete_branches(self):
    if len(self.branches_to_be_deleted()) > 0:
      os.popen("git branch -D " + " ".join(self.branches_to_be_deleted()))
      self.delete_remote_branches()
      print Color.BOLD + Color.OK_COLOR + "Cleaned Successfully!!" + Color.ENDC

  def delete_remote_branches(self):
    try:
      os.popen("git push origin --delete " + " ".join(self.branches_to_be_deleted()))
    except:
      print "There was an error deleting remote branches: ", sys.exc_info()[0]

  def remove_current_branch(self, branches):
    if(self.git.current_branch() in branches):
      branches.remove(self.git.current_branch())
