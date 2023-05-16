<script lang="ts">
	import { drawerStore } from '@skeletonlabs/skeleton';

	function drawerClose(): void {
		drawerStore.close();
	}
</script>

<nav class="list-nav text-5xl h-full flex flex-col place-content-evenly">
	<a class="grow" href="/" on:click={drawerClose}>Home</a>
	<a class="grow" href="/blog" on:click={drawerClose}>Blog</a>
	<a class="grow" href="/contact" on:click={drawerClose}>Contact</a>
	<a class="grow" href="/projects" on:click={drawerClose}>Projects</a>
</nav>

<style>
	a {
		border-radius: 0;
	}
</style>
