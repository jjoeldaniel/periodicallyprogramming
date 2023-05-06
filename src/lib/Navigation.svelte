<script lang="ts">
	import { page } from '$app/stores';
	import { drawerStore } from '@skeletonlabs/skeleton';

	function drawerClose(): void {
		drawerStore.close();
	}

	$: classesActive = (href: string) => (href === $page.url.pathname ? '!bg-primary-500' : '');
</script>

<nav class="list-nav">
	<ul>
		<li><a href="/" class={classesActive('/about')} on:click={drawerClose}>Home</a></li>
		<li><a href="/about" class={classesActive('/about')} on:click={drawerClose}>About</a></li>
		<li><a href="/blog" class={classesActive('/blog')} on:click={drawerClose}>Blog</a></li>
		<li><a href="/contact" class={classesActive('/contact')} on:click={drawerClose}>Contact</a></li>
		<li>
			<a href="/projects" class={classesActive('/projects')} on:click={drawerClose}>Projects</a>
		</li>
	</ul>
</nav>

<style>
	li a {
		border-radius: 0;
	}
</style>
