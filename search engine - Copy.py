def matchingwords(sen1,sen2):
    words1=sen1.strip().split(' ')
    words2=sen2.strip().split(' ')
    score=0
    for word1 in words1:
        for word2 in words2 :
            if word1.lower()==word2.lower():
                score=+1
    return score 

if __name__=='__main__':
    serhis=['Anime series', 'MCU Marvel', 'manga comic Anime',
     'marvel comic','kdrama series', 'webtoon comic kdrama ']
    
    query=input("Enter..\n")
    scores=[matchingwords(query,search) for search in serhis]
    sortedsentscores=[sentscore for sentscore in sorted(
        zip(scores,serhis), reverse=True) if sentscore[0] !=0]

    print(f"{len(sortedsentscores)} results found!")
    for score , item in sortedsentscores :
        print(f' \'{item}\' : with a relevance of {score}') 
