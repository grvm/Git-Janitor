from worker import Worker

class GitJanitor:

  def __init__(self, args):
    self.args = args

  def want_to_clean(self):
    return "--clean" in self.args

  def want_to_delete_remote(self):
    return "--remote" in self.args

  def start(self):
    if self.want_to_clean():
      self.__clean()
    else:
      print self.__preview()
    
  def __clean(self):
    Worker(self.args).delete_branches(remote=True)
    # `sh -c "git branch origin --delete #{branches_to_be_deleted}"`

  def __preview(self):
    return Worker(self.args).branches_to_be_deleted()
