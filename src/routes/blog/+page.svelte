<script lang="ts">
	import { goto } from '$app/navigation';
	import { Autocomplete } from '@skeletonlabs/skeleton';
	import type { AutocompleteOption } from '@skeletonlabs/skeleton';
	import { redirect } from '@sveltejs/kit';
	import { prevent_default } from 'svelte/internal';

	/** @type {import('./$types').PageData} */
	export let data;

	// @ts-ignore
	const posts = data.posts.posts;
	
	// convert posts to array
	const arr = Object.values(posts);

	// array of post names
	const postNames = arr.map((post: any) => post.title);

	// build autocomplete options
	let query = '';
	let flavorOptions: AutocompleteOption[] = [];

	arr.forEach((post: any) => {
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
				{#each arr as {slug, title}}
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
