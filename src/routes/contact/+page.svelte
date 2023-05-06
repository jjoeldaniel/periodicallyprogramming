<script lang="ts">
	import BlogHeader from '$lib/BlogHeader.svelte';
</script>

<div class="container h-full mx-auto flex flex-col justify-center text-center">
	<div class="space-y-5">
		<BlogHeader title={'Contact Me'} />

		<p>Start by exploring:</p>
		<ul>
			<li>
				<code>/src/routes/+layout.svelte</code> - barebones layout, the CSS import order is critical!
			</li>
			<li>
				<code>/src/app.postcss</code> - minimal css to make the page full screen, may not be relevant
				for your project
			</li>
			<li><code>/src/routes/+page.svelte</code> - this page, you can replace the contents</li>
		</ul>
	</div>
</div>
