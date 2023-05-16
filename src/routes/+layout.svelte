<script lang="ts">
	// The ordering of these imports is critical to your app working properly
	import '@skeletonlabs/skeleton/themes/theme-crimson.css';
	import '@skeletonlabs/skeleton/styles/all.css';
	// Most of your app wide CSS should be put in this file
	import '../app.postcss';
	import { AppShell, AppBar, LightSwitch, Drawer, drawerStore } from '@skeletonlabs/skeleton';
	import Navigation from '$lib/Navigation.svelte';

	function drawerOpen(): void {
		drawerStore.open({
			padding: 'p-3',
			width: 'md:w-1/3 xl:w-1/6 lg:w-3/12 xl:w-3/12 w-8/12',
			rounded: 'rounded-lg'
		});
	}
</script>

<Drawer>
	<Navigation />
</Drawer>

<AppShell>
	<svelte:fragment slot="header">
		<AppBar gridColumns="grid-cols-3" slotDefault="place-self-center" slotTrail="place-content-end">
			<svelte:fragment slot="lead"
				><button class="btn btn-sm mr-4" on:click={drawerOpen}>
					<span>
						<svg viewBox="0 0 100 80" class="fill-token w-4 h-4">
							<rect width="100" height="20" />
							<rect y="30" width="100" height="20" />
							<rect y="60" width="100" height="20" />
						</svg>
					</span>
				</button></svelte:fragment
			>
			<h4 class="font-bold gradient-heading"><a href="/">periodicallyprogramming</a></h4>
			<svelte:fragment slot="trail"><LightSwitch /></svelte:fragment>
		</AppBar>
	</svelte:fragment>

	<slot />

	<svelte:fragment slot="pageFooter">
		<hr class="h-px mt-6 mb-6 border-0" />
		<ul class="ul pb-5 flex space-x-7 justify-center">
			<li class="li"><a href="https://github.com/jjoeldaniel/">GitHub</a></li>
			<li class="li"><a href="/contact">Contact</a></li>
			<li class="li">
				<a href="https://github.com/jjoeldaniel/periodicallyprogramming">Source Code</a>
			</li>
		</ul></svelte:fragment
	>
</AppShell>
