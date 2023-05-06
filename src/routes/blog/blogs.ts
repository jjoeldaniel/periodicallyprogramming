export function searchPosts(query: string) {
  const posts = getPosts().posts;

  return {
    posts: posts.filter((post) => post.slug.includes(query.toLowerCase()))
  };
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
    const slug = file_name.toLowerCase();
    const title = file_name.replace(/_/g, ' ');

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