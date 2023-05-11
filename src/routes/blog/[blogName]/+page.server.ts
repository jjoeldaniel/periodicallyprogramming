import { error } from '@sveltejs/kit';
import { searchPosts } from '../blogs';

/** @type {import('./$types').PageLoad} */
export function load({ params }) {
    const post = searchPosts(params.blogName).posts[0];

    if (!post || !post.content || !post.title) {
        throw error(404);
    } 

    return {
        title: post.title,
        content: post.content
    };
}