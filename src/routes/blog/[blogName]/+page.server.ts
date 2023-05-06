import { searchPosts } from '../blogs';

/** @type {import('./$types').PageLoad} */
export function load({ params }) {
    const post = searchPosts(params.blogName).posts[0];

    return {
        title: post.title,
        content: post.content
    };
}