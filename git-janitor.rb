#!/usr/bin/ruby

class GitJanitor

  attr_accessor :skip_pattern

  def kleen
    p branches_to_be_deleted

    # `sh -c "git branch origin --delete #{branches_to_be_deleted}"`
  end

  def preview
    p branches_to_be_deleted
  end

  def set_skip_pattern(arguments)
    arguments.join(" ").match /(--skip-pattern=\w+)/
    @skip_pattern = $1.split("=").last if $1
  end

  private

    def current_branch
      merged_branches.split("\n").select {|br| br.include? "*"}.first.gsub("*", "").strip
    end

    def pattern_matching_branches
      `sh -c "git branch -a --list *#{skip_pattern}* --merged"`
    end

    def merged_branches
      `git branch -a --merged`
    end

    def to_a(branch_string)
      branch_string.gsub("*", "").split("\n").collect(&:strip)
    end

    def branches_to_be_deleted
      branchs = to_a(merged_branches) - to_a(pattern_matching_branches)
      branchs.delete(current_branch)
      branchs
    end

end

if ARGV.size > 0

  ARGV.join(" ").match /(--skip-pattern=\w+)/
  preview = ARGV.include? "--preview"
  clean = ARGV.include? "--clean"
  @janitor = GitJanitor.new
  @janitor.set_skip_pattern(ARGV)
  @janitor.preview if preview || !clean
  @janitor.kleen if clean
end