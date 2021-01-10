# Run this script after adding a new question to the database system
from dbmsconnect import *
from gtts import gTTS
def preload_questions():
    ques = get_all_questions()
    cnt = 0
    t1 = "Thank you , We'll get Back to you later"
    ob = gTTS(text=t1, lang='en', slow=False)
    ob.save(f'sentences_folder\\sentence-end.mp3')
    t1 = "Now let's taake a look at your resume"
    ob = gTTS(text=t1, lang='en', slow=False)
    ob.save(f'sentences_folder\\sentence-resume.mp3')
    for x in ques:
        print(f"Question{cnt+1} loading")
        cnt += 1
        ob = gTTS(text=x[0], lang='en', slow=False)
        ob.save(f'sentences_folder\\sentence-{cnt}.mp3')
        print(f"Question{cnt} done")
    print('All questions are saved as mp3')

# this fucntiion will be called at the runtime to preload the questions of the resume wwhile the interview is on the fly
# try to load it in the three second delay time so that the candidate doesn't need to wait during the interview process
# check for the spleeling ffor all the dictinoary keys metioned down in this function

def preload_resume_questions(resume_dict):
    # Achievements Skills Hobbies
    # creating the voice files for playing the sound
    print('Started preloading the resume questions on the background')
    expert=resume_dict['Skills ']
    cnt=1
    t1 = f"Your resume says you are exepertised at {expert}, could you tell me more about it?"
    ob = gTTS(text=t1, lang='en', slow=False)
    ob.save(f'sentences_folder\\resume_questions\\resume-{cnt}.mp3')
    cnt+=1
    achieve=resume_dict['Achievements ']
    t1 = f"Lets take a look at your achievements, {achieve} ,That's quite a few achievements, how did these achievements affect your career?"
    ob = gTTS(text=t1, lang='en', slow=False)
    ob.save(f'sentences_folder\\resume_questions\\resume-{cnt}.mp3')
    cnt += 1
    hobbies=resume_dict['Hobbies ']
    t1 = f"hmmm interesting.....You have mentioned that you like {hobbies} tell some more about it"
    ob = gTTS(text=t1, lang='en', slow=False)
    ob.save(f'sentences_folder\\resume_questions\\resume-{cnt}.mp3')
    # add more resume specific questions into this area
    # writing the questiions to the database into the resum_ques table
    write_to_resume_ques(f"Your resume says you are exepertised at {expert}, could you tell me more about it?")
    write_to_resume_ques(f"Lets take a look at your achievements, {achieve} ,That's quite a few achievements, how did these achievements affect your career?")
    write_to_resume_ques(f"hmmm interesting.....You have mentioned that you like {hobbies} tell some more about it")
    print('Preloading the questions are done')
# testing code comments
# try a way to add the questions from the resume to this interview
# preload_questions()
