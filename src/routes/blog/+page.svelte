<script lang="ts">
	import { goto } from '$app/navigation';
	import { Autocomplete } from '@skeletonlabs/skeleton';
	import type { AutocompleteOption } from '@skeletonlabs/skeleton';

	/** @type {import('./$types').PageData} */
	export let data;

	const posts = Object.values(data.posts.posts);

	// build autocomplete options
	let query = '';
	let flavorOptions: AutocompleteOption[] = [];
	let names: string[] = [];

	posts.forEach((post: any) => {
		let title: string = post.title.toLowerCase();
		title = title.replaceAll(' ', '_');

		names.push(title);
		flavorOptions.push({
			label: post.title,
			value: post.slug
		});
	});

	// check for query param
	let search = '';
	if (typeof window !== 'undefined') {
		const urlParams = new URLSearchParams(window.location.search);
		search = urlParams.get('query') || '';
		search = search.replaceAll(' ', '_').toLocaleLowerCase();
	}

	// goto post if query param is present and valid
	if (search) {
		// check if post exists
		if (names.includes(search)) {
			goto(`/blog/${search}`);
		} else {
			goto(`/blog/`);
		}
	}

	function onFlavorSelection(event: any): void {
		query = event.detail.label;
	}
</script>

<div class="container h-full mx-auto flex justify-center items-center">
	<div class="space-y-8">
		<h1>Welcome to my blog!</h1>

		<form data-sveltekit-reload action="/blog/">
			<input
				class="input"
				required
				autocomplete="off"
				bind:value={query}
				type="search"
				name="query"
				placeholder="Search..."
			/>
		</form>

		<div class="card w-full max-w-sm max-h-48 p-4 overflow-y-auto">
			<Autocomplete bind:input={query} options={flavorOptions} on:selection={onFlavorSelection} />
		</div>
	</div>
</div>
