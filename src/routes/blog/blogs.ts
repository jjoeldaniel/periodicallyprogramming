import fs from 'fs';
import path from 'path';

export function searchPosts(query: string) {
  const posts = getPosts().posts;

  return {
    posts: posts.filter((post) => post.title.toLowerCase().includes(query.toLowerCase()))
  };
}

export function getPosts() {
  const posts = fs.readdirSync(path.join(process.cwd(), 'static/blog_posts')).map((file) => {
    const post = fs.readFileSync(path.join(process.cwd(), 'static/blog_posts', file), 'utf-8').split('\n').slice(1).join('\n');
    const [meta, content] = post.split('---');
    const [title, date] = meta.split('\n');
    
    const title_ = title.replace('title: ', '');
    return {
      slug: title_.replace(/ /g, '-').toLowerCase(),
      title: title_,
      date: date.replace('date: ', ''),
      content
    };
  });

  return {
    posts
  };
}