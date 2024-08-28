from flask import Blueprint, render_template, flash
import praw
import requests
import json

from app import db
from app.models import User

digg_bp = Blueprint('digg', __name__,url_prefix="/digg")
# 配置PRAW
reddit = praw.Reddit(
    client_id="DQcsXpPRlUi-f1S-7Yb7dA",
    client_secret="gTLVj0HfzC5bfBuzu5ixSuA7UMDHDw",
    user_agent="web:com.trasearch.digg:v1.0 (by u/Frequent-System3064)",
)
@digg_bp.route('/')
def index():
    user = User(username="test12112", email="12212111112112@126.com")
    db.session.add(user)
    db.session.commit()
    flash('User created successfully!', 'success')
    return render_template('digg.html')
@digg_bp.route('/digg')
def digg():
    url = "https://google.serper.dev/search"
    payload = json.dumps({
        "q": """
      site:reddit.com "youtube" "i wish there was"
      """
    })
    headers = {
        'X-API-KEY': '5aa1dd0f13a234a59e81c0ae7f615a5a426cdba4',
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    data = json.loads(response.text)

    for item in data['organic']:
        print(f"Title: {item['title']}")
        print(f"Link: {item['link']}")
        # 帖子的URL
        post_url = item['link']
        # 获取帖子
        submission = reddit.submission(url=post_url)
        # 打印帖子的基本信息
        print(f"标题: {submission.title}")
        print(f"作者: {submission.author}")
        print(f"分数: {submission.score}")
        print(f"评论数: {submission.num_comments}")
        print(f"内容: {submission.selftext}")
        print(f"Snippet: {item['snippet']}")
        print('-' * 80)
        # 打印所有评论
        submission.comments.replace_more(limit=None)
        for comment in submission.comments.list():
            print(f"评论作者: {comment.author}")
            print(f"评论内容: {comment.body}")
            print('-' * 80)
    return render_template('user.html')



