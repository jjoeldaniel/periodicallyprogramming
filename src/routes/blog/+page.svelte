<script lang="ts">
	import { goto } from '$app/navigation';
	import { Autocomplete, type AutocompleteOption } from '@skeletonlabs/skeleton';
	import { Toast, toastStore, type ToastSettings } from '@skeletonlabs/skeleton';

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
	let empty = query == '' ? true : false;
	let flavorOptions: AutocompleteOption[] = [];
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
		goto(`/blog/${event.detail.value}`);
	}
</script>

<Toast />

<div class="container h-full mx-auto flex md:max-w-md max-w-xs justify-center items-center">
	<div class="space-y-8 relative pt-5 md:pt-0">
		<h1 class="font-semibold">Welcome to my blog!</h1>
		<p>Here you'll find my technological hot takes and blog posts</p>

		<form data-sveltekit-reload action="/blog/">
			<input
				class="input"
				required
				autocomplete="off"
				bind:value={query}
				on:input={() => (empty = query == '' ? true : false)}
				type="search"
				name="query"
				placeholder="Search..."
			/>

			{#if !empty}
				<div class="card absolute w-full max-h-48 p-4 mt-3 overflow-y-auto">
					<Autocomplete
						bind:input={query}
						options={flavorOptions}
						on:selection={onFlavorSelection}
					/>
				</div>
			{/if}
		</form>

		<div id="posts" class="space-y-5">
			<h2 class="font-semibold">All Posts</h2>
			{#each posts as post}
				<div>
					<header>
						<a href={`/blog/${post.slug}`}>
							<h3 class="font-semibold">{post.title}</h3>
						</a>
					</header>
					<section class="pb-2 pt-1">
						Lorem, ipsum dolor sit amet consectetur adipisicing elit. Autem, sunt nam. Facilis,
						eveniet dolore nemo ea officiis obcaecati rem maiores minus? At, totam repellendus
						fugiat aperiam unde natus voluptate architecto.
					</section>
				</div>
			{/each}
		</div>
	</div>
</div>
