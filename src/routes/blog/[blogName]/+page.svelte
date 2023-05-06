<script>
	import BlogHeader from '$lib/BlogHeader.svelte';
	import MarkdownIt from 'markdown-it';
	import meta from 'markdown-it-meta'

	/** @type {import('./$types').PageData} */
	export let data;

    let md = new MarkdownIt();
	md.use(meta);

	const html = md.render(data.content);
	const title = md.meta.title;
	const date = new Date(md.meta.date).toLocaleDateString('en-US');

	console.log(md.meta);
</script>

<div class="container h-full mx-auto flex flex-col justify-center">
	<div class="space-y-5">
		<BlogHeader title={title} date={date}/>
		{@html html}
    </div>
</div>