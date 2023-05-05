import { getPosts } from './blogs';

/** @type {import('./$types').PageServerLoad} */
export function load() {
  const posts = getPosts();
  return {
    status: 200,
    posts
  };
}
