"""The Git Janitor Module."""

from worker import Worker


class GitJanitor:
    """The Git Janitor Class."""

    def __init__(self, args):
        """The constructor."""
        self.args = args

    def want_to_clean(self):
        """Return True if --clean is passed as an argument."""
        return "--clean" in self.args

    def want_to_delete_remote(self):
        """Return True if --remote is passed as an argument."""
        return "--remote" in self.args

    def start(self):
        """Start the cleaning process."""
        if self.want_to_clean():
            self.__clean()
        else:
            print self.__preview()

    # Private Methods
    def __clean(self):
        """Clean the rogue branches."""
        Worker(self.args).delete_branches(remote=True)
        # `sh -c "git branch origin --delete #{branches_to_be_deleted}"`

    def __preview(self):
        """Preview the rogue branches."""
        return Worker(self.args).branches_to_be_deleted()
