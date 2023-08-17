# lfsData

This document provides instructions on how to work with Git Large File Storage (LFS) for the `qomnet` project.

## Getting Started with Git LFS

Git LFS is a Git extension that improves handling of large files by replacing them with text pointers inside Git, while
storing the file content on a remote server.

### Installation

To install Git LFS, use the following command:

``` shell
git lfs install
```

## Clone Repository

To clone repository with only pointer files, use following commands:

* Linux (bash):

``` shell
GIT_LFS_SKIP_SMUDGE=1 git clone ssh://git@git.arusha.dev:9022/majd/datasets/qomnet.git
```

* Windows:

``` shell
$env:GIT_LFS_SKIP_SMUDGE="1"
git clone ssh://git@git.arusha.dev:9022/majd/datasets/qomnet.git
``` 

## Tracking Files :

``` shell
git lfs track "*.psd"
git add .gitattributes
```

## Committing & Pushing Changes :

To commit and push changes, type:

``` shell
git add file.psd
git commit -m "Add design file"
git push origin main
```

For more information about Git LFS, check [here](https://git-lfs.com/)