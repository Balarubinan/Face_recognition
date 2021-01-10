import sqlite3 as sq
import traceback

con = sq.connect("C:\\Users\\Balarubinan\\emp_score_DB.db")
cur = con.cursor()

# Writes the dscore data to the data base
def write_to_base(fscore,dscore,d1score,tscore,Cname,Cid):
    global cur,con
    fscore=round(fscore,2)
    tscore = round(tscore, 2)
    dscore=round(dscore,2)
    d1score=round(d1score,2)
    cur.execute('insert into CandidScore values(?,?,?,?,?,?)',[Cid,Cname,fscore,dscore,d1score,tscore])
    con.commit()
    print('written to base')

# deletes all the CandidSore entries for cleaaring the whole DB
def clear_db():
    global con,cur
    cur.execute('delete from CandidScore')
    con.commit()

# to get the current data inside the data base
def fetch_data_from_base():
    global con,cur
    cur.execute('select * from CandidScore order by Tscore desc')
    return cur.fetchall()

#  saves a report of the session to the folder
def write_report(Cname,writedata):
    try:
        f = open(f"reports\\Report_{Cname}.doc", "w+")
        f.write(writedata)
        f.close()
        return
    except:
        print('Error Occured while generating the report!!')
        return

# returns all the general questions in the data base
def get_all_questions():
    try:
        global cur,con
        cur.execute('select question from questions')
        return cur.fetchall()
    except:
        print('error occured while fetching questions')

# writes the question to base for the add quesion functinality
def write_question_to_base(ques,wt,desc):
    try:
        global cur,con
        cur.execute('insert into questions values(?,?,?)',[ques,wt,desc])
    except:
        print('Error occurred while adding question to base')

#  returns the questions table's all rows
def get_all_ques_values():
    try:
        cur.execute('select * from questions')
        return cur.fetchall()
    except:
        print('Error occured while fetching from the database')
        return None

# returns a list of the columns of the chracter code needed
def fetch_character_details(code):
    try:
        global con,cur
        cur.execute(f'select * from character_codes where code="{code}"')
        return list(cur.fetchall()[0])
    except:
        print('Error while fetching character code from the database')
        return None

# wriite the reumse questions to the resume table
def write_to_resume_ques(ques):
    try:
        global con,cur
        print('the questions tried to inserted is')
        print(ques)
        cur.execute(f"insert into resume_ques values('{ques}')")
    except:
        print('Error writing to the database'+str(traceback.print_exc()))

# fetchs session specific resume only questions
def fetch_resume_questions():
    try:
        global con,cur
        cur.execute('select * from resume_ques')
        return cur.fetchall() # check if this works
    except:
        print("Error while trying to fetch resume questions from the database")
        return None

# clears resume questions
def clear_resume_ques():
    try:
        global cur,con
        cur.execute('delete from resume_ques')
    except:
        print('Error while trying to clear the resume questions database')

# print('details of INTP',fetch_character_details("INTP"))
# write_to_base(1,'bala',90,98,89,76
# clear_db()
# #  all the above functions work
# daata=fetch_data_from_base()
# for x in daata:
#     print(x)
# clear_resume_ques()
# write_to_resume_ques("Hllo this is bala rubinan")
# # cur.execute("insert into resume_ques values('hello balarubinan')")
# print(fetch_resume_questions())
# str11="hello"
# cur.execute(f"insert into resume_ques values('{str11}')")