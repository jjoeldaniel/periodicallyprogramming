/** @type {import('./$types').PageServerLoad} */
export function load() {
  const posts: [] = [];
  // TODO: Return all blog posts
  // as an array of objects with
  // the following shape:
  //
  // {
  //   slug: string;
  //   title: string;
  //   date: string;
  //   content: string;
  // } 
  return {
    status: 200,
    posts
  };
}
