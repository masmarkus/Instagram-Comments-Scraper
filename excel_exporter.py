import pandas as pd
from pandas import ExcelWriter
import os.path

def export(names, comments, dates, fname='comments.xlsx', sheetName='IG-Comments'):
    temp = {}
    temp_names = []
    temp_comments = []
    temp_dates = []
    if os.path.isfile(fname):
        saved = pd.read_excel(fname)
        temp_names.extend(saved['name'])
        temp_comments.extend(saved['comment'])
        temp_dates.extend(saved['date'])
    temp_names.extend(names)
    temp_comments.extend(comments)
    temp_dates.extend(dates)
    temp.update({'name': temp_names, 'comment': temp_comments, 'date': temp_dates})
    df = pd.DataFrame(temp)
    writer = ExcelWriter(fname)
    df.to_excel(writer, sheetName, index=False)
    writer.save()
