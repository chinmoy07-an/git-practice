## Hello Git and GitHub members
*This repository will contain quirky snippets which can make coding and analytics easy and fun*

**Must to know GIT commands**

1. **To check your Git configuration**

git config -l

2. **To setup your Git username**

git config --global user.name "Chinmoy"

3. **To setup your Git user email**

git config --global user.email "anandchinmoy36@gmail.com"

4. **To cache your login credentials so you dn't have to type them each time**

git config --global credential.helper cache

5. **To initialize a Git Repo -First step to do**

git init

6. **To add files in staging area**

git add filename

7. **To add all files in the staging area- Using wildcard .**

git add .

8. **To add certain files in the staging area -Using wildcard for pattern**

git add filen

9. **To check Repository status-will show staged , unstaged and untracked files etc**

git status

10. **To commit changes**

git commit

11. **To commit changes with a message**

git commit -m "message for commit"

12. **To add and commit tracked files with a single command**

git commit -a -m "commit message"

13. **To check commit history**

git log

14. **To check commit history including changes**

git log -p

15. **To check specific commit**

git show commit-id

16. **To see log stats - i.e lines changed & file names etc**

git log --stat

17. **To check changes made before committing**

git diff
git diff filename

*git diff shows unstaged changes by default*

18. **To check staged changes difference before committing**

git diff --staged

19. **To interactively see the changes and to stage changes or not,other options too**

git add -p

20. **To remove tracked files -also need commit for reason**

git rm filename

21. **To rename files**

git mv oldfile newfile

22. **To ignore files**

create .gitignore file and commit

23. **To revert unstaged changes**

git checkout filename

24. **To revert staged changes**

git reset HEAD filename
git reset HEAD -p

*use -p option to specify the change you want to reset*

25. **To modify and add changes to most recent commit**

git commit --amend

26. **To rollback last commit**

git revert

*create new commit opposite of recent commit*

27. **To revert latest commit using alias**

git revert HEAD

28. **To revert old commit**

git revert commitid 

29. **To create new Branch**

git branch branchname

30. **To switch to newly created branch**

git checkout branchname

31. **To list branch names**

git branch

32. **To create and switch to a branch single command**

git checkout -b branchname

33. **To delete a branch**

git branch -d branchname

34. **To merge two branches**

git merge branchname

35. **To show commit log as a graph**

git log --graph --oneline

*oneline limits the commit to single line*

36. **To show commit log as a graph for all branches**

git log --graph --oneline --all

37. **To abort a conflicting merge--throw a merge away and start**

git merge --abort

38. **To add a remote repository in git**

git add remote https://reponame

39. **To see all remote urls**

git remote -v

40. **To get info about the remote repository**

git remote show origin

*replace origin with remote name to check info for*

41. **To push changes to remote repo**

git push

42. **To pull changes from remote repo**

git pull

43. **To check remote branches that git is tracking**

git branch -r

44. **To get remote repo changes in git**

git fetch

*This will download the changes from remote repo but not perform merge on local branch*

45. **To check recent commit logs for remote repo**

git log origin/main

46. **To merge remote repo with local repo**

git merge origin/main

47. **To get contents of remote branches without auto merging**

git remote update

48. **To push new branch to remote repo**

git push -u origin branchname

49. **To remove a remote branch**

git push --delete origin branchname

50. **To transfer completed work from one branch to another**

git rebase branchname

51. **To run rebase interactively**

git rebase -i master

*will open editor and present set to commands you can use*

52. **To force a push request**

git push -f

***The above content source***[Git commands](https://www.freecodecamp.org/news/git-cheat-sheet/)

Reach out to me for suggestions or to connect
[![Linkedin](https://i.stack.imgur.com/gVE0j.png) LinkedIn](https://www.linkedin.com/in/chinmoy-anand-b56a4812b)
