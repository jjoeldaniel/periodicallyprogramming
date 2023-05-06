<script lang='ts'>
	// The ordering of these imports is critical to your app working properly
	import '@skeletonlabs/skeleton/themes/theme-crimson.css';
	import '@skeletonlabs/skeleton/styles/all.css';
	// Most of your app wide CSS should be put in this file
	import '../app.postcss';
	import { AppShell } from '@skeletonlabs/skeleton';
	import { Drawer, drawerStore } from '@skeletonlabs/skeleton';
	import Navigation from '$lib/Navigation.svelte';

	function drawerOpen(): void {
		drawerStore.open({});
	}
</script>

<Drawer>
	<Navigation />
</Drawer>

<AppShell slotSidebarLeft="bg-surface-500/5 w-0 lg:w-64">
	<svelte:fragment slot="header">
    <div class="flex items-center">
        <button class="lg:hidden btn btn-sm mr-4" on:click={drawerOpen}>
            <span>
                <svg viewBox="0 0 100 80" class="fill-token w-4 h-4">
                    <rect width="100" height="20" />
                    <rect y="30" width="100" height="20" />
                    <rect y="60" width="100" height="20" />
                </svg>
            </span>
        </button>
        <strong class="text-xl uppercase">
			<a href="/" style="text-decoration: none; color: white">periodicallyprogramming</a>
		</strong>
    </div>
</svelte:fragment>

	<svelte:fragment slot="sidebarLeft">
		<!-- Insert the list: -->
		<nav class="list-nav">
			<ul>
				<li><a href="/">Home</a></li>
				<li><a href="/about">About</a></li>
				<li><a href="/blog">Blog</a></li>
				<li><a href="/contact">Contact</a></li>
				<li><a href="/projects">Projects</a></li>
			</ul>
		</nav>
	</svelte:fragment>
	<slot />
</AppShell>