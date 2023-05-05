<script>
	/** @type {import('./$types').PageData} */
	export let data;

	// @ts-ignore
	const posts = data.posts;
</script>

<div class="container h-full mx-auto flex justify-center items-center">
	<div class="space-y-8">
		<h1>Welcome to my blog!</h1>
		
		<input class="input" type="search" name="blogSearch" placeholder="Search..." />

		<div class="space-y-3">
			<h2>Recent Posts</h2>
			<ul>
				{#each posts as post}
					<li>
						<a href="/blog/{post.slug}">
							{post.title}
						</a>
					</li>
				{/each}
			</ul>
		</div>
	</div>
</div>
