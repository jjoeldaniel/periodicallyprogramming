import { searchPosts } from '../blogs';

/** @type {import('./$types').PageLoad} */
export function load({ params }) {
    let title = params.blogName.replace(/-/g, ' ');
    
    // capitalize first letter of each word
    title = title.split(' ').map((word) => word[0].toUpperCase() + word.slice(1)).join(' ');

    const post = searchPosts(title).posts[0];

    return {
        title,
        content: post.content
    };
}