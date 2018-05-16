#Team David + Ling
#David Lupea and Ling Chen
#IntroCS2 pd 5
#MadLibs Lab
#2018-05-15

def main():
    punc = ''' '"/?!:; '''

    fileIn = open('newspaper_article.txt', 'rU')
    text = fileIn.read()

    print text

    words = text.split()
    fillIns = []

    for i in range(len(words)):
        
        if words[i].strip(punc)[0] == '{' and words[i].strip(punc)[-1] == '}':
             fillIns.append(words[i][1:-1])

        elif words[i].strip(punc)[-2:] == ')}':
             fillIns.append(''.join(words[i - 2 : i + 1])[1:-1])

    responses = []
        
    for item in fillIns:
        responses.append(raw_input("Enter a " + item.lower() + ": "))

    fText = '''Mrs. Fifi Vanderbold, the {} and {} heiress,
has filed for divorce from her husband. Percy Vanderbold, the former
{} {} of Harvard, class of '38, now in the
{} business. Mrs. Vanderbold claimed that her husband
had {} her bed of {} flowers and tracked
{} mud into the house. He also criticized her cooking.
Mr. Vanderbold, when asked to comment, said, "{}!
I didn't do it. The pet {} ruined the flowers. And I
offered to take her out to restuarants more often!"'''    

    fileOut = open('newsMadLibs.txt', 'w')

    fileOut.write(fText.format(responses[0],responses[1],responses[2],responses[3],responses[4],responses[5],responses[6],responses[7],responses[8], responses[9]))

    fileOut.close()

main()
