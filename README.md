# BYB_Project - Submitted by Bhavya Patteeswaran
"""
● Login to GitHub using the account you created in a previous task.
● Create a new repository by selecting the ‘New’ button as shown in the image below.
● Name the repository ‘byb_project’ and make sure that it is public.
● Next, create an empty folder called byb_project on your local machine.
● Open your terminal or command prompt and then change directory (cd) to your newly created folder.
● Enter the git init command to initialise your new repository. 
git init
● Enter the git status command and make a note of what you see. You should have a clean working directory.
git status
● Create a new file in the byb_project folder called helloWorld.py and write a program that prints out the message “Hello World!”.
● Run the git status command again. You should now see that your helloWorld.py file is untracked.
git status
● Enter the git add command followed by helloWorld.py to start tracking your new file.
git add helloworld.py
● Once again, run the git status command. You should now see that your helloWorld.py file is tracked and staged to be committed
git status
● Now that it is tracked, let us change the file helloWorld.py. Change the message printed out by the program to “Git is Awesome!”
● Run git status again. You should see that helloWorld.py appears under a section called “Changes not staged for commit”. This means that the file is
tracked but has been modified and not yet staged.
● To stage your file, simply run git add helloWorld.py again.
● If you run git status again you should see that it is once again staged for your next commit.
● You can now commit your changes by running the git commit -m command. Remember to enter a suitable commit message after the -m switch. 
● Running the git status command should now show a clean working directory once again.
● Push the repository on your local machine to the remote repository on GitHub by following these steps:
○ Open your terminal or command prompt. Change directory (cd) into the byb_project folder you created.
○ Add your remote repository using the following command: git remote add [remote-name] [url]
e.g. git remote add origin https://github.com/HyperionDev/byb_project.git.
Now you can use the short name (e.g. origin) on the command line in lieu of the whole URL. The URL will be indicated under the heading shown below once you have created your repository on GitHub.
○ Push your local repository to your remote repository using the following command:
git push -u [remote-name] master
E.g. git push -u origin master
● Make the repository public and put a link to it in a Google doc (help for this is available here). Make it clear that the link is for Compulsory Task 1.


Command to remember:
git init
git status
git add .
git commit -m "First Commit"
git remote add byb3 https://github.com/BhavyaP17/byb3_project
git push -u byb3 master

git commit -m "message"
git remote add [shortname] [url]
git push -u [shortname] [branchname]

"""
