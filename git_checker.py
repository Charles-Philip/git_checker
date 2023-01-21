import git
from datetime import datetime as dtt
import datetime as dt


target_name = "Rufus"

def git_status_checker(git_dir) :

    # get and test the input git directory 
    repo_to_check = git.Repo(git_dir)
    assert not (repo_to_check.bare), f"Repo error: Repo empty, got: {repo_to_check}"

    # git repo check
    head_to_check = repo_to_check.head
    active_branch_check = head_to_check.is_detached
    modified_files_check = repo_to_check.is_dirty()

    # time check setup 
    today = dtt.now()
    last_week = dt.timedelta(days = 7)
    last_commit_dt = dtt.fromtimestamp(head_to_check.commit.committed_date)

    # boolean check for last week 
    last_week_check = ( (today - last_week) < (last_commit_dt) )

    # check if target author ("Rufus") is the last author
    authored_target_name = False
    last_git_author = head_to_check.commit.author.name
    
    if last_git_author == target_name :
        authored_target_name = True
    else :
        authored_target_name = False

    print("Datestamp : ", today)
    print("Active Branch : ", active_branch_check)
    print("Local Changes : ", modified_files_check)
    print("Recent Commit : ", last_week_check)
    print("Authored by" + target_name + ": " + authored_target_name)


git_dir_input = input("Please enter the directory of the git repository: ")
git_status_checker(git_dir_input)