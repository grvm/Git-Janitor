from worker import Worker

class GitJanitor:

  def __init__(self, args):
    self.args = args
    self.worker = Worker(args)

  def want_to_preview(self):
    return "--preview" in self.args

  def want_to_clean(self):
    return "--clean" in self.args

  def clean(self):
    return self.worker.delete_branches()
    # `sh -c "git branch origin --delete #{branches_to_be_deleted}"`

  def preview(self):
    return self.worker.branches_to_be_deleted()

  def do_ya_thang(self):
    if(self.want_to_preview() or not self.want_to_clean()):
      self.preview()
    if self.want_to_clean():
      self.clean()