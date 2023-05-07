<script lang="ts">
	import { goto } from '$app/navigation';
	import { Autocomplete } from '@skeletonlabs/skeleton';
	import type { AutocompleteOption } from '@skeletonlabs/skeleton';
	import { Toast, toastStore } from '@skeletonlabs/skeleton';
	import type { ToastSettings } from '@skeletonlabs/skeleton';

	function noMatch() {
		const t: ToastSettings = {
			message: 'No blog post found!',
			background: 'variant-filled-warning'
		};
		toastStore.trigger(t);
	}

	/** @type {import('./$types').PageData} */
	export let data;

	const posts = Object.values(data.posts.posts);

	// build autocomplete options
	let query = '';
	let flavorOptions: AutocompleteOption[] = [];
	let currentIndex = 0;
	let names: string[] = [];

	posts.forEach((post: any) => {
		let title: string = post.title.toLowerCase();
		title = title.replaceAll(' ', '-');

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
		search = search.replaceAll(' ', '-').toLocaleLowerCase();
	}

	// goto post if query param is present and valid
	if (search) {
		// check if post exists
		if (names.includes(search)) {
			goto(`/blog/${search}`);
		} else {
			goto(`/blog/`);
			noMatch();
		}
	}

	function onFlavorSelection(event: any): void {
		query = event.detail.label;
	}

	function navigateList(event: any): void {
		query = flavorOptions[currentIndex].label;
		if (event.key === 'ArrowDown') {
			currentIndex + 1 > flavorOptions.length - 1 ? (currentIndex = 0) : currentIndex++;
		} else if (event.key === 'ArrowUp') {
			currentIndex - 1 < 0 ? (currentIndex = 0) : currentIndex--;
		}
	}
</script>

<Toast />

<div class="container h-full mx-auto flex justify-center items-center">
	<div class="space-y-8">
		<h1>Welcome to my blog!</h1>

		<form data-sveltekit-reload action="/blog/">
			<input
				class="input"
				on:keydown={navigateList}
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
