"""Module to find branches to be deleted & which ones to skip."""

import os
import re
from formatter import Formatter


class Git:
    """The git class."""

    def __init__(self, args):
        """The constructor."""
        self.args = args

    def skip_pattern(self):
        """Check if --skip-pattern exists in args."""
        pattern = re.compile("--skip-pattern=(.+)")
        strng = " ".join(self.args)
        mtch = pattern.search(strng)
        return mtch.group(1) if mtch else ""

    def current_branch(self):
        """Return the current branch working on."""
        return os.popen("git rev-parse --abbrev-ref HEAD").read().strip()

    def merged_branches(self):
        """Return the branches already merged."""
        return self.sanitize_branch_list(
            os.popen("git branch --merged").readlines()
        )

    def pattern_matching_branches(self):
        """Find branches which match the pattern specified, and return them."""
        """Return a blank Array if no matches."""
        if self.skip_pattern_exists():
            cmd = "git branch --list '" + str(self.skip_pattern()) + "' \
            --merged"
            branches = self.sanitize_branch_list(os.popen(cmd).readlines())
            self.warn_if_no_branch_matches_pattern(branches)
            return branches
        else:
            return []

    def sanitize_branch_list(self, branches):
        """Strip whitespaces and newlines."""
        return [x.replace("*", "").strip() for x in branches]

    def skip_pattern_exists(self):
        """Check if a skip pattern exists."""
        return str(self.skip_pattern()) != ""

    def warn_if_no_branch_matches_pattern(self, branches):
        """Show message if no branch matches the specified pattern."""
        if len(branches) == 0:
            Formatter.print_pretty_fail_message("No branch name matches the \
            given skip pattern: " + " " + Formatter.UNDERLINE + str(self.
                                                skip_pattern()))
