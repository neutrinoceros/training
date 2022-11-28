
# Introduction

## What is `git` ?

[git](https://git-scm.com) is a **distributed version control system** (VCS).

A *version control system* enables *management of change history* for files.
We will see about the "distributed" part later.

Here's a representation of a simple (single branch) change history, where the arrow indicates time, each dot represents a different *version*

<p align="center">
<img title="a simple linear history" src="https://raw.githubusercontent.com/neutrinoceros/training/git_intro/git/intro/docs/single_branch_linear_history.png">
</p>

(We will see more interesting examples later).

Essentially, a VCS enables a workflow where change is *incremental*, *reversible*, and *searchable*.
This drastically decreases the cost of making mistakes and breaking things, because it's easy to go back to a previous version !


## When do you need it ?

`git` is useful for any project you work on today and will still care about tommorow. It could be some source code, but it can also be a **paper manuscript**.
This website itself is backed-up with `git`.


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
