import frappe
import pandas as pd
import json


def cron():
    df = pd.read_csv("/home/kishan/Downloads/oodo-ncr integration_YAC_16Aug2021 New Update.csv")
    df.rename(columns = {'Debit':'debit_in_account_currency', 
                        'Credit':'credit_in_account_currency',
                        'Account':'account',
                        'Date':'posting_date',
                        'Journal Name':'voucher_type',
                        'Reference/Narration':'cheque_no'
                        }, inplace = True)
    df['posting_date'] = pd.to_datetime(df['posting_date'])
    # df['cheque_date'] = df['posting_date']
    df['posting_date'] = df['posting_date'].dt.strftime('%Y/%m/%d')
    df['posting_date'] = df['posting_date'].astype(str)
    df['cheque_date'] = df['posting_date'].astype(str)
    x = df.groupby('Journal No.').apply(lambda x: x.to_json(orient='records'))
    for i in x:
        y = json.loads(i)
        posting_date = y[0]['posting_date']
        cheque_no = y[0]['cheque_no']
        voucher_type = y[0]['voucher_type']
        cheque_date = y[0]['cheque_date']
        title = y[0]['account']
        
        for j in y:
            del j['Partner']
            del j['Journal No.']
            del j['voucher_type']
            del j['posting_date']
            del j['cheque_no']
            del j['cheque_date']
            print('\n\n\n\n\n','accounts \n',j,'\n\n')

        journal = frappe.get_doc({
            "doctype": "Journal Entry",
            "naming_series":"ACC-JV-.YYYY.-",
            "title":title,
            "company":"IRSAA Business Solution",
            "voucher_type": voucher_type,
            "posting_date":posting_date,
            "cheque_no":cheque_no,
            "cheque_date":cheque_date,
            "accounts":y    
        })
        journal.insert()
        journal.run_method('submit')
        frappe.db.commit()
        
        # print('\n\n\n',json.dumps(journal,indent=2),'\n\n\n')
