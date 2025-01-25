import requests

cookies = {
    '_ga_WXBEYVQG0P': 'GS1.1.1725462812.1.0.1725462832.0.0.0',
    '_ga_TD5S9XEB03': 'GS1.1.1725463098.1.1.1725463404.60.0.0',
    '_ga_LFJQS6K98C': 'GS1.1.1725463893.1.1.1725463921.32.0.0',
    '_ga_W3BFRPSG9B': 'GS1.1.1725462813.1.1.1725463921.34.0.0',
    '_ga_ZCQJVP62ZW': 'GS1.1.1725462859.1.1.1725464181.0.0.0',
    '_ga': 'GA1.2.1755579152.1725462813',
    '_ga_11FWXNQWRT': 'GS1.2.1725476994.2.1.1725477360.0.0.0',
    'PS_DEVICEFEATURES': 'width:1366 height:768 pixelratio:0.8999999761581421 touch:0 geolocation:1 websockets:1 webworkers:1 datepicker:1 dtpicker:1 timepicker:1 dnd:1 sessionstorage:1 localstorage:1 history:1 canvas:1 svg:1 postmessage:1 hc:0 maf:0',
    '_tracking_consent': '%7B%22con%22%3A%7B%22CMP%22%3A%7B%22a%22%3A%22%22%2C%22m%22%3A%22%22%2C%22p%22%3A%22%22%2C%22s%22%3A%22%22%7D%7D%2C%22v%22%3A%222.1%22%2C%22region%22%3A%22CAON%22%2C%22reg%22%3A%22%22%2C%22purposes%22%3A%7B%22a%22%3Atrue%2C%22p%22%3Atrue%2C%22m%22%3Atrue%2C%22t%22%3Atrue%7D%2C%22display_banner%22%3Afalse%2C%22sale_of_data_region%22%3Afalse%2C%22consent_id%22%3A%225B81472A-b56f-49DF-b9c7-01570939fa09%22%7D',
    '_shopify_y': 'e5a2c900-58f2-4320-ad70-6037221ac3cb',
    'SSESS7fe4fa045b4b671400939eaec062f709': 'Fvvswtt1liPx4L7uhTbUHfTObD2bdtodGU-7foku23s',
    'CSPRPDB-PORTAL-PSJSESSIONID': 'QFCe_qGpbKb9vKGgxo_etpye4x96-qT0!1192111326',
    'PS_LOGINLIST': 'https://quest.pecs.uwaterloo.ca/SS',
    'PS_TOKEN': 'qAAAAAQDAgEBAAAAvAIAAAAAAAAsAAAABABTaGRyAk4AcQg4AC4AMQAwABRwPcmVf4jcjSna3rI9YoGT9q35IGgAAAAFAFNkYXRhXHicNYnRCkBAEEXPLnmUH7Gxu8izNh4k0SZPvsH/+TiTMrfmnJl7A2milRI+mm+KiZmWhZHISSAL35FHDi4GdlY2vKXC0lAKa9m/9xi8xODkY6SzdOJOjBe0EQwO',
    'PS_TokenSite': 'https://quest.pecs.uwaterloo.ca/psc/SS/?CSPRPDB-PORTAL-PSJSESSIONID',
    'SignOnDefault': '',
    'ps_theme': 'node:SA portal:ACADEMIC theme_id:UWSA_DEFAULT_THEME_FLUID css:UWSA_CLASSIC_TEMPLTE_FLUID css_f:UWSA_BRAND_FLUID_TEMPLATE_860 accessibility:N macroset:UWSA_DEFAULT_MACROSET_860 formfactor:3 piamode:2',
    'X-Oracle-BMC-LBS-Route': '6ab04ce01b4cc39ed22a67a4206316993d4f76dba955101351b2a3d0e4fe6d526184d9d15fa976c0479857f7d31ceb292ee5f7986482bc41f55f3b57',
    'ExpirePage': 'https://quest.pecs.uwaterloo.ca/psp/SS/',
    'PS_LASTSITE': 'https://quest.pecs.uwaterloo.ca/psp/SS/',
    'psback': '%22%22url%22%3A%22https%3A%2F%2Fquest.pecs.uwaterloo.ca%2Fpsc%2FSS%2FACADEMIC%2FSA%2Fc%2FNUI_FRAMEWORK.PT_AGSTARTPAGE_NUI.GBL%3FCONTEXTIDPARAMS%3DTEMPLATE_ID%253aPTPPNAVCOL%26scname%3DADMN_ENROLL%26PanelCollapsible%3DY%26PTPPB_GROUPLET_ID%3DUW_ENROLL%26CRefName%3DADMN_NAVCOLL_1%26AJAXTransfer%3DY%22%20%22label%22%3A%22Enrollment%3A%20%20Add%20Classes%22%20%22origin%22%3A%22PIA%22%20%22layout%22%3A%220%22%20%22refurl%22%3A%22https%3A%2F%2Fquest.pecs.uwaterloo.ca%2Fpsc%2FSS%2FACADEMIC%2FSA%22%22',
    'PS_TOKENEXPIRE': '25_Jan_2025_19:52:55_GMT',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': '_ga_WXBEYVQG0P=GS1.1.1725462812.1.0.1725462832.0.0.0; _ga_TD5S9XEB03=GS1.1.1725463098.1.1.1725463404.60.0.0; _ga_LFJQS6K98C=GS1.1.1725463893.1.1.1725463921.32.0.0; _ga_W3BFRPSG9B=GS1.1.1725462813.1.1.1725463921.34.0.0; _ga_ZCQJVP62ZW=GS1.1.1725462859.1.1.1725464181.0.0.0; _ga=GA1.2.1755579152.1725462813; _ga_11FWXNQWRT=GS1.2.1725476994.2.1.1725477360.0.0.0; PS_DEVICEFEATURES=width:1366 height:768 pixelratio:0.8999999761581421 touch:0 geolocation:1 websockets:1 webworkers:1 datepicker:1 dtpicker:1 timepicker:1 dnd:1 sessionstorage:1 localstorage:1 history:1 canvas:1 svg:1 postmessage:1 hc:0 maf:0; _tracking_consent=%7B%22con%22%3A%7B%22CMP%22%3A%7B%22a%22%3A%22%22%2C%22m%22%3A%22%22%2C%22p%22%3A%22%22%2C%22s%22%3A%22%22%7D%7D%2C%22v%22%3A%222.1%22%2C%22region%22%3A%22CAON%22%2C%22reg%22%3A%22%22%2C%22purposes%22%3A%7B%22a%22%3Atrue%2C%22p%22%3Atrue%2C%22m%22%3Atrue%2C%22t%22%3Atrue%7D%2C%22display_banner%22%3Afalse%2C%22sale_of_data_region%22%3Afalse%2C%22consent_id%22%3A%225B81472A-b56f-49DF-b9c7-01570939fa09%22%7D; _shopify_y=e5a2c900-58f2-4320-ad70-6037221ac3cb; SSESS7fe4fa045b4b671400939eaec062f709=Fvvswtt1liPx4L7uhTbUHfTObD2bdtodGU-7foku23s; CSPRPDB-PORTAL-PSJSESSIONID=QFCe_qGpbKb9vKGgxo_etpye4x96-qT0!1192111326; PS_LOGINLIST=https://quest.pecs.uwaterloo.ca/SS; PS_TOKEN=qAAAAAQDAgEBAAAAvAIAAAAAAAAsAAAABABTaGRyAk4AcQg4AC4AMQAwABRwPcmVf4jcjSna3rI9YoGT9q35IGgAAAAFAFNkYXRhXHicNYnRCkBAEEXPLnmUH7Gxu8izNh4k0SZPvsH/+TiTMrfmnJl7A2milRI+mm+KiZmWhZHISSAL35FHDi4GdlY2vKXC0lAKa9m/9xi8xODkY6SzdOJOjBe0EQwO; PS_TokenSite=https://quest.pecs.uwaterloo.ca/psc/SS/?CSPRPDB-PORTAL-PSJSESSIONID; SignOnDefault=; ps_theme=node:SA portal:ACADEMIC theme_id:UWSA_DEFAULT_THEME_FLUID css:UWSA_CLASSIC_TEMPLTE_FLUID css_f:UWSA_BRAND_FLUID_TEMPLATE_860 accessibility:N macroset:UWSA_DEFAULT_MACROSET_860 formfactor:3 piamode:2; X-Oracle-BMC-LBS-Route=6ab04ce01b4cc39ed22a67a4206316993d4f76dba955101351b2a3d0e4fe6d526184d9d15fa976c0479857f7d31ceb292ee5f7986482bc41f55f3b57; ExpirePage=https://quest.pecs.uwaterloo.ca/psp/SS/; PS_LASTSITE=https://quest.pecs.uwaterloo.ca/psp/SS/; psback=%22%22url%22%3A%22https%3A%2F%2Fquest.pecs.uwaterloo.ca%2Fpsc%2FSS%2FACADEMIC%2FSA%2Fc%2FNUI_FRAMEWORK.PT_AGSTARTPAGE_NUI.GBL%3FCONTEXTIDPARAMS%3DTEMPLATE_ID%253aPTPPNAVCOL%26scname%3DADMN_ENROLL%26PanelCollapsible%3DY%26PTPPB_GROUPLET_ID%3DUW_ENROLL%26CRefName%3DADMN_NAVCOLL_1%26AJAXTransfer%3DY%22%20%22label%22%3A%22Enrollment%3A%20%20Add%20Classes%22%20%22origin%22%3A%22PIA%22%20%22layout%22%3A%220%22%20%22refurl%22%3A%22https%3A%2F%2Fquest.pecs.uwaterloo.ca%2Fpsc%2FSS%2FACADEMIC%2FSA%22%22; PS_TOKENEXPIRE=25_Jan_2025_19:52:55_GMT',
    'Origin': 'https://quest.pecs.uwaterloo.ca',
    'Referer': 'https://quest.pecs.uwaterloo.ca/psc/SS/ACADEMIC/SA/c/SA_LEARNER_SERVICES.SSR_SSENRL_CART.GBL?NavColl=true&ICAGTarget=start&ICAJAXTrf=true',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = 'ICAJAX=1&ICNAVTYPEDROPDOWN=0&ICType=Panel&ICElementNum=0&ICStateNum=40&ICAction=CLASS_SRCH_WRK2_SSR_PB_CLASS_SRCH&ICModelCancel=0&ICXPos=259&ICYPos=370&ResponsetoDiffFrame=-1&TargetFrameName=None&FacetPath=None&PrmtTbl=&PrmtTbl_fn=&PrmtTbl_fv=&TA_SkipFldNms=&ICFocus=&ICSaveWarningFilter=0&ICChanged=-1&ICSkipPending=0&ICAutoSave=0&ICResubmit=0&ICSID=u9aHY7Y9Bbb0RI1z9n6J0F0J2CMKsbZkIk8OcCbivoM%3D&ICAGTarget=true&ICActionPrompt=false&ICTypeAheadID=&ICBcDomData=UnknownValue&ICPanelHelpUrl=&ICPanelName=&ICFind=&ICAddCount=&ICAppClsData=&DERIVED_SSTSNAV_SSTS_MAIN_GOTO$27$=&SSR_CLSRCH_WRK_SUBJECT$0=AFM&SSR_CLSRCH_WRK_SSR_EXACT_MATCH1$1=E&SSR_CLSRCH_WRK_CATALOG_NBR$1=&SSR_CLSRCH_WRK_ACAD_CAREER$2=&SSR_CLSRCH_WRK_SSR_OPEN_ONLY$chk$3=Y&SSR_CLSRCH_WRK_SSR_OPEN_ONLY$3=Y&SSR_CLSRCH_WRK_SSR_START_TIME_OPR$4=GE&SSR_CLSRCH_WRK_MEETING_TIME_START$4=&SSR_CLSRCH_WRK_SSR_END_TIME_OPR$4=LE&SSR_CLSRCH_WRK_MEETING_TIME_END$4=&SSR_CLSRCH_WRK_INCLUDE_CLASS_DAYS$5=I&SSR_CLSRCH_WRK_SUN$chk$5=&SSR_CLSRCH_WRK_MON$chk$5=&SSR_CLSRCH_WRK_TUES$chk$5=&SSR_CLSRCH_WRK_WED$chk$5=&SSR_CLSRCH_WRK_THURS$chk$5=&SSR_CLSRCH_WRK_FRI$chk$5=&SSR_CLSRCH_WRK_SAT$chk$5=&SSR_CLSRCH_WRK_DESCR$6=&SSR_CLSRCH_WRK_CAMPUS$7=&SSR_CLSRCH_WRK_SESSION_CODE$8='

response = requests.post(
    'https://quest.pecs.uwaterloo.ca/psc/SS/ACADEMIC/SA/c/SA_LEARNER_SERVICES.SSR_SSENRL_CART.GBL',
    cookies=cookies,
    headers=headers,
    data=data,
)