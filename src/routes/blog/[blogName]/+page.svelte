<script>
	import BlogHeader from '$lib/BlogHeader.svelte';
	import { marked } from 'marked';
	import {markedHighlight} from "marked-highlight";

	/** @type {import('./$types').PageData} */
	export let data;
	const html = marked.parse(data.content);
</script>

<div class="container h-full mx-auto flex flex-col justify-center">
	<div class="space-y-5">
		<BlogHeader title={data.title}/>
		{@html html}
    </div>
</div>