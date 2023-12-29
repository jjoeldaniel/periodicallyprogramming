export const prerender = false

export async function GET({ params, redirect }) {
  const { repo } = params;
  const link = "https://github.com/jjoeldaniel/" + repo;

  if (!repo) {
    return new Response(null, {
      status: 404,
      statusText: 'Not found'
    });
  }

  return redirect(link, 307);
}
