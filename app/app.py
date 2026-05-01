from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate, PostResponse

app = FastAPI()


text_posts = {
    1: {
        'title': 'Testing API',
        'content': 'Building APIs is one thing, but properly testing them is what separates stable systems from fragile ones. I’ve been focusing on validating endpoints, handling edge cases, and ensuring consistent responses. It’s a crucial step toward building reliable backend services.'
    },
    2: {
        'title': 'Learning System Design',
        'content': 'System design has completely changed how I think about software. It’s no longer just about writing code, but about scalability, reliability, and efficiency. Breaking down complex systems into manageable components is a skill I’m actively developing.'
    },
    3: {
        'title': 'My ALX Journey',
        'content': 'Completing the ALX Software Engineering program was a defining moment for me. From writing low-level C programs to understanding system administration, the experience pushed me beyond my limits and helped me grow into a better engineer.'
    },
    4: {
        'title': 'Why C Still Matters',
        'content': 'Learning C programming gave me a deeper understanding of how computers actually work. Memory management, pointers, and performance optimization are concepts that have strengthened my foundation across all other languages I use.'
    },
    5: {
        'title': 'Debugging Mindset',
        'content': 'Debugging is not just about fixing errors—it’s about thinking critically. I’ve learned to approach bugs systematically: reproduce, isolate, analyze, and fix. This mindset has improved both my efficiency and confidence as a developer.'
    },
    6: {
        'title': 'System Administration Basics',
        'content': 'Understanding system administration has made me more effective as a developer. From managing servers to handling permissions and processes, it bridges the gap between code and real-world deployment.'
    },
    7: {
        'title': 'Consistency Over Motivation',
        'content': 'Motivation comes and goes, but consistency builds results. Showing up every day to write code, learn, and improve—even when it’s hard—is what truly makes the difference in the long run.'
    },
    8: {
        'title': 'Version Control Discipline',
        'content': 'Using Git effectively has been a game changer. Writing meaningful commit messages, managing branches, and collaborating properly are essential skills that every developer should master early.'
    },
    9: {
        'title': 'Building Real Projects',
        'content': 'The best way to learn is by building. Working on real-world projects has helped me understand practical challenges like performance, scalability, and user needs beyond just theoretical knowledge.'
    },
    10: {
        'title': 'Do Hard Things',
        'content': 'One principle that stuck with me from ALX is simple: Do Hard Things. Growth doesn’t come from comfort. Taking on difficult challenges, failing, and learning from them is what drives real progress.'
    }
}

@app.get('/posts')
def get_all_posts(limit: int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts


@app.get('/posts/{id}')
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail='Post not found')
    return text_posts.get(id)


@app.post("/posts")
def create_post(post: PostCreate) -> PostResponse:
    new_post = {"title": post.title, "content": post.content}
    text_posts[max(text_posts.keys()) + 1] = new_post
    return new_post



