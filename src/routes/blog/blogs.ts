import { error } from '@sveltejs/kit';

export function searchPosts(query: string) {
  const posts = getPosts().posts;

  // check if query is a valid title within the posts
  const valid: boolean = posts.some((post) => post.title.toLowerCase().includes(query.toLowerCase()));

  if (valid) {
    return {
      posts: posts.filter((post) => post.title.toLowerCase().includes(query.toLowerCase()))
    };
  }
  throw error(404, {
    message: "Uh oh! We couldn't find that post."
});
}

export function getPosts() {
  const posts = import.meta.glob(
    '$lib/blog_posts/*.md', { 
      as: 'raw', eager: true 
    }
  );

  const data = [];
  const arr = Object.entries(posts);

  for (const [path, content] of arr) {

    const file_name = path.split('/')[path.split('/').length - 1].replace('.md', '');
    const slug = file_name.replaceAll('_', '-').toLowerCase();
    const title = file_name.replaceAll(/_/g, ' ');

    data.push({
      slug,
      title,
      content
    });
  }

  return {
    posts: data
  };
}