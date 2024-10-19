import re
from PyPDF2 import PdfReader
import justextract
possibe_sections = [
    "abstract","introduction","conclusion","literaturereview","methodology","method","methods"
    "results","discussion","references","findings","recommendations","backgroundinformation","researchproblem",
    "researchquestion","objectives","aims","significanceofthestudy","theoreticalframework","researchdesign","datacollectionmethods",
    "dataanalysistechniques","ethicalconsiderations","participants","sampleselection","instrumentation","statisticalmethods",
    "interpretationofresults","implicationsoffindings","comparisonwithpreviousresearch","limitationsofthestudy",
    "futurework","acknowledgments","appendices","figures","tables","glossaryofterms","dataavailability","conflictofinterest",
    "studydesign","operationaldefinitions","researchhypotheses","qualitativeanalysis","quantitativeanalysis","datapresentation","casestudies",
    "interviews","surveys","limitationsanddelimitations","contributionstothefield"
]

def section_analysis(text):
    section_content = dict()
    
    last = None

    lines = text.splitlines()
    for i in lines:
        words = i.split()
        if len(words)<=3:
            text = ''.join(words).lower()
            if text in possibe_sections:
                last = i
                section_content[last]  = ""
        elif last!=None:
            section_content[last]+="".join(i)
                
    print(section_content.keys())
                   
             
    return section_content
