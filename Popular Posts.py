def identify_popular_posts(data):
    # Identify popular posts based on engagement metrics
    posts = data.get("posts", [])
    popular_posts = [post for post in posts if post.get("likes", 0) > 1000]
    return popular_posts

popular_posts = identify_popular_posts(social_media_data)
print("Popular Posts:", popular_posts)
