<script lang="ts">
	import { Autocomplete } from '@skeletonlabs/skeleton';
	import type { AutocompleteOption } from '@skeletonlabs/skeleton';

	/** @type {import('./$types').PageData} */
	export let data;

	const posts = Object.values(data.posts.posts);

	// build autocomplete options
	let query = '';
	let flavorOptions: AutocompleteOption[] = [];

	posts.forEach((post: any) => {
		flavorOptions.push({
			label: post.title,
			value: post.slug
		});
	});

	function onFlavorSelection(event: any): void {
		query = event.detail.label;
	}	
</script>

<div class="container h-full mx-auto flex justify-center items-center">
	<div class="space-y-8">
		<h1>Welcome to my blog!</h1>
		
		<input class="input" bind:value={query} type="search" name="blogSearch" placeholder="Search..." />

		<div class="card w-full max-w-sm max-h-48 p-4 overflow-y-auto">
			<Autocomplete bind:input={query} options={flavorOptions} on:selection={onFlavorSelection} />
		</div>

		<div class="space-y-3">
			<h2>Recent Posts</h2>
			<ul>
				<!-- add each json -->
				{#each posts as {slug, title}}
					<li>
						<a href="/blog/{slug}">
							{title}
						</a>
					</li>
				{/each}
			</ul>
		</div>
	</div>
</div>
