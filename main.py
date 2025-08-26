import os
import sys
import subprocess

git = "/usr/bin/git"
home = os.path.expanduser("~")
git_dir = f"{home}/.dotfiles"
work_tree = home

git_cmd_untracked = [
    git,
    f"--git-dir={git_dir}",
    f"--work-tree={home}",
    "config",
    "status.showuntrackedfiles",
    "no",
]

git_cmd_config = [
    git,
    f"--git-dir={git_dir}",
    f"--work-tree={home}",
]


def config(commit=None):
    if commit:
        message = sys.argv[2]
        cmd = git_cmd_config[:3]
        commit_cmd = ["commit", "-m", message]
        cmd = cmd + commit_cmd
        subprocess.run(cmd)
    else:
        cmd = git_cmd_config[:3]
        cmd = git_cmd_config + sys.argv[1:]
        subprocess.run(cmd)


if sys.argv[1] == "commit":
    config(commit=True)
else:
    config()
