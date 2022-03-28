# Sources list

ProGit(Book)
[Git and GitHub for Beginners - Crash Course ](https://www.youtube.com/watch?v=RGOj5yH7evk&ab_channel=freeCodeCamp.org)
[Atlassian - setting up a repo](https://www.atlassian.com/git/tutorials/setting-up-a-repository)





# Todo

Large File storage
git init --SEPARATE-GIT-DIR=
# Pro Git
## What is git 
### Version control 
What is “version control”, and why should you care? Version control is a system that records changes to a file or set of files over time so that you can recall specific versions later. 

![[Pasted image 20220215143750.png]]

### Centralized version control
The next major issue that people encounter is that they need to collaborate with developers on other systems. To deal with this problem, Centralized Version Control Systems (CVCSs) were developed. These systems (such as CVS, Subversion, and Perforce) have a single server that contains all the versioned files, and a number of clients that check out files from that central place. For many years, this has been the standard for version control.
![[Pasted image 20220215143848.png]]


### Distributed version control
This is where Distributed Version Control Systems (DVCSs) step in. In a DVCS (such as Git, Mercurial, Bazaar or Darcs), clients don’t just check out the latest snapshot of the files; rather, they fully mirror the repository, including its full history.
![[Pasted image 20220215143951.png]]

![[Pasted image 20220220161558.png]]

 ![[Pasted image 20220220161605.png]]


### Nearly Every Operation Is Local

### Git Has Integrity

Everything in Git is checksummed before it is stored and is then referred to by that checksum. This means it’s impossible to change the contents of any file or directory without Git knowing about it. This functionality is built into Git at the lowest levels and is integral to its philosophy. You can’t lose information in transit or get file corruption without Git being able to detect it.

 A SHA-1 hash looks something like this:

```
24b9da6552252987aa493b52f8696cd6d3b00373
```


### The Three States S.15

Pay attention now — here is the main thing to remember about Git if you want the rest of your learning process to go smoothly. Git has three main states that your files can reside in: _modified_, _staged_, and _committed_:

-   Modified means that you have changed the file but have not committed it to your database yet.
    
-   Staged means that you have marked a modified file in its current version to go into your next commit snapshot.
    
-   Committed means that the data is safely stored in your local database.
    

This leads us to the three main sections of a Git project: the working tree, the staging area, and the Git directory.
![[Pasted image 20220220161453.png]]

#### Unstaging a staged file
```bash
git reset HEAD <file> #or  
git restore --staged <file>
```


#### Reset changes on unstaged file
```bash
git restore <file>
```
This reset all changes to the file and reverts it to last commit version, be careful if you do this all your changes are gone

#### Showing remotes
```bash
git remote
```
`-v` to see the corresponding url's

#### Getting data from remotes
```bash
git fetch
```
No automatic merge is done 
![[Pasted image 20220325120142.png]]

### Tagging 
#### Listing tags
Lists tags in alphabetical order
```bash
git tag
```

#### Creating Tags
There exist two types of tags *lightweight* and *annotated*
```bash
git tag -a v1.4 -m "<Message>" #annotated tag
git tag v1.4 #lightweight tag
```
This will tag your current commit 

#### Tagging earlier commits
```bash
git tag -a v1.2 <commit id>
```


#### Push tags
```bash
git push --tags
````

#### deleting tag names 
```
git tag -d <name>
```

Using tags enables you to checkout specific tags
```bash
git checkout v2.0.0
```
But this put you in a detached head state so you can use 
```bash
git checkout -b <branch-name> <tag-name>
```
to automatically create a new branch 


## Git branching
### What are branches
![[Pasted image 20220326155633.png]]
![[Pasted image 20220326155642.png]]
![[Pasted image 20220326155736.png]]
![[Pasted image 20220326155809.png]]
A branch in Git is simply a lightweight movable pointer to one of these commits. The default branch name in Git is master. As you start making commits, you’re given a master branch that points to the last commit you made. Every time you commit, the master branch pointer moves forward automatically
How does Git know what branch you’re currently on? It keeps a special pointer called HEAD. Note that this is a lot different than the concept of HEAD in other VCSs you may be used to, such as Subversion or CVS.

See on which commits the branches are
```bash
 git log --oneline --decorate
```

So checkout just moves the <mark style="background: #FF5582A6;">HEAD</mark> to point the new branch

![[Pasted image 20220326160110.png]]
![[Pasted image 20220326161112.png]]

```bash
 git log --oneline --graph --all --decorate
```
![[Pasted image 20220326160551.png]]
Because a branch in Git is actually a simple file that contains the 40 character SHA-1 checksum of the commit it points to, branches are cheap to create and destroy. Creating a new branch is as quick and simple as writing 41 bytes to a file (40 characters and a newline).

![[Pasted image 20220326161105.png]]
![[Pasted image 20220326161157.png]]

### Basic merging 
State: your are on iss53
Merge changes into your branch
```bash
git checkout master
git merge iss53
```
Git does a simple three-way merge, using the two snapshots pointed to by the branch tips and the common ancestor of the two.
![[Pasted image 20220326162130.png]]
![[Pasted image 20220326162201.png]]
Instead of just moving the branch pointer forward, Git creates a new snapshot that results from this three-way merge and automatically creates a new commit that points to it. This is referred to as a merge commit, and is special in that it has more than one parent.
![[Pasted image 20220326162206.png]]
G
### Branching workflows
Long running branches
![[Pasted image 20220326163105.png]]
#### origin/master
![[Pasted image 20220326163305.png]]
![[Pasted image 20220326163334.png]]
You can also do git push origin serverfix:serverfix, which does the same thing — it says, “Take my serverfix and make it the remote’s serverfix.” You can use this format to push a local branch into a remote branch that is named differently. If you didn’t want it to be called serverfix on the remote, you could instead run git push origin serverfix:awesomebranch to push your local serverfix branch to the awesomebranch branch on the remote projec

#### Rebasing

102
220-340

### First time setup
https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup

## Git basics

Init empty git repository with `git init`
```bash
git init
```
Clone existing(possibly local) repo with `git clone`


# git commands

## Git basics

### git init

### git clone 
git clone \<repo-name> creates a directory called \<repo-name and copies the necessary files into it.

git clone \<repo-name> \<new-name> creates a directory called \<new-name> and copies the necessary files into it.
### git add

### git commit


Pro Git: https://git-scm.com/





# Git and GitHub for Beginners - Crash Course 




# Git workflow

## First step(Configure git)


## Working with git
Initializing a new git repository(a repository is basically another for a project) i.e. in our case a folder
```bash
git init <repo_name>
or 
git init . #init repo in existing directory
```
or cloning(copying) an already existing git repository
```bash
git clone <url>
```
TODO:ssh vs https

TODO How to get help i.e. -h and man pages

TODO: git status
	Shows branch and other things we will get into later.
	![[Pasted image 20220220185445.png]]


```bash
touch main.py
```
```python
#!/usr/bin/python3
def main():
	print("hello from python")
	
	
if __name__ == "__main__":
	main()

```

```bash
chmod +x main.py
```

Now this file is in your working directory but its not checked by git. To make this file  know to git you have to add it 
```bash
git add main.py
```
Now the file is at the staging are of git(!The file is not stored in git yet)
```bash
git status
```

TODO: 3 STAGES OF GIT


The next thing to do is commit the file so git really knows about the file and later also its changes
```bash
git commit -am "message"
or
git commit main.py -m "message" #If the file is already know to git
or 
git commit 
```

Useful flags for commit
```bash
git commit -v
git commit -a
```
TODO: What should be the content of a single commit(semantically different changes)
TODO: Amend

Lets add a new feature to our python program
```python
#!usr/bin/python3
def main():
	name = input("Please enter your name: ")
	print(f"hello from python {name}")
	
	
if  __name__ == "__main__":
	main()

```


```python
#!usr/bin/python3
def main():
	name = readline()
	print("hello from python {name}")
	
	
def sayGoodBye(name):
	print(f"Goodbye {name}")

if  __name__ == "__main__":
	name = main()
	sayGoodBye(name)

```
Two semantically different things i.e. changes that should not be mixed in a commit
```bash
git add -p
use e to get into editing mode
git commit -m "Added function to read in name"



git add -p
git commit -m "Added functionality to say Goodbye"
```

Enables you to stage different hunks of a given file.
This will present you with a chunk of changes and prompt you for a command. Use `y` to stage the chunk, `n` to ignore the chunk, `s` to split it into smaller chunks, `e` to manually edit the chunk, and `q` to exit.


-   y stage this hunk for the next commit
-   n do not stage this hunk for the next commit
-   q quit; do not stage this hunk or any of the remaining hunks
-   a stage this hunk and all later hunks in the file
-   d do not stage this hunk or any of the later hunks in the file
-   g select a hunk to go to
-   / search for a hunk matching the given regex
-   j leave this hunk undecided, see next undecided hunk
-   J leave this hunk undecided, see next hunk
-   k leave this hunk undecided, see previous undecided hunk
-   K leave this hunk undecided, see previous hunk
-   s split the current hunk into smaller hunks
-   e manually edit the current hunk
-   ? print hunk help

This is quite cumbersome, we will later mention a few tools to make this easier, but I think its important to know the terminal commands 
No lets review what we did, which brings use to the next git command `git log` and `git diff`
`git log.`
TODO HEAD HASH IDs
Shows you the history of the TODO branch or repo?

`git diff`
![[Pasted image 20220326223555.png]]
But lets say you want to look at the difference between two files(later more uses)(only considers non-staged files)
how to diff staged file `git diff --stages`
TODO include example
```bash
git diff <file-1> <file-2>
```
This creates a diff of the current aka. latest comited version against the one version you specified i.e. every line with a `-` does not exist in your current but in the old, and every line that starts with a `+` does exist in the current but not the old version. Explain this correct
https://www.atlassian.com/git/tutorials/saving-changes/git-diff
![[Pasted image 20220220194313.png]]
TODO git with HEAD 
TODO git with uncommited changed

By default i.e. if you call `git diff` without any arguments it will show you all uncommited changes since the last commit.

I you want to look at all the commits you did you can call git log
```bash
git log 
```
Here you can also see the specific hashes of each commit, to for example look at a diff of two specific commits(will only show commits of the current branch, we will cover branches in a few minutes)
![[Pasted image 20220321150857.png]]

But what happens if you make a mistake i.e. you want to delete changes to the files or maybe even undo whole commits or you just want to revisit an old commit, maybe because you found some weird behavior in the behavior of the program you are working on at the moment
Lets say you changed the line down below from `Hello` to `Goodbye` but you are not sure if that was always the case, and you also don't know which commit might have changed the behavior of the program
![[Pasted image 20220321151348.png]]
You look at the last message(remember `git log`) but the author clearly stated that nothing happened in this commit
so your try a random earlier commit or one for which you remember that the program was still working there(maybe you even wrote some test)
![[Pasted image 20220321151543.png]]
So you do 
```bash
git checkout 5571c51f41733de093ed178ce4291fd1d5471810
```
You try out the program and everything is correct, so lets do a diff
![[Pasted image 20220321151937.png]]
You go back to main
```bash
git checkout main
```
and you dou
```bash
git diff 5571c51f41733de093ed178ce4291fd1d5471810
```
And you easily found the mistake, so it was the last commit after all, but how we get rid of the last commit 
![[Pasted image 20220321152128.png]]
There three ways of doing this `git checkout`, `git revert`, `git reset`

Lets start with `git revert`, to revert the last commit just write
```bash
git revert HEAD
```
We will talk about HEAD later.
![[Pasted image 20220321153002.png]]
And everything is back in order
![[Pasted image 20220321153105.png]]

TODO git clean
TODO git reset
1.  `git reset --soft HEAD^1`
TODO git rm
TODO Undoing uncomited changes https://www.atlassian.com/git/tutorials/undoing-changes

 ### [Branching](https://www.atlassian.com/git/tutorials/using-branches)
Lets say you want to implement a new feature which will take a while and might leave your program in an "unusable" state, but you still want to be able to run the current version of your program. There ofc is a feature for that called branching
`git branch \<branch name>`
This creates a new branch called \<branch-name>
Lets implement a class to store information about the user as well as ask for their age to do this we switch to a new branch

TODO Picture about tree 
![[Pasted image 20220323091534.png]]
```
git branch feature-age #this only creates a branch, but we are still on main. see git status
git checkout feature-age
```

```python
#!/usr/bin/python3     
    
class User():    
    def __init__(self, name, age):    
        self.name = name    
        self.age = age    
    
    def toString(self):    
        return f"Hello {self.name} you are {self.age} years old"    
    
def main():    
    name = input("Please enter your name: " )    
    age = input("Please enter your age: " )    
    user = User(name, age)    
        
    print(user.toString())    
    
    return name    
    
def sayGoodBye(name):    
    print(f"Goodbye {name}")    
    
    
if __name__ ==  "__main__":    
    name = main()    
    sayGoodBye(name)    
```

After doing implementing our new feature, we of course want to bring the changes to the main working branch
this brings us to `git merge`
`Git merge` will combine multiple sequences of commits into one unified history. In the most frequent use cases, `git merge` is used to combine two branches.
![[Pasted image 20220323091542.png]]
Execute `git status` to ensure that `HEAD` is pointing to the correct merge-receiving branch.
```bash
git checkout main
```

```bash
git merge age-feature
```
Now the changed made on the *age-feature* branch are merged onto the new and you can delete the *feature branch*
```bash
git branch -d age-feature
```
*-d* is safe delete i.e. if there are unmerged changed on the feature branch the delete will fail, if you want to delete the branch anyway there is *-D*


# Git collaboration
We know how to
* execute basic git commands
* create/delete branches
Those are the basics of working locally. But you are probably asking yourself: Whats up with GitLab and GitHub and how can I backup my files,
because atm all of our files are still only stored on our local computer i.e. if the drive fails all of our data is gone. So lets talk about GitLab
![[Pasted image 20220323101238.png]]
Now lets clone the repo into a new folder to simulate another person which whom you are collaborating
We now have the same files/same repo is the two folders *repo1* and *repo2*
```bash
git remove add git@github.com:Unaimend/test.git
```

```bash
git pull -u origin man
```

Now image the other persons thinks it would be a good idea to move the user class to a seperate file
![[Pasted image 20220323103223.png]]
Further imagine your collaborater wants to have lunch, but before this he wants to save his changes online, for this he uses `git push`
![[Pasted image 20220323103357.png]]
```bash
git push
```

Now it is possible to see the new changes online and everything is safe, so he can go to lunch 
![[Pasted image 20220323103425.png]]
But if you look at your own directory 
```
git branch -a #also shows remote branches
```
![[Pasted image 20220323115419.png]]
you can see that you currently do not have the user branch in your repository, also there is no user.py and your main.py looks like before
```bash
git pull
```
Executing git pull now synchs your local copy with the online repository and you can checkout the user branch
Now you now the basics of collaborating with other people via git(hub)

We will now talk about a few more advanced features

## git stash
Lets imagine your are working on some feature and a colleague asks you to look at what he did.
So you pull down his changes with *git pull*
And try to switch to his branch and you see this, git asks to you to commit or stash(?) your changes, your of couse do not wan't to make a commit be cause you did not name any meaning full change
![[Pasted image 20220323120336.png]]
The `git stash` command takes your uncommitted changes (both staged and unstaged), saves them away for later use, and then reverts them from your working copy. Now you are able to checkout his changes.
![[Pasted image 20220323120826.png]]
And go back to your branch and continue to work as if nothing hapend
![[Pasted image 20220323120902.png]]
Lets revert the changes with
```bash
git restore main.py
```
By default, running `git stash` will stash:

-   changes that have been added to your index (staged changes)
-   changes made to files that are currently tracked by Git (unstaged changes)

But it will **not** stash:

-   new files in your working copy that have not yet been staged
-   files that have been ignored

For more on git stash see https://www.atlassian.com/git/tutorials/saving-changes/git-stash
## git bisect

Automatic git bisect
![[Pasted image 20220323130814.png]]

## git difftool
## merge conflicts

## git merge in-depth
TODO Merge conflicts
https://www.atlassian.com/git/tutorials/using-branches/git-merge
https://www.atlassian.com/git/tutorials/using-branches/merge-conflicts
https://www.atlassian.com/git/tutorials/using-branches/merge-strategy

TODO: Tools
	GitKraken
	GitHubDesktop
	SourceTree
	Magit(Emacs)

Cheatsheets
![[SWTM-2088_Atlassian-Git-Cheatsheet.pdf#page=1]]
```bash
git init <repo_name2>
```

To watch
Minute 30
https://www.youtube.com/watch?v=RGOj5yH7evk&ab_channel=freeCodeCamp.org
Not started
https://www.youtube.com/watch?v=Uszj_k0DGsg&ab_channel=freeCodeCamp.org
Not started

Reading List
https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent
https://www.atlassian.com/git/tutorials/advanced-overview
https://www.atlassian.com/git/articles/core-concept-workflows-and-tips
https://www.atlassian.com/git/articles/alternatives-to-git-submodule-git-subtree
https://www.atlassian.com/git/articles/git-team-workflows-merge-or-rebase
https://www.atlassian.com/git/articles/simple-git-workflow-is-simple
https://www.atlassian.com/git/articles/simple-git-workflow-is-simple
https://www.atlassian.com/git/tutorials/comparing-workflows
https://docs.dolthub.com/introduction/what-is-dolt

# Jan
TODO git tag
## Semver
Given a version number MAJOR.MINOR.PATCH, increment the:

1.  MAJOR version when you make incompatible API changes,
2.  MINOR version when you add functionality in a backwards compatible manner, and
3.  PATCH version when you make backwards compatible bug fixes.

Additional labels for pre-release and build metadata are available as extensions to the MAJOR.MINOR.PATCH format.


For this system to work, you first need to declare a public API. This may consist of documentation or be enforced by the code itself. Regardless, it is important that this API be clear and precise. Once you identify your public API, you communicate changes to it with specific increments to your version number.

Bug fixes not affecting the API increment the patch version, backwards compatible API additions/changes increment the minor version, and backwards incompatible API changes increment the major version.

https://semver.org/

# Lena
## Work with git and Rstudio
You need to create a **Project** in R, and then at the Tools label you can select version control, but the R git support is quite bad 
![[Pasted image 20220323133442.png]]

## What kind of data to put in to
You can basically put everything in git, but I would be careful if you bug files which are quite big >100mb
Also uploading binary files does not make much sense, you will for example not get meaningful diffs for binary files

## git LFS
Git is a _distributed_ version control system, meaning the entire history of the repository is transferred to the client during the cloning process. For projects containing large files, particularly large files that are modified regularly, this initial clone can take a huge amount of time, as every version of every file has to be downloaded by the client.
![[Pasted image 20220323134312.png]]
![[Pasted image 20220323134912.png]]

But to be hones I don't think it is that useful for use because we do not work with regular changing big files

# Stefano
CI/CD
Project management/issues

# Git Local Advanced 
TODO HEAD
TODO git mv
git rm --cached README
Another useful thing you may want to do is to keep the file in your working tree but remove it from your staging area. In other words, you may want to keep the file on your hard drive but not have Git track it anymore. This is particularly useful if you forgot to add something to your .gitignore file and accidentally staged it, like a large log file or a bunch of .a compiled files. To do this, use the --cached option:
TODO git diff branch
TODO git rebase
TODO git workflows
TODO git cherrypick https://www.atlassian.com/git/tutorials/cherry-pick
TODO merge vs rebase https://www.atlassian.com/git/tutorials/merging-vs-rebasing
TODO git reflog
TODO .gitignore
TODO git bisect  https://git-scm.com/docs/git-bisect
git alias
g git config --global credential.helper cache.

Revert single file 
![[Pasted image 20220327192506.png]]