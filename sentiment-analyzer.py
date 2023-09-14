#natural language toolkit
import nltk
nltk.download('vader_lexicon')
import nltk.sentiment

#create sentiment analyzer object
analyzer = nltk.sentiment.SentimentIntensityAnalyzer()

#function to get the sentiment score of the user-entered text.
#runs the polarity_score() method from the analyzer object on the text which returns 3 scores for how
#positive, negative, and neutral the text is, and stores it in 'scores'.
#then gets the compund score of these 3 scores
def get_sentiment(user_text):
  scores = analyzer.polarity_scores(user_text)
  sentiment_score = scores['compound']
  return sentiment_score

#choose appropriate emoji reaction based on calculated compound score
def get_reaction(score):
  if score>0:
    return ":)"
  if score == 0:
    return ":/"
  if score < 0:
    return ":("

#get text from user
#call get_sentiment() to get the score
#print the reaction ands score.
def main():
  while True:
    user_text = input('phrase: ')
    score = get_sentiment(user_text)
    reaction = get_reaction(score)
    print(reaction)
    print(score)
    print(' ')

#check if script is being run directly and not imported somewhere else, execute main()
#because in that case you would run the main() of the module that houses this script, and you could reuse the functions in
#this script in the other module.
if __name__ == "__main__":
  main()
