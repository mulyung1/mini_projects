# What the code does. 
- The code will read a csv to a pandas dataframe. 
- A new dataframe will be constructed with only the desired columns.
- A list of dictionaries will be constructed that resmebles the JSON structure desired.
- A JSON will be constructed from the list above. 
- The JSON string above is wrote to file. 


# How ro run

1. **Set Up a Virtual Environment**

```bash
python3 -m venv csv2json_venv
```
2. **Activate the virtual environment**
```bash
source csv2json_venv/bin/activate
```
3. **Clone only the csv_to_json mini-project**

```bash
#initialise an empty repo in your local
git init

#add the remote repo
git remote add -f origin git@github.com:mulyung1/mini_projects.git

#add the sparse checkout folder
git config core.sparseCheckout true

#add the csv_to_json folder to checkout
echo 'csv_to_json' >> .git/info/sparse-checkout

#pull this folder to your local
git pull origin main

#go into your mini_project
cd csv_to_json
```
3.1 **Add/download another mini_project?**
```bash
#add the file/folder of interest to your sparse-checkout folder
echo 'name_another_file/folder' >> .git/info/sparse-checkout

#pull the new folder
git sparse-checkout reapply
```

4. **Install Required Dependencies**
```bash
pip install pandas
```

5. **Run the script**
```bash
python3 csv2json.py
```



