**Use** `git` **to Clone Partially**:

- Use the sparse-checkout feature to clone only a portion of the repo:

```bash
git init #initialise the repo
git remote add -f origin [remote repository URL] # add the remote repo
git config core.sparseCheckout true # add the sparse checkout folder
echo "name_of_file/folder_you_want_to_download*" >> .git/info/sparse-checkout # specify the file/folder to checkout
git pull origin main #pull the file from the remote repo

#add another file to the sparse-checkout folder
echo 'name_of_another_file/folder' >> .git/info/sparse-checkout 
git sparse-checkout reapply #apply these newest files: pull the additional files
```

Example;
- use with our repository
- Download only the README.md file

```bash
git init
git remote add origin git@github.com:mulyung1/mini_projects.git
git config core.sparseCheckout true
echo "README.md" >> .git/info/sparse-checkout
git pull origin main

echo 'python_docker.py' >> .git/info/sparse-checkout
git sparse-checkout reapply
```
- Replace `[repository URL]` with the URL of the repo, and `path/to/folder/*` with the folder path you want to check out.
