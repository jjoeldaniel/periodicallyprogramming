<script lang="ts">
	import { AppRailTile, drawerStore } from '@skeletonlabs/skeleton';

	function drawerClose(): void {
		drawerStore.close();
	}
</script>

<div class=" h-fit flex justify-center items-center">
	<div class="grid grid-cols-1 gap-3 text-2xl">
		<AppRailTile href="/" on:click={drawerClose}
			><div class="flex place-items-center flex-col">
				<span class="material-symbols-outlined"> home </span>
				Home
			</div></AppRailTile
		>
		<AppRailTile href="/blog" on:click={drawerClose}
			><div class="flex place-items-center flex-col">
				<span class="material-symbols-outlined"> book </span>
				Blog
			</div></AppRailTile
		>
		<AppRailTile href="/projects" on:click={drawerClose}
			><div class="flex place-items-center flex-col">
				<span class="material-symbols-outlined"> trophy </span>
				Projects
			</div></AppRailTile
		>
		<AppRailTile href="/contact" on:click={drawerClose}
			><div class="flex place-items-center flex-col">
				<span class="material-symbols-outlined"> phone </span>
				Contact
			</div></AppRailTile
		>
	</div>
</div>
