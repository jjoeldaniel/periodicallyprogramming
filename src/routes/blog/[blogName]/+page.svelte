<script lang='ts'>
	import BlogHeader from '$lib/BlogHeader.svelte';
	import MarkdownIt from 'markdown-it';
	import meta from 'markdown-it-meta'
	import hljs from 'highlight.js';

	/** @type {import('./$types').PageData} */
	export let data;

    let md = new MarkdownIt({
		highlight: function (str: string, lang: string) {
			if (lang && hljs.getLanguage(lang)) {
			try {
				return '<pre class="hljs"><code>' +
					hljs.highlight(str, { language: lang, ignoreIllegals: true }).value +
					'</code></pre>';
			} catch (__) {}
			}

			return '<pre class="hljs"><code>' + md.utils.escapeHtml(str) + '</code></pre>';
		}
	});
	md.use(meta);

	const html = md.render(data.content);
	md.ht
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