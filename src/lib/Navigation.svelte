<script lang="ts">
	import { drawerStore } from '@skeletonlabs/skeleton';

	function drawerClose(): void {
		drawerStore.close();
	}
</script>

<nav class="list-nav">
	<ul>
		<li class="hidden"><a href="/">easter egg</a></li>
		<li><a href="/" on:click={drawerClose}>Home</a></li>
		<li><a href="/about" on:click={drawerClose}>About</a></li>
		<li><a href="/blog" on:click={drawerClose}>Blog</a></li>
		<li><a href="/contact" on:click={drawerClose}>Contact</a></li>
		<li>
			<a href="/projects" on:click={drawerClose}>Projects</a>
		</li>
	</ul>
</nav>

<style>
	li a {
		border-radius: 0;
	}
</style>
