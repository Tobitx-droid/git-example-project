#git init -> For initializing or creating a git repository.                                                            The repository would now be created and you have to go to github to manually give a name to the repository

#git status -> For checking whether there is a file in the repository you have modified or given a commit message.

#git add . || git add <file name> -> This is for adding all modified files or a file(git add <file name>) to the git repository. 

#git push -> After naming the file in github you need to copy the git url of the file and run it in the terminal to allow git push.

#git pull -> This command updates the local repository with the remote repository if the remote repository is ahead of the local repository.

# git restore <filename> -> This command is to restore a change in a modified file to make the file an unmodified file

#git restore --staged <filename> -> This command is to undo the command to add a file to the repository.

#git log -> This gives us a full history of all the commits we've made

#git log --oneline -> This give a one line each history of all the commits made to a repository

#git commit -v --amend -> This command helps you to correct errors in your commit messages. The (-v) stands for verbose meaning we a amending something verbose in the commit message.                                           To close the editor that is opened, you just need to hit on the x button, it closes the file.

#We are now going to talk about creating branches in git.                      Branches help different people work on different aspects of the the same project together so that it can be later merged after each aspect has been perfected.

#git branch --list -> This command gives us a list of the various branches of the same project.

#git branch <branch name> ->             This command is for creating a new branch with a given name.

#git checkout <branch name>  ->                        This command is for switching from one branch to the other

#touch <filename(with extension)>                         ->                        This command is for creating a new file