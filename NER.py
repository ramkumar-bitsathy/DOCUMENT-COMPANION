import spacy

# Load pre-trained model
nlp = spacy.load("en_core_web_sm")

# Input text
text = """GOVERNMENT OF TAMIL NADU
DIRECTORATE OF TECHNICAL EDUCATION
TAMIL NADU ENGINEERING ADMISSIONS - 2024
Application Number:  297695
Application locked status: No
Choice 
orderCollege 
CodeCollege Name Branch Name
12618Sona College of Technology (Autonomous), Sona Nagar, Thia-
garajar Polytechnic College Road, Suramangalam (P.O),Salem Dis-
trict-636005.Artificial Intelligence and Data Science
22618Sona College of Technology (Autonomous), Sona Nagar, Thia-
garajar Polytechnic College Road, Suramangalam (P.O),Salem Dis-
trict-636005.COMPUTER SCIENCE AND ENGI-
NEERING
32618Sona College of Technology (Autonomous), Sona Nagar, Thia-
garajar Polytechnic College Road, Suramangalam (P.O),Salem Dis-
trict-636005.INFORMATION TECHNOLOGY
42653Knowledge Institute of Technology (Autonomous), KIOT Campus,
Kakapalayam (PO), Salem-637504.Artificial Intelligence and Data Science
52653Knowledge Institute of Technology (Autonomous), KIOT Campus,
Kakapalayam (PO), Salem-637504.INFORMATION TECHNOLOGY
62653Knowledge Institute of Technology (Autonomous), KIOT Campus,
Kakapalayam (PO), Salem-637504.COMPUTER SCIENCE AND ENGI-
NEERING
72618Sona College of Technology (Autonomous), Sona Nagar, Thia-
garajar Polytechnic College Road, Suramangalam (P.O),Salem Dis-
trict-636005.ELECTRONICS AND COMMUNI-
CATION ENGINEERING
82653Knowledge Institute of Technology (Autonomous), KIOT Campus,
Kakapalayam (PO), Salem-637504.ELECTRONICS AND COMMUNI-
CATION ENGINEERING
92618Sona College of Technology (Autonomous), Sona Nagar, Thia-
garajar Polytechnic College Road, Suramangalam (P.O),Salem Dis-
trict-636005.COMPUTER SCIENCE AND EN-
GINEERING (AI AND MACHINE
LEARNING)
102607K S Rangasamy College of Technology (Autonomous), K.S.R Kalvi
Nagar, Thokkavadi, Tiruchengode Tk, Namakkal-637215.Artificial Intelligence and Data Science
112607K S Rangasamy College of Technology (Autonomous), K.S.R Kalvi
Nagar, Thokkavadi, Tiruchengode Tk, Namakkal-637215.COMPUTER SCIENCE AND ENGI-
NEERING
122607K S Rangasamy College of Technology (Autonomous), K.S.R Kalvi
Nagar, Thokkavadi, Tiruchengode Tk, Namakkal-637215.INFORMATION TECHNOLOGY
132609Mahendra Engineering College (Autonomous), Mahendhirapuri,
Mallasamudram West, Vadugapalayam Post,Tiruchengodu Taluk,
Namakkal District-637503.Artificial Intelligence and Data Science
142609Mahendra Engineering College (Autonomous), Mahendhirapuri,
Mallasamudram West, Vadugapalayam Post,Tiruchengodu Taluk,
Namakkal District-637503.COMPUTER SCIENCE AND ENGI-
NEERING
152609Mahendra Engineering College (Autonomous), Mahendhirapuri,
Mallasamudram West, Vadugapalayam Post,Tiruchengodu Taluk,
Namakkal District-637503.INFORMATION TECHNOLOGY
162613K S R College of Engineering (Autonomous), K S R Kalvi Nagar,
Thokkavadi, Tiruchengode, Namakkal Dist-637215.COMPUTER SCIENCE AND ENGI-
NEERING
172613K S R College of Engineering (Autonomous), K S R Kalvi Nagar,
Thokkavadi, Tiruchengode, Namakkal Dist-637215.INFORMATION TECHNOLOGYGOVERNMENT OF TAMIL NADU
DIRECTORATE OF TECHNICAL EDUCATION
TAMIL NADU ENGINEERING ADMISSIONS - 2024
Application Number:  297695
182345Dhirajlal Gandhi College of Technology, Sikkanampatty, Opposite
to Airport,Omalur Taluk, Salem District-636309.COMPUTER SCIENCE AND ENGI-
NEERING
192345Dhirajlal Gandhi College of Technology, Sikkanampatty, Opposite
to Airport,Omalur Taluk, Salem District-636309.Artificial Intelligence and Data Science
202345Dhirajlal Gandhi College of Technology, Sikkanampatty, Opposite
to Airport,Omalur Taluk, Salem District-636309.INFORMATION TECHNOLOGY
212632Mahendra Institute of Technology (Autonomous), Mahendhirapuri,
Mallasamudram West, Vadugapalayam Post, Tiruchengodu Taluk,
Namakkal District-637503.INFORMATION TECHNOLOGY
222632Mahendra Institute of Technology (Autonomous), Mahendhirapuri,
Mallasamudram West, Vadugapalayam Post, Tiruchengodu Taluk,
Namakkal District-637503.COMPUTER SCIENCE AND ENGI-
NEERING
232609Mahendra Engineering College (Autonomous), Mahendhirapuri,
Mallasamudram West, Vadugapalayam Post,Tiruchengodu Taluk,
Namakkal District-637503.ELECTRONICS AND COMMUNI-
CATION ENGINEERING
242607K S Rangasamy College of Technology (Autonomous), K.S.R Kalvi
Nagar, Thokkavadi, Tiruchengode Tk, Namakkal-637215.COMPUTER SCIENCE AND EN-
GINEERING (AI AND MACHINE
LEARNING)
252611Paavai Engineering College (Autonomous), NH-7, Paavai Nagar,
Pachal, Namakkal-637018.COMPUTER SCIENCE AND ENGI-
NEERING
262611Paavai Engineering College (Autonomous), NH-7, Paavai Nagar,
Pachal, Namakkal-637018.INFORMATION TECHNOLOGY
Disclaimer: Since this PDF was generated from data that was available to us at the server when the user requested it, it may not match
exactly with your browser's copy of your selection due to network or cache issues. Please check your browser version of selections and
PDF list, and if any mismatch is found, reload the page and fix the selection again. If you need any help please reach out to us through
our helpline or contact near by TFC.
PDF Requested At: Sunday, August 11th, 2024, 9:39:38 PM"""

# Process text
doc = nlp(text)

# Extract entities
for ent in doc.ents:
    print(ent.text, ent.label_)