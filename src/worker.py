"""The worker Module."""


import os
import sys
from git import Git
from formatter import Formatter


class Worker:
    """The worker Class."""

    def __init__(self, args):
        """Constructor."""
        self.args = args
        self.git = Git(args)

    def branches_to_be_deleted(self):
        """Return branches to be deleted."""
        branches = self.branches_to_be_deleted_excluding_skipped()
        if len(branches) > 0:
            Formatter.print_pretty_warn_message("Following local branches would \
                be deleted:")
            return branches
        else:
            Formatter.print_pretty_fail_message("No branches to be deleted")
            return []

    def branches_to_be_deleted_excluding_skipped(self):
        """Return branches to be deleted except pattern matching branches."""
        branches = list(
            set(
                self.git.merged_branches()
            ).difference(
                self.git.pattern_matching_branches())
            )
        self.exclude_current_branch(branches)
        return branches

    def delete_branches(self, remote=False):
        """Delete the branches."""
        """If Remote=True, deletes remote branches as well."""
        if len(self.branches_to_be_deleted()) > 0:
            self.delete_local_branches()
            if remote:
                self.delete_remote_branches()
            Formatter.print_pretty_ok_message("Cleaned Successfully!!")

    def delete_remote_branches(self):
        """Delete remote branches."""
        try:
            os.popen("git push origin --delete " + " ".join(
                self.branches_to_be_deleted())
            )
        except:
            print "There was an error deleting remote branches: ",
            sys.exc_info()[0]

    def delete_local_branches(self):
        """Delete local branches."""
        os.popen("git branch -D " + " ".join(self.branches_to_be_deleted()))

    def exclude_current_branch(self, branches):
        """Exclude current branch from list of branches to be deleted."""
        if(self.git.current_branch() in branches):
            branches.remove(self.git.current_branch())
