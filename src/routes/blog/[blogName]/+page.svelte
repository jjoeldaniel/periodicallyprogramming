<script>
	import BlogHeader from '$lib/BlogHeader.svelte';
	import MarkdownIt from 'markdown-it';

	/** @type {import('./$types').PageData} */
	export let data;

    let md = new MarkdownIt();
	const html = md.render(data.content);
</script>

<div class="container h-full mx-auto flex flex-col justify-center">
	<div class="space-y-5">
		<BlogHeader title={data.title}/>
		{@html html}
    </div>
</div>