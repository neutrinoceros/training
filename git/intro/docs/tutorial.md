
# Hands-on tutorial

## git command line interface (CLI)

There exist *many* GUIs (Graphical User Interfaces) for git, and most IDEs
contain some kind of `git` interface, but the fundamental interface, and the
*only* one that is available on servers typically accessed via `ssh` tunnels, is
the command line, so that's what we will use here.

The `git` CLI is composed of many sub-commands `git <stuff>`. In this tutorial
we will go through the essential ones.

I strongly recommend *sticking* to the CLI after you've mastered the basics,
because it is by far the most portable way to use git: it is the only one
available everywhere.

### Pre-requisites
> if you've used git on your current machine in the past, skip this section

make sure `git` is available on your system
```
$ which git
```
if not, follow [official docs](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

Next, you'll want to configure git globally
```
$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com
```

### Additional recommendations

It is also recommended to associate a terminal-based editor of your choice to `git`.
For instance this is how you'd set `nano`
```
$ git config --global core.editor nano
```
This is because some advanced sub-commands require an editor, and its preferable
to know that you are confortable with the one you get (otherwise it may default
to `vi`, which is infamously hard to exit when you've never used it).

It it recommended that to sign up on GitHub.

### Getting started (first commits)
> In this section we will create a dummy project *from scratch*. You can use an
> actual project of yours instead if you feel confortable to.



Create a new project (or *repository* from now on)
```
$ mkdir my-project
$ cd my-project
$ git init
```
We now have an empty project: no files are currently being *tracked*, and we
have no history. Let's introduce a very useful command that will help us
visualize the current state of the repository : `git status`.

> While the output of `git status` calls is included in the page, it is strongly
> recommended to run these yourself in a terminal.

<details><summary> git status </summary>
```

On branch main

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```

</details>

Now let's start by creating some file
```
$ echo "Hello world !" > README.txt
```

and see how this affects the state

<details><summary> git status </summary>
```
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
    README.txt

nothing added to commit but untracked files present (use "git add" to track)
```
</details>

We see that the file we just created is currently *untracked*, meaning its evolution is not followed by `git`.
The output of `git status` also contains a helpful hint at what to do next to start tracking it:

```
$ git add README.txt
```
<details><summary> git status </summary>
```
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
    new file:   README.txt
```
</details>

We see that `README.txt` is now being *tracked* by the system, but it is not *commited* yet, meaning we haven't created an actual *version* (or *commit*, from now on) in the history. So let's do just that

```
$ git commit -m "Add README.txt"
```

with `-m`, with associate a *message* to our commit.
The message should be *concise* yet *meaningful* and describe the change that was performed.

<details><summary> git status </summary>
```
On branch main
nothing to commit, working tree clean
```
</details>

Hurray ! Now `README.txt` is being tracked by `git` *and* we have a history that should look something like this

<img title="one lonely commit" src="https://raw.githubusercontent.com/neutrinoceros/training/git_intro/git/intro/docs/single_commit_history.png">


<details><summary> git log </summary>
```
commit 956206c5db49848047ef45161ed9e457dcb5f9a8 (HEAD -> main)
Author: John Doe <johndoe@example.com>
Date:   Mon Nov 28 15:22:38 2022 +0100

    Add README.txt
```
</detail>
