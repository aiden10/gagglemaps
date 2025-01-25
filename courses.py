import requests
from bs4 import BeautifulSoup
import json

cookies = {
}

headers = {
}

subject_string = open('subjects.json', 'r').read()
subjects = json.loads(subject_string)
for subject in subjects:
    print(f'getting {subject}...')
    data = f'ICAJAX=1&ICNAVTYPEDROPDOWN=0&ICType=Panel&ICElementNum=0&ICStateNum=9&ICAction=%23KEY%0D&ICModelCancel=0&ICXPos=0&ICYPos=0&ResponsetoDiffFrame=-1&TargetFrameName=None&FacetPath=None&PrmtTbl=&PrmtTbl_fn=&PrmtTbl_fv=&TA_SkipFldNms=&ICFocus=SSR_CLSRCH_WRK_SUBJECT%240&ICSaveWarningFilter=0&ICChanged=-1&ICSkipPending=0&ICAutoSave=0&ICResubmit=0&ICSID=GKxD1Q60OsFhoqIhBabrqHtaquWuZ7Ov8CD1Kg6jWrs%3D&ICAGTarget=true&ICActionPrompt=false&ICTypeAheadID=&ICBcDomData=UnknownValue&ICPanelHelpUrl=&ICPanelName=&ICFind=&ICAddCount=&ICAppClsData=&DERIVED_SSTSNAV_SSTS_MAIN_GOTO$27$=&SSR_CLSRCH_WRK_SUBJECT$0={subject}&SSR_CLSRCH_WRK_SSR_EXACT_MATCH1$1=E&SSR_CLSRCH_WRK_CATALOG_NBR$1=&SSR_CLSRCH_WRK_ACAD_CAREER$2=&SSR_CLSRCH_WRK_SSR_OPEN_ONLY$chk$3=Y&SSR_CLSRCH_WRK_SSR_OPEN_ONLY$3=Y&SSR_CLSRCH_WRK_SSR_START_TIME_OPR$4=GE&SSR_CLSRCH_WRK_MEETING_TIME_START$4=&SSR_CLSRCH_WRK_SSR_END_TIME_OPR$4=LE&SSR_CLSRCH_WRK_MEETING_TIME_END$4=&SSR_CLSRCH_WRK_INCLUDE_CLASS_DAYS$5=I&SSR_CLSRCH_WRK_SUN$chk$5=&SSR_CLSRCH_WRK_MON$chk$5=&SSR_CLSRCH_WRK_TUES$chk$5=&SSR_CLSRCH_WRK_WED$chk$5=&SSR_CLSRCH_WRK_THURS$chk$5=&SSR_CLSRCH_WRK_FRI$chk$5=&SSR_CLSRCH_WRK_SAT$chk$5=&SSR_CLSRCH_WRK_DESCR$6=&SSR_CLSRCH_WRK_CAMPUS$7=&SSR_CLSRCH_WRK_SESSION_CODE$8='

    response = requests.post(
        'https://quest.pecs.uwaterloo.ca/psc/SS/ACADEMIC/SA/c/SA_LEARNER_SERVICES.SSR_SSENRL_CART.GBL',
        cookies=cookies,
        headers=headers,
        data=data,
    )
    with open(f'schedules/{subject}.html', 'w', encoding='utf-8') as file:
        file.write(response.text)
    