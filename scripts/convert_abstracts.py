#!/usr/bin/python
import openpyxl

excel_filename = "abstracts.xlsx"
yaml_filename = excel_filename.replace('xlsx', 'yaml')
abstracts = {}

excel_ws = openpyxl.load_workbook(excel_filename).active


for row in excel_ws.iter_rows(min_row=2):
  # save the csv as a dictionary
  authors=[]
  for author in row[3].value.split(';'):
    (last, first)=author.strip("*").strip().split(',',2)
    author = f"{first.strip()} {last}"
    authors.append(author)
  abstracts[row[0].value] = {'title': row[1].value, 'abstract': row[2].value, 'authors': authors, 'format': row[4].value, 'year': row[5].value}

print(abstracts)
with open(yaml_filename, "w+") as yf :
  for id, abstract in abstracts.items():
    yf.write(f"- abstract_id: {id} \n")
    yf.write(f"""  title: > \n    {abstract['title']}\n""")
    abs = abstract['abstract'].strip().replace("\n", " \n    ")
    yf.write(f"""  abstract: | \n    {abs}\n""")
    yf.write(f"""  format: "{abstract['format']}"\n""")
    yf.write(f"""  year: {abstract['year']}\n""")
    yf.write(f"""  authors:\n""")
    for author in abstract["authors"]:
      yf.write(f"""  - "{author}"\n""")
    yf.write("\n")