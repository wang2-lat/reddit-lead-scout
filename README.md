# Reddit Lead Scout

Automatically find potential customers on Reddit by monitoring buying intent keywords.

## Problem It Solves

Entrepreneurs spend 2-3 hours daily manually browsing Reddit for customers, often missing opportunities. This tool automates the process of finding potential leads in niche subreddits by detecting buying intent keywords.

## Features

- Monitor specified subreddits for new posts and comments
- Detect buying intent keywords (e.g., "looking for", "need help", "recommend")
- Export leads to CSV with username, post link, and content summary

## Installation


## Configuration

Before running, you need Reddit API credentials:

1. Go to https://www.reddit.com/prefs/apps
2. Create an app (script type)
3. Update `reddit_monitor.py` with your `client_id` and `client_secret`

## Usage

Basic usage:


Custom keywords:


Options:
- `-s, --subreddit`: Subreddit to monitor (required)
- `-k, --keywords`: Comma-separated keywords (default: "looking for,need help,recommend,suggestion")
- `-l, --limit`: Number of posts to check (default: 50)
- `-o, --output`: Output CSV filename (default: "leads.csv")

## Output

The tool generates a CSV file with:
- username: Reddit username
- type: "post" or "comment"
- url: Direct link to the post/comment
- title: Post title
- content: Content preview (first 200 characters)
- created_utc: Timestamp

## Example


This will scan the last 100 posts in r/SaaS for buying intent and save results to `leads.csv`.
python main.py monitor -s entrepreneur -k "looking for,need help,recommend" -l 100 -o leads.csv