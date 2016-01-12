class Formatter:

  WARNING_COLOR = '\033[93m'
  FAIL_COLOR = '\033[91m'
  OK_COLOR = '\033[92m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'

  def bold_and_fail(self):
    self.FAIL_COLOR + self.BOLD

  @staticmethod
  def print_pretty_bold_message(color, message):
    print Formatter.BOLD + color + message + Formatter.ENDC