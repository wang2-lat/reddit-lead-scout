import praw
from lead_detector import LeadDetector

class RedditMonitor:
    def __init__(self):
        self.reddit = praw.Reddit(
            client_id="your_client_id",
            client_secret="your_client_secret",
            user_agent="reddit-lead-scout/1.0"
        )
        self.detector = LeadDetector()
    
    def scan_subreddit(self, subreddit_name, keywords, limit=50):
        leads = []
        subreddit = self.reddit.subreddit(subreddit_name)
        
        for submission in subreddit.new(limit=limit):
            if self.detector.has_buying_intent(submission.title + " " + submission.selftext, keywords):
                leads.append({
                    'username': str(submission.author),
                    'type': 'post',
                    'url': f"https://reddit.com{submission.permalink}",
                    'title': submission.title,
                    'content': submission.selftext[:200],
                    'created_utc': submission.created_utc
                })
            
            submission.comments.replace_more(limit=0)
            for comment in submission.comments.list()[:10]:
                if self.detector.has_buying_intent(comment.body, keywords):
                    leads.append({
                        'username': str(comment.author),
                        'type': 'comment',
                        'url': f"https://reddit.com{comment.permalink}",
                        'title': submission.title,
                        'content': comment.body[:200],
                        'created_utc': comment.created_utc
                    })
        
        return leads
